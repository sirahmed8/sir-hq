# runtime-cache

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\runtime-cache\SKILL.md`
- SKILL.md size: 7554 chars

## What it does

Configure Vercel Runtime Cache API for.

## When to use (from skill text)

- | `revalidateTag(tag, { expire: 0 })` | Route Handlers (webhooks) | Immediate expiration from external triggers |
- Monitor hit rates, invalidation patterns, and storage usage in the Vercel Dashboard under **Observability → Runtime Cache**. The CDN dashboard (March 5, 2026) provides a unified view of global traffic distribution, cache performance metrics, a redesigned purging interface, and **project-level routin

## Structure (headings inside SKILL.md)

- Vercel Runtime Cache API
- What It Is
- Key APIs
- Basic Cache Operations
- Cache Options
- Full Example (Framework-Agnostic)
- Tag Expiration from Server Action
- CDN Cache Purging Functions
- Next.js Integration
- Next.js 16+ (`use cache: remote`)
- Next.js 16 Invalidation APIs
- Runtime Cache vs ISR Isolation
- CLI Cache Commands
- Purge all cached data
- Invalidate by tag (stale-while-revalidate)
- Hard delete by tag (blocks until revalidated)
- Image invalidation
- CDN Cache Tags
- Limits
- Observability
- When to Use
- When NOT to Use
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Isolated**: Scoped per deployment environment (`preview` vs `production`); scoped per project on Pro/Enterprise, but shared across all projects on a Hobby team
- - `invalidateByTag()` / `dangerouslyDeleteByTag()` — purges CDN + Runtime + Data caches

## Key rules (verbatim lines from SKILL.md)

1. - **Regional**: Each Vercel region has its own isolated cache
2. - **Isolated**: Scoped per deployment environment (`preview` vs `production`); scoped per project on Pro/Enterprise, but shared across all projects on a Hobby team
3. - **Persistent across deployments**: Cached data survives new deploys; invalidation via TTL or `expireTag`

## Files inside the skill

- (SKILL.md only)
