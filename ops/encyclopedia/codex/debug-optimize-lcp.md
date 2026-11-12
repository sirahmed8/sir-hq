# debug-optimize-lcp

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\debug-optimize-lcp\SKILL.md`
- SKILL.md size: 6588 chars

## What it does

Guides debugging and optimizing Largest Contentful Paint (LCP) using Chrome DevTools MCP tools. Use this skill whenever the user asks about LCP performance, slow page loads, Core Web Vitals optimization, or wants to understand why their page's main content takes too long to appear. Also use when the user mentions "largest contentful paint", "page load speed", "CWV", or wants to improve how fast their hero image or main content renders.

## Structure (headings inside SKILL.md)

- What is LCP and why it matters
- LCP Subparts Breakdown
- Debugging Workflow
- Step 1: Record a Performance Trace
- Step 2: Analyze LCP Insights
- Step 3: Identify the LCP Element
- Step 4: Check the Network Waterfall
- Step 5: Inspect HTML for Common Issues
- Optimization Strategies
- 1. Eliminate Resource Load Delay (target: <10%)
- 2. Eliminate Element Render Delay (target: <10%)
- 3. Reduce Resource Load Duration (target: ~40%)
- 4. Reduce TTFB (target: ~40%)
- Verifying Fixes & Emulation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Fix**: Use standard `<img>` with `src`. **Never** lazy-load the LCP image.

## Files inside the skill

- `references/elements-and-size.md` — "Elements and Size for LCP"
- `references/lcp-breakdown.md` — "Largest Contentful Paint (LCP) Breakdown"
- `references/lcp-snippets.md` — "LCP Debugging Snippets"
- `references/optimization-strategies.md` — "LCP Optimization Strategies"
