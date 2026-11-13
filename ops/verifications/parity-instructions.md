# Verification: parity-instructions

## Checklist Results
| Item | Description | PASS/FAIL | Evidence |
|------|-------------|-----------|----------|
| 1 | Audit how each free tool loads project instructions (config / --help / config folder). Read only outside `_SIR`. | PASS | `ops/agy-runs/reports/parity-instructions.md` rows 9-16: table covers all 8 required tools (Kilo, OpenCode, Pi, Cursor agent, Devin, Codex, Antigravity agy, Auggie) with the config/flag each uses to load instructions (e.g. `~/.config/kilo/kilo.jsonc`, `~/.config/opencode/opencode.jsonc`, `agy --print`, Auggie `--workspace-root`/`--rules`). |
| 2 | Write `ops/agy-runs/reports/parity-instructions.md` table: tool \| instruction file \| loads AGENTS.md? \| loads skills? \| gap. | PASS | File exists at `D:/Projects/_SIR/ops/agy-runs/reports/parity-instructions.md` with the exact 5-column table for all 8 tools plus a Summary section. |
| 3 | Close every gap that can be fixed inside `_SIR` (preamble, runner, project rule files). Do not touch AHome. Do not edit settings outside `_SIR`. | PASS | Report lines 28-30 explicitly analyze in-`_SIR` gaps and conclude none are closable inside `_SIR`: tools without instruction-file loading (Pi, Cursor, Devin, Codex, agy) already receive parity via the CLI runner prompt (`cli-run2.sh` passes `ops/WORKER_PREAMBLE.md`, which names `D:/Projects/AGENTS.md`, `GEMINI.md`, `CLI_AGENT_INSTRUCTIONS.md`, `GEMINI_QUALITY_CHARTER.md`, `23-premium-code-bar.md`); remaining gaps require changing external tool configs, which the brief forbids. `git show 05e1883 --stat` confirms no files outside `_SIR` were touched and no AHome content modified. |
| 4 | Commit and push to main. Local verify while `ops/ci-quota-exhausted.flag` exists. Done marker: `python scripts/agy-done.py parity-instructions ok "<one line>"`. | PASS | Commit `05e1883 feat: add parity-instructions report for free tool instruction file loading` is on `origin/main` (`git log origin/main --oneline` line 8). Done marker exists: `ops/agy-runs/done/parity-instructions.done` = `{"name":"parity-instructions","status":"ok","summary":"parity-instructions report created and pushed","at":"2026-11-13T06:46:31"}`. `ops/ci-quota-exhausted.flag` exists; the change is a single markdown report (no code), so no local test/lint/build applies. |

## Overall: PASS

## Notes
- Ran: `git log origin/main`, `git show 05e1883 --stat`, read of the report, checklist, brief, `ops/WORKER_PREAMBLE.md`, and `ops/agy-runs/done/parity-instructions.done`.
- The only commit for this task (05e1883) adds the report file alone; the "close gaps" item is satisfied by the report's documented conclusion that parity for non-config tools is already achieved through the runner prompt, and that remaining gaps are outside `_SIR` scope by the brief's own rules.
- Could not independently re-run each tool's `--help`/config audit (read-only external configs), but the report records the findings for all 8 named tools.
- CI was not consulted per the quota flag rule; change is docs-only, no build applicable.
