# One memory, one set of instructions, every AI (Claude, Antigravity, Codex, OpenCode, Kilo, Muse, Pi)
Problem: each CLI has its own instruction and memory files and often does not read them; a new manager forgets what the last one did. Fix: one canonical set of files, thin pointers for each tool, a read log that proves they were read, and update duties so nothing is forgotten.

## 1. Canonical files (the only source of truth)
- Global law: `D:\Projects\AGENTS.md` (+ `_SIR/standard/*`, `START_ANY_AI.md`, `plans/COMPANY...`, `MANAGER_BRIEF_*`). Per project: `AGENTS.md`, `.sir/CHECKPOINT.md`, `PLAN.md`, `TASKS.md`, `BOARD.md`, `ARCHITECTURE.md`, `DESIGN.md`, `QUALITY.md`, `PRODUCTION.md`, `PLATFORMS.md`, `BENCHMARK.md`, `TEAM.md`, `TOOLKIT.md`, `decisions/`, `reports/`, `evidence/`, plus `.sir/MEMORY.md` (what this project's agents have learned: decisions, traps, fixes, preferences) and `CHANGELOG.md` (detailed, newest first).
- Company level in `D:\Projects\_SIR\ops`: `HQ_CHECKPOINT.md`, `MANAGER_STATE.md` (live state for succession), `MANAGER_MEMORY.md` (learned knowledge), `AGENT_QUEUE.md`, `OWNER_ACTIONS.md`, `MISSION_LOG.md`, `AGENTSROOM_CHANGELOG.md` (name kept; it is the change log of rules and process, AgentsRoom itself was retired), `agy-accounts-usage.md`, `READ_LOG.md`, and one file per agent in `ops/agents/<name>.md` (role, current task, last 20 actions, lessons, what it still owes).
- Rule: facts live in exactly one file; every other place links to it.

## 2. Same instructions for every tool
- `AGENTS.md` is canonical. `CLAUDE.md` and `GEMINI.md` (and `.codex`, `.opencode`, `.kilo`, Muse and Pi rule files) in each folder contain only: "Read AGENTS.md completely first, then .sir/CHECKPOINT.md" plus tool-specific notes that do not contradict it. A generator (`_SIR/plans/generate_kit.py` or `_SIR/scripts/memory/sync-agent-profiles.mjs`) regenerates the pointers and fails CI if a tool file holds rules that differ from AGENTS.md. Global user files (`~/.claude/CLAUDE.md`, `~/.gemini/GEMINI.md`, `~/.codex/AGENTS.md`, OpenCode, Kilo) point to `D:\Projects\AGENTS.md` and `START_ANY_AI.md`.
- Skills, agents and roles: one canonical copy (`_SIR/standard/roles` and the skills folder); each tool gets generated copies, never hand-edited divergent ones. Check with a script that lists every tool's agents and flags differences.
- Hooks (Claude `SessionStart`, equivalent in other CLIs where available) print the read-first list and the current checkpoint so reading is automatic, not optional.

## 3. Prove they read it
- At session start every agent appends one line to `ops/READ_LOG.md`: time, tool, agent id, project, files read (names and the modified-time of each), and the checkpoint "Next step" it is continuing. The manager's weekly check flags sessions that worked without a read line, and reviewers reject work whose read line is missing or stale.
- At session end (or before a limit) every agent updates its own `ops/agents/<name>.md`, the project `CHECKPOINT.md`, `MEMORY.md` if it learned something, `CHANGELOG.md`, `TASKS.md` ticks with evidence, and the queue.
- When one agent changes a rule or a process, it edits the canonical file, appends a line to `AGENTSROOM_CHANGELOG.md`, and runs the sync script so all tools get it. Agents tell each other through the bus files (`ops/bus/<slug>.md`), not through chat.

## 4. Monitoring (professional, nothing skipped)
- The Control Room reads `AGENT_QUEUE.md`, `OWNER_ACTIONS.md`, `TASKS.md` counts, `READ_LOG.md` freshness and the per-agent files; it shows per project: last checkpoint time, open tasks, running agents, last verify result, last deploy, and a red flag for any project whose checkpoint is older than 7 days or whose agents did not read the files.
- A nightly job (script, not an AI) validates the structure: every project has the required files with content, no zero-byte files (some were found empty), checkpoint timestamps, pointers match AGENTS.md, no tool file contradicting it. It writes `ops/HEALTH_REPORT.md` and alerts the manager.
- Plans are living: every agent that learns something that changes the plan edits PLAN and TASKS and logs why.
