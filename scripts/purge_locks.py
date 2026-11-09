#!/usr/bin/env python3
"""
purge_locks.py - Automated Stale Lock Purge Worker for SIR Headquarters.
Follows AGENTS.md rule: locks older than 2 hours in _SIR/ops/locks/ are stale.
Preserves active locks, removes abandoned locks, logs structured output.
"""

import sys
import os
import time
import argparse
from pathlib import Path
from datetime import datetime, timezone

# Ensure project paths are resolved relative to _SIR
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_LOCKS_DIR = REPO_ROOT / "ops" / "locks"

def parse_lock_file(file_path: Path):
    """
    Parses a lock file. A standard lock contains:
    owner: <agent/worker>
    acquired_at: <ISO timestamp>
    pid: <process id>
    """
    try:
        content = file_path.read_text(encoding="utf-8").strip()
        lines = content.splitlines()
        data = {}
        for line in lines:
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip().lower()] = v.strip()
        return data
    except Exception:
        return {}

def purge_stale_locks(locks_dir: Path, max_age_hours: float = 2.0, dry_run: bool = False, verbose: bool = False):
    """
    Inspects all lock files in locks_dir. Purges files older than max_age_hours.
    Returns (stale_purged_count, active_kept_count, errors_count).
    """
    if not locks_dir.exists():
        locks_dir.mkdir(parents=True, exist_ok=True)
        return 0, 0, 0

    now_ts = time.time()
    max_age_sec = max_age_hours * 3600.0

    stale_count = 0
    active_count = 0
    error_count = 0

    # Scan for any lock files (.lock, .txt, or extensionless files)
    lock_files = [f for f in locks_dir.iterdir() if f.is_file() and not f.name.startswith(".")]

    for lock_path in lock_files:
        try:
            mtime = lock_path.stat().st_mtime
            age_sec = now_ts - mtime
            age_hours = age_sec / 3600.0

            # Check if file has an explicit timestamp inside, fallback to mtime
            parsed = parse_lock_file(lock_path)
            iso_time = parsed.get("acquired_at") or parsed.get("timestamp")
            if iso_time:
                try:
                    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
                    age_from_payload = (datetime.now(timezone.utc) - dt).total_seconds()
                    if age_from_payload > 0:
                        age_sec = age_from_payload
                        age_hours = age_sec / 3600.0
                except Exception:
                    pass # Fall back to mtime

            is_stale = age_sec > max_age_sec

            if is_stale:
                stale_count += 1
                owner = parsed.get("owner", "unknown")
                if verbose or dry_run:
                    action = "[DRY-RUN] Would remove" if dry_run else "[PURGED]"
                    print(f"{action} stale lock: {lock_path.name} (age: {age_hours:.1f}h, owner: {owner})")
                if not dry_run:
                    lock_path.unlink(missing_ok=True)
            else:
                active_count += 1
                if verbose:
                    print(f"[ACTIVE] Preserving lock: {lock_path.name} (age: {age_hours:.1f}h)")

        except Exception as e:
            error_count += 1
            print(f"[ERROR] Failed processing lock file {lock_path}: {e}", file=sys.stderr)

    return stale_count, active_count, error_count

def main():
    parser = argparse.ArgumentParser(description="Purge stale lock files in SIR workspace.")
    parser.add_argument("--locks-dir", type=Path, default=DEFAULT_LOCKS_DIR, help="Path to locks directory")
    parser.add_argument("--max-age-hours", type=float, default=2.0, help="Maximum lock age in hours (default: 2.0)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate purge without deleting files")
    parser.add_argument("--verbose", action="store_true", help="Print detailed lock information")

    args = parser.parse_args()

    stale, active, errors = purge_stale_locks(
        locks_dir=args.locks_dir,
        max_age_hours=args.max_age_hours,
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    summary = f"Stale locks purged: {stale}, Active locks preserved: {active}, Errors: {errors}"
    if args.dry_run:
        summary = f"[DRY-RUN] {summary}"
    print(summary)
    sys.exit(1 if errors > 0 else 0)

if __name__ == "__main__":
    main()
