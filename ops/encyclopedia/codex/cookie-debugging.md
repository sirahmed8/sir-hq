# cookie-debugging

- Tool: `codex`
- Category: security
- Source: `C:\Users\a7med\.codex\skills\cookie-debugging\SKILL.md`
- SKILL.md size: 9977 chars

## What it does

Uses Chrome DevTools MCP for inspecting, debugging, and testing cookies, session state, authentication issues, and cookie consent compliance. Use when diagnosing 401/403 errors, authentication redirects, session expiration, Cookie/Set-Cookie header issues, cookie banner consent conformance, or third-party cookie/SameSite/Partitioned cookie warnings.

## When to use (from skill text)

- 4. **Trigger Active Inspection (If no recent request exists)**:
- - If the cookie was set in a previous session and no network call is listed, trigger a request:
- - Locate and click the "Cookie Settings", "Manage Preferences", or footer privacy trigger (`take_snapshot` $\rightarrow$ `click`).

## Structure (headings inside SKILL.md)

- Core Concepts
- HttpOnly vs Client-Side Storage
- Session Strategy: Live Tab vs Isolated Context
- Client-Side Capabilities & Limitations
- Workflow Patterns
- 1. Diagnosing Authentication Failures & Redirects (401 / 403)
- 2. Cookie Banner & Consent Conformance Testing
- 3. Auditing Cookie Security, SameSite & CHIPS (Partitioned Cookies)
- 4. Client-Side Cookie Inspection & Manipulation
- Troubleshooting
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Verify if the `Cookie` header was attached and whether required tokens (e.g. `SESSION_ID`, `auth_token`) were sent.
- 2. **Record Baseline Cookies**: Before interacting with the banner, run `evaluate_script` with `async () => await cookieStore.getAll()`.
- - Call `list_console_messages` with `types: ["issue"]` to check for tracking warnings.
- 4. **Interact with Consent Banner**:

## Key rules (verbatim lines from SKILL.md)

1. - Verify if the `Cookie` header was attached and whether required tokens (e.g. `SESSION_ID`, `auth_token`) were sent.
2. - **Secure flag on HTTP**: `Secure` cookies are never sent over unencrypted `http://`.
3. 2. **Record Baseline Cookies**: Before interacting with the banner, run `evaluate_script` with `async () => await cookieStore.getAll()`.
4. - Call `list_network_requests` to ensure no third-party tracking beacons fired before consent.
5. - Run `evaluate_script` with `async () => await cookieStore.getAll()` after clicking to assert that only strictly necessary or consent-state cookies exist.

## Files inside the skill

- (SKILL.md only)
