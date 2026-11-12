# resize-for-social-media (canva-resize-for-social-media)

Tools: gemini-plugin (canva). Source: C:\Users\a7med\.gemini\config\plugins\canva\skills\resize-for-social-media\SKILL.md (149 lines, read in full)

## Summary
Resizes one Canva design into up to five social formats in parallel — Facebook post 1200x630, Facebook story 1080x1920, Instagram post 1080x1080, Instagram story 1080x1920, LinkedIn post 1200x627 — via Canva MCP tools (search-designs/get-design/resize-design), returning edit links for each result.

## When to use / not use
Use when the user wants one Canva design distributed across multiple social platforms at once. NOT for single-format resize (manual resize suffices), non-Canva assets, or platforms outside the five listed (TikTok, X, YouTube thumbnails are absent).

## Inputs, outputs, dependencies
Input: a design ID (D...), design URL, design name (via search-designs), or current-context design + platform selection. Output: resized designs with `urls.edit_url` links. Needs: Canva MCP with resize-design tool; falls back to informing user if unavailable.

## Key rules
1. Resolve the source design first: direct ID > URL extraction > search-designs by name (confirm on multiple matches) > conversation context.
2. Always ask which formats (or honor "all") — never assume all five.
3. Resize in PARALLEL — one resize-design call per selected format with exact pixel specs.
4. Error resilience: continue remaining formats on failure; report per-format success/failure at the end.
5. Present results as clickable edit links organized by platform; note FB story = IG story dimensions (1080x1920) so users don't expect two different files.

## Risks / owner items
- Requires resize-design in the host's MCP toolset — skill degrades gracefully but can't resize without it.
- Auto-resize quality: Canva's resize may need manual touch-up for aspect-ratio extremes (1:1 to 9:16); edit links are the remediation path.
- Only five hardcoded formats; new platforms need skill updates.
- No approval gate between steps — full workflow runs automatically once format selection is confirmed.

## Category and tags
media, business — canva, resize, social-media, design, mcp.

## Revision note
Single plugin revision; note frontmatter name is `canva-resize-for-social-media` while file lives under `resize-for-social-media`.
