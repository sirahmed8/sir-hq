# next-cache-components

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\next-cache-components\SKILL.md`
- SKILL.md size: 9372 chars

## What it does

Next.js 16 Cache Components guidance: PPR, 'use cache', cacheLife, cacheTag, and invalidation.

## When to use (from skill text)

- Use when you need the cache refreshed within the same request:

## Structure (headings inside SKILL.md)

- Cache Components (Next.js 16+)
- Enable Cache Components
- Three Content Types
- 1. Static (Auto-Prerendered)
- 2. Cached (`use cache`)
- 3. Dynamic (Suspense)
- `use cache` Directive
- File Level
- Component Level
- Function Level
- Cache Profiles
- Built-in Profiles
- `cacheLife()` - Custom Lifetime
- Inline Configuration
- Cache Invalidation
- `cacheTag()` - Tag Cached Content
- `updateTag()` - Immediate Invalidation
- `revalidateTag()` - Background Revalidation
- Runtime Data Constraint
- Solution: Pass as Arguments
- Exception: `use cache: private`
- Cache Key Generation
- Complete Example
- Migration from Previous Versions
- Migrating `unstable_cache` to `use cache`
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Edge runtime not supported** - requires Node.js

## Files inside the skill

- `overlay.yaml`
