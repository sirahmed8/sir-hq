"""Tests for the r42 free-agent team: verifier evidence rules, scout dedupe, review loop, notifications.

Run: python -m pytest tests/test_r42_team.py -q
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


team = load("hq_team")
verifier = load("hq_verifier")
scout = load("scout")
review = load("hq_review")
notify = load("hq_notify")


class TempRoot(unittest.TestCase):
    """Point every team file at a temporary folder so tests never touch the real queue or suggestions."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        (root / "ops" / "briefs").mkdir(parents=True)
        (root / "ops" / "bus").mkdir(parents=True)
        self.root = root
        self.queue = root / "ops" / "AUTOPILOT_QUEUE.json"
        self.suggestions = root / "ops" / "SUGGESTIONS.md"
        self.rejects = root / "ops" / "suggestion-rejects.json"
        self.queue.write_text("[]", encoding="utf-8")
        self.suggestions.write_text("# Suggestions\n\n", encoding="utf-8")
        self.patches = [
            (team, "QUEUE_FILE", self.queue),
            (team, "SUGGESTIONS_FILE", self.suggestions),
            (team, "REJECTS_FILE", self.rejects),
            (review, "OPS", root / "ops"),
            (review, "APPROVALS_JSONL", root / "ops" / "approvals.jsonl"),
            (review, "STATE", root / "ops" / "review-state.json"),
            (notify, "VERIFICATIONS", root / "ops" / "verifications"),
            (notify, "STATE", root / "ops" / "notify-state.json"),
        ]
        self.saved = [(mod, name, getattr(mod, name)) for mod, name, _v in self.patches]
        for mod, name, value in self.patches:
            setattr(mod, name, value)

    def tearDown(self):
        for mod, name, value in self.saved:
            setattr(mod, name, value)


class EvidenceRuleTest(TempRoot):
    def test_pass_without_evidence_is_downgraded(self):
        text = ("# Verification: t\n\n## Checklist Results\n"
                "| Item | Description | PASS/FAIL | Evidence |\n"
                "| 1 | tab bar | PASS | tests pass |\n"
                "| 2 | lock screen | PASS |  |\n"
                "| 3 | ci | FAIL | red run 123 |\n\n## Overall: PASS\n")
        new_text, changed, rows = verifier.enforce_evidence(text)
        self.assertEqual(changed, 1)
        verdicts = {r["item"]: r["verdict"] for r in rows}
        self.assertEqual(verdicts["1"], "PASS")
        self.assertEqual(verdicts["2"], "FAIL")
        self.assertIn("## Overall: FAIL", new_text)
        self.assertIn("Verifier notes", new_text)

    def test_overall_defaults_to_fail_without_rows(self):
        self.assertEqual(verifier.overall_of("nothing here", []), "FAIL")

    def test_parse_rows_reads_only_pass_fail(self):
        text = "| Item | Desc | Verdict | Evidence |\n|---|---|---|---|\n| 1 | a | PASS | shot.png |\n"
        rows = verifier.parse_rows(text)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["evidence"], "shot.png")

    def test_checklist_files_returns_brief(self):
        brief = self.root / "ops" / "briefs" / "r99-demo.md"
        brief.write_text("1. item", encoding="utf-8")
        saved = verifier.OPS
        try:
            verifier.OPS = self.root / "ops"
            found = verifier.checklist_files("r99-demo", str(self.root))
        finally:
            verifier.OPS = saved
        self.assertTrue(any("r99-demo" in str(p) for p in found))


class SuggestionFileTest(TempRoot):
    def test_roundtrip_keeps_fields_and_id(self):
        entry = {
            "header": "2026-11-12T03:00 | SIR Jobs | high",
            "fields": {"Finding": "Tab bar hides the active tab", "Evidence": "shot.png",
                       "Proposed Brief": "r43-jobs-tabbar", "Project": "SIR Jobs", "Severity": "high",
                       "Category": "bug", "Status": "pending"},
            "extra": [],
            "id": team.suggestion_id("Tab bar hides the active tab"),
        }
        team.rewrite_suggestions([entry])
        parsed = team.load_suggestions()
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["fields"]["Finding"], "Tab bar hides the active tab")
        self.assertEqual(parsed[0]["fields"]["Status"], "pending")
        self.assertEqual(parsed[0]["id"], entry["id"])

    def test_id_is_stable_and_normalized(self):
        a = team.suggestion_id("Tab bar hides  the active tab!")
        b = team.suggestion_id("tab bar hides the active tab")
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("sug-"))

    def test_reject_is_never_proposed_again(self):
        team.add_reject("Tab bar hides the active tab", "owner rejected")
        self.assertTrue(team.is_rejected("tab bar hides the active tab"))
        self.assertFalse(team.is_rejected("a different finding entirely"))


class DedupeTest(TempRoot):
    def test_open_queue_task_blocks_the_same_finding(self):
        self.queue.write_text(json.dumps([{"name": "r43-jobs-tabbar", "folder": "D:/Projects/SIR Jobs",
                                           "title": "r43-jobs-tabbar", "done": False}]), encoding="utf-8")
        self.assertTrue(team.is_duplicate("Anything at all", "r43-jobs-tabbar"))

    def test_existing_suggestion_blocks_a_near_copy(self):
        entry = {"header": "2026-11-12T03:00 | SIR Jobs | high",
                 "fields": {"Finding": "The tab bar hides the active tab on phones", "Evidence": "x",
                            "Project": "SIR Jobs", "Severity": "high", "Status": "pending"},
                 "extra": [], "id": team.suggestion_id("The tab bar hides the active tab on phones")}
        team.rewrite_suggestions([entry])
        self.assertTrue(team.is_duplicate("The tab bar hides the active tab on phones at 390 px"))

    def test_new_finding_is_not_duplicate(self):
        self.assertFalse(team.is_duplicate("The save button loses the draft when the network drops"))


