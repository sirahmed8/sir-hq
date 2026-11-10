import unittest
import os
import sys
import tempfile
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "plans"))
from dashboard_privacy import assert_no_private_leaks


class TestPrivacy(unittest.TestCase):
    def test_fixture_secret_task_filtered(self):
        # simulate rendered output containing leaked private task
        with self.assertRaises(ValueError):
            assert_no_private_leaks("AHome task SECRET-TASK-XYZ camouflage")

    def test_clean_text_passes(self):
        assert_no_private_leaks("AHome (private) status only")


if __name__ == "__main__":
    unittest.main()
