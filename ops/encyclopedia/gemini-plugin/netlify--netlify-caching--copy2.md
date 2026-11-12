# netlify-caching (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-caching\SKILL.md`. CDN caching for dynamic/static responses on Netlify.

## Summary
Dynamic responses (Functions/Edge Functions/proxies) are NOT cached by default — opt in with `Netlify-CDN-Cache-Control` (CDN-only, preferred), `CDN-Cache-Control` (all CDNs), or `Cache-Control` (downstream/browser). Directives: `public`/`private`/`no-store`, `s-maxage` (shared cache, overrides max-age), `max-age`, `stale-while-revalidate`, `durable` (serverless-only — persists in Netlify durable cache so other edge nodes reuse it; no effect on Edge Functions). Defaults: static = `public, s-maxage=31536000, must-revalidate`; dynamic = `public, max-age=0, must-revalidate`. `Netlify-Vary` varies the cache key by query/header/cookie/country/language (`query=item_id`, `country=es+de`, `language=en|es+pt` with `+` groups, `cookie=key`); can't vary by Accept*/Cookie/Host/Referer/UA etc. — a URL must return the SAME `Netlify-Vary` on every response (first cached wins). Tags: `Netlify-Cache-Tag`/`Cache-Tag` (≤1024 chars, ≤500 tags) for taggable purge; `Netlify-Cache-ID` opts OUT of automatic atomic-deploy invalidation (auto-registers as purge tags, 500-ID limit — purge manually after proxy/function changes). Purge via `purgeCache` from `@netlify/functions` (no args = whole site; tags+deployAlias+domain targeting; Lambda-style handlers must pass `context.clientContext.custom.purge_api_token`) or direct `POST api.netlify.com/api/v1/purge` with PAT. Footguns: static assets fresh up to a year (shorter max-age ignored — only new deploy/manual purge changes them); basic-auth on ANY page disables caching ENTIRE site; Cache API silently drops responses >10MB; never opt sensitive content out of auto-invalidation; avoid legacy On-demand Builders (TTL-only, URL-path keying, no Netlify-Vary).

## When to use / when NOT
Use when adding cache headers, tuning TTL/SWR, setting up durable cache, varying cache keys, purging by tag, or debugging `Cache-Status`. NOT for ODB-style TTL caching in new code or for caching sensitive content improperly.

## Inputs, outputs, tools
- Inputs: response headers (`Netlify-CDN-Cache-Control`, `Netlify-Vary`, `Netlify-Cache-Tag`/`Cache-ID`), purge calls.
- Outputs: CDN-cached responses, varied cache keys, tag-scoped purges.
- Tools: `@netlify/functions` (`purgeCache`, `fetchWithCache`/`cacheHeaders`/`getCacheStatus`), Cache API, purge API.

## 5 most important rules
1. Dynamic responses need explicit `Netlify-CDN-Cache-Control` — nothing caches by default.
2. `durable` is serverless-only; `Netlify-Vary` must be identical on every response for a URL (first wins).
3. `Netlify-Cache-ID` opts out of auto-invalidation — you then own purging.
4. Static assets ignore max-age <1yr; basic-auth anywhere kills site-wide caching.
5. Cache API drops >10MB responses silently; never exempt sensitive content from auto-invalidation.

## Risks / owner notes
Stale content after deploys if purge tags are wrong; site-wide cache kill via basic-auth is a nasty surprise; >10MB silent misses; PAT needed for direct API purges.

## Category and tags
Category: cloud. Tags: netlify, caching, cdn, cache-control, vary, purge, durable-cache, edge-functions.
