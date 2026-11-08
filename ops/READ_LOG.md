# READ LOG (one line per session start, newest at the bottom)
Every agent of every CLI appends ONE line when it starts a session, after reading its instruction files. Format (pipe separated):
`ISO-time | tool | agent | project | files read as name@modified-time, ... | next step it continues`

Automated:
- Claude Code: hooked automatically into `_SIR/scripts/memory/session-start.mjs`.
- Other CLIs manual one-line start command:
  `node D:/Projects/_SIR/scripts/memory/read-log.mjs --tool <tool> --agent <agent>`
- Verification:
  `node D:/Projects/_SIR/scripts/memory/read-log.mjs --verify`
A session with work but no line here is flagged by the nightly structure check and by reviewers.

2026-11-08T04:13:00Z | claude-code (AgentsRoom) | pm (manager) | HQ | _SIR/START_ANY_AI.md@2026-11-08, plans/MANAGER_BRIEF_2026-11-08.md@2026-11-08, plans/MEMORY_AND_SYNC_SYSTEM.md@2026-11-08, plans/SIR_COMPANY_BLUEPRINT.md@2026-11-08, ops/HQ_CHECKPOINT.md@2026-11-08 | review of START_PROMPT replaced by brief section 0: memory system, then Study/Life/Jobs/Laptop workers
2026-11-08T04:18:00Z | antigravity (AgentsRoom) | automation-engineer | SIR Life | _SIR/START_ANY_AI.md@2026-11-08, AGENTS.md@2026-11-08, SIR Life/AGENTS.md@2026-11-08, SIR Life/.sir/CHECKPOINT.md@2026-11-08, SIR Life/.sir/PLAN.md@2026-11-08, SIR Life/.sir/TASKS.md@2026-11-08, _SIR/plans/MANAGER_BRIEF_2026-11-08.md@2026-11-08, SIR Study/.sir/SCHEDULE.md@2026-11-08 | T-100 Calendar bridge and study schedule import
2026-11-08T04:17:30Z | antigravity-cli (Gemini) | builder (agent-1793661439917-6hvtyl) | HQ | _SIR/START_ANY_AI.md@2026-11-08, AGENTS.md@2026-11-08, plans/MEMORY_AND_SYNC_SYSTEM.md@2026-11-08, plans/MANAGER_BRIEF_2026-11-08.md@2026-11-08, standard/roles/ROSTER.md@2026-11-08, ops/PORTFOLIO.md@2026-11-08 | M1 sync-agent-files.mjs, M2 read-log.mjs, M3 ops/agents, M4 structure-check.mjs, M5 scheduled task, M6 dashboard.html
2026-11-08T04:17:00Z | antigravity-cli (Gemini 3.8 Flash) | study-coach | SIR Study | _SIR/START_ANY_AI.md@2026-11-08, AGENTS.md@2026-11-08, SIR Study/AGENTS.md@2026-11-08, SIR Study/.sir/CHECKPOINT.md@2026-10-30, SIR Study/.sir/PLAN.md@2026-11-08, SIR Study/.sir/TASKS.md@2026-11-08, SIR Study/.sir/SCHEDULE.md@2026-11-08, _SIR/plans/MANAGER_BRIEF_2026-11-08.md@2026-11-08, SIR Study/materials/digest/2026-11-01.md@2026-11-01 | T-100: verify schedule, create guides/START_HERE.html countdown & 3-day study plan, then SAD cram sheet
2026-11-08T04:24:22.016Z | ahome-daemon | ahome-worker | AHome | AHome/AGENTS.md@2026-11-07 | Initial session / no checkpoint
