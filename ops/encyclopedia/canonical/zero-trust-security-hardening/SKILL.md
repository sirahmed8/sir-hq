---
name: zero-trust-security-hardening
description: "Use when hardening an app's secrets, auth sessions, RLS tenant isolation, parameterized queries, or rate limiting."
---

# Zero-Trust Security & Hardening Engine ("Anti-Hack" Protocol)

Comprehensive defensive engineering, authentication isolation, vulnerability remediation, and production hardening to prevent unauthorized access, data leaks, credential stuffing, and cyberattacks.

---

## 1. Secret Hygiene & Environment Isolation

- **Client Bundle Sanitization**: Zero API keys, database URLs, service role secrets, or private certificates in client bundles.
- **Git History Purge**: If secrets were ever committed to Git, use `git-filter-repo` to purge them completely and immediately rotate the keys.
- **Boot-Time Validation**: Validate all environment variables server-side at startup using strict Zod or Pydantic schemas; crash fast if any required secret is missing or malformed.
- **Disable Production Source Maps**: Set `productionBrowserSourceMaps: false` in framework configs to avoid leaking internal business logic and file structures.

---

## 2. Authentication, Session & Identity Hardening

- **Secure Session Cookies (Zero localStorage)**:
  - `HttpOnly: true` (prevents JavaScript access via XSS).
  - `Secure: true` (transmitted only over HTTPS).
  - `SameSite: 'Strict'` or `'Lax'` (prevents CSRF attacks).
- **Server-Side Admin & RBAC Verification**:
  - Never trust client-side role states (`user.isAdmin === true`).
  - Validate role claims cryptographically on every request via server middleware and database-level checks.
- **Multi-Factor Authentication (2FA / OTP)**:
  - Integrate standard TOTP (Authenticator App) or Email OTP flows with encrypted single-use backup recovery codes.
- **Row-Level Security (RLS) & UUID Tenant Locking**:
  - Extract the authenticated user UUID server-side from verified session tokens.
  - Enforce database-level RLS policies: users may ONLY access records where `user_id = auth.uid()`.
- **Password Strength & Breach Check**:
  - Validate password complexity with Zod + `zxcvbn`.
  - Check passwords against the **HaveIBeenPwned Pwned Passwords API** using k-Anonymity SHA-1 ranges to block known breached passwords.
- **Cryptographic Hashing**: Hash all passwords with **Argon2id** (preferred) or **bcrypt** with a cost factor >= 12.

---

## 3. Injection Defense & Endpoint Protection

- **100% Parameterized Queries**: Every database query must use parameterized statements or ORM builders (Drizzle, Prisma). Zero raw string interpolation.
- **XSS Sanitization & CSP**:
  - Sanitize all user-submitted rich text using DOMPurify before rendering.
  - Set a strict `Content-Security-Policy` header blocking inline scripts and unauthorized external domains.
- **Sliding-Window Rate Limiting & Bot Protection**:
  - Apply sliding-window rate limiting on `/login`, `/register`, `/reset-password`, and API endpoints (e.g. max 5 failed attempts per 15 min).
  - Integrate CAPTCHA / Cloudflare Turnstile on public endpoints to prevent credential stuffing.
- **CORS Lockdown**: Whitelist only verified production domains in `Access-Control-Allow-Origin`. Never use wildcard `*` with credentials.
- **Security Headers**: Send `Strict-Transport-Security` (HSTS), `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, and `Referrer-Policy: strict-origin-when-cross-origin`.
