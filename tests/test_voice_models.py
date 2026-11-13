import json
import os
import subprocess
import sys
import unittest

SIR_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(SIR_ROOT, "scripts"))

import voice_models_report  # noqa: E402

HUB = os.path.join(os.path.dirname(SIR_ROOT), "AI_Models_Hub")


class TestVoiceModelsReport(unittest.TestCase):
    def test_collect_schema(self):
        report = voice_models_report.collect(hub_root=os.path.join(SIR_ROOT, "tests", "fixtures", "no-such-hub"))
        self.assertIn("hub_root", report)
        self.assertIn("generated_at", report)
        self.assertGreaterEqual(len(report["models"]), 4)
        for m in report["models"]:
            for key in ("id", "label", "path", "exists", "size_bytes", "note"):
                self.assertIn(key, m)
        # A nonexistent hub must report every model as missing, never crash.
        self.assertTrue(all(m["exists"] is False for m in report["models"]))

    def test_cli_json(self):
        out = subprocess.run(
            [sys.executable, os.path.join(SIR_ROOT, "scripts", "voice_models_report.py"), "--hub", HUB],
            capture_output=True, text=True, check=True,
        )
        report = json.loads(out.stdout)
        self.assertEqual(report["hub_root"], HUB)

    @unittest.skipUnless(os.path.isdir(HUB), "AI_Models_Hub not present on this machine")
    def test_models_present_on_this_machine(self):
        report = voice_models_report.collect(hub_root=HUB)
        by_id = {m["id"]: m for m in report["models"]}
        for model_id in ("whisper-faster-base", "kokoro-model", "kokoro-voices", "kokoro-runtime"):
            self.assertIn(model_id, by_id)
            self.assertTrue(by_id[model_id]["exists"], f"{model_id} missing at {by_id[model_id]['path']}")
            self.assertGreater(by_id[model_id]["size_bytes"], 0)


if __name__ == "__main__":
    unittest.main()
