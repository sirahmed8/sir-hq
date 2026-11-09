#!/usr/bin/env python3
"""
test_purge_locks.py - Unit test suite for stale lock auto-purge worker.
"""

import os
import time
import shutil
import tempfile
import unittest
from pathlib import Path
from datetime import datetime, timezone, timedelta

from purge_locks import purge_stale_locks, parse_lock_file

class TestPurgeLocks(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp(prefix="sir_test_locks_"))

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_preserve_active_lock(self):
        active_lock = self.test_dir / "sir-active.lock"
        active_lock.write_text("owner: test_worker\npid: 1234\n", encoding="utf-8")
        
        stale, active, errors = purge_stale_locks(self.test_dir, max_age_hours=2.0)
        self.assertEqual(stale, 0)
        self.assertEqual(active, 1)
        self.assertEqual(errors, 0)
        self.assertTrue(active_lock.exists(), "Active lock should NOT be deleted")

    def test_purge_stale_lock_by_mtime(self):
        stale_lock = self.test_dir / "sir-stale.lock"
        stale_lock.write_text("owner: old_worker\n", encoding="utf-8")
        
        # Set mtime back by 3 hours (10800 seconds)
        old_time = time.time() - 10800
        os.utime(stale_lock, (old_time, old_time))

        stale, active, errors = purge_stale_locks(self.test_dir, max_age_hours=2.0)
        self.assertEqual(stale, 1)
        self.assertEqual(active, 0)
        self.assertEqual(errors, 0)
        self.assertFalse(stale_lock.exists(), "Stale lock should be deleted")

    def test_dry_run_preserves_stale_lock(self):
        stale_lock = self.test_dir / "sir-dry-stale.lock"
        stale_lock.write_text("owner: abandoned_worker\n", encoding="utf-8")
        
        old_time = time.time() - 15000
        os.utime(stale_lock, (old_time, old_time))

        stale, active, errors = purge_stale_locks(self.test_dir, max_age_hours=2.0, dry_run=True)
        self.assertEqual(stale, 1)
        self.assertEqual(active, 0)
        self.assertEqual(errors, 0)
        self.assertTrue(stale_lock.exists(), "Dry-run should NOT delete stale lock")

    def test_parse_lock_file_with_iso_timestamp(self):
        payload_lock = self.test_dir / "sir-payload.lock"
        old_iso = (datetime.now(timezone.utc) - timedelta(hours=3)).isoformat()
        payload_lock.write_text(f"owner: payload_worker\nacquired_at: {old_iso}\n", encoding="utf-8")

        stale, active, errors = purge_stale_locks(self.test_dir, max_age_hours=2.0)
        self.assertEqual(stale, 1)
        self.assertEqual(active, 0)
        self.assertFalse(payload_lock.exists(), "Stale lock based on payload timestamp should be deleted")

    def test_corrupt_empty_lock_file(self):
        empty_lock = self.test_dir / "empty.lock"
        empty_lock.write_text("", encoding="utf-8")
        
        old_time = time.time() - 8000
        os.utime(empty_lock, (old_time, old_time))

        stale, active, errors = purge_stale_locks(self.test_dir, max_age_hours=2.0)
        self.assertEqual(stale, 1)
        self.assertEqual(errors, 0)
        self.assertFalse(empty_lock.exists(), "Corrupt old lock should be deleted")

if __name__ == "__main__":
    unittest.main()
