# auth

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\auth\SKILL.md`
- SKILL.md size: 21055 chars

## What it does

Integrate user authentication in Next.js.

## Structure (headings inside SKILL.md)

- Authentication Integrations
- Clerk (Recommended — Native Marketplace Integration)
- Install via Marketplace
- Install Clerk from Vercel Marketplace (auto-provisions env vars)
- SDK Setup
- Install the Clerk Next.js SDK
- Proxy Configuration
- Protect Routes
- Frontend API Proxy (Core 3)
- Provider Setup
- Sign-In and Sign-Up Pages
- Access User Data
- API Route Protection
- Better Auth (Self-Hosted)
- Agent Workflow
- Install
- Postgres from the Marketplace (auto-provisions DATABASE_URL)
- Environment Variables
- Server Config
- Route Handler
- Database Schema
- Client
- Access Session Data (Server)
- Protect Routes
- Keep It Fast on Vercel
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, mcp --cursor

## Risks / cautions found in text

- - **Production:** set `BETTER_AUTH_URL` to your production domain.
- - **Sign-in through a Vercel Connect connector with Better Auth (`@vercel/connect/betterauth`); provider API tokens use `getToken()`** → `⤳ skill: vercel-connect`

## Key rules (verbatim lines from SKILL.md)

1. 8. **Re-run migrate** after every plugin change.
2. - **Cookie cache on** (`session.cookieCache`) — avoids a DB read per request in Fluid Compute functions.
3. - **Cookie check only in middleware** — `getSessionCookie()` is synchronous and works on the Edge runtime; `auth.api.getSession()` in middleware requires the Node.js runtime and costs a DB hit per request.
4. - **`ClerkProvider` must be inside `<body>`, not wrapping `<html>`** — the CLI handles this automatically
5. - **Redirect props renamed** — `afterSignInUrl`/`afterSignUpUrl`/`redirectUrl` → `fallbackRedirectUrl`/`signUpFallbackRedirectUrl`/`forceRedirectUrl`

## Files inside the skill

- (SKILL.md only)
