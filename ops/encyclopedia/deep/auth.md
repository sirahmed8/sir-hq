# auth

**Source:** `C:\Users\a7med\.codex\skills\auth\SKILL.md` (canonical copy; kilo, opencode and cursor hold byte-identical content)
**Category:** security
**Tags:** auth, clerk, descope, auth0, nextjs, vercel, middleware, security

## Summary
An integration guide for adding authentication to Vercel-deployed Next.js apps, covering three providers: Clerk (recommended, a native Vercel Marketplace integration with auto-provisioned env vars), Descope (visual flow builder, also Marketplace-native), and Auth0 (enterprise SSO/SAML/multi-tenant). It provides install commands, SDK setup, middleware/proxy configuration, sign-in and sign-up pages, session access, API route protection, a decision matrix, and the Clerk Core 3 (March 2026) breaking changes.

## When to use / when not to
Use it when adding login or signup to a Next.js app on Vercel, choosing between Clerk, Descope and Auth0, protecting routes or API routes, or upgrading Clerk to Core 3. Do not use it for other frameworks (separate skills cover those), for auth with no Vercel deployment, or as a general auth theory reference. It is distinct from `vibe-auth-hardening`, which fixes specific flaws rather than integrating a provider.

## Inputs, outputs, tools
Inputs: the project's framework and `package.json`, a Vercel CLI login, and the chosen provider's credentials. Outputs: working auth middleware, provider pages, session access, protected API routes, and a decision matrix. Tools: Vercel CLI (`vercel integration add clerk|descope`), npm and Next.js. No MCP.

## Five most important rules
1. Choose by need: Clerk for fastest setup and pre-built UI, Descope for passwordless and visual flows, Auth0 for enterprise SSO/SAML/multi-tenant.
2. Install through the Vercel Marketplace so environment variables are auto-provisioned, and never echo secret values in output or logs.
3. Clerk Core 3 changes: `auth()` is async, `auth.protect()` is awaited directly, `clerkMiddleware()` replaces the removed `authMiddleware()`, and `@clerk/types` is deprecated.
4. Protect routes with `createRouteMatcher` plus `auth.protect()`, and proxy Clerk's Frontend API through your own domain to avoid third-party requests.
5. Verify the required env-key diff against `.env.local` is empty before treating setup as complete.

## Risks and owner actions
Provider accounts and credentials (Clerk/Descope/Auth0 keys) are owned by the user; the Clerk Core 3 upgrade needs Node.js 20.9.0+. The skill cross-references `marketplace`, `routing-middleware` and `env-vars`.

## Revisions
The codex/kilo/opencode/cursor copies (7922 bytes, 2026-10-11) cover Clerk, Descope and Auth0 only. The gemini-plugin/vercel-plugin copy (21143 bytes, 2026-11-02, 539 lines) is a newer revision that adds Better Auth (self-hosted), Vercel-native primitives (Sign in with Vercel, Passport, KMS), Next.js 16 `proxy.ts`, and a longer decision matrix. The vercel-plugin revision is the best for current Vercel/Next.js 16 work; the codex revision is the stable baseline shared by the other tools.
