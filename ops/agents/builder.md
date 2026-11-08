# builder (specialist, Gemini 3.8 Flash / Antigravity, AgentsRoom "builder")
Role: Implements features and refactors from a written task spec (web, backend, shared packages).

## Current task
Idle / Ready for assignment (Completed One-Memory & Sync System M1-M6, approved by reviewer).

## Last actions
- 2026-11-08 Review approved by reviewer (agent-1793661441891-zho80i): One-Memory & Sync System (M1-M6) verified and complete
- 2026-11-08 Resolved reviewer fixes P0-P2: patched regex runaway, purged READ_LOG, added stub filter in verify, tightened threshold to 3d, updated test suite (17/17 pass)
- 2026-11-08 Completed M6 dashboard.html update, full test suite pass (15/15), and generated evidence report
- 2026-11-08 Completed M5: Windows Scheduled Task SIR-Nightly-Structure-Check created and verified; logged in AGENTSROOM_CHANGELOG.md
- 2026-11-08 Completed M4 structure-check.mjs with HEALTH_REPORT.md and health.json; fixed Negm zero-byte files
- 2026-11-08 Completed M3 ops/agents generator and agent-note.mjs helper
- 2026-11-08 Completed M2: read-log.mjs implemented, tests passing, SessionStart hook integrated, --verify passes, committed.
- 2026-11-08 Completed M1: sync-agent-files.mjs with tests passing, --check passing across all 16 projects, committed.
- 2026-11-08 Read instruction files and appended session entry to _SIR/ops/READ_LOG.md.
- 2026-11-08 Accepted assignment asg-0mw7bis5l-eccc6422 and updated state to in_progress.
- 2026-11-08 Created _SIR/ops/agents/builder.md.
## Lessons
- Canonical law is AGENTS.md; all tool-specific files (CLAUDE.md, GEMINI.md, etc.) must remain thin pointers without divergent rules.
- Memory system scripts must be standalone Node.js (.mjs), zero external dependencies, files under 300 lines, with tests next to logic.

## Owes
- None. One-Memory & Sync System (M1–M6) approved and verified. Ready for next assignment.
