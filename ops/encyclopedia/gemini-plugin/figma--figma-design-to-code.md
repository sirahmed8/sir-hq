# figma-design-to-code

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-design-to-code\SKILL.md`
- SKILL.md size: 3571 chars

## What it does

Implement and translate Figma frames.

## Structure (headings inside SKILL.md)

- Figma design to code
- Context
- Implementation
- Verification
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP resource

## Risks / cautions found in text

- - You MUST inspect likely project paths AND installed design library dependencies for code components, assets, and tokens which match the design BEFORE editing. You MUST reuse or compose suitable matches instead of recreating them with raw markup, inline styles or hardcoded values; modify or supplem

## Key rules (verbatim lines from SKILL.md)

1. - **Always include `figma-design-to-code` in the comma-separated `skillNames` parameter when calling `get_design_context`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-design-to-code`).** This is a logging parameter used to track skill
2. - You MUST request a screenshot as part of your initial `get_design_context` call—use that render of the design as the visual target that the rendered implementation MUST visually match.
3. - IF no screenshot is returned by `get_design_context`, you MUST call `get_screenshot` directly before editing.
4. - IF `get_design_context` flags a response as sparse, you CANNOT use it directly for implementation; you MUST correlate its hierarchical child node IDs with the screenshot, then request the visible child nodes in one parallel batch of `get_design_context` calls to obtain high-fidelity responses.
5. - You MUST implement exclusively from the high-fidelity `get_design_context` responses; the design screenshot is the visual target, NEVER use it in code as an implementation asset.

## Files inside the skill

- (SKILL.md only)
