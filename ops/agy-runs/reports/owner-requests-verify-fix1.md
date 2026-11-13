# owner-requests-verify-fix1 report

Task: fix every item that failed verification of `owner-requests-verify` (`ops/verifications/owner-requests-verify.md`). Only item 4 failed.

## Item 4 — Voice: Kokoro voice pack + Whisper small model locations

**Verdict: FIXED (cause fixed, not the report).**

### What was wrong
The verification FAILed because the Kokoro voice pack had no model binaries anywhere on disk — only a plugin catalog YAML (`SIR AI/legacy/.../plugin-catalog/kokoro-tts.yaml`, also shipped inside the Hermes Agent payload) and test files existed.

### Investigation (real commands)
- `find` over `D:\Projects\AI_Models_Hub`, `C:\Users\a7med\AppData`, `.cache`, `.local`, `.openclaw`, `.hermes`, `D:\Projects`, `D:\Caches` (depth 4-6): zero kokoro hits.
- Hermes Agent v0.23.1 is installed (`hermes --version`), data dir `C:\Users\a7med\AppData\Local\hermes` — `models/`, `plugins/`, `audio_cache/` all empty.
- Hermes built-in TTS providers (`agent/tts_registry.py`): edge, elevenlabs, openai, minimax, xai, mistral, gemini, neutts, kittentts, piper, deepinfra — Kokoro is NOT built in.
- The kokoro-tts plugin YAML declares `platforms: [macos, linux]` — it cannot install on this Windows machine through Hermes. SIR AI plans (`plans/sir-ai-DEEP.md`, `SIR_AI_ASSISTANT_REQUIREMENTS.md`) specify faster-whisper + piper-tts for local voice; Kokoro is English-only anyway.

### Fix applied
Provisioned the Kokoro-82M pack for real into the canonical model store, runnable on Windows via ONNX (no espeak-ng system install needed; `espeakng-loader` fetches the lib automatically):

- `D:\Projects\AI_Models_Hub\kokoro\model\kokoro-v1.0.fp16.onnx` — 163,527,961 bytes (156.0 MB), from `thewh1teagle/kokoro-onnx` release `model-files-v1.1`
- `D:\Projects\AI_Models_Hub\kokoro\model\voices-v1.0.bin` — 28,214,398 bytes (26.9 MB), same release
- `D:\Projects\AI_Models_Hub\kokoro\.venv\` — Python 3.13.11 venv (uv), `kokoro-onnx==0.6.1`, `onnxruntime==1.32.0`, `soundfile==0.14.0`, `espeakng-loader==0.2.4` (117 MB)
- `D:\Projects\AI_Models_Hub\kokoro\synthesize.py` — CLI wrapper: `.venv\Scripts\python.exe synthesize.py "<text>" [out.wav] [voice] [speed]`

### Proof it works (not just files on disk)
```
$ ./.venv/Scripts/python.exe synthesize.py "Voice pack check. Kokoro is ready." kokoro-check.wav af_heart 1.0
kokoro-check.wav (2.5s @ 24000 Hz, voice=af_heart)
```
`kokoro-check.wav` = 119,212 bytes valid WAV written under `AI_Models_Hub\kokoro\`. ONNX runtime printed harmless constant-folding CPU-kernel warnings only.

### New repo files (committed)
- `scripts/voice_models_report.py` — stdlib JSON/text report of all local voice model locations (whisper faster-base dir, HF cache copy, kokoro model/voices/runtime). Resolves the hub as the sibling of the repo, so it works from any checkout.
- `tests/test_voice_models.py` — 3 tests: schema + missing-hub behavior, CLI JSON, and on-machine presence guard (skips off-machine).
- `.gitignore` — repaired a UTF-16-corrupted `nul` entry (`n\0u\0l\0`) into a real `nul` line; the stray `nul` redirect artifact is now ignored (verification note item).

### Report output (real)
```
$ python scripts/voice_models_report.py --text
OK      whisper-faster-base       141.0 MB  D:/Projects/AI_Models_Hub/whisper/faster-whisper-base
OK      whisper-hf-cache          282.1 MB  D:/Projects/AI_Models_Hub/huggingface/hub/models--Systran--faster-whisper-base
OK      kokoro-model              156.0 MB  D:/Projects/AI_Models_Hub/kokoro/model/kokoro-v1.0.fp16.onnx
OK      kokoro-voices              26.9 MB  D:/Projects/AI_Models_Hub/kokoro/model/voices-v1.0.bin
OK      kokoro-runtime            117.0 MB  D:/Projects/AI_Models_Hub/kokoro/.venv
```

## Checks run
- `python -m compileall -q plans scripts` — exit 0
- `python -m pytest tests -q` — **60 passed, 5 skipped** in 9.26s (was 57 passed before; +3 new voice tests)
- `git push origin main` — `8c541c4..4f6d938 main -> main` (two commits: code+test, then checkpoint/team bus)
- CI: `ops/ci-quota-exhausted.flag` still present; `gh run list` shows the push runs queued. Per WORKER_PREAMBLE rule 18, local verification substitutes for CI while the flag exists.

## Untouched / notes
- The many other modified/untracked files in `git status` belong to concurrent runners (backup_manager, cli_pool, telegram-inbox, audit reports); I staged only my three files plus checkpoint/team bus.
- Kokoro v1.0 voices are English-only; for Arabic TTS the better local/cloud path is edge-tts ar-EG (Hermes built-in) or piper per the SIR AI plan. Noted in the checkpoint.
- `AI_Models_Hub` is outside the `_SIR` repo, so ~300 MB of model binaries are not committed anywhere — correct.
- No browser was opened this task. No owner messages sent.

## Commits
- `8c541c4` voice: provision Kokoro-82M pack in AI_Models_Hub, add location report + test
- `4f6d938` checkpoint: owner-requests-verify-fix1 done (Kokoro pack provisioned)
