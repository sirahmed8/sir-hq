# Verify the Telegram voice pipeline after the hang fix

Owner complaint (voice, 2026-11-12): voice message transcription sometimes hangs. The manager just changed `D:/Projects/_SIR/scripts/backup_manager.py`: transcription now runs inside a hard-capped thread (210 s budget), Groq timeout lowered to 75 s, Cloudflare fallback to 120 s, and an interim "[بسمع الفويس]" message is sent before transcribing.

This task only verifies and hardens; it writes only under `D:/Projects/_SIR` (ops files, small script fixes if a real bug is found).

## What to do

1. Syntax and import check: `python -c "import ast; ast.parse(open('scripts/backup_manager.py', encoding='utf-8').read())"` and confirm `python scripts/backup_manager.py` with no args exits cleanly (it should fail on missing argv, that is fine).
2. Live transcription test: pick the newest saved voice file in `ops/telegram-media/voice-*.oga` (or `.ogg`) and time a direct call to the module functions:
   `python -c "import sys,time; sys.path.insert(0,'scripts'); import backup_manager as b; from pathlib import Path; t=time.time(); print(repr(b.transcribe(Path('ops/telegram-media/<file>')))); print('seconds', round(time.time()-t,1))"`
   Never print API keys. Confirm it returns Arabic text in under ~210 s.
3. Check `ops/agy-runs/backup-manager.log` tail for `groq whisper failed`, `cloudflare whisper failed` or `transcribe timed out` entries from the last hours; if a provider is consistently failing, note which one in the verification file (do not change keys).
4. Edge cases to confirm in code (read only): the busy.lock wait (30 min) still works, the reply file flow is unchanged, and a timed-out transcription sends the "could not hear" message instead of hanging forever.
5. Write `ops/verifications/r67-voice-pipeline.md` with: what was tested, exact commands, timings, the transcript result (first 120 chars), and PASS/FAIL per check. If you find and fix a small bug, commit and push to main.
