# cli-install (Postman CLI)

## Summary
Tiny install skill for the Postman CLI. It gives the three platform commands (npm global, unix curl installer, Windows PowerShell installer) and a verification step, with a fallback pointer to the hosted postman-mcp-server when installing is blocked.

## When to use / when NOT
Use when `postman` is "command not found" or the CLI is missing and a task needs it (collection runs, lint, workspace push). Do NOT use to configure auth — that is a separate login step — or for API design work that only needs the MCP server.

## Inputs, outputs, tools
- Inputs: the user's OS/shell.
- Outputs: `postman` on PATH, plus a reported version.
- Tools: `npm install -g postman-cli`, `curl ... install/unix.sh | sh`, or the win64 PowerShell installer from dl-cli.pstmn.io. Fallback: postman-mcp-server for hosted operations.

## 5 most important rules
1. Prefer `npm install -g postman-cli` when Node is available — it works on every platform.
2. On Windows use the official win64.ps1 installer, not the unix script.
3. Verify after install: report the version and confirm `postman` on PATH resolves to that copy.
4. If install is blocked (no Node, no network, corporate policy), switch to the hosted MCP server rather than failing.
5. Piping a remote script to a shell is the documented install path — do not improvise a different download.

## Risks / things needing the owner
Global npm/powershell installs need appropriate permissions; the PowerShell command sets `ExecutionPolicy AllSigned` for the session. Corporate machines may block dl-cli.pstmn.io — owner decides whether to allow it.

## Category / tags
ops · cli, postman, install, tooling

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\postman\skills\cli-install\SKILL.md`. Only gemini-plugin holds it.
