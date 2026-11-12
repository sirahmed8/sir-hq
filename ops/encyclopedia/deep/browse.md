# browse

Tools: claude (browserbase CLI). Source: C:\Users\a7med\.gemini\config\plugins\browse\skills\browse\SKILL.md (359 lines, read in full)

## Summary
Operating manual for the `browse` Browserbase CLI: a browser automation tool that drives local or hosted browser sessions, inspects pages via accessibility snapshots/screenshots/DOM/text/network, interacts by refs/selectors/XPath/keyboard/mouse, and manages Browserbase cloud APIs, Functions, templates, and catalog skills. Emphasises snapshot-first interaction (refs like @0-5) and named sessions for parallel work.

## When to use / not use
Use for browser automation, scraping, web testing, or Browserbase platform management. NOT for simple HTTP fetches where no browser interaction is needed (use browse cloud fetch or curl), or for sites where a dedicated catalog skill already exists (search first).

## Inputs, outputs, dependencies
Input: URLs, selectors, refs, session names. Output: snapshots, screenshots, extracted text/markdown/HTML, JSON diagnostics. Needs: Chrome/Chromium for --local; BROWSERBASE_API_KEY for --remote and cloud APIs; Node.js for skill install.

## Key rules
1. Prefer `browse snapshot` over screenshots for most work — structured, fast, returns refs for reliable interaction; re-snapshot after any navigation/DOM change.
2. Use named sessions (`--session`) for non-trivial/parallel work; commands without a session share the `default` session and overwrite each other's page.
3. Choose target correctly: --local for dev/localhost, --remote for protected sites/CAPTCHA/proxies; if --local fails with "No Chrome found" and key is set, switch to --remote without retrying.
4. Never retry a failing command unchanged twice; run `browse doctor --json` and change approach (fix key, switch local/remote, stop --force).
5. Stop sessions when finished (`browse stop` or per-session) to clean up daemon state; close the browser in finally for tests.

## Risks / owner items
- 401 on driver commands if BROWSERBASE_API_KEY is set but invalid — unset it or pass --local.
- Refs are ephemeral: stale refs after re-render cause failed actions.
- Remote Verified mode requires Browserbase Scale plan; --verified/--proxies only apply to --remote.
- Newly installed catalog skills only available in future sessions.

## Category and tags
automation, browser, web — browserbase, cli, scraping, testing, cloud-api.

## Revision note
Single skill file, 359 lines, no references. Covers CLI through troubleshooting section.