"""Unit tests for the free-model pool pick and the headless agent command table.

Covers the 2026-11-14 verifier fix: the pool pick can exclude tools that cannot
verify (aider has no file-read tool), and every pool tool has a real command
(the missing `pi` entry made the verifier die with exit 127 "unknown tool").
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cli_pool  # noqa: E402
import hq_team  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
