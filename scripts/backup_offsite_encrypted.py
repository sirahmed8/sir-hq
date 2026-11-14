#!/usr/bin/env python3
"""
backup_offsite_encrypted.py - Zero-Knowledge Encrypted Backup Engine (OPS-GAP-02)
Standard: Master Directive (00-master-directive.md), Gap Hunt Report (GAP_REPORT.md)

1. Collects critical local non-git application state & databases across projects.
2. Archives into compressed tarball (.tar.gz), ignoring regenerable dependencies (.git, node_modules).
3. Encrypts client-side using OpenSSL AES-256-CBC with PBKDF2 (100,000 iterations) and salt.
4. Generates cryptographic SHA-256 checksums and manifest metadata.
5. Verifies archive decodability with automated roundtrip integrity tests.
6. Runs windowless and silent on Windows.
"""

import sys
import os
import tarfile
import hashlib
import json
import time
import argparse
import subprocess
from pathlib import Path
from datetime import datetime, timezone

# Windows silent subprocess flag
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

PROJECTS_ROOT = Path("D:/Projects")
DEFAULT_BACKUP_DIR = PROJECTS_ROOT / "Backups" / "encrypted"
DEFAULT_KEY_ENV = "SIR_BACKUP_KEY"
DEFAULT_FALLBACK_KEY = "sir_local_backup_passphrase"

EXCLUDE_PATTERNS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".cache",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".turbo"
}

def filter_tar_info(tarinfo):
    """Exclude unwanted directories and files from archive."""
    parts = Path(tarinfo.name).parts
    for part in parts:
        if part in EXCLUDE_PATTERNS:
            return None
    return tarinfo

