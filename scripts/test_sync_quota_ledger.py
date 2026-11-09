#!/usr/bin/env python3
"""
test_sync_quota_ledger.py - Unit test suite for sync_quota_ledger.py (HQ-02)
"""

import tempfile
import shutil
import unittest
from pathlib import Path

from sync_quota_ledger import (
    parse_percentage,
    evaluate_rotation_needed,
    append_ledger_entry
)

class TestSyncQuotaLedger(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="sir_test_ledger_"))
        self.ledger_file = self.temp_dir / "TEST_LEDGER.md"

    def tearDown(self):
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_parse_percentage(self):
        self.assertEqual(parse_percentage("15%"), 15.0)
        self.assertEqual(parse_percentage("24.5%"), 24.5)
        self.assertEqual(parse_percentage("100"), 100.0)
        self.assertEqual(parse_percentage("0%"), 0.0)
        self.assertIsNone(parse_percentage("invalid"))
        self.assertIsNone(parse_percentage(""))

    def test_evaluate_rotation_healthy(self):
        needs_rot, reason = evaluate_rotation_needed(weekly_left_str="24%", five_hour_left_str="100%")
        self.assertFalse(needs_rot)
        self.assertIn("healthy", reason.lower())

    def test_evaluate_rotation_weekly_breached(self):
        needs_rot, reason = evaluate_rotation_needed(weekly_left_str="12%", five_hour_left_str="80%")
        self.assertTrue(needs_rot)
        self.assertIn("Weekly quota is 12%", reason)

    def test_evaluate_rotation_five_hour_breached(self):
        needs_rot, reason = evaluate_rotation_needed(weekly_left_str="50%", five_hour_left_str="10%")
        self.assertTrue(needs_rot)
        self.assertIn("5-hour quota is 10%", reason)

    def test_append_ledger_entry(self):
        ok = append_ledger_entry(
            ledger_path=self.ledger_file,
            account="test_account",
            models="Gemini 3.8",
            five_hour_left="80%",
            weekly_left="24%",
            five_hour_resets="4h",
            weekly_resets="5d",
            note="unit test note"
        )
        self.assertTrue(ok)
        self.assertTrue(self.ledger_file.exists())
        
        content = self.ledger_file.read_text(encoding="utf-8")
        self.assertIn("| test_account | Gemini 3.8 | 80% | 24% | 4h | 5d | unit test note |", content)

if __name__ == "__main__":
    unittest.main()
