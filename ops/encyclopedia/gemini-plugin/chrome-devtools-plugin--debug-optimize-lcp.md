# debug-optimize-lcp

## Summary
Chrome DevTools MCP workflow for debugging and optimizing Largest Contentful Paint: record a reload trace, analyze LCP insights (LCPBreakdown subparts, DocumentLatency, RenderBlocking, LCPDiscovery), identify the LCP element via script snippet, inspect the network waterfall timing, audit HTML for lazy-loaded LCP images/missing fetchpriority/render-blockers, then apply prioritized fixes per bottleneck subpart (TTFB ~40%, load delay <10%, load duration ~40%, render delay <10%) and verify by re-tracing, optionally under Fast 3G + 4x CPU throttle.

## When to use / when NOT
Use when the user reports slow page loads, asks about LCP/Core Web Vitals, or wants hero-image/main-content speed. Do NOT use for general JS profiling, INP/CLS work, or non-browser performance.

## Inputs, outputs, tools
- Inputs: target page URL.
- Outputs: LCP subpart breakdown, identified LCP element, prioritized fixes, before/after trace comparison.
- Tools: Chrome DevTools MCP — navigate_page, performance_start_trace (reload+autoStop), performance_analyze_insight, evaluate_script, list_network_requests, get_network_request, emulate; references/lcp-snippets.md.

## 5 most important rules
1. Optimize the BOTTLENECK subpart, not just the biggest file — check all four subparts first; shrinking an image doesn't help if render delay dominates.
2. Never lazy-load the LCP image; use plain `<img src>`, add `fetchpriority="high"` and preload link if discovered late.
3. Render delay fixes: inline critical CSS, defer non-critical, break long tasks, SSR so the element is in initial HTML.
4. Duration fixes: WebP/AVIF + srcset, CDN, Cache-Control; `font-display: swap` for font-blocked text LCP.
5! Verify with a fresh reload trace comparing subparts; lab ≠ field — emulate Fast 3G + CPU throttle to surface real-world issues.

## Risks / things needing the owner
Trace/insight names are DevTools-MCP-specific and may change. Fixes touch production HTML/headers — owner reviews before deploy.

## Category / tags
web · performance, lcp, core-web-vitals, devtools, optimization

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all ~6588 bytes identical.
