# get-design-feedback (canva plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\canva\skills\get-design-feedback\SKILL.md` (only revision; gemini-plugin only).

## Summary
A read-only design critic for Canva. It resolves a design (short link, URL, or raw `D...` ID), pulls the rendered thumbnail plus text content (and optionally a read-only editing transaction for element geometry), then returns prioritised feedback across visual hierarchy, layout/spacing, copy, consistency, readability/contrast, accessibility, and fitness for the stated channel. Output is structured per page with High/Med/Low severities and concrete fixes, ending with an offer to hand off to `canva-edit-design` or `canva-implement-feedback`.

## When to use / when NOT
Use when the user asks to review, critique, or get feedback on a Canva design ("review my design", "what's wrong with this slide"). Do NOT use to actually change the design (that is `canva-edit-design`/`canva-implement-feedback`), and do not use for non-Canva images.

## Inputs, outputs, tools
- Inputs: a Canva short link, full URL, or design ID; optionally the user's stated purpose/channel.
- Outputs: markdown feedback report grouped by page with severities and fixes.
- Tools: Canva MCP tools `get-design`, `get-design-thumbnail`, `get-design-pages`, `get-design-content`, `resolve-shortlink`, and optionally `start-editing-transaction`/`cancel-editing-transaction` (never commit).

## 5 most important rules
1. Strictly read-only: any editing transaction opened for inspection must be cancelled, never committed.
2. The thumbnail is the primary source for color, contrast, and typography judgement; `get-design-content` returns text only.
3. Colors and fonts are NOT reliably exposed by the API; never report a specific hex/font as fact unless the payload contained it.
4. Every critique point must be grounded in something actually observed; no generic advice.
5. Prioritise: lead with the few highest-impact items, pair every problem with a specific located fix.

## Risks / owner notes
Low risk. Requires Canva MCP connection and an authenticated Canva account. Transaction inspection depends on API behaviour that the skill itself documents as unreliable for styles.

## Category and tags
Category: design. Tags: canva, mcp, design-review, feedback, read-only, accessibility.
