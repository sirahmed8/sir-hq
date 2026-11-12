# auth

Source read: `C:\Users\a7med\.config\kilo\skills\auth\SKILL.md` (kilo revision; identical copies in codex/cursor/windsurf/opencode; not in claude).

## Summary
A security skill that manages authentication flows for applications, supporting OAuth 2.0, OpenID Connect, JWT validation, and session management. It provides middleware for protecting routes, handling token refresh, and revoking sessions. The skill enforces password policies, social login integration, and can generate secure authentication URLs with proper redirect handling.

## When to use / when NOT
Use when building authentication for any web or mobile application — the skill provides a secure, standards-based foundation that handles the complex details of OAuth and OIDC. Do NOT implement custom authentication from scratch — the skill's OAuth/OIDC handling has been audited for common vulnerabilities (CSRF, token replay, open redirect). Do NOT skip the token validation step; the skill validates JWT signatures and expiration before granting access, and will reject requests with invalid or expired tokens.

## Inputs, outputs, tools
- Inputs: request with auth header, OAuth client config, OIDC discovery URL, session store configuration.
- Outputs: authenticated user session, JWT payload, access decision (grant/deny), refreshed access token (if applicable), error response for invalid auth.
- Tools: OAuth 2.0 libraries, OpenID Connect discovery, JWT library, session store (Redis, Memcached), password hashing (bcrypt, argon2). MCP: none required (pure auth logic).

## 5 most important rules
1. **Always validate JWT signature and expiration** — the skill will reject tokens with invalid signatures or expired `exp` claims; never trust the raw token without validation.
2. **Use OAuth 2.0 Authorization Code Flow with PKCE for mobile** — the skill enforces PKCE to prevent authorization code interception; do not use the implicit flow for new mobile apps.
3. **Implement token refresh before expiry** — the skill can auto-refresh access tokens using refresh tokens; do not wait for token expiry to trigger re-authentication.
4. **Store refresh tokens securely** — the skill recommends httpOnly, secure cookies with SameSite=Strict; never store refresh tokens in localStorage or expose them in URLs.
5. **Revoke sessions on logout** — the skill invalidates all active sessions for the user; do not rely on browser close to clear sessions.

## Risks / owner notes
The most common auth vulnerability is missing PKCE on mobile flows, which exposes authorization codes to interception. The owner should ensure that all mobile OAuth flows include PKCE. Token leakage through logs is another risk; the skill sanitizes headers before logging, but application code must also avoid logging auth headers.

## Category / tags
security · authentication, oauth, oidc, jwt, session-management, password-policy, middleware

## Revisions
The kilo copy is the canonical source; codex, cursor, and windsurf copies are identical. The gemini-plugin version exists as `<plugin>--auth.md` but lacks the PKCE enforcement and cookie security rules present in the kilo revision. The kilo revision is the canonical source for this skill.