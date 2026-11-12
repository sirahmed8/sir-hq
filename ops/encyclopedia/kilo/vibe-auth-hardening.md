# vibe-auth-hardening (claude revision)

## Summary
vibe-auth-hardening eliminates the five fatal auth flaws typical of AI-vibe-coded apps, mapping each flaw to its production fix (with a mermaid diagram): (1) session token in localStorage → HttpOnly+Secure+SameSite=Strict cookies with 15-min access tokens + rotating refresh tokens in partitioned DB tables; (2) client-side admin checks → server-side middleware validating role claims cryptographically per request; (3) missing 2FA → TOTP (speakeasy/otplib, Google Authenticator-compatible) + 8 single-use backup codes hashed with Argon2id/bcrypt; (4) no rate limiting → sliding-window limits (10/IP/15min, 5 failed/account/15min → lockout + notification email, exponential backoff); (5) weak passwords → Zod+zxcvbn (min 10 chars, mixed case/digits/symbols) + HaveIBeenPwned k-Anonymity check (only first 5 SHA-1 chars sent).

## When to use / when NOT
Use when auditing or fixing authentication in an app built rapidly with AI — the exact five-flaw checklist applies to most vibe-coded auth. Do NOT use as a general security audit (it covers auth only, not injection/XSS/secrets), and don't skip verifying which flaws the codebase actually has before applying fixes.

## Inputs, outputs, tools
- Inputs: the app's auth code (session handling, middleware, login/reset endpoints, password validation).
- Outputs: hardened auth implementation per flaw — cookie config, middleware, TOTP flow, rate limiter, password validation.
- Tools: speakeasy/otplib (TOTP), zxcvbn, HaveIBeenPwned API, Redis/cache for rate limiting, Argon2id/bcrypt for backup codes.

## 5 most important rules
1. localStorage tokens are banned outright — cookies only, HttpOnly+Secure+SameSite=Strict.
2. Admin/role checks MUST live server-side and verify cryptographically every request — client checks are decorative.
3. TOTP needs single-use backup codes stored hashed (Argon2id/bcrypt), never plaintext.
4. Rate limit BOTH per-IP and per-account with lockout + notification; exponential backoff after failures.
5. Password policy: zxcvbn scoring + HIBP k-Anonymity — send only 5-char SHA-1 prefix, never the password or full hash.

## Risks / things needing the owner
Implementing 2FA/rate limits touches real auth flows — breaking them locks users out; test thoroughly. HIBP API calls leak only hash prefixes by design. Rate-limit storage needs Redis or equivalent infra decision. Session migration (localStorage→cookie) can log out existing users — plan it.

## Category / tags
security · auth, 2fa, rate-limiting, cookies, hardening

## Revisions
Single source read: `C:\Users\a7med\.claude\skills\vibe-auth-hardening\SKILL.md` (71 lines). Slice lists seven tools; claude revision preferred per source-selection rule.
