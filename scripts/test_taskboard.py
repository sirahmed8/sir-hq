#!/usr/bin/env python3
"""Unit tests for taskboard.py, hq_verifier.py AHome policy, and hq_autopilot.py cap."""

import json
import subprocess
import sys
import time
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import hq_autopilot  # noqa: E402
import hq_verifier  # noqa: E402
import taskboard  # noqa: E402


class PidAliveTests(unittest.TestCase):
    def test_invalid_pids_return_false(self):
        for bad in (0, -1, None, "", "not-a-pid", True, False):
            self.assertFalse(taskboard.pid_alive(bad))

    def test_bool_pid_does_not_spawn_tasklist(self):
        with mock.patch.object(taskboard.subprocess, "run") as mrun:
            self.assertFalse(taskboard.pid_alive(True))
            self.assertFalse(taskboard.pid_alive(False))
            mrun.assert_not_called()

    def test_alive_allowed_images(self):
        for img in ("bash.exe", "node.exe", "python.exe", "pythonw.exe"):
            proc = mock.Mock(stdout=f'"{img}","4321","Console","1","10,000 K"\n')
            with mock.patch.object(taskboard.subprocess, "run", return_value=proc) as mrun:
                self.assertTrue(taskboard.pid_alive(4321), msg=f"expected alive for {img}")
                _, kwargs = mrun.call_args
                self.assertEqual(kwargs.get("creationflags"), taskboard.CREATE_NO_WINDOW)

    def test_rejects_recycled_non_worker_image_and_missing_pid(self):
        for out in (
            '"svchost.exe","4321","Services","0","8,000 K"\n',
            "INFO: No tasks are running which match the specified criteria.\n",
            "",
        ):
            proc = mock.Mock(stdout=out)
            with mock.patch.object(taskboard.subprocess, "run", return_value=proc):
                self.assertFalse(taskboard.pid_alive(4321))

    def test_subprocess_error_returns_false(self):
        with mock.patch.object(taskboard.subprocess, "run", side_effect=subprocess.TimeoutExpired("tasklist", 10)):
            self.assertFalse(taskboard.pid_alive(4321))


class TaskboardSyncTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self._tmp = tempfile.TemporaryDirectory(prefix="sir_tb_test_")
        self.root = Path(self._tmp.name)
        self.board = self.root / "ops" / "tasks"
        for s in taskboard.STAGES:
            (self.board / s).mkdir(parents=True, exist_ok=True)
        self.queue = self.root / "ops" / "AUTOPILOT_QUEUE.json"
        self.state_file = self.root / "ops" / "autopilot_state.json"
        self.ver_dir = self.root / "ops" / "verifications"
        self.ver_dir.mkdir(parents=True, exist_ok=True)
        self.project_dir = self.root / "proj"
        self.project_dir.mkdir()

        self._patches = [
            mock.patch.object(taskboard, "ROOT", self.root),
            mock.patch.object(taskboard, "BOARD", self.board),
            mock.patch.object(taskboard, "QUEUE", self.queue),
            mock.patch.object(taskboard, "STATE_FILE", self.state_file),
            mock.patch.object(taskboard, "VERIFICATIONS", self.ver_dir),
        ]
        for p in self._patches:
            p.start()

    def tearDown(self):
        for p in reversed(self._patches):
            p.stop()
        self._tmp.cleanup()

    def _write_queue(self, items):
        self.queue.write_text(json.dumps(items), encoding="utf-8")

    def _write_state(self, data):
        self.state_file.write_text(json.dumps(data), encoding="utf-8")

    def test_inbox_to_active_requires_live_pid(self):
        self._write_queue([
            {"name": "t-dead", "folder": str(self.project_dir), "title": "Dead", "done": False},
            {"name": "t-live", "folder": str(self.project_dir), "title": "Live", "done": False},
        ])
        self._write_state({
            "last_tick": 1234.0,
            "runners": {"t-dead": {"pid": 111}, "t-live": {"pid": 222}},
        })
        with mock.patch.object(taskboard, "pid_alive", side_effect=lambda p: int(p) == 222):
            taskboard.sync()

        self.assertTrue((self.board / "inbox" / "5-t-dead.md").exists())
        self.assertTrue((self.board / "active" / "5-t-live.md").exists())

    def test_reclaims_dead_autopilot_runner_when_idle_and_preserves_other_state(self):
        self._write_queue([
            {"name": "t-stale", "folder": str(self.project_dir), "title": "Stale", "done": False},
            {"name": "t-busy", "folder": str(self.project_dir), "title": "Busy", "done": False},
            {"name": "t-manual", "folder": str(self.project_dir), "title": "Manual", "done": False},
        ])
        self._write_state({
            "listener_pid": 9999,
            "last_tick": 5555.0,
            "runners": {
                "t-stale": {"pid": 333, "started": 100.0},
                "t-busy": {"pid": 444, "started": 200.0},
            },
        })
        taskboard.write(
            self.board / "active" / "5-t-stale.md",
            {"folder": str(self.project_dir), "title": "Stale", "parallel_ok": "false",
             "claimed_by": "autopilot runner", "claimed_at": "11-14 01:00"},
            "body\n\n## Log\n",
        )
        taskboard.write(
            self.board / "active" / "5-t-busy.md",
            {"folder": str(self.project_dir), "title": "Busy", "parallel_ok": "false",
             "claimed_by": "autopilot runner", "claimed_at": "11-14 01:00"},
            "body\n\n## Log\n",
        )
        taskboard.write(
            self.board / "active" / "5-t-manual.md",
            {"folder": str(self.project_dir), "title": "Manual", "parallel_ok": "false",
             "claimed_by": "worker", "claimed_at": "11-14 01:00"},
            "body\n\n## Log\n",
        )
        busy_dir = self.root / "busy_proj"
        busy_dir.mkdir()
        self._write_queue([
            {"name": "t-stale", "folder": str(self.project_dir), "title": "Stale", "done": False},
            {"name": "t-busy", "folder": str(busy_dir), "title": "Busy", "done": False},
            {"name": "t-manual", "folder": str(self.project_dir), "title": "Manual", "done": False},
        ])

        def fake_activity(folder):
            return 5.0 if Path(folder) == busy_dir else 20.0

        with mock.patch.object(taskboard, "pid_alive", return_value=False), \
             mock.patch.object(taskboard, "minutes_since_activity", side_effect=fake_activity):
            taskboard.sync()

        reclaimed = self.board / "inbox" / "5-t-stale.md"
        self.assertTrue(reclaimed.exists(), "dead idle runner task must return to inbox")
        meta, body = taskboard.header(reclaimed.read_text(encoding="utf-8"))
        self.assertEqual(meta["claimed_by"], "")
        self.assertEqual(meta["claimed_at"], "")
        self.assertIn("returned to inbox", body)

        self.assertTrue((self.board / "active" / "5-t-busy.md").exists(), "recent folder activity keeps active")
        self.assertTrue((self.board / "active" / "5-t-manual.md").exists(), "non-autopilot claim stays active")

        saved_state = json.loads(self.state_file.read_text(encoding="utf-8"))
        self.assertEqual(saved_state["listener_pid"], 9999)
        self.assertEqual(saved_state["last_tick"], 5555.0)
        self.assertNotIn("pid", saved_state["runners"]["t-stale"])
        self.assertEqual(saved_state["runners"]["t-busy"]["pid"], 444)

    def test_verification_overall_pass_vs_fail_and_fix1(self):
        tasks = [
            "t-fail-table",
            "t-pass",
            "t-fail-fixed",
            "t-fail-still-broken",
        ]
        self._write_queue([{"name": n, "folder": str(self.project_dir), "title": n, "done": True} for n in tasks])
        self._write_state({"runners": {}})
        for n in tasks:
            taskboard.write(
                self.board / "review" / f"5-{n}.md",
                {"folder": str(self.project_dir), "title": n, "parallel_ok": "false",
                 "claimed_by": "autopilot runner", "claimed_at": "11-14 01:00"},
                "body\n\n## Log\n",
            )

        # Fail with PASS/FAIL header (the old false-positive bug!)
        (self.ver_dir / "t-fail-table.md").write_text(
            "# Verification: t-fail-table\n| Item | Desc | PASS/FAIL | Evidence |\n| 1 | a | FAIL | bad |\n\n## Overall: FAIL\n",
            encoding="utf-8",
        )
        # Unrelated file substring that shouldn't promote t-fail-table
        (self.ver_dir / "t-fail-table-extra.md").write_text("## Overall: PASS\n", encoding="utf-8")

        # Direct overall pass (case-insensitive check)
        (self.ver_dir / "t-pass.md").write_text(
            "| Item | Desc | PASS/FAIL | Evidence |\n\n## overall: pass\n",
            encoding="utf-8",
        )

        # Failed originally, fix1 passed
        (self.ver_dir / "t-fail-fixed.md").write_text(
            "| Item | Desc | PASS/FAIL | Evidence |\n\n## Overall: FAIL\n",
            encoding="utf-8",
        )
        (self.ver_dir / "t-fail-fixed-fix1.md").write_text("## Overall: PASS\n", encoding="utf-8")

        # Failed originally, fix1 also failed
        (self.ver_dir / "t-fail-still-broken.md").write_text("## Overall: FAIL\n", encoding="utf-8")
        (self.ver_dir / "t-fail-still-broken-fix1.md").write_text("## Overall: FAIL\n", encoding="utf-8")

        taskboard.sync()

        self.assertTrue((self.board / "review" / "5-t-fail-table.md").exists())
        self.assertTrue((self.board / "done" / "5-t-pass.md").exists())
        self.assertTrue((self.board / "done" / "5-t-fail-fixed.md").exists())
        self.assertTrue((self.board / "review" / "5-t-fail-still-broken.md").exists())

    def test_minutes_since_activity_ignores_past_80_ignored_dirty_lines(self):
        src_dir = self.project_dir / "src"
        src_dir.mkdir()
        app_file = src_dir / "app.py"
        app_file.write_text("print('fresh')\n", encoding="utf-8")
        old_commit_ts = str(int(time.time() - 7200))
        ignored_lines = [f" M assets/brand/icon_{i:03d}.png" for i in range(95)]
        porcelain = "\n".join(ignored_lines + [" M src/app.py"]) + "\n"
        with mock.patch.object(
            taskboard.subprocess,
            "run",
            side_effect=[
                mock.Mock(returncode=0, stdout=old_commit_ts),
                mock.Mock(returncode=0, stdout=porcelain),
            ],
        ):
            age = taskboard.minutes_since_activity(str(self.project_dir))
        self.assertLess(age, 1.0)

    def test_minutes_since_activity_root_scans_ops_public_dir(self):
        pub_dir = self.root / "ops" / "public"
        pub_dir.mkdir(parents=True, exist_ok=True)
        index_html = pub_dir / "index.html"
        index_html.write_text("<h1>fresh</h1>", encoding="utf-8")
        old_commit_ts = str(int(time.time() - 7200))
        with mock.patch.object(
            taskboard.subprocess,
            "run",
            return_value=mock.Mock(returncode=0, stdout=old_commit_ts),
        ):
            age = taskboard.minutes_since_activity(str(self.root))
        self.assertLess(age, 1.0)

    def test_sync_handles_non_dict_runner_entry(self):
        self._write_queue([{"name": "t-null-runner", "folder": str(self.project_dir), "title": "Null", "done": False}])
        self._write_state({"runners": {"t-null-runner": None}})
        res = taskboard.sync()
        self.assertIn("board synced", res)
        self.assertTrue((self.board / "inbox" / "5-t-null-runner.md").exists())


