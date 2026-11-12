# routing-middleware

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\routing-middleware\SKILL.md`
- SKILL.md size: 8607 chars

## What it does

Vercel Routing Middleware guidance: request interception, rewrites, redirects, and edge routing.

## When to use (from skill text)

- **Project-level routes** (added March 2026) let you update routing rules — response headers, rewrites to external APIs — without triggering a new deployment. They run after bulk redirects and before deployment config routes. Available on all plans.

## Structure (headings inside SKILL.md)

- Vercel Routing Middleware
- What It Is
- CRITICAL: Middleware Disambiguation
- Bun Runtime
- Basic Example
- Helper Methods (`@vercel/functions`)
- Matcher Configuration
- Common Patterns
- IP-Based Header Injection
- A/B Testing via Edge Config
- Background Processing
- Request Limits
- Three CDN Routing Mechanisms
- Project-Level Routes — Configuration Methods
- Programmatic Configuration with `vercel.ts`
- When to Use
- When NOT to Use
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Default export required** (function name can be anything)
2. - Geo-personalization of static pages (runs before cache)

## Files inside the skill

- (SKILL.md only)
