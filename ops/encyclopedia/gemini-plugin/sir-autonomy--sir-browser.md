# sir-browser

Tools: gemini-plugin (sir-autonomy). Source: C:\Users\a7med\.gemini\config\plugins\sir-autonomy\skills\sir-browser\SKILL.md (24 lines, read in full)

## Summary
Zero-prompt autonomous control of Ahmed's real signed-in Chrome session for Antigravity/SIR agents: tab management, accessibility-tree snapshots with numbered element refs, click/fill/scroll, arbitrary JS eval, and screenshots — via `sir_browser_*` tools or the `sir_ctl.py browser` CLI. No permission popups by design.

## When to use / not use
Use when an agent needs to drive the user's actual authenticated browser (sessions, cookies, logged-in state) for research, form filling, or site automation. NOT for public unauthenticated scraping (plain HTTP is cheaper/safer), and NOT when approval prompts are desired — this skill deliberately bypasses them.

## Inputs, outputs, dependencies
Input: browser intents (navigate, snapshot, click ref_N, fill, scroll, eval, screenshot). Output: page state, screenshots, action results. Needs: the sir-autonomy MCP tools or `python D:\Projects\_SIR\tools\sir-autonomy\sir_ctl.py browser <cmd>`; a running signed-in Chrome instance the bridge can attach to.

## Key rules
1. Snapshot-first workflow: get the accessibility tree with numbered [ref_N] references, then target actions by ref or CSS selector — refs are the stable addressing scheme.
2. Arbitrary JS eval is available (`sir_browser_eval`) — powerful but runs in the user's real session; treat page context as untrusted input AND privileged output.
3. CLI fallback exists for every capability (tabs/snapshot/click...) so agents without MCP can still drive it via sir_ctl.py.
4. Operates inside the SIGNED-IN profile — actions carry the user's real accounts, cookies, and reputational surface.

## Risks / owner items
- "Zero-prompt" means no human gate: a bad agent can click/buy/post as the user. Scope tasks tightly; this is the highest-blast-radius skill family on the machine.
- Page JS can exfiltrate session data through eval/screenshot channels — sanitize what gets sent to external services.
- Automation on logged-in sites may violate platform ToS and trigger bot detection on the user's accounts.
- Depends on the local bridge (sir_ctl.py + Chrome attachment) being running and the Chrome version staying compatible.

## Category and tags
automation, ai — browser-automation, chrome, mcp, owner-specific, high-privilege.

## Revision note
Single plugin revision; part of the sir-autonomy plugin pair with sir-computer-use.
