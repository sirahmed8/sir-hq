# netlify-edge-functions (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-edge-functions\SKILL.md`. Deno-based edge handlers in `netlify/edge-functions`.

## Summary
Edge Functions are Deno TypeScript/JS handlers running at the network edge in front of static files and serverless functions. Form: one file = default-export handler `(request, context)` + `config` export with `path`/`pattern`/`excludedPath` (or `[[edge_functions]]` in toml). `Request`/`Response` are global; import `Context`/`Config` types from `@netlify/edge-functions`; env vars via `Netlify.env.get()` (`process.env` only for Next.js middleware). Return semantics: `Response` = send + end chain; `URL` = same-site rewrite (200, address bar unchanged); `undefined`/`return;` = skip, chain continues. Footguns: no route = silent no-op; `path:"/*"` hits EVERY request incl. assets (narrow or use excludedPath); caching needs BOTH `cache:"manual"` in config AND cache headers on the Response; cached functions SHADOW static files (a cached `/*` serves `/cat.png` instead of the file); returning a Response ends the redirect chain; same-site `fetch()`/URL rewrites start a NEW request chain (matching edge functions re-run — use `context.next()` for static/SSR at same path); request body readable once (pass `new Request(req,{body})` to `context.next()`); same-named `.ts`+`.js` → JS deploys, TS ignored; 50ms CPU per request incl. waitUntil; NOT executed on Split Testing sites; custom headers/basic-auth don't apply; unsupported on HIPAA hosting; `netlify.app` is on Public Suffix List (cross-subdomain cookies need custom domain). Avoid: deno.json import maps (use `[functions] deno_import_map`), toml env vars (invisible), `Netlify.env.set/delete` as persistence (per-invocation only), same-site fetch for current path.

## When to use / when NOT
Use for auth middleware/login gates, geo/cookie redirects, localization, A/B testing, HTML transforms, edge SSR, edge caching. NOT for HIPAA sites, Split Testing sites, or anything needing >50ms CPU.

## Inputs, outputs, tools
- Inputs: route config, request/geo/cookie context, env vars via `Netlify.env`.
- Outputs: Response/URL-rewrite/pass-through; edge-cached responses.
- Tools: `@netlify/edge-functions` types, `context.geo`/`context.next()`/`context.cookies`, `Netlify.env`, `netlify/edge-functions/` dir or `[build] edge_functions`.

## 5 most important rules
1. Every function needs an explicit route — no route = silent no-op.
2. Caching = `cache:"manual"` + response cache headers, BOTH required; cached `/*` shadows static files.
3. `context.next()` for same-path static/SSR; same-site fetch/URL rewrite re-runs the whole chain.
4. Env via `Netlify.env.get()` only; toml vars invisible; `Netlify.env.set` isn't persistence.
5. Request body is single-read — reconstruct Request when passing to `context.next()`.

## Risks / owner notes
50ms CPU cap kills heavy work silently into waitUntil; ordering bugs (edge before redirects, Response ends chain) cause confusing routing; basic-auth/custom headers bypass is a security consideration for gated content.

## Category and tags
Category: cloud. Tags: netlify, edge-functions, deno, middleware, geo-targeting, caching, low-latency.
