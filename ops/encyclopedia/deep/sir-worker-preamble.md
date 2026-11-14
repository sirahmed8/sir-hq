# sir-worker-preamble

Source read: `D:\Projects\_SIR\ops\WORKER_PREAMBLE.md`, `D:\Projects\_SIR\standard\23-premium-code-bar.md`, and `D:\Projects\.agents\skills\sir-worker-preamble\SKILL.md`.

## Summary
Mandatory startup and engineering quality skill for every SIR coding worker (Antigravity/Gemini and workspace `.agents/skills` consumers such as Devin CLI). Packages the operational guardrails from `WORKER_PREAMBLE.md` (checkpoint continuity, PowerShell 5 syntax, atomic commits to `main`, CI flag vs `gh run watch`, team/taskboard coordination, privacy rules for AHome/Habiba, headless single-tab browser rule, Telegram message formatting) alongside the `23-premium-code-bar.md` implementation floor (current stable stack, <300-line layered files, strict TypeScript with zero `any`, 4 themes, RTL logical CSS, 5 screen states, 44 px touch targets, zero mock data, green verify + UI screenshots).

## When to use / when NOT
Use at the start of every SIR worker round or build/fix task across active projects (`SIR Study`, `SIR Jobs`, `SIR AI`, `SIR Laptop Manager`, `SIR Portfolio`, `AHome` source). Do NOT use as a substitute for reading the target project's own `.sir/CHECKPOINT.md`, `AGENTS.md`, or assigned brief; do NOT build in planning-only projects.

## Inputs, outputs, tools
- Inputs: `D:\Projects\AGENTS.md`, project `AGENTS.md`, `.sir/CHECKPOINT.md` (or `_SIR/ops/HQ_CHECKPOINT.md`), assigned brief, `OWNER_DEFAULTS.md`, `ops/bus/team.md`.
- Outputs: verified code changes pushed straight to `main`, updated `.sir/CHECKPOINT.md`, task report in `ops/agy-runs/reports/<task>.md` or `ops/tasks/reports/<task>.md`, and `agy-done.py` completion marker.
- Tools: `git -C`, PowerShell 5, `taskboard.py`, `agy-done.py`, project verify runners (`tsc`, `eslint`, tests, build), headless Playwright when visual verification is required.

## 5 most important rules
1. Read `AGENTS.md`, `.sir/CHECKPOINT.md`, and `git status`/`git log -5` first; never revert prior model work and never build in planning-only projects.
2. Work in small atomic steps: refactor file + importers + tests together, verify green locally (or check `gh run watch` when `ci-quota-exhausted.flag` is absent), commit, and push straight to `main` (no PRs).
3. Enforce the 23-premium-code-bar floor: strict types (no `any`), <300-line layered files, 4 themes, RTL logical CSS, 5 screen states, 44 px targets, zero fake/mock data.
4. Respect privacy and safety boundaries: never open AHome private data, never commit secrets or private names, never delete `legacy\`, keep version `1.0.0`, and never leave stray browser tabs open.
5. Never stop to ask the owner: decide, log, and continue; route true owner-only steps (login/2FA/CAPTCHA/payment) to `OWNER_ACTIONS.md`, and flush state to the checkpoint on quota limits.

## Risks / owner notes
OpenCode and Kilo already inject `WORKER_PREAMBLE.md` and `23-premium-code-bar.md` via `instructions` in `opencode.jsonc`/`kilo.jsonc`; this skill closes the gap for Antigravity (`~/.gemini/config/skills/`) and workspace-aware CLI tools like Devin CLI (`D:\Projects\.agents\skills/`).

## Category and tags
Category: ops. Tags: worker-preamble, onboarding, quality-bar, premium-code-bar, workflow, guardrails.

## Revisions
Canonical copy created 2026-11-14 identically at `C:\Users\a7med\.gemini\config\skills\sir-worker-preamble\SKILL.md` and `D:\Projects\.agents\skills\sir-worker-preamble\SKILL.md`.
