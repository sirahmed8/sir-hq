# custom-metrics

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\custom-metrics\SKILL.md`
- SKILL.md size: 4662 chars

## What it does

Emit and query Vercel Custom Metrics.

## Structure (headings inside SKILL.md)

- Vercel Custom Metrics
- Emit a metric
- Model metrics for useful queries
- Discover and query the metric
- Use the right signal
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - `tags` are optional string attributes. After ingestion, discovered tag keys appear as dimensions for filtering and grouping.
2. - `metric()` is synchronous and returns `void`; do not `await` it.
3. - Do not use the reserved `vercel.` prefix for application-defined names.
4. - Keep variable data in tags instead of metric names. Use `checkout.completed` with `{ plan: 'pro' }`, not `checkout.completed.pro`.
5. - Keep tag cardinality bounded. Good tags are `outcome`, `plan`, `provider`, or a normalized route. Do not attach user IDs, request IDs, email addresses, raw URLs, or other unique or sensitive values.

## Files inside the skill

- (SKILL.md only)
