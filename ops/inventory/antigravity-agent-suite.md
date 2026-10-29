# Inventory: antigravity-agent-suite (2026-10-29, scout, read-only)

**What:** private repo (sirahmed8, MIT per LICENSE). 97 SKILL.md (22 core, 75 plugins; README says 92), rules, a Windows and mac/Linux installer that writes into ~/.gemini, ~/.claude, ~/.cursor, ~/.codex and ~/.config/opencode, an MCP template, and a Firebase Hosting landing page (`portal/index.html`, site `sir-agent-suite`).
**Repo:** main = origin/main, clean, 10 commits, last 2026-10-26; last 3 CI runs: 2 success, 1 failure (oldest). Stack: PowerShell, Python http.server, static HTML.
**Relation to canonical config:** not a duplicate. `Laptop manager/agent-config` has 18 agents and 1 skill (sir-session-end); its rules/AGENTS.md (2,989 bytes) is not a copy of this repo's (20,462 bytes). `D:\Projects\.agents\skills` holds only sir-session-end, so these 97 skills are synced nowhere. Unique here: the skills, the installer, the portal, the MCP template.

## Scores (0-5)
Architecture 3 (skills duplicated across core and plugins, not synced) · Code quality 2 (installer deletes stale dirs, `install.ps1:176-220`) · Security 2 (`mcp/mcp_config.template.json:37,:65` hold a GitHub-token key and an Authorization header that do not look like placeholders: confirm, the template is tracked so it is in history) · Completeness 3 (92 vs 97 count and portal copy disagree).

## Red flags
- Licence mix: 13 plugins declare Apache-2.0 with no LICENSE/NOTICE; sir-ecosystem is "Proprietary"; a SKILL.md says "MIT / Commercial Pro".
- Hard-coded paths: `scripts/start-web.ps1:1`, sir-ecosystem and laptop-admin skills cite `D:\Projects`.
- `vercel-plugin/projects/d-obour-academic-hub` holds 136 files of another project's data inside a shared plugin.
- Tracked binary zip (`antigravity-agent-suite.zip`) and `.firebase` cache.
- Desktop folder "Antigravity Agent Suite" has 4 .lnk (powershell, install.bat, wscript).

## Decision: merge into Laptop manager (not old projects: the skills are in use)
Move skills and rules into `agent-config` after a licence audit; fix hard-coded paths and the d-obour folder; check the template tokens; retire the global installer (it writes into other tools' global config, which is an owner-only action); keep the repo as a private archive until the move is verified.
Upgrade size: M. Open: portal's Agensi.io claim (`portal/index.html:109`), zip vs tree, Desktop .lnk icon.
