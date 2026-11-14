# auth

Source read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\auth\SKILL.md` (vercel-plugin revision, 539 lines; supersedes the identical 321-line codex/cursor/kilo/opencode copies).

## Summary
An authentication integration guide for Vercel-deployed Next.js apps covering four providers: Clerk (recommended, native Vercel Marketplace integration with auto-provisioned env vars and unified billing), Better Auth (self-hosted, data stays in your own database), Descope (Marketplace native, visual flow builder), and Auth0 (enterprise SSO/SAML). It also covers Vercel-native primitives: Sign in with Vercel (OAuth/OIDC provider), Vercel Passport (deployment protection), and Vercel KMS (managed signing keys). All examples target Next.js 16, where the request-interception file is `proxy.ts`; Next.js 15 and earlier use `middleware.ts`.

## When to use / when NOT
Use when adding sign-in/sign-up to a Vercel-hosted Next.js app and choosing or wiring an auth provider. Do NOT use it to audit or fix an existing auth implementation's security posture (that is vibe-auth-hardening / owasp-vulnerability-shield), and do NOT use it for non-Next.js frameworks beyond reading the provider decision matrix.

## Inputs, outputs, tools
- Inputs: the target framework (Next.js version), chosen provider, env vars (`CLERK_SECRET_KEY`, `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`, `DATABASE_URL`, etc.), route protection requirements.
- Outputs: `proxy.ts`/`middleware.ts` config, provider setup, sign-in/sign-up pages, session access patterns, protected API routes.
- Tools: `vercel integration add clerk|descope`, `npm install @clerk/nextjs` / `@descope/nextjs-sdk` / `@auth0/nextjs-auth0`, Better Auth server + route handler + DB schema. MCP: none; cross-references marketplace, routing-middleware, env-vars skills.

## 5 most important rules
1. **Clerk is the default recommendation** — fastest setup via `vercel integration add clerk`, which auto-provisions env vars and bills through Vercel.
2. **Use `proxy.ts` on Next.js 16** (export `proxy`), `middleware.ts` on 15 and earlier (export `middleware`) — the skill's examples are written for 16.
3. **Clerk Core 3 breaking changes (March 2026)**: `auth()` is async, `auth.protect()` is awaited directly, `clerkClient()` is async, `authMiddleware()` removed, `@clerk/types` deprecated; upgrade via `npx @clerk/upgrade` (Node 20.9+).
4. **Pick by need, not habit**: fastest setup/prebuilt UI → Clerk; passwordless/social flows → Descope; enterprise SSO/SAML/multi-tenant → Auth0; data in your own DB → Better Auth.
5. **Better Auth needs Postgres** — provision `DATABASE_URL` from the Marketplace and define the schema; keep it fast on Vercel per the skill's checklist.

## Risks / owner notes
Marketplace installs create real billing relationships on the Vercel account — confirm the owner wants Clerk/Descope billing before running `vercel integration add`. Auth env vars are secrets; never commit them. Choosing Auth0 vs Clerk is a long-term identity decision the owner should confirm.

## Category / tags
security · authentication, nextjs, clerk, better-auth, descope, auth0, oauth, vercel-marketplace, middleware

## Revisions
The vercel-plugin copy (539 lines) is the newest and best: it adds Better Auth, Vercel Passport/KMS/Sign-in-with-Vercel primitives, and Next.js 16 `proxy.ts` guidance. The codex/cursor/kilo/opencode copies (321 lines, identical) cover only Clerk/Descope/Auth0 with `middleware.ts` examples — still correct but older.
