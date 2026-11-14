# Verification: owner-requests-verify-fix1

## Checklist Results
| Item | Description | PASS/FAIL | Evidence |
|------|-------------|-----------|----------|
| 4 | Voice: report where the Kokoro voice pack and the Whisper small model live on disk. Copy nothing without reporting first. | PASS | Listing of `D:\Projects\AI_Models_Hub` shows folders `kokoro` and `whisper`. Kokoro: `D:\Projects\AI_Models_Hub\kokoro\model\kokoro-v1.0.fp16.onnx` (163527961 bytes), `D:\Projects\AI_Models_Hub\kokoro\model\voices-v1.0.bin` (28214398 bytes, the voice pack), plus `kokoro-check.wav` (119212 bytes). Whisper: `D:\Projects\AI_Models_Hub\whisper\faster-whisper-base\model.bin` (145217532 bytes) plus config, tokenizer, vocabulary; also HF cache `huggingface\hub\models--Systran--faster-whisper-base` and `...faster-whisper-large-v3`. Nothing was copied. The earlier FAIL ("Kokoro NOT FOUND") was a wrong search: the pack is on disk. |
| CI | CI is green (or blocked by quota with local verification passing) | PASS | CI blocked by the Actions quota, local verification passed (`ops/ci-quota-exhausted.flag` exists). Local: `python -m compileall -q plans scripts` exit 0; `python plans/generate_dashboard.py` exit 0 ("generated ... control-room.html (75765 bytes, e660900a)"); `python -m pytest tests -q` = `65 passed in 22.05s`. `gh run list`: latest main commit 2cf7f8a runs verify 43574008694 and test 43574008710 both success (an older run 43573492696 on 8178d65 failed). |
| 1-3, 5-6 | Other items of owner-requests-verify (Ollama, OpenClaw, Telegram poller, Chrome tab count, cleanup report) | PASS | Not part of this fix. Re-checked item 1 only: `ollama list` shows nemotron-3-nano:4b, qwen3.5:9b, gemma4:e4b, qwen3:4b, bge-m3; no qwen2.5 or deepseek-r1. Items 2, 3, 5, 6 were not re-run; they stay as PASS in `ops/verifications/owner-requests-verify.md`. |

## Overall: PASS

## Notes
- The task asks for the "Whisper small model". No `faster-whisper-small` exists on disk. The only Whisper models are `faster-whisper-base` and `faster-whisper-large-v3`. The location is reported as asked, but the size differs from "small". If small is really wanted, the owner should confirm before a download. I did not download or copy anything.
- Item 4 was a report-only request. The fix is a corrected report, so no test applies.
- Not checked: the working tree has many uncommitted files from other tasks (`git status`). The checkpoint update and commit were not done here.
- The `nul` file mentioned in the earlier notes was not looked at again.
