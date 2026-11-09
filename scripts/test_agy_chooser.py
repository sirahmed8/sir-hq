#!/usr/bin/env python3
"""
test_agy_chooser.py - Unit test suite for agy-chooser.py (Task HQ-01)
"""

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

SCRIPT_PATH = Path(__file__).resolve().parent / "agy-chooser.py"
spec = importlib.util.spec_from_file_location("agy_chooser", SCRIPT_PATH)
agy_chooser = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agy_chooser)


class TestAgyChooser(unittest.TestCase):
    def test_unapproved_accounts_blocked(self):
        for bad_email in ["other.user@gmail.com", "stranger@example.com", "unauthorized123@gmail.com", ""]:
            ok, reason = agy_chooser.is_account_permitted(bad_email)
            self.assertFalse(ok, f"Should block unapproved account: {bad_email}")

    def test_approved_owner_accounts_allowed(self):
        for good_email in [
            "a7medorabe7@gmail.com",
            "1sir1ahmed1@gmail.com",
            "ahmedalaa2006.7.6@gmail.com",
            "a01083835229@gmail.com",
            "1sir1ahmed1",
        ]:
            ok, reason = agy_chooser.is_account_permitted(good_email)
            self.assertTrue(ok, f"Should allow owner account: {good_email}")
            self.assertEqual(reason, "ok")

    def test_parse_snapshot_authenticated(self):
        snap_text = "You have successfully authenticated with Antigravity."
        action, ref = agy_chooser.parse_snapshot_action(snap_text, "1sir1ahmed1")
        self.assertEqual(action, "authenticated")
        self.assertIsNone(ref)

    def test_parse_snapshot_choose_account(self):
        snap_text = (
            "Choose an account\n"
            "[e12] <link> 1sir1ahmed1@gmail.com\n"
            "[e15] <link> a7medorabe7@gmail.com\n"
        )
        action, ref = agy_chooser.parse_snapshot_action(snap_text, "1sir1ahmed1")
        self.assertEqual(action, "click_account")
        self.assertEqual(ref, "e12")

    def test_parse_snapshot_click_signin(self):
        snap_text = (
            "Make sure that you downloaded this app from Google\n"
            "[btn9] <button> Cancel\n"
            "[btn10] <button> Sign in\n"
        )
        action, ref = agy_chooser.parse_snapshot_action(snap_text, "1sir1ahmed1")
        self.assertEqual(action, "click_signin")
        self.assertEqual(ref, "btn10")

    def test_parse_snapshot_needs_owner_2fa(self):
        snap_text = "2-Step Verification: Verify it's you"
        action, ref = agy_chooser.parse_snapshot_action(snap_text, "1sir1ahmed1")
        self.assertEqual(action, "needs_owner")

    def test_ctl_handles_malformed_output_gracefully(self):
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(stdout="not valid json", stderr="")
            res = agy_chooser.ctl("browser", "tabs")
            self.assertFalse(res.get("ok", True))
            self.assertIn("malformed JSON", res.get("error", ""))

    def test_main_dry_run_and_guardrail(self):
        code_ok = agy_chooser.main(["1sir1ahmed1@gmail.com", "--dry-run"])
        self.assertEqual(code_ok, 0)

        code_forbidden = agy_chooser.main(["unauthorized@gmail.com", "--dry-run"])
        self.assertEqual(code_forbidden, 3)


if __name__ == "__main__":
    unittest.main()
