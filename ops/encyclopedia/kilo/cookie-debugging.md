# cookie-debugging

## Summary
Chrome DevTools MCP skill for cookie/session debugging: how to read HttpOnly vs client-visible cookies (HttpOnly only via request `Cookie` headers and `Set-Cookie` responses, never via JS), when to use the live tab vs a clean `isolatedContext`, workflows for 401/403 auth failures, consent-banner conformance testing (no trackers before consent, revocation lifecycle), SameSite/CHIPS security audits via console issues and Lighthouse, and client-side cookie manipulation via the `cookieStore` API.

## When to use / when NOT
Use when diagnosing auth redirects, session expiry, missing/blocked cookies, consent-compliance checks, or SameSite/Partitioned-cookie warnings. Do NOT use for non-browser bugs or server-side session store issues (this inspects the client side only).

## Inputs, outputs, tools
- Inputs: page URL or live session, target request, consent banner actions.
- Outputs: cookie inventories, Set-Cookie attribute analysis, network-request findings, Lighthouse third-party-cookie audit.
- Tools: Chrome DevTools MCP — `list_network_requests`, `get_network_request`, `navigate_page`, `evaluate_script` (cookieStore), `take_snapshot`, `click`, `list_console_messages`, `lighthouse_audit`, `new_page`/`close_page` with `isolatedContext`.

## 5 most important rules
1. HttpOnly cookies are invisible to JS — inspect them via request `Cookie` headers and `Set-Cookie` responses only.
2. JS attempts to delete/modify HttpOnly cookies fail silently — use `new_page` with a unique `isolatedContext` for clean-state tests, and `close_page` after.
3. For auth failures: find the failing request → check outgoing Cookie header → if absent, trace the original Set-Cookie for Path/Domain/Secure/SameSite/expiry mismatches.
4. Consent tests: snapshot baseline cookies in an isolated context, verify no tracking beacons pre-consent, click Decline, re-verify, then test revocation and teardown.
5. Fast security audit: `list_console_messages` types `["issue"]` for CookieIssue entries; Lighthouse `third-party-cookies` audit extractable via node one-liner.

## Risks / things needing the owner
Drives a real browser with the user's session — avoid mutating cookies on production accounts without need. Isolated contexts still share the browser profile's storage partitioning rules; verify teardown.

## Category / tags
security · cookies, auth, consent, gdpr, devtools, browser

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all 9977/9995 bytes near-identical.
