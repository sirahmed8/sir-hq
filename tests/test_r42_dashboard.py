"""Tests for the Control Room verification and suggestion data.

The Verification and Suggestions sections of the Control Room are fed by
plans/dashboard_feeds.py (verification verdicts and rounds) and plans/dashboard_notes.py
(suggestions). Both read ops/ read-only; here every file lives in a temporary folder.

Run: python -m pytest tests/test_r42_dashboard.py -q
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "plans"))

import dashboard_feeds as feeds  # noqa: E402
import dashboard_notes as notes  # noqa: E402

VERIFICATION = "| Item | Description | PASS/FAIL | Evidence |\n|---|---|---|---|\n{rows}\n"


class LiveFeedsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ops = Path(self.tmp.name)
        self.saved_feeds = feeds.OPS
        self.saved_notes = notes.OPS
        feeds.OPS = str(self.ops)
        notes.OPS = str(self.ops)

    def tearDown(self):
        feeds.OPS = self.saved_feeds
        notes.OPS = self.saved_notes

    def write_verification(self, name, rows):
        folder = self.ops / "verifications"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / name).write_text(VERIFICATION.format(rows=rows), encoding="utf-8")

    def write_round_labels(self, items):
        (self.ops / "round_labels.json").write_text(json.dumps(items), encoding="utf-8")

    def write_suggestions(self, body):
        (self.ops / "SUGGESTIONS.md").write_text(body, encoding="utf-8")

    def test_all_pass_verification_is_pass(self):
        self.write_verification("r50-demo.md", "| 1 | a | PASS | tests |")
        self.assertEqual(feeds.verification_verdicts(), {"r50-demo": "PASS"})

    def test_one_failed_row_makes_the_verification_fail(self):
        self.write_verification("r50-demo.md", "| 1 | a | PASS | tests |\n| 2 | b | FAIL | red ci |")
        self.assertEqual(feeds.verification_verdicts(), {"r50-demo": "FAIL"})

    def test_missing_verifications_folder_is_empty_not_an_error(self):
        self.assertEqual(feeds.verification_verdicts(), {})

    def test_round_is_verified_only_when_a_verification_passes(self):
        self.write_round_labels([
            {"label": "Laptop R1", "task": "r15-laptop", "title": "Laptop work", "state": "done by worker"},
            {"label": "Jobs R1", "task": "r15-jobs", "title": "Jobs work", "state": "done by worker"},
            {"label": "Study R1", "task": "r15-study", "title": "Study work", "state": "running"},
        ])
        self.write_verification("r15-laptop.md", "| 1 | a | PASS | tests |")
        self.write_verification("r15-jobs.md", "| 1 | a | PASS | tests |\n| 2 | b | FAIL | red ci |")
        rounds = {r["task"]: r["verified"] for r in feeds.rounds()}
        self.assertEqual(rounds["r15-laptop"], "verified")
        self.assertEqual(rounds["r15-jobs"], "failed")
        self.assertEqual(rounds["r15-study"], "not verified")

    def test_suggestions_are_counted_by_status(self):
        self.write_suggestions(
            "# Suggestions from Scouts (HQ)\n\n"
            "## 2026-11-12T03:00 | SIR Jobs | high\n\n"
            "**Finding:** Tab bar hides the active tab\n"
            "**Proposed Brief:** r43-jobs-tabbar\n"
            "**Status:** pending\n\n---\n\n"
            "## 2026-11-12T04:00 | SIR Study | medium\n\n"
            "**Finding:** Tables overflow on phones\n"
            "**Status:** approved\n\n---\n")
        result = notes.suggestions()
        self.assertEqual(result["counts"], {"pending": 1, "approved": 1, "rejected": 0})
        self.assertEqual(len(result["pending"]), 1)
        self.assertEqual(result["pending"][0]["project"], "SIR Jobs")
        self.assertEqual(result["pending"][0]["severity"], "high")
        self.assertEqual(result["pending"][0]["finding"], "Tab bar hides the active tab")

    def test_missing_suggestions_file_gives_empty_counts(self):
        result = notes.suggestions()
        self.assertEqual(result["counts"], {"pending": 0, "approved": 0, "rejected": 0})
        self.assertEqual(result["pending"], [])

    def test_notes_collect_never_raises_on_a_missing_ops_folder(self):
        collected = notes.collect()
        self.assertEqual(collected["suggestions"]["counts"], {"pending": 0, "approved": 0, "rejected": 0})
        self.assertEqual(collected["owner_actions"], [])


if __name__ == "__main__":
    unittest.main()
