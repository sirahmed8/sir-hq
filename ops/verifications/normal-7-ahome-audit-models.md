# Verification: normal-7-ahome-audit-models

## Checklist Results
| Item | Description | PASS/FAIL | Evidence |
|------|-------------|-----------|----------|
| 1 | Read `D:/Projects/AHome/.sir/CHECKPOINT.md` and `D:/Projects/AHome/AGENTS.md` for context | PASS | Report `ops/agy-runs/reports/7-ahome-audit-models.md` cites checkpoint r80 state and live `ollama ps` output; spot-checks below confirm its claims match source |
| 2 | Check the current fallback chain config: find ollama/lm-studio refs, model fallback chain, list models and priorities | PASS | `grep` on `apps/local-core/domain/ai_profiles.py` shows `CHAT_MODEL = "qwen3.5:9b"`, `CHAT_CONTEXT = 16384`, all 4 efforts (fast/balanced/deeper/code) on same profile; `data/background_models.py` lists classify/tag/summarize = `qwen3:4b`, automation = `nemotron-3-nano:4b`; `data/conn_ai.py` `CLASSIFY_MODEL = "nemotron-3-nano:4b"`; `data/notes_search.py` embeddings `bge-m3` then `nomic-embed-text` |
| 3 | Verify each model in the chain: `ollama list`, check LM Studio, test one prompt per model | PASS | `ollama list` output (run by verifier): nemotron-3-nano:4b, qwen3.5:9b, gemma4:e4b, qwen3:4b, bge-m3, nomic-embed-text all installed, nothing missing; report documents live "Say hello" prompts through /api/chat for qwen3.5:9b, nemotron-3-nano:4b, qwen3:4b and embedding dim checks; LM Studio not running and not referenced (confirmed no :1234 refs in chain) |
| 4 | Check for broken links or missing models | PASS | `ollama list` shows every chain model installed; report issue list matches source reality (stale "65536" comment still present at `conn_ai.py:7`, gemma4:e4b unused) |
| 5 | Write short report to `ops/agy-runs/reports/7-ahome-audit-models.md` with chain, availability, issues, recommendations | PASS | File exists with all 4 required sections (chain, live availability, issues 1-5, recommendations) |
| 6 | Done when: report file is written AND committed | PASS | Fix1 round: report written at the required path `ops/agy-runs/reports/normal-7-ahome-audit-models.md` and at `ops/agy-runs/reports/7-ahome-audit-models.md`, then committed in the _SIR repo; `git -C D:/Projects/_SIR status` no longer lists the report as untracked |
| 7 | Done when: `ops/verifications/7-ahome-audit-models.md` confirms the audit was completed | PASS | File exists: "PASS: audit completed 2026-11-14. Chain read from source, Ollama models listed, each model prompted live, 1090 local-core tests pass."; committed in the _SIR repo during the fix1 round |

## Overall: PASS

## Notes
- Local verification run by verifier: `cd D:/Projects/AHome/apps/local-core && ./.venv/Scripts/python.exe -m pytest tests -q` -> `1090 passed in 109.00s` (matches report claim).
- CI: `gh run list --limit 3` in D:/Projects/AHome shows 3 recent `verify` runs all `failure` in 3-4s; `ops/ci-quota-exhausted.flag` exists, so CI is quota-blocked and local verification is the substitute (passed).
- The audit content itself is real and accurate: every claim in the report (model chain, installed models, 16384 ctx, nemotron classify routing, embedding fallback) was independently confirmed against `ollama list` and source greps.
- Fix task `normal-7-ahome-audit-models-fix1` (2026-11-14) done: the missing worker report `ops/agy-runs/reports/normal-7-ahome-audit-models.md` was written, the report and verification files were committed in D:/Projects/_SIR, and checklist item 6 was ticked PASS. Optionally apply the report's own recommendations in a separate task (docs sync to 16384, move classify to nemotron, Arabic TTS).
- No web UI was touched by this task; screenshot step not applicable. No private AHome content was read.
