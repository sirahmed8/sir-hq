# cdn-caching

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\cdn-caching\SKILL.md`
- SKILL.md size: 20335 chars

## What it does

Debug Vercel CDN caching.

## When to use (from skill text)

- - **What triggered revalidation** — group `vercel.request.count` by `triggering_tag` to see which tags fire most often (`triggering_tag` is on request count only, not ISR operation metrics. It is one of the tags that triggered the page to be stale):
- -f "triggering_tag:*" --group-by triggering_tag --since 24h
- **Confirm in code.** Metrics tell you _which_ tag is hot; the repo tells you _why_. Grep for the tag's invalidation call site — `revalidateTag(`, `invalidateByTag(`, `updateTag(`, `dangerouslyDeleteByTag(` — and read the trigger. A CMS webhook or a sync cron that invalidates a **broad** tag on every

## Structure (headings inside SKILL.md)

- Vercel Caching
- Core Knowledge
- How caching works
- Investigating cache issues
- Cache hit rate
- Analyzing ISR costs
- numerator: cache serves — sum the HIT + STALE + PRERENDER buckets
- denominator: ISR writes
- Debugging BYPASS traffic
- Reducing ISR cost
- Inspect one path
- FAQ
- Related skills
- References:
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Invalidate vs. dangerously-delete** — two ways to clear content, with very different blast on hit rate:
- - _Dangerously-delete_ (`dangerouslyDeleteByTag`, Next.js `updateTag`, `revalidatePath`, or `revalidateTag(tag)` with no profile) = hard removal. The next request blocks in the **foreground** to regenerate → `x-vercel-cache: REVALIDATED`.
- - **Cache tags & blast radius** — tags group cached entries so one call can clear many. A coarse tag attached to thousands of paths has a large _blast radius_: a single write drops them all and the hit rate collapses until they re-warm. Prefer granular tags (`product-${id}`) plus a roll-up tag.

## Key rules (verbatim lines from SKILL.md)

1. - **Image cache** — optimized images, cached on the CDN after the first transform.
2. - **Revalidation** — refreshing cached content. **Time-based** runs automatically after an interval; **on-demand** runs when you call an API. Both use stale-while-revalidate: visitors keep getting the cached version while the new one regenerates in the background.
3. - **Does PPR avoid function invocations?** No — a PPR route has dynamic holes by definition, so the cached shell hit still runs the function to fill them. (A route with _no_ holes is just ISR and serves a pure `prerender` HIT — see Key concepts.)

## Files inside the skill

- (SKILL.md only)
