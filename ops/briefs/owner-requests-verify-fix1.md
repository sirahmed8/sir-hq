Fix every item that failed verification of owner-requests-verify.

Verification file: D:\Projects\_SIR\ops\verifications\owner-requests-verify.md
Project: D:/Projects/_SIR

Failed items:
- Item 4: Voice: report where the Kokoro voice pack and the Whisper small model live on disk. Copy nothing without reporting first. -> Whisper small model (faster-whisper-base) at `D:\Projects\AI_Models_Hub\whisper\faster-whisper-base`. Kokoro voice pack NOT FOUND on disk — only a plugin YAML at `D:\Projects\SIR AI\legacy\agentic-os-research\hermes-agent\plugin-catalog\kokoro-tts.yaml` and test files. No model binaries present.

Rules: fix the cause, not the report. Add or update a test for each fixed item where the project has tests. Check the shared lessons in D:/Projects/_SIR/ops/LESSONS.md for the touched screens. Run the project's checks and CI until green, commit and push to main, update the project checkpoint, and write a short report with the real command output.
