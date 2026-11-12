# zero-trust-security-hardening

- Tool: `claude`
- Category: security
- Source: `C:\Users\a7med\.claude\skills\zero-trust-security-hardening\SKILL.md`
- SKILL.md size: 3392 chars

## What it does

Use when hardening an app's secrets, auth sessions, RLS tenant isolation, parameterized queries, or rate limiting.

## Structure (headings inside SKILL.md)

- Zero-Trust Security & Hardening Engine ("Anti-Hack" Protocol)
- 1. Secret Hygiene & Environment Isolation
- 2. Authentication, Session & Identity Hardening
- 3. Injection Defense & Endpoint Protection
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Client Bundle Sanitization**: Zero API keys, database URLs, service role secrets, or private certificates in client bundles.
- - **Git History Purge**: If secrets were ever committed to Git, use `git-filter-repo` to purge them completely and immediately rotate the keys.
- - **Boot-Time Validation**: Validate all environment variables server-side at startup using strict Zod or Pydantic schemas; crash fast if any required secret is missing or malformed.
- - **Disable Production Source Maps**: Set `productionBrowserSourceMaps: false` in framework configs to avoid leaking internal business logic and file structures.

## Key rules (verbatim lines from SKILL.md)

1. - **Boot-Time Validation**: Validate all environment variables server-side at startup using strict Zod or Pydantic schemas; crash fast if any required secret is missing or malformed.
2. - **Disable Production Source Maps**: Set `productionBrowserSourceMaps: false` in framework configs to avoid leaking internal business logic and file structures.
3. - Never trust client-side role states (`user.isAdmin === true`).
4. - **100% Parameterized Queries**: Every database query must use parameterized statements or ORM builders (Drizzle, Prisma). Zero raw string interpolation.
5. - Sanitize all user-submitted rich text using DOMPurify before rendering.

## Files inside the skill

- (SKILL.md only)
