#!/usr/bin/env python3
"""
test_backup_offsite_encrypted.py - Unit tests for encrypted backup daemon (OPS-GAP-02)
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

from backup_offsite_encrypted import (
    create_backup,
    verify_backup,
    compute_sha256,
    encrypt_file_openssl,
    decrypt_file_openssl
)

class TestEncryptedBackup(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="sir_test_backup_"))
        self.source_dir = self.temp_dir / "test_source"
        self.dest_dir = self.temp_dir / "test_dest"
        self.source_dir.mkdir(parents=True, exist_ok=True)
        self.dest_dir.mkdir(parents=True, exist_ok=True)

        # Create dummy test files
        (self.source_dir / "important_data.json").write_text('{"status": "ok", "count": 42}', encoding="utf-8")
        (self.source_dir / "notes.txt").write_text("Confidential operational state.", encoding="utf-8")
        
        # Create excluded folders to verify filter
        node_modules = self.source_dir / "node_modules"
        node_modules.mkdir()
        (node_modules / "junk.js").write_text("console.log('junk');", encoding="utf-8")

        self.test_password = "test-encryption-key-12345"

    def tearDown(self):
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_backup_create_and_verify(self):
        enc_path, sha256 = create_backup(
            targets=[self.source_dir],
            output_dir=self.dest_dir,
            password=self.test_password,
            tag="test"
        )
        self.assertIsNotNone(enc_path)
        self.assertTrue(enc_path.exists())
        self.assertEqual(compute_sha256(enc_path), sha256)

        # Verification with correct password must pass
        is_valid = verify_backup(enc_path, self.test_password)
        self.assertTrue(is_valid, "Backup verification with correct password must succeed")

        # Verification with incorrect password must fail
        is_invalid = verify_backup(enc_path, "wrong-password")
        self.assertFalse(is_invalid, "Backup verification with wrong password must fail")

    def test_dry_run(self):
        enc_path, sha256 = create_backup(
            targets=[self.source_dir],
            output_dir=self.dest_dir,
            password=self.test_password,
            tag="dry",
            dry_run=True
        )
        self.assertIsNone(enc_path)
        self.assertEqual(len(list(self.dest_dir.glob("*.enc"))), 0)

if __name__ == "__main__":
    unittest.main()
