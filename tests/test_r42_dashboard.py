"""Tests for the Control Room data behind the r42 Verification and Suggestions sections.

Run: python -m pytest tests/test_r42_dashboard.py -q
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE.parent / "plans" / "generate_dashboard.py"
sys.path.insert(0, str(HERE.parent / "plans"))

spec = importlib.util.spec_from_file_location("generate_dashboard", MODULE_PATH)
dashboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dashboard)


class DashboardSectionsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ops = Path(self.tmp.name)
        (self.ops / "verifications").mkdir()
        self.saved = dashboard.OPS
        dashboard.OPS = str(self.ops)

    def tearDown(self):
        dashboard.OPS = self.saved

    def test_verification_counts_and_overall(self):
        (self.ops / "verifications" / "r50-demo.md").write_text(
            "| Item | D | PASS/FAIL | Evidence |\n"
            "| 1 | a | PASS | tests |\n"
            "| 2 | b | FAIL | red ci |\n\n## Overall: FAIL\n", encoding="utf-8")
        rows = dashboard.parse_verifications()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["task"], "r50-demo")
        self.assertEqual(rows[0]["overall"], "FAIL")
        self.assertEqual((rows[0]["pass"], rows[0]["fail"]), (1, 1))

    def test_missing_folder_is_empty_not_an_error(self):
        dashboard.OPS = str(self.ops / "nope")
        self.assertEqual(dashboard.parse_verifications(), [])

    def test_suggestions_are_parsed_with_status(self):
        (self.ops / "SUGGESTIONS.md").write_text(
            "# Suggestions from Scouts (HQ)\n\n"
            "## 2026-11-12T03:00 | SIR Jobs | high\n\n"
            "**Finding:** Tab bar hides the active tab\n"
            "**Evidence:** ops/scout-evidence/jobs-390.png\n"
            "**Proposed Brief:** r43-jobs-tabbar\n"
            "**Project:** SIR Jobs\n"
            "**Severity:** high\n"
            "**Category:** bug\n"
            "**Status:** pending\n"
            "**Id:** sug-x\n\n---\n", encoding="utf-8")
        rows = dashboard.parse_suggestions()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["project"], "SIR Jobs")
        self.assertEqual(rows[0]["severity"], "high")
        self.assertEqual(rows[0]["status"], "pending")
        self.assertEqual(rows[0]["proposed_brief"], "r43-jobs-tabbar")

    def test_empty_suggestions_file(self):
        (self.ops / "SUGGESTIONS.md").write_text("# Suggestions\n", encoding="utf-8")
        self.assertEqual(dashboard.parse_suggestions(), [])


if __name__ == "__main__":
    unittest.main()
