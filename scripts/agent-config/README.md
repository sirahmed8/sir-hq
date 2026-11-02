# agent-config

Canonical source for the rules, skills and agent roster used by Claude Code, Antigravity, Codex, OpenCode and Kilo.

- `rules/AGENTS.md`: copy of `D:\Projects\AGENTS.md` (every tool reads that file natively).
- `skills/`: one folder per skill with a `SKILL.md`.
- `agents/`: the SIR roster (role, model tier, tools, prompt).
- `node sync-agent-config.mjs [workspace]`: writes project-scope copies (`.agents/skills`, `.claude/agents`) into the workspace.

Global installs (`~/.codex`, `~/.gemini/config/plugins`) are not written by agents; they are owner actions.
Parity test status: see `D:\Projects\_SIR\ops\TOOLS.md`.
