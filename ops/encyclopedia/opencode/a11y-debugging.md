# a11y-debugging

Source read: `C:\Users\a7med\.codex\skills\a11y-debugging\SKILL.md` plus `references/a11y-snippets.md`.

## Summary
This skill turns Chrome DevTools MCP into a practical accessibility audit loop for web pages. It starts with Lighthouse and Chrome's native issue reports, then uses the accessibility tree, DOM order, form labels, keyboard focus, tap-target measurements, contrast checks, and document-level checks to find semantic and operability problems that a normal visual pass misses.

## When to use / when NOT
Use while building or reviewing web UI, before release, or when a page feels usable but may fail keyboard, screen-reader, contrast, or touch-target requirements. Do not treat it as a complete substitute for manual screen-reader testing, and do not use it for native mobile apps or non-browser surfaces without an equivalent inspection path.

## Inputs, outputs, tools
Inputs are an open browser page, its `pageId`, target elements or `uid`s, and the audit goal. Outputs are prioritized findings with selectors or element references plus concrete fixes. Tools are Chrome DevTools MCP functions such as `list_pages`, `new_page`, `take_snapshot`, `list_console_messages`, `evaluate_script`, `press_key`, `take_screenshot`, and `lighthouse_audit`, plus the bundled JavaScript snippets and web.dev `.md.txt` pages. The skill expects the Chrome DevTools MCP connector.

## 5 most important rules
1. Page-scoped tools need a valid `pageId`; get it from `list_pages` or `new_page`.
2. Treat the accessibility tree from `take_snapshot` as the source of truth for what assistive technology sees.
3. Run Lighthouse first for a baseline, then parse the JSON for failing audits instead of reading the whole report.
4. Check Chrome's native `issue` console messages before manually investigating labels, contrast, and semantics.
5. Use the bundled snippets for orphaned inputs, tap-target size, approximate contrast, and global page checks, then verify focus movement with Tab snapshots.

## Risks / owner notes
Automated contrast math is approximate and can miss gradients, transparency, or complex backgrounds; Lighthouse and headless runs can also miss issues. Findings still need human review before changing brand or layout. The owner should decide which WCAG level the product must meet and whether legal or customer requirements apply.

## Category / tags
web · accessibility, a11y, wcag, chrome-devtools, keyboard, contrast, tap-targets, frontend

## Revisions
The codex, kilo, cursor, and windsurf copies are byte-identical and selected here because codex has the fuller description. The gemini-plugin chrome-devtools copy has the same workflow body but a shorter frontmatter description.
