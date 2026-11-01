# COMPUTER USE: any chat may use the computer, browser and apps for any task

Ahmed (2026-10-30): when something is hard or needs a screen, do it yourself and work out how. Never hand him steps. Examples HQ already proved: deleting leaked keys and removing an app from GitHub in his signed-in Chrome, generating all 17 logos in the Gemini desktop app.

## Mindset
Never say "I cannot" or wait for a permission. Say "let's try a different way": search how to do it, look at the tools, connectors and apps you have, try the browser, try the desktop app, try a smaller step. The Gemini desktop app, Antigravity, OpenCode and Kilo are installed and can be used for work too (`plans/WORKFORCE.md`).

## Which tool
1. A direct tool first when it exists: MCP connectors (Cloudflare, Firebase, Google Workspace, PostHog), CLIs (`gh`, `firebase`, `wrangler`, `magick`), APIs.
2. Web apps and sites: Claude in Chrome (`mcp__claude-in-chrome__*`, his real signed-in Chrome) or the built-in browser pane. Load the tools with one ToolSearch call; start with `tabs_context_mcp`; open your own tab; close it when done. If Chrome says not connected, check `list_connected_browsers`, then `select_browser`.
3. Desktop apps: computer use. `request_access` once per app (he approves a dialog; a process may need its own name, for example `gemini.exe`), then `open_application`, screenshot, click and type. Use `computer_batch` for predictable sequences. Terminals and IDEs are click-only, so use Bash for shell work; Antigravity is an IDE, so prefer the Gemini app or a CLI for generation.
4. If one route is blocked, try the next one that is legitimate. Never work around a refusal from the safety checks.

## What stays Ahmed's
Signing in, passkeys and 2FA codes, CAPTCHAs, payments and buying, typing passwords or secrets into forms, and accepting terms on his behalf. When a page asks for one of these, stop on that page, say which one, and carry on with everything else.

## Patterns that worked
- Native dialogs: the Save dialog appears several seconds after the click; wait, then type the full path into the file name box and press Enter. Do not click the dialog's command bar.
- Editors that ask "Discard edits?": choose Discard when you did not mean to edit.
- Pages that freeze after a click usually opened a native confirm dialog; ask Ahmed to accept it once, then continue.
- Lists that reorder after each change: act from the bottom up, and re-find the element each time (`find`) instead of reusing old coordinates.
- Verify every irreversible action by reading the page or the file system afterwards, and say what you verified.
- Logo recipe (Gemini app): `ops/TOOLS.md`, section "Logo generation with the Gemini desktop app".

## Privacy
AHome and Habiba data never go through any outside app, site or AI, including Gemini. Everything else is fair game when the task needs it.
