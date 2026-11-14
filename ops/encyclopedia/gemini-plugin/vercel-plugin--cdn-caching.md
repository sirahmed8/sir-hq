# cdn-caching (Vercel)

## Summary
Expert runbook for debugging Vercel CDN caching across the CDN cache, durable ISR cache, function invocation, and image cache layers. Covers cache status/reason headers, PPR state, hit-rate and ISR-cost analysis via `vercel metrics`/`vercel logs`, BYPASS traffic triage, and concrete remediation (tag scoping, revalidation strategy, Cache-Control headers).

## When to use / when NOT
Use when investigating cache hit rates, ISR costs, stale content, BYPASS traffic, or per-path caching behavior on Vercel. Applies to any framework using ISR/PPR on Vercel (Next.js, SvelteKit, Nuxt, Astro). Do NOT use for caching data between a function and a backend (that's runtime-cache) or for non-Vercel hosts.

## Inputs, outputs, tools
- Inputs: team/project identifiers, deployment URL/path, optional request IDs, time window.
- Outputs: cache diagnosis, metric breakdowns, per-request CDN records, remediation guidance.
- Tools: Vercel CLI (`vercel metrics`, `vercel logs`, `vercel httpstat`), `curl` header inspection, dashboard Logs panel.

## 5 most important rules
1. Read `x-vercel-cache` (outcome) AND `cacheReason` (explanation) — metrics lump MISS/STALE together; reason distinguishes cold/collapsed/error/vary-key and stale_time/stale_tag/stale_error.
2. Treat HIT/STALE/PRERENDER as cache-served; focus on MISS; exclude BYPASS and (not set) from hit-rate math.
3. Prefer granular cache tags (`product-${id}`) plus a roll-up; broad tags have large blast radius and collapse hit rate.
4. Prefer tag-based on-demand revalidation over short time-based intervals; invalidate (SWR) keeps serving stale, delete forces foreground regen (REVALIDATED).
5. PPR still invokes the function on a shell hit (dynamic holes) — a Partial serve is not a cache miss; no holes means pure ISR HIT.

## Risks / things needing the owner
Metrics commands require Observability Plus (or a Priority project) for per-request logs; aggregate metrics need team/project flags. Purges propagate globally in ~300ms and are irreversible-ish (broad invalidation drops hit rate until re-warm). Never treat expected BYPASS (Draft Mode, SEO crawlers) as a bug.

## Category / tags
cloud · vercel, cdn, caching, isr, ppr, observability

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\cdn-caching\SKILL.md` (~20KB). No duplicate. Skill name in frontmatter: cdn-caching.