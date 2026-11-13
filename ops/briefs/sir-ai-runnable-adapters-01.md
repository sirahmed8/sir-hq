# SIR AI: make the remaining CLI adapters runnable (8 detect-only -> runnable)

Folder: D:/Projects/SIR AI
Project: SIR AI (Agentic OS)
Priority: normal. parallel_ok: false (touches shared adapter registry).

## Context
SIR AI is the active build target (owner 2026-11-13). Phase 1 of the Agentic OS shipped the adapter registry + status plane (commit 3f4fe3b, 827b80f). The checkpoint lists the next unblockers, and the biggest product gap is:

"Only 4 of 12 CLIs are runnable (Claude Code, OpenCode, Kilo, Ollama); the other 8 are detect-only."

The 8 detect-only adapters are: Codex, Gemini/Antigravity, Qwen Code, Devin, Cursor Agent, Aider, LM Studio (list per checkpoint; confirm exact names in code).

## What to do
1. Read the adapter registry and one working runnable adapter (e.g. Kilo or OpenCode) end to end first. Match its exact interface/pattern. Do NOT invent a new abstraction.
2. For each detect-only adapter, implement the minimal real run path: detect -> resolve binary/config -> build argv -> spawn -> parse output/status -> report. Use only what is actually installed and verified on this PC. If a CLI is not installed, keep detect-only but make the reason explicit (not a silent stub) and record it in the checkpoint.
3. Add/extend tests for each newly runnable adapter (mock spawn, assert argv shape and status parsing). Do not call real paid CLIs in tests.
4. Update the status panel so a runnable adapter shows as runnable and a still-missing one shows the exact missing binary.
5. Update .sir/CHECKPOINT.md with what became runnable and what stayed detect-only and why.

## Done when
- `npm run typecheck` / lint / the project's verify command is green (CI quota flag is up until ~2026-12-01, so local green is the gate - paste the passing output).
- Every adapter either runs or has a one-line explicit reason in the checkpoint.
- Report written to ops/tasks/reports/ (what changed, commands with real output, what is still open).

## Rules
- No mock/fake data. No emoji. No em-dash in copy. Version stays 1.0.0.
- Never delete legacy/. Commit and push straight to main after verify passes (no pull requests).
- Never open AHome private content.