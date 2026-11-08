# SIR Memory Scripts

System scripts for the One Memory system across all AIs (Claude, Antigravity, Codex, OpenCode, Kilo).
Spec: `_SIR/plans/MEMORY_AND_SYNC_SYSTEM.md`.

## Scripts

- `read-log.mjs`:
  Appends session start lines to `_SIR/ops/READ_LOG.md` and verifies session integrity.
  - Automatic: Hooked into `session-start.mjs` for Claude Code sessions.
  - Manual one-liner for any CLI:
    ```bash
    node D:/Projects/_SIR/scripts/memory/read-log.mjs --tool <tool> --agent <agent>
    ```
  - Verify session read compliance today:
    ```bash
    node D:/Projects/_SIR/scripts/memory/read-log.mjs --verify
    ```
- `session-start.mjs`: Claude Code SessionStart hook.
- `stop-guard.mjs`: Claude Code Stop hook.
- `pre-compact.mjs`: Claude Code PreCompact hook.
- `agent-note.mjs`: Appends an action to an agent's `_SIR/ops/agents/<name>.md` and trims history to 20 actions.
- `structure-check.mjs`: Nightly audit script generating `_SIR/ops/HEALTH_REPORT.md` and `_SIR/ops/health.json`.
- `lib.mjs`: Common helpers and context resolver.
