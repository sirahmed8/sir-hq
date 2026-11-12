# next-cache-components

Tools: codex, cursor, kilo, opencode, windsurf (codex copy used; content identical across tools).
Source: C:\Users\a7med\.codex\skills\next-cache-components\SKILL.md

## Summary
Guide to Next.js 16 Cache Components: enabling `cacheComponents: true` in next.config, then composing a route from three tiers of content — auto-prerendered static, `'use cache'` cached async work (with `cacheLife` profiles and `cacheTag`/`updateTag`/`revalidateTag` invalidation), and dynamic runtime data wrapped in Suspense. It replaces the old experimental PPR flag and supersedes `unstable_cache`, `force-static`, and `revalidate` exports.

## When to use / not use
Use when building or reviewing Next.js 16 App Router pages that mix static shells, cacheable data, and per-request dynamic content (PPR). Do not use for Pages Router, Next.js 15 or older (the API does not exist), Edge runtime routes, or fully static exports — Cache Components require a Node.js server.

## Inputs, outputs, dependencies
Input: a Next.js 16 project; the skill supplies config snippets and code patterns. Output: a route file mixing `'use cache'` functions, Suspense boundaries, and cache tags. Needs: `next/cache` (`cacheLife`, `cacheTag`, `updateTag`, `revalidateTag`), `next/server` (`connection`), React `Suspense`, a database or fetch source. No external MCPs.

## Key rules
1. Enable once with `cacheComponents: true`; never use `experimental.ppr`.
2. Three tiers: sync JSX prerenders, `'use cache'` caches async work, Suspense-wrapped runtime reads stream fresh data.
3. `'use cache'` can sit at file, component, or function level; `cacheLife()` picks a built-in profile (`'minutes'`…`'max'`) or inline `{stale, revalidate, expire}`.
4. `cookies()`, `headers()`, `searchParams` are forbidden inside `use cache`; extract them outside and pass values as arguments (they join the cache key). Escape hatch: `'use cache: private'`.
5. Invalidate deliberately: `updateTag` for same-request freshness in server actions, `revalidateTag` for background SWR.

## Risks / owner items
- `Math.random()`/`Date.now()` inside `use cache` freeze at build time; use `await connection()` to force request-time execution.
- Migration table provided (`unstable_cache` → `'use cache'`, `revalidate` → `cacheLife`) — upgrading a codebase needs this applied everywhere or stale cache bugs appear.
- `'use cache: private'` relaxes the runtime-API ban; use only for compliance cases.

## Category and tags
build, web — nextjs, caching, ppr, performance, app-router.

## Revision note
Only one revision found (identical across five tools); codex copy read in full.
