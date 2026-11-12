# netlify-caching

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-caching\SKILL.md`
- SKILL.md size: 14813 chars

## What it does

Cache dynamic and static responses on.

## Structure (headings inside SKILL.md)

- Netlify caching
- Cache-control header to reach for
- Footguns (read first)
- Directives
- Cache key variation — `Netlify-Vary`
- Cache tags & opt-out
- On-demand invalidation (purge)
- Cache API (`caches` global)
- `@netlify/cache` module
- `cacheHeaders(settings)` → header object
- `fetchWithCache(resource, options?, cacheSettings?)`
- `getCacheStatus(response | headers | headerString)`
- `needsRevalidation(response)` → boolean
- Durable cache
- Debugging with `Cache-Status`
- Netlify house rules (caching)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Cache API silently drops responses over 10 MB.** `cache.put()` doesn't store them and later lookups miss. Compress the content or split it across multiple entries.
- - `cache.delete(request)` returns `true`.
- 4. `purgeCache()` has ambient credentials only inside a deployed function.

## Key rules (verbatim lines from SKILL.md)

1. - Never opt sensitive content out of automatic invalidation. It can stay publicly cached after deploys/firewall changes.
2. - `stale-while-revalidate=N` serves stale for N seconds after expiry while revalidating in the background.
3. - `durable` (serverless only) stores the response in Netlify's durable cache so other edge nodes reuse it instead of re-invoking the function.
4. - Static: `Netlify-CDN-Cache-Control: public, s-maxage=31536000, must-revalidate`
5. - Dynamic: `Cache-Control: public, max-age=0, must-revalidate`

## Files inside the skill

- (SKILL.md only)
