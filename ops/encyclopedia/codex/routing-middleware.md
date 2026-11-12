# routing-middleware

Tools: codex (also claude/cursor/opencode/windsurf; codex chosen). Source: C:\Users\a7med\.codex\skills\routing-middleware\SKILL.md (222 lines, read in full)

## Summary
Vercel Routing Middleware expert guide: platform-level `middleware.ts` request interception running before cache on any framework (Edge/Node/Bun runtimes), helpers from `@vercel/functions` (next/rewrite/geolocation/ipAddress/waitUntil), matcher scoping, plus the three CDN routing mechanisms (Bulk Redirects, Project-Level Routes, deployment config) and programmatic `vercel.ts` config.

## When to use / not use
Use for request interception before cache: geo-personalization, A/B rewrites, header injection, lightweight defense-in-depth checks. NOT for auth as sole protection, heavy logic/DB work, or Next.js 16 network-boundary proxying (that's `proxy.ts`); Edge Functions are for standalone compute, not interception.

## Inputs, outputs, dependencies
Input: HTTP requests matching config.matcher. Output: next()/rewrite()/redirect()/Response with modified headers. Needs: `@vercel/functions` package (non-Next.js), Edge Config for A/B, `vercel link` context; limits: 14KB URL, 4MB body, 64 headers/16KB.

## Key rules
1. Disambiguate the THREE middlewares: Vercel Routing Middleware (`middleware.ts`, any framework) vs Next.js 16 Proxy (`proxy.ts`, Node-only, renamed due to CVE-2025-29927 middleware-auth-bypass) vs Edge Functions — picking wrong file/runtime breaks silently.
2. Always scope with `config.matcher` — default runs on EVERY route and burns compute; regex-exclude static assets.
3. Middleware runs BEFORE cache — it's the right layer for geo/AB/header logic that must precede cached responses.
4. Request limits are hard: 14KB URL, 4MB body, 64 headers — exceeding them fails the request.
5. For operational routing changes without redeploy, use Project-Level Routes (Dashboard/API/CLI/SDK); reserve deployment config for deploy-coupled rules; only one of vercel.json OR vercel.ts per project.

## Risks / owner items
- Auth in middleware is explicitly defense-in-depth only — sole-auth architectures are vulnerable (CVE-2025-29927 history).
- Bun runtime is public beta (~28% latency claim); Node.js runtime via `runtime:'nodejs'` + `bunVersion` in vercel.json.
- Project-Level Routes (March 2026 feature) evaluation order matters: Bulk Redirects → Project routes → deployment config.
- Deprecated `middleware.ts` in Next.js 16 logs warnings; migration codemod exists.

## Category and tags
web, cloud — vercel, middleware, edge, routing, cdn, nextjs.

## Revision note
Single codex revision; unusually current (covers Next.js 16 proxy rename and 2026 project-level routes).
