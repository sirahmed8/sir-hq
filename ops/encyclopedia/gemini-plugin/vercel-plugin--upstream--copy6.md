# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\is-agentic\upstream\SKILL.md`
- SKILL.md size: 3849 chars

## What it does

Score how ready a website, domain, or public MCP endpoint is for AI agents using Is Agentic, and read or act on the resulting report. Use when asked to check a site's agent readiness, get its Is Agentic score, fetch a scored report as JSON, or fix the issues that lower a site's score.

## Structure (headings inside SKILL.md)

- Is Agentic
- Get a score
- Read a report
- Improve a site's score
- Errors
- Gotchas

## Tools / MCPs it needs

- MCP mentions: MCP hosts, MCP server

## Risks / cautions found in text

- - For token-light reading, content pages and completed reports honor `Accept: text/markdown`.

## Key rules (verbatim lines from SKILL.md)

1. - `score`: 0 to 100, or `null` when the target could not be scored (for example an MCP server that requires authentication). `score_label` explains a null score.
2. - `score_breakdown.bonus`: `points` and `positive_signals`. Bonus is additive and never required; do not treat missing bonus signals as defects.
3. 4. After deploying fixes, get a fresh score and compare `scanned_at` to confirm you are not reading the old snapshot (see gotchas).
4. - `report_not_found` (404): no completed report exists; create one with the CLI, or open `https://is-agentic.com/scan/<target>` to start a scan, then retry after it completes.
5. - `rate_limit_exceeded` (429): honor `Retry-After` before retrying.

## Files inside the skill

- (SKILL.md only)
