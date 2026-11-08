# builder (specialist, Gemini 3.8 Flash / Antigravity, AgentsRoom "builder")
Role: Implements features and refactors from a written task spec (web, backend, shared packages).

## Current task
Make the one-memory system real (sync pointers, read log, health check, per-agent files) — Assignment asg-0mw7bis5l-eccc6422 (M1-M6).

## Last actions
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
- M3: ops/agents/<name>.md generator/updater and agent-note.mjs helper
- M4: structure-check.mjs, Negm Furniture zero-byte files content fix, HEALTH_REPORT.md, health.json
- M5: Windows Scheduled Task registration (03:30 nightly, hidden)
- M6: update-dashboard-data.mjs and dashboard.html data extension
- Evidence report in _SIR/ops/reports/memory-system-2026-11-08.md
