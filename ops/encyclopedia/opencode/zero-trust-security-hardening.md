# zero-trust-security-hardening (claude revision)

## Summary
zero-trust-security-hardening ("Anti-Hack" Protocol) is a three-section production hardening standard broader than vibe-auth-hardening: (1) SECRET HYGIENE — zero keys/db URLs/service-role secrets in client bundles, git-filter-repo purge + immediate rotation if secrets were ever committed, boot-time Zod/Pydantic env validation crashing fast on missing secrets, productionBrowserSourceMaps disabled; (2) AUTH/SESSION/IDENTITY — HttpOnly+Secure+SameSite cookies (zero localStorage), server-side RBAC verified cryptographically per request, TOTP/email OTP + encrypted backup codes, database-level RLS with UUID tenant locking (`user_id = auth.uid()`), zxcvbn + HIBP k-Anonymity passwords, Argon2id/bcrypt cost>=12 hashing; (3) INJECTION/ENDPOINT DEFENSE — 100% parameterized queries (Drizzle/Prisma, zero string interpolation), DOMPurify sanitization + strict CSP blocking inline scripts, sliding-window rate limits on auth endpoints (5 fails/15min) + CAPTCHA/Turnstile, CORS whitelist (never `*` with credentials), full security headers (HSTS, X-Frame-Options DENY, nosniff, Referrer-Policy).

## When to use / when NOT
Use as the security checklist when hardening an app's secrets, sessions, tenant isolation, queries or rate limiting — especially before production launch or after a vibe-coded build. Do NOT use as a substitute for a real pentest, and don't apply checklist items blindly — verify which apply to the stack (e.g., RLS is Postgres/Supabase-specific).

## Inputs, outputs, tools
- Inputs: the app's auth/session/data-access/endpoint code and config.
- Outputs: hardened implementation per section — env validation, cookie/RLS/auth config, query sanitization, headers, rate limits.
- Tools: Zod/Pydantic, git-filter-repo, speakeasy/otplib-style TOTP, Argon2id/bcrypt, zxcvbn, HIBP API, DOMPurify, Drizzle/Prisma, Turnstile, RLS policies.

## 5 most important rules
1. Secrets in git history = purge with git-filter-repo AND rotate — deletion alone leaves them exposed.
2. Zero secrets in client bundles + crash-fast env validation at boot + no prod source maps.
3. Cookies HttpOnly/Secure/SameSite; roles verified server-side cryptographically EVERY request; RLS enforces `user_id = auth.uid()` at DB level.
4. 100% parameterized queries — zero raw interpolation anywhere.
5. Defense in depth on endpoints: rate limit + CAPTCHA on auth routes, CORS whitelist never `*`+credentials, full header set (HSTS/frame/nosniff/referrer).

## Risks / things needing the owner
Secret rotation and git history rewrites affect live credentials — coordinate with owner. RLS policies can lock out legitimate access if user_id mapping is wrong — test with real sessions. Rate limits/CAPTCHA can block real users if thresholds mis-set. HSTS is hard to undo once deployed. These are production-affecting changes needing care.

## Category / tags
security · zero-trust, secrets, rls, injection, hardening

## Revisions
Single source read: `C:\Users\a7med\.claude\skills\zero-trust-security-hardening\SKILL.md` (52 lines). Six-tool skill; claude revision preferred.
