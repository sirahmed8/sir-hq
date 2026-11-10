"""Tests for scripts/deliver/approval.py registry and expiry rules (M8)."""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE.parent / "scripts" / "deliver" / "approval.py"

spec = importlib.util.spec_from_file_location("approval", MODULE_PATH)
approval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(approval)


class ApprovalRegistryTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        approval.APPROVALS = root / "approvals.jsonl"
        approval.APPROVALS_JSON = root / "bus" / "approvals.json"

    def _registry(self):
        return json.loads(approval.APPROVALS_JSON.read_text(encoding="utf-8"))

    def test_register_pending_creates_system_row(self):
        approval.register_pending("req-1", "سؤال")
        rows = self._registry()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["id"], "req-1")
        self.assertEqual(rows[0]["status"], "pending")
        self.assertTrue(rows[0]["created_at"])

    def test_is_expired_25h_old(self):
        old = (datetime.now(timezone.utc) - timedelta(hours=25)).isoformat()
        self.assertTrue(approval.is_expired(old))

    def test_is_expired_fresh_and_missing(self):
        fresh = datetime.now(timezone.utc).isoformat()
        self.assertFalse(approval.is_expired(fresh))
        self.assertTrue(approval.is_expired(None))
        self.assertTrue(approval.is_expired("not-a-date"))

    def test_registry_answer_only_for_answered(self):
        approval.register_pending("req-2", "سؤال")
        self.assertIsNone(approval.registry_answer("req-2"))
        rows = self._registry()
        rows[0]["status"] = "approved"
        rows[0]["answer"] = "approved"
        approval.APPROVALS_JSON.write_text(json.dumps(rows), encoding="utf-8")
        self.assertEqual(approval.registry_answer("req-2"), "approved")

    def test_answer_for_reads_jsonl(self):
        approval.APPROVALS.write_text(
            json.dumps({"id": "req-3", "answer": "approved", "at": "x"}) + "\n",
            encoding="utf-8",
        )
        self.assertEqual(approval.answer_for("req-3"), "approved")
        self.assertIsNone(approval.answer_for("req-4"))

    def test_main_returns_existing_answer_without_sending(self):
        approval.APPROVALS.write_text(
            json.dumps({"id": "req-5", "answer": "rejected", "at": "x"}) + "\n",
            encoding="utf-8",
        )
        argv = ["approval.py", "req-5", "سؤال", "0.001"]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(approval.subprocess, "run") as run_mock:
            self.assertEqual(approval.main(), 1)
            run_mock.assert_not_called()

    def test_main_send_failure_marks_send_failed(self):
        fake = subprocess.CompletedProcess(args=[], returncode=1, stdout="boom", stderr="")
        argv = ["approval.py", "req-6", "سؤال", "0.001"]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(approval.subprocess, "run", return_value=fake):
            self.assertEqual(approval.main(), 3)
        rows = self._registry()
        self.assertEqual(rows[0]["status"], "send_failed")


if __name__ == "__main__":
    unittest.main()