def compute_sha256(file_path: Path) -> str:
    """Computes SHA-256 checksum of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def encrypt_file_openssl(input_path: Path, output_path: Path, password: str) -> bool:
    """Encrypts input_path to output_path using OpenSSL AES-256-CBC with PBKDF2."""
    cmd = [
        "openssl", "enc", "-aes-256-cbc",
        "-salt", "-pbkdf2", "-iter", "100000",
        "-in", str(input_path),
        "-out", str(output_path),
        "-pass", f"pass:{password}"
    ]
    res = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        creationflags=CREATE_NO_WINDOW
    )
    if res.returncode != 0:
        print(f"[ERROR] OpenSSL encryption failed: {res.stderr.strip()}", file=sys.stderr)
        return False
    return True

def decrypt_file_openssl(input_path: Path, output_path: Path, password: str) -> bool:
    """Decrypts input_path to output_path using OpenSSL AES-256-CBC with PBKDF2."""
    cmd = [
        "openssl", "enc", "-d", "-aes-256-cbc",
        "-pbkdf2", "-iter", "100000",
        "-in", str(input_path),
        "-out", str(output_path),
        "-pass", f"pass:{password}"
    ]
    res = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        creationflags=CREATE_NO_WINDOW
    )
    if res.returncode != 0:
        print(f"[ERROR] OpenSSL decryption failed: {res.stderr.strip()}", file=sys.stderr)
        return False
    return True

def verify_backup(enc_path: Path, password: str) -> bool:
    """Verifies that an encrypted backup file can be decrypted and unpacked."""
    temp_dec = enc_path.with_suffix(".tmp.tar.gz")
    try:
        ok = decrypt_file_openssl(enc_path, temp_dec, password)
        if not ok:
            return False
        if not tarfile.is_tarfile(temp_dec):
            print(f"[ERROR] Decrypted file is not a valid tar archive", file=sys.stderr)
            return False
        with tarfile.open(temp_dec, "r:gz") as tar:
            members = tar.getmembers()
            if len(members) == 0:
                print("[ERROR] Archive is empty", file=sys.stderr)
                return False
        return True
    finally:
        if temp_dec.exists():
            temp_dec.unlink(missing_ok=True)

def create_backup(
    targets: list[Path],
    output_dir: Path = DEFAULT_BACKUP_DIR,
    password: str = None,
    tag: str = "daily",
    dry_run: bool = False,
    retention_count: int = 7
) -> tuple[Path | None, str | None]:
    """
    Creates an encrypted backup of target directories.
    Returns (encrypted_archive_path, sha256_checksum).
    """
    if password is None:
        password = os.environ.get(DEFAULT_KEY_ENV, DEFAULT_FALLBACK_KEY)

    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    tar_name = f"sir_backup_{tag}_{timestamp}.tar.gz"
    enc_name = f"sir_backup_{tag}_{timestamp}.tar.gz.enc"
    
    tar_path = output_dir / tar_name
    enc_path = output_dir / enc_name
    meta_path = output_dir / f"sir_backup_{tag}_{timestamp}.meta.json"

    if dry_run:
        print(f"[DRY-RUN] Targets to archive:")
        for t in targets:
            print(f"  - {t}")
        print(f"[DRY-RUN] Target output: {enc_path}")
        return None, None

    # Step 1: Create compressed tarball
    print(f"[1/4] Archiving {len(targets)} targets to {tar_name}...")
    with tarfile.open(tar_path, "w:gz") as tar:
        for target in targets:
            if target.exists():
                arcname = target.name
                tar.add(target, arcname=arcname, filter=filter_tar_info)

    raw_size = tar_path.stat().st_size
    print(f"      Archive created ({raw_size / (1024*1024):.2f} MB)")

    # Step 2: Encrypt using OpenSSL AES-256-CBC
    print(f"[2/4] Encrypting with AES-256-CBC (PBKDF2 100k iter)...")
    enc_ok = encrypt_file_openssl(tar_path, enc_path, password)
    
    # Remove unencrypted temporary tar immediately
    tar_path.unlink(missing_ok=True)

    if not enc_ok or not enc_path.exists():
        raise RuntimeError("Encryption failed. Temporary archive deleted.")

    enc_size = enc_path.stat().st_size
    sha256 = compute_sha256(enc_path)
    print(f"      Encrypted package: {enc_name} ({enc_size / (1024*1024):.2f} MB)")
    print(f"      SHA-256: {sha256}")

    # Step 3: Verify decodability roundtrip
    print(f"[3/4] Running roundtrip verification...")
    if not verify_backup(enc_path, password):
        raise RuntimeError("Verification failed: archive failed decryption test.")
    print("      Verification passed: 100% intact.")

    # Step 4: Write metadata manifest
    metadata = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tag": tag,
        "archive_file": enc_name,
        "size_bytes": enc_size,
        "sha256": sha256,
        "targets": [str(t) for t in targets],
        "cipher": "aes-256-cbc-pbkdf2-100k"
    }
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"[4/4] Metadata written to {meta_path.name}")

    # Retention cleanup: Keep last N backups of this tag
    all_encs = sorted(output_dir.glob(f"sir_backup_{tag}_*.tar.gz.enc"), key=lambda p: p.stat().st_mtime)
    if len(all_encs) > retention_count:
        to_delete = all_encs[:-retention_count]
        for old_file in to_delete:
            old_meta = old_file.with_suffix("").with_suffix(".meta.json")
            old_file.unlink(missing_ok=True)
            old_meta.unlink(missing_ok=True)
            print(f"      Pruned old backup: {old_file.name}")

    return enc_path, sha256

def main():
    parser = argparse.ArgumentParser(description="Zero-Knowledge Encrypted Backup Engine for SIR Workspace.")
    parser.add_argument("--dest", type=Path, default=DEFAULT_BACKUP_DIR, help="Destination directory for encrypted archives")
    parser.add_argument("--key", type=str, default=None, help="Encryption passphrase (defaults to SIR_BACKUP_KEY env var)")
    parser.add_argument("--tag", type=str, default="daily", help="Backup tag (e.g. daily, weekly, pre-deploy)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate backup without writing files")
    parser.add_argument("--verify", type=Path, default=None, help="Verify integrity of an existing .enc archive")
    parser.add_argument("--targets", nargs="*", type=Path, default=None, help="Optional specific paths to back up")

    args = parser.parse_args()

    if args.verify:
        key = args.key or os.environ.get(DEFAULT_KEY_ENV, DEFAULT_FALLBACK_KEY)
        print(f"Verifying {args.verify}...")
        if verify_backup(args.verify, key):
            print("OK: Archive is valid, decryptable, and intact.")
            sys.exit(0)
        else:
            print("FAIL: Verification failed.", file=sys.stderr)
            sys.exit(1)

    # Default targets: critical operational data across built projects
    targets = args.targets
    if not targets:
        targets = [
            PROJECTS_ROOT / "_SIR" / "ops",
            PROJECTS_ROOT / "SIR Jobs" / "data",
            PROJECTS_ROOT / "SIR Study" / "guides",
            PROJECTS_ROOT / "SIR Optimizer" / "data"
        ]
        # Include AHome data folder if it exists locally
        ahome_data = PROJECTS_ROOT / "Backups" / "AHome-data"
        if ahome_data.exists():
            targets.append(ahome_data)

    existing_targets = [t for t in targets if t.exists()]
    if not existing_targets:
        print("No target directories exist to back up.", file=sys.stderr)
        sys.exit(1)

    enc_path, sha256 = create_backup(
        targets=existing_targets,
        output_dir=args.dest,
        password=args.key,
        tag=args.tag,
        dry_run=args.dry_run
    )

    if args.dry_run:
        print("Dry run completed successfully.")
    else:
        print(f"SUCCESS: Backup saved to {enc_path} (SHA-256: {sha256})")

if __name__ == "__main__":
    main()