class VerifierAndAutopilotTests(unittest.TestCase):
    def test_max_parallel_capped_at_5(self):
        self.assertEqual(hq_autopilot.MAX_PARALLEL, 5)

    def test_enforce_evidence_rewrites_lowercase_overall_and_missing_header(self):
        text_lower = (
            "# Verification: t\n\n"
            "| Item | Description | PASS/FAIL | Evidence |\n"
            "| 1 | check | PASS | - |\n\n"
            "## overall: pass\n"
        )
        new_text, changed, rows = hq_verifier.enforce_evidence(text_lower)
        self.assertEqual(changed, 1)
        self.assertEqual(hq_verifier.overall_of(new_text, rows), "FAIL")
        self.assertRegex(new_text, r"(?m)^## Overall: FAIL$")
        self.assertIsNone(hq_verifier.re.search(r"(?im)^##\s*Overall:\s*PASS\b", new_text))

        text_missing = (
            "# Verification: t\n\n"
            "| Item | Description | PASS/FAIL | Evidence |\n"
            "| 1 | check | PASS | n/a |\n"
        )
        new_text2, changed2, rows2 = hq_verifier.enforce_evidence(text_missing)
        self.assertEqual(changed2, 1)
        self.assertEqual(hq_verifier.overall_of(new_text2, rows2), "FAIL")
        self.assertRegex(new_text2, r"(?m)^## Overall: FAIL$")

    def test_ahome_verifier_allowed_with_privacy_guard(self):
        import tempfile
        with tempfile.TemporaryDirectory(prefix="sir_ver_test_") as tmp:
            ver_dir = Path(tmp) / "verifications"
            ver_dir.mkdir()
            shots_dir = ver_dir / "evidence"
            ahome_task = {"name": "r75-ahome-calling-fix", "folder": "D:/Projects/AHome", "title": "AHome calling", "done": True}

            prompt = hq_verifier.build_prompt(ahome_task, [])
            self.assertIn("apps/", prompt)
            self.assertIn("unit/integration tests", prompt)
            self.assertIn("synthetic", prompt.lower())
            for forbidden in ("messages", "notes", "photos", "calendar", "vault"):
                self.assertIn(forbidden, prompt.lower())

            # Also triggers guard when task name has ahome even with generic root folder
            prompt_generic = hq_verifier.build_prompt(
                {"name": "r81-ahome-check", "folder": "D:/Projects", "title": "Check", "done": True}, []
            )
            self.assertIn("AHOME PRIVACY GUARD", prompt_generic)

            seen = []
            with mock.patch.object(hq_verifier, "VERIFICATIONS", ver_dir), \
                 mock.patch.object(hq_verifier, "SHOTS", shots_dir), \
                 mock.patch.object(hq_verifier, "game_mode_active", return_value=False), \
                 mock.patch.object(hq_verifier, "load_queue", return_value=[ahome_task]), \
                 mock.patch.object(hq_verifier, "verify_task", side_effect=lambda t, d: seen.append(t["name"]) or {"task": t["name"], "status": "dry"}):
                rc = hq_verifier.main(["--dry"])
            self.assertEqual(rc, 0)
            self.assertEqual(seen, ["r75-ahome-calling-fix"])


if __name__ == "__main__":
    unittest.main()
