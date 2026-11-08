# AgentsRoom retired (2026-11-08, Ahmed's order)

AgentsRoom 1.259.0 crashed on every agent terminal (React error #185, log `C:\Users\a7med\AppData\Roaming\desktop\logs\main-errors.log`, same on 1.258.0) and its agents were left "Interrupted". Ahmed moved the work out of it. HQ is now: Claude (Sonnet, high) as manager and reviewer in the Claude desktop app, and Antigravity CLI (`agy`, Gemini 3.8 Flash high) as the worker.

## Where everything is (read it, do not rebuild it)
- Archive: `D:\Projects\SIR AI\legacy\agentsroom\` (gitignored): `app-src\` (the extracted app, for study), `app.asar`, `app-resources\` (kb docs, hooks, MCP servers), `user-data\` (roles, templates, agent-mail, sessions, stats; no tokens), `project-state\` (D:\Projects\.agentsroom: assignments, inbox, memory), `transcripts\` (Claude console transcripts of 2026-11-07 and 2026-11-08, jsonl).
- The previous manager's own notes: `_SIR/ops/MANAGER_STATE.md` (the live state of every assignment and the queue), `MANAGER_MEMORY.md`, `READ_LOG.md`, `plans/MANAGER_BRIEF_2026-11-08.md`, `agy-accounts-usage.md`, `PM_HEARTBEAT.txt`.
- The install itself (`C:\Program Files\AgentsRoom`) and `C:\Users\a7med\.agentsroom` were left in place and untouched except as listed in `AGENTSROOM_CHANGELOG.md` (settings, roles moved to `Backups/agentsroom-2026-11-07`). The app must not start again at login.

## How work runs now
1. The manager reads `MANAGER_STATE.md`, checkpoints and git logs, and writes each task as a brief file in `_SIR/ops/briefs/`.
2. A worker runs with `python D:/Projects/_SIR/scripts/agy-worker.py <name> <brief-file> <cwd>`: it calls `agy --print` (Gemini 3.8 Flash high, no `--effort` flag, the model id carries the level) and writes the reply to `_SIR/ops/agy-runs/<name>.md`. Up to 3 at once.
3. The manager (Claude) reviews each diff (git diff, tests, on-screen check) before commit and push to main. The author never grades its own work.
4. Fallback workers when Antigravity credits are out: OpenCode (`opencode run`), Kilo, Pi, local Ollama for private work. Private data (AHome, Habiba, study material) stays on local models.
5. Study stays coaching only (guides, practice, hints); no graded work is solved.
