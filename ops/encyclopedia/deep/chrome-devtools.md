# chrome-devtools

## Summary
Chrome DevTools MCP skill: drives a real Chrome browser for debugging, automation, performance and network inspection. Covers browser lifecycle (persistent profile, CLI flags), page targeting by `pageId`, element interaction via uids from `take_snapshot`, efficient data retrieval (`filePath`, pagination, `includeSnapshot`), tool selection (snapshot vs screenshot vs CSS styles vs `evaluate_script`), parallel execution ordering, and an extension testing workflow (install, trigger, verify service worker, verify page). Extension tools require `--categoryExtensions`; memory tools require `--memoryDebugging`.

## When to use / when NOT
Use for web page debugging, browser automation, performance/network inspection, extension testing. Do NOT use in `--slim` MCP mode or for purely server-side issues.

## Inputs, outputs, tools
- Inputs: page URL, `pageId`, element uid, optional `filePath`, CLI flags.
- Outputs: snapshots, screenshots, traces, network requests, console messages, CSS cascade, evaluated JS results.
- Tools: Chrome DevTools MCP — `navigate_page`, `new_page`, `list_pages`, `take_snapshot`, `take_screenshot`, `click`, `fill`, `evaluate_script`, `wait_for`, `get_network_request`/`list_network_requests`, `get_css_styles`, `lighthouse_audit`, `install_extension`/`list_extensions`/`trigger_extension_action`.

## 5 most important rules
1. Always navigate → wait → snapshot → interact; use uids from a fresh snapshot.
2. Use `take_snapshot` (text) for automation; `take_screenshot` only for visual inspection.
3. Pass `filePath` for large outputs (screenshots, snapshots, traces) to avoid huge tool responses.
4. Extension tools only exist with `--categoryExtensions`; stop and ask the user to update config if missing.
5. For `evaluate_script`, `pageId` is required unless targeting an extension service worker (then `serviceWorkerId`).

## Risks / things needing the owner
Drives a real browser with the user's profile; extension testing needs the flag enabled and an MCP restart. Service-worker state evaluation needs the correct id.

## Category / tags
research · chrome, devtools, mcp, debugging, automation, performance, network, extensions

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all 4345 chars identical across tools.