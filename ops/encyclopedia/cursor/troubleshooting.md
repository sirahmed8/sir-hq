# troubleshooting (codex/cursor/kilo/windsurf/opencode copies)

## Summary
troubleshooting is a narrow diagnostic wizard for the Chrome DevTools MCP server: it triggers when `list_pages`, `new_page` or `navigate_page` fails, or when the MCP server won't initialize. It walks a fixed six-step triage — (1) find and read the MCP config file (`.mcp.json`, `gemini-extension.json`, `.claude/settings.json`, `.vscode/launch.json`, `.gemini/settings.json`) looking for wrong args, missing env vars or bad `--autoConnect` usage; (2) match the error to known patterns (`Could not find DevToolsActivePort` → Chrome not running/debugging not enabled; empty profile → flag typos like `--autoBronnect`; only ~9 tools → client read-only mode; missing extension tools → missing `--categoryExtensions` or pre-149 Chrome can't load extensions on connect); (3) read the official troubleshooting.md; (4) formulate the corrected config (`--browser-url` vs `--autoConnect`, `--logFile`, longer `startup_timeout_ms`); (5) run diagnostics (`npx chrome-devtools-mcp@latest --help`, `DEBUG=*` with a log file); (6) search GitHub issues via `gh`.

## When to use / when NOT
Use ONLY for Chrome DevTools MCP connectivity/target problems. Do NOT use for general app debugging (that is systematic-debugging), for page-level bugs once the MCP is connected (use chrome-devtools/a11y-debugging/cookie-debugging/debug-optimize-lcp skills), or for non-Chrome MCP servers.

## Inputs, outputs, tools
- Inputs: the MCP error message or failed tool call, plus the client's config files.
- Outputs: a corrected MCP configuration snippet and verified reconnection (`list_pages` succeeds).
- Tools: filesystem reads of config files, `npx chrome-devtools-mcp`, `DEBUG=*` logging, `gh issue list` against ChromeDevTools/chrome-devtools-mcp, and web fetch of the official troubleshooting doc.

## 5 most important rules
1. Find and read the config file BEFORE asking the user anything; only ask for config content if no file exists.
2. `Could not find DevToolsActivePort` means Chrome isn't debuggable: confirm the right Chrome build is running, have the user enable remote debugging at `chrome://inspect/#remote-debugging`, then verify with `list_pages` alone before retrying anything complex.
3. Only ~9 tools visible = the client is in read-only/plan mode; full tool set needs write-enabled MCP settings.
4. Extensions need `--categoryExtensions` AND a launched (not connected) Chrome before v149.
5. Never guess flags — check `--help`, use `DEBUG=*` + `--logFile` for evidence, and search existing GitHub issues before inventing a fix.

## Risks / things needing the owner
Enabling remote debugging and interactive auth happen in the user's own browser — owner-adjacent but routine. `npx chrome-devtools-mcp@latest` pulls the latest package each run (supply-chain note). The skill assumes the user can edit MCP client settings. Nothing else needs the owner.

## Category / tags
build · chrome-devtools, mcp, debugging, configuration, browser

## Revisions
Five copies exist (codex, cursor, kilo, windsurf, opencode; no claude copy). Same content, only description wording differs. Best revision: the codex copy (used here); identical substance.
