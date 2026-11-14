"""Unit tests for the free-model pool pick and the headless agent command table.

Covers the 2026-11-14 verifier fix: the pool pick can exclude tools that cannot
verify (aider has no file-read tool), and every pool tool has a real command
(the missing `pi` entry made the verifier die with exit 127 "unknown tool").
"""
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cli_pool  # noqa: E402
import hq_team  # noqa: E402
import hq_verifier  # noqa: E402

NO_WINDOW = 0x08000000


class PickExcludeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self._state = cli_pool.STATE
        self._pool = list(cli_pool.POOL)
        cli_pool.STATE = Path(self.tmp.name) / "pool.json"
        cli_pool.POOL = ["aider|cerebras/x", "pi|radius/recursive/flint", "devin|swe-2-flash-medium"]

    def tearDown(self):
        cli_pool.STATE = self._state
        cli_pool.POOL = self._pool
        self.tmp.cleanup()

    def test_exclude_never_returns_excluded_tool(self):
        for _ in range(6):
            entry = cli_pool.pick(exclude=("aider",))
            self.assertFalse(entry.startswith("aider|"), entry)

    def test_without_exclude_the_excluded_tool_is_still_reachable(self):
        picks = {cli_pool.pick() for _ in range(3)}
        self.assertTrue(any(p.startswith("aider|") for p in picks), picks)


class AgentCommandTest(unittest.TestCase):
    def test_pi_has_a_real_command(self):
        cmd = hq_team.agent_command("pi|radius/recursive/flint", "PROMPT")
        self.assertTrue(cmd)
        self.assertIn("--model", cmd)
        self.assertIn("radius/recursive/flint", cmd)

    def test_every_pool_entry_builds_a_command(self):
        for entry in cli_pool.POOL:
            tool = entry.split("|", 1)[0]
            if tool in ("qwen", "goose", "crush"):
                continue  # local tools are wired with env, checked elsewhere
            self.assertTrue(hq_team.agent_command(entry, "P"), entry)

    def test_unknown_tool_is_empty(self):
        self.assertEqual(hq_team.agent_command("not-a-tool|x", "P"), [])


class VerifyRetryTest(unittest.TestCase):
    def test_retries_until_a_model_writes_the_file(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        vdir = Path(tmp.name) / "verifications"
        vdir.mkdir()
        task = {"name": "fake-task", "folder": tmp.name, "title": "fake"}
        calls = {"n": 0, "picks": []}

        def fake_pick(exclude=()):
            calls["picks"].append(tuple(exclude))
            return "pi|radius/recursive/flint"

        def fake_run(pick, prompt, cwd, tag, timeout=1800):
            calls["n"] += 1
            if calls["n"] == 2:  # first model writes nothing, second writes the file
                (vdir / "fake-task.md").write_text(
                    "# Verification: fake-task\n\n## Checklist Results\n"
                    "| Item | Description | PASS/FAIL | Evidence |\n"
                    "|------|-------------|-----------|----------|\n"
                    "| 1 | thing | PASS | ran npm test, 5 passed |\n\n## Overall: PASS\n",
                    encoding="utf-8")
            return 1, "boom", Path(tmp.name) / "log.txt"

        orig = (hq_verifier.VERIFICATIONS, hq_verifier.pool_pick, hq_verifier.run_agent, hq_verifier.log)
        hq_verifier.VERIFICATIONS = vdir
        hq_verifier.pool_pick = fake_pick
        hq_verifier.run_agent = fake_run
        hq_verifier.log = lambda *a, **k: None
        try:
            result = hq_verifier.verify_task(task, dry=False)
        finally:
            hq_verifier.VERIFICATIONS, hq_verifier.pool_pick, hq_verifier.run_agent, hq_verifier.log = orig
        self.assertEqual(result["status"], "verified")
        self.assertEqual(calls["n"], 2, "must retry after a model writes no file")
        self.assertEqual(calls["picks"][0], ("aider",), "aider must be excluded from verify picks")

    def test_gives_up_after_all_tries(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        vdir = Path(tmp.name) / "verifications"
        vdir.mkdir()
        task = {"name": "fake-task2", "folder": tmp.name, "title": "fake"}
        calls = {"n": 0}

        def fake_pick(exclude=()):
            return "pi|radius/recursive/flint"

        def fake_run(pick, prompt, cwd, tag, timeout=1800):
            calls["n"] += 1
            return 1, "boom", Path(tmp.name) / "log.txt"

        orig = (hq_verifier.VERIFICATIONS, hq_verifier.pool_pick, hq_verifier.run_agent, hq_verifier.log)
        hq_verifier.VERIFICATIONS = vdir
        hq_verifier.pool_pick = fake_pick
        hq_verifier.run_agent = fake_run
        hq_verifier.log = lambda *a, **k: None
        try:
            result = hq_verifier.verify_task(task, dry=False, tries=3)
        finally:
            hq_verifier.VERIFICATIONS, hq_verifier.pool_pick, hq_verifier.run_agent, hq_verifier.log = orig
        self.assertEqual(result["status"], "no-file")
        self.assertEqual(calls["n"], 3, "must stop after the configured number of tries")


@unittest.skipUnless(sys.platform == "win32", "process-tree kill is Windows-specific")
class TimeoutTreeKillTest(unittest.TestCase):
    def test_kill_tree_kills_the_grandchild(self):
        import subprocess
        proc = subprocess.Popen(["cmd", "/c", "ping -n 60 127.0.0.1 > nul"],
                                creationflags=NO_WINDOW, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)
        hq_team._kill_tree(proc.pid)
        time.sleep(2)
        self.assertIsNotNone(proc.poll(), "the process tree must be dead after _kill_tree")

    def test_run_agent_does_not_hang_after_timeout(self):
        import subprocess
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        orig = (hq_team.agent_command, hq_team.pool_report, hq_team.OPS)
        hq_team.agent_command = lambda pick, prompt: ["cmd", "/c", "ping -n 60 127.0.0.1 > nul"]
        hq_team.pool_report = lambda *a, **k: None
        hq_team.OPS = Path(tmp.name)
        try:
            t0 = time.time()
            code, _out, logf = hq_team.run_agent("pi|x", "P", Path(tmp.name), "test-timeout", timeout=2)
            elapsed = time.time() - t0
        finally:
            hq_team.agent_command, hq_team.pool_report, hq_team.OPS = orig
        self.assertEqual(code, 124)
        self.assertTrue(logf.exists())
        self.assertLess(elapsed, 40, "run_agent must return after the timeout instead of hanging on the pipe")

    def test_run_agent_captures_output_on_success(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        orig = (hq_team.agent_command, hq_team.pool_report, hq_team.OPS)
        hq_team.agent_command = lambda pick, prompt: ["cmd", "/c", "echo hello-from-agent"]
        hq_team.pool_report = lambda *a, **k: None
        hq_team.OPS = Path(tmp.name)
        try:
            code, out, logf = hq_team.run_agent("x|y", "P", Path(tmp.name), "test-ok", timeout=30)
        finally:
            hq_team.agent_command, hq_team.pool_report, hq_team.OPS = orig
        self.assertEqual(code, 0)
        self.assertIn("hello-from-agent", out)
        self.assertIn("hello-from-agent", logf.read_text(encoding="utf-8", errors="replace"))


if __name__ == "__main__":
    unittest.main()
