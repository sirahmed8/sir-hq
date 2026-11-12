# twg-setup (gemini-plugin: atlassian-twg-cli)

## Summary
twg-setup installs, upgrades, authenticates or repairs `twg` — Atlassian's Teamwork Graph CLI — for Antigravity (the installer also names 12 other recognized hosts: claude-code, codex, copilot, cursor, devin, gemini, hermes, intellij, opencode, pi, qoder, vscode). TWG gives the agent grounded work context across Jira, Confluence, Bitbucket, JSM, Assets, Slack and Google Drive so it can connect tickets/docs/code/people. The skill is a strict conversational protocol, not a script: infer the host, run the OS-specific Inspect block (`command -v twg` / LOCALAPPDATA fallback, then `twg doctor`), and only if the CLI is missing hand the user the exact installer command in a fenced block ending "When it finishes, reply done." — the agent never executes the installer itself. After `done`, the agent reruns Inspect, then installs skills via `twg skills install --agent antigravity --yes` (Antigravity reads global skills only from `~/.gemini/config/skills`), then resumes the original request. Doctor remediation covers `twg login --force` (interactive, user-run), `twg setup`, `twg setup bitbucket`, and skill refresh/restore for quarantined skills.

## When to use / when NOT
Use when twg is missing, broken, unauthenticated, or its skills aren't visible to Antigravity — typically at the start of a task that needs Jira/Confluence context. Do NOT use to actually query TWG data (that is twg's own commands: `twg work query`, `twg collaborators`), for non-Atlassian tools, or to perform auth yourself — interactive auth and secret entry always belong to the user.

## Inputs, outputs, tools
- Inputs: the host runtime (inferred, never asked), OS (Unix/macOS bash vs Windows PowerShell blocks), and `twg doctor` output.
- Outputs: a working twg CLI + installed agent skills, or one-line summaries of remaining issues.
- Tools: `twg` binary (`doctor`, `skills install/list/restore`, `login`, `setup`), curl/powershell installer from teamwork-graph.atlassian.com, Bash tool. No MCP.

## 5 most important rules
1. Never execute the installer yourself — hand it to the user in a fenced block and end with "When it finishes, reply done."; auth, agreements, browser login and secrets are always the user's.
2. Never ask the user to identify the host or run `doctor`/paste output — infer host, run Inspect yourself.
3. A sandboxed "not found" does not prove absence (sandbox can hide the home dir); ask approval to run unsandboxed before concluding.
4. Never reinstall for auth/permission/command errors — those are doctor-remediation cases (`twg login --force`, `twg setup`), and interactive fixes are given to the user, not executed.
5. Quarantined skills keep content but lose discovery links; `twg skills restore <name>` only when the user asks, and Antigravity needs a restart after skill install.

## Risks / things needing the owner
This skill deliberately routes ALL authentication, OAuth device codes, API keys and 2FA to the user — nothing secret may be requested or exposed by the agent. The installer is a remote script from Atlassian (supply-chain trust in teamwork-graph.atlassian.com). Skills install globally into `~/.gemini/config/skills`, affecting all Antigravity sessions. Browser auth and any paid Atlassian seats are owner territory.

## Category / tags
ops · atlassian, twg, jira, confluence, installation, cli

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\atlassian-twg-cli\antigravity\skills\twg-setup\SKILL.md` (the digest filename had a `--copy2` suffix, suggesting a duplicated plugin copy, but only one skills folder was found). No divergent revisions to compare.
