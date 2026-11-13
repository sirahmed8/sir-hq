# Verify every owner request from the 2026-11-13 chat (verifier, read and test only)
Folder: D:/Projects/_SIR. Do not change product code. For each item write PASS or FAIL with the command and its real output.
1. Ollama: `ollama list` shows qwen3.5:9b, gemma4:e4b, nemotron-3-nano:4b. Old qwen2.5 and deepseek-r1 are gone. Report the list.
2. OpenClaw: `openclaw models list --refresh` shows the default model; report the default.
3. Telegram: exactly one poller per bot token. Report the process list (no tokens printed).
4. Voice: report where the Kokoro voice pack and the Whisper small model live on disk. Copy nothing without reporting first.
5. Browser: count visible SIR Study tabs in the owner's Chrome. Report only the count.
6. Projects cleanup: list top-level items that are empty or pure caches. Report only, delete nothing.
Write ops/agy-runs/reports/owner-requests-verify.md, commit reports only, push to main. Done marker: python D:/Projects/_SIR/scripts/agy-done.py owner-requests-verify ok "<one line>".