class ScoutTest(TempRoot):
    def test_parse_findings_keeps_valid_rows_only(self):
        output = ('noise [{"finding": "Tab bar hides the active tab", "evidence": "shot.png", '
                  '"severity": "high", "category": "bug", "proposed_brief": "r43-jobs-tabbar"}, '
                  '{"finding": "short", "severity": "low"}] tail')
        rows = scout.parse_findings(output)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["severity"], "high")
        self.assertEqual(rows[0]["proposed_brief"], "r43-jobs-tabbar")

    def test_parse_findings_survives_garbage(self):
        self.assertEqual(scout.parse_findings("no json at all"), [])
        self.assertEqual(scout.parse_findings("[not json]"), [])

    def test_append_findings_dedupes(self):
        rows = [{"finding": "Tab bar hides the active tab on phones", "evidence": "shot.png",
                 "severity": "high", "category": "bug", "proposed_brief": "r43-jobs-tabbar"}]
        added, dropped = scout.append_findings("sir-jobs", rows)
        self.assertEqual((added, dropped), (1, 0))
        added2, dropped2 = scout.append_findings("sir-jobs", rows)
        self.assertEqual((added2, dropped2), (0, 1))

    def test_lens_rotates_per_project(self):
        team.save_json(scout.LENSES_FILE, {})
        first, idx1 = scout.next_lens("sir-jobs")
        second, idx2 = scout.next_lens("sir-jobs")
        self.assertNotEqual(first, second)
        self.assertEqual((idx1, idx2), (0, 1))

    def test_forced_lens_wins(self):
        lens, idx = scout.next_lens("sir-jobs", "a forced lens")
        self.assertEqual((lens, idx), ("a forced lens", -1))


class ReviewTest(TempRoot):
    def test_folder_lookup_by_display_name(self):
        self.assertEqual(review.folder_for("SIR Jobs"), "D:/Projects/SIR Jobs")
        self.assertEqual(review.folder_for("sir-jobs"), "D:/Projects/SIR Jobs")
        self.assertEqual(review.folder_for("Nope"), "")

    def test_brief_name_prefers_valid_proposal(self):
        entry = {"fields": {"Proposed Brief": "r43-jobs-tabbar", "Project": "SIR Jobs",
                            "Finding": "Tab bar hides the active tab"}, "id": "x"}
        self.assertEqual(review.brief_name(entry), "r43-jobs-tabbar")

    def test_brief_name_falls_back_to_finding(self):
        entry = {"fields": {"Proposed Brief": "", "Project": "SIR Jobs",
                            "Finding": "Tab bar hides the active tab"}, "id": "x"}
        name = review.brief_name(entry)
        self.assertTrue(name.startswith("r43-sir-jobs-"))
        self.assertRegex(name, r"^[a-z0-9][a-z0-9-]+$")

    def test_owner_answers_reads_only_suggestion_ids(self):
        (self.root / "ops" / "approvals.jsonl").write_text(
            '{"id": "sug-a", "answer": "approved"}\n{"id": "other", "answer": "approved"}\n'
            '{"id": "sug-b", "answer": "rejected"}\n', encoding="utf-8")
        answers = review.owner_answers()
        self.assertEqual(answers, {"sug-a": "approved", "sug-b": "rejected"})

    def test_reject_records_a_permanent_block(self):
        entry = {"fields": {"Finding": "Tab bar hides the active tab", "Status": "pending"}, "id": "sug-a"}
        review.reject(entry, "owner rejected on Telegram")
        self.assertEqual(entry["fields"]["Status"], "rejected")
        self.assertTrue(team.is_rejected("Tab bar hides the active tab"))


class NotifyTest(TempRoot):
    def test_overall_and_rows(self):
        folder = self.root / "ops" / "verifications"
        folder.mkdir(parents=True, exist_ok=True)
        good = folder / "a.md"
        good.write_text("| Item | D | PASS/FAIL | Evidence |\n| 1 | x | PASS | test |\n\n## Overall: PASS\n",
                        encoding="utf-8")
        bad = folder / "b.md"
        bad.write_text("| Item | D | PASS/FAIL | Evidence |\n| 1 | x | FAIL | red |\n\n## Overall: FAIL\n",
                       encoding="utf-8")
        self.assertEqual(notify.overall_of(good), "PASS")
        self.assertEqual(notify.overall_of(bad), "FAIL")
        self.assertEqual(notify.rows_of(bad)[0]["verdict"], "FAIL")

    def test_fails_dry_sends_nothing(self):
        folder = self.root / "ops" / "verifications"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "b.md").write_text("## Overall: FAIL\n| 1 | x | FAIL | red |\n", encoding="utf-8")
        self.assertEqual(notify.fails(["--dry"]), 0)


if __name__ == "__main__":
    unittest.main()
