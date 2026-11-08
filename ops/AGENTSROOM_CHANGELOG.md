# AGENTSROOM CHANGELOG

Log of system infrastructure, memory tooling, scheduled tasks, and agent configuration changes.

## 2026-11-08
- **Scheduled Task Registered**: `SIR-Nightly-Structure-Check`
  - Schedule: Daily at 03:30 AM (hidden execution via `wscript.exe D:\Projects\_SIR\scripts\memory\run-structure-check.vbs`)
  - Target: `node D:\Projects\_SIR\scripts\memory\structure-check.mjs`
  - Output: `_SIR/ops/HEALTH_REPORT.md` and `_SIR/ops/health.json`
  - Run-now command: `schtasks /run /tn "SIR-Nightly-Structure-Check"`
- **M1 Agent Pointers Sync**: `_SIR/scripts/agent-config/sync-agent-files.mjs` (--check, --write, dry-run).
- **M2 Read Log System**: `_SIR/scripts/memory/read-log.mjs` (auto-hooked to `session-start.mjs`, --verify).
- **M3 Agent Roster Profiles**: `_SIR/scripts/memory/sync-agent-profiles.mjs` and `agent-note.mjs`.
- **M4 Structure Integrity Check**: `_SIR/scripts/memory/structure-check.mjs`.
- 2026-11-08 HQ: removed HKCU Run entry com.agentsroom.desktop (value was the AgentsRoom.exe path) and set launchAtLogin false; AgentsRoom retired, archive in SIR AI/legacy/agentsroom.
