# figma-shaders

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-shaders\SKILL.md`
- SKILL.md size: 5416 chars

## What it does

Author, edit, and iterate on custom.

## Structure (headings inside SKILL.md)

- Create and update Figma shaders
- Create workflow
- Update workflow
- Authoring rules
- Completion
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP resources

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1. Identify the shader with `list_shaders`, then call `get_shader`. Use its `type` (`effect` or `fill`) as the required update kind.
2. 2. Read every source URI returned by `get_shader` before editing. If the client cannot read MCP resources, call it with `includeSource: true`. Treat those files as the current source of truth.
3. - Before writing the `main.ts` replacement, read [Shader source authoring](references/authoring.md). It contains the required module shape, WebGPU lifecycle, supported parameter schemas, effect/fill alpha rules, and WGSL failure checklist.
4. - Prefer `frame.time` for animation so skipped frames do not change the result. It is an absolute millisecond clock; convert it to seconds with `Number(frame.time) * 0.001` when useful.
5. - For effects, sample the input raster intentionally. For fills, do not assume an input raster exists.

## Files inside the skill

- `references/authoring.md` — "Shader source authoring"
