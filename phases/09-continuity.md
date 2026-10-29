# Phase 9 — Continuity and handoff (start by week 3; finish before the month ends)

> **Read first:** `START_HERE.md`, then `standard/14-continuity.md` and `standard/12-quality-gates.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with `phases/10-real-builds.md`.

- Every repo: required CI checks with branch protection on `main` (private repos need GitHub Pro for this, free through the Student Developer Pack; until then, enforce the gate in CI plus a local pre-push hook); a PR template with the DoD checklist; `CODEOWNERS` (Ahmed); pre-commit hooks; a one-command `pnpm verify` gate; up-to-date CHECKPOINT, ROADMAP and ADRs; `GEMINI.md` guardrails.
- `_SIR/ops/HANDOFF.md`: how to run everything; how to continue each product; open owner actions; known risks; the recurring maintenance calendar (module 14).
- A final "State of the Portfolio" report.
- **After the subscription:** everything keeps working without Claude. Automations and routines that call `claude -p` fall back to the other providers through `ask.ps1`; the memory reload has its Antigravity equivalent (Phase 1.13); `HANDOFF.md` explains how to resume with Claude Code if it is renewed.
- **The standard keeps evolving.** Improvements found in any project (from PMs, the Ideas Inbox, or lessons after releases) become proposals in `_SIR/standard/PROPOSALS.md`. HQ accepts them, bumps `STANDARD_VERSION` (SemVer), writes `_SIR/standard/CHANGELOG.md`, and runs `sync-standard`. Nothing Ahmed adds later gets lost, and every project receives it.
