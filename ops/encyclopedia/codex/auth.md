# auth

- Tool: `codex`
- Category: security
- Source: `C:\Users\a7med\.codex\skills\auth\SKILL.md`
- SKILL.md size: 7880 chars

## What it does

Auth integration guidance: Clerk, Descope, and Auth0 setup, middleware patterns, and Next.js auth flows.

## Structure (headings inside SKILL.md)

- Authentication Integrations
- Clerk (Recommended — Native Marketplace Integration)
- Install via Marketplace
- Install Clerk from Vercel Marketplace (auto-provisions env vars)
- SDK Setup
- Install the Clerk Next.js SDK
- Middleware Configuration
- Protect Routes
- Frontend API Proxy (Core 3)
- Provider Setup
- Sign-In and Sign-Up Pages
- Access User Data
- API Route Protection
- Descope
- Install via Marketplace
- SDK Setup
- Provider and Middleware
- Sign-In Flow
- Auth0
- SDK Setup
- Configuration
- Middleware
- Access Session Data
- Decision Matrix
- Clerk Core 3 Breaking Changes (March 2026)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **`auth()` is async** — always use `const { userId } = await auth()`, not synchronous

## Files inside the skill

- (SKILL.md only)
