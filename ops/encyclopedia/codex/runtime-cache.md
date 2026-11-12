# runtime-cache

Tools: codex (also claude/cursor/opencode/windsurf; codex chosen). Source: C:\Users\a7med\.codex\skills\runtime-cache\SKILL.md (234 lines, read in full)

## Summary
Vercel Runtime Cache API guide: per-region ephemeral key-value store for Functions/Middleware/Builds via `@vercel/functions` `getCache()` — set/get/delete with TTL + tags, `expireTag` for tag invalidation, plus the separate CDN purge layer (`invalidateByTag` stale-while-revalidate vs `dangerouslyDeleteByTag`), Next.js 16 `'use cache: remote'` integration, CLI cache commands, and hard limits.

## When to use / not use
Use for caching API responses/computed data across functions within a region, tag-based invalidation on content change, reducing DB load. NOT for framework page caching (use Cache Components), persistent storage (use a DB), CDN response caching (use Cache-Control headers), cross-region state, or per-user data.

## Inputs, outputs, dependencies
Input: cache keys, values (<=2MB), TTL seconds, up to 64 tags per item. Output: cached values or undefined; invalidation via expireTag/invalidateByTag/vercel CLI. Needs: `@vercel/functions`, Vercel deployment; Next.js 16 users need `cacheComponents: true` for remote cache.

## Key rules
1. THREE separate cache layers exist and tags do NOT cross them: `cache.expireTag` = Runtime Cache only; `invalidateByTag` = CDN+Runtime+Data (SWR); `dangerouslyDeleteByTag` = hard delete (stampede risk); ISR is isolated from ALL of them — manage both layers with the same tag via invalidateByTag.
2. Regional + isolated: each region has its own cache, scoped per project AND per environment (preview vs production) — never assume cross-region or cross-env visibility.
3. Ephemeral: fixed per-project storage, LRU eviction when full — it's a cache, not storage; persistent data needs a database.
4. Next.js 16: `'use cache: remote'` stores in Runtime Cache; plain `'use cache'` is in-memory per-instance only. Single-arg `revalidateTag(tag)` is DEPRECATED — always pass a cacheLife profile; `updateTag` = Server Actions immediate, `revalidateTag(tag,'max')` = SWR.
5. Limits are hard: 2MB items, 64 tags/item (Runtime) vs 128 (CDN), 256-byte tags, case-sensitive, no commas, 16 tags per bulk REST call.

## Risks / owner items
- `dangerouslyDeleteByTag` causes cache stampedes (next request blocks on origin) — prefer invalidateByTag unless freshness is critical.
- Data survives deploys but evicts under memory pressure — cold-cache storms possible after LRU pressure.
- Tag propagation is ~300ms global — brief stale windows after expireTag.
- Observability via Dashboard → Observability → Runtime Cache; CLI purge commands can nuke ALL cached data (`vercel cache purge`) — destructive, use --type scoping.

## Category and tags
cloud, web, build — vercel, caching, runtime-cache, nextjs, invalidation.

## Revision note
Single codex revision; current through March 2026 CDN dashboard changes.
