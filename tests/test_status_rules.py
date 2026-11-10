import unittest
import json
import tempfile
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "plans"))
from status_rules import state_for


class TestStatusRules(unittest.TestCase):
    def _write_evidence(self, root, data):
        ev_dir = os.path.join(root, ".sir", "evidence")
        os.makedirs(ev_dir, exist_ok=True)
        with open(os.path.join(ev_dir, "verified.json"), "w", encoding="utf-8") as f:
            json.dump(data, f)

    def test_verified_today(self):
        with tempfile.TemporaryDirectory() as d:
            self._write_evidence(d, {"date": "2026-11-10", "command": "pytest", "exit_code": 0, "reviewer": "r"})
            self.assertEqual(state_for(d, "2026-11-10"), "verified")

    def test_verified_yesterday(self):
        with tempfile.TemporaryDirectory() as d:
            self._write_evidence(d, {"date": "2026-11-09", "command": "pytest", "exit_code": 0, "reviewer": "r"})
            self.assertEqual(state_for(d, "2026-11-10"), "built_unverified")

    def test_no_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(state_for(d, "2026-11-10"), "not_started")

    def test_malformed_json(self):
        with tempfile.TemporaryDirectory() as d:
            ev_dir = os.path.join(d, ".sir", "evidence")
            os.makedirs(ev_dir, exist_ok=True)
            with open(os.path.join(ev_dir, "verified.json"), "w", encoding="utf-8") as f:
                f.write("{bad json")
            self.assertEqual(state_for(d, "2026-11-10"), "built_unverified")


if __name__ == "__main__":
    unittest.main()
