# figma-shaders

## Summary
Workflow for authoring and updating custom Figma shaders (WebGPU/WGSL effects and fills) in the account library via MCP tools `create_shader`, `get_shader`, `update_shader`, `list_shaders`. Two kinds: `effect` (post-processes the rendered layer beneath — blur, glow, color grading, halftone) and `fill` (generates pixels — gradients, noise, textures). `create_shader` only makes a starter scaffold; the agent must author the full `main.ts` replacement. Module shape, parameter schemas and WGSL failure checklist live in references/authoring.md.

## When to use / when NOT
Load before every `create_shader`/`update_shader` call. Reading or applying existing shaders does not need this skill. Do NOT switch `kind` during an update, and do NOT treat animation/mouse capability errors as retryable — they are terminal gates.

## Inputs, outputs, tools
- Inputs: desired visual (effect vs fill), planKey, shader id for updates, authored `main.ts`.
- Outputs: shader name/kind/id/version plus a try-it URL `figma.com/file/new?try-tool-resource-content-id=<id>&try-tool-resource-type=<gen_effect|gen_fill>&type=design&mode=design`.
- Tools: Figma MCP `whoami`, `create_shader`, `get_shader` (read every source URI, or `includeSource: true`), `update_shader` (complete `main.ts` replacement via `files` array; `metadata` updates name/description/isAnimated/usesMouse; empty files array = metadata-only), `list_shaders`.

## 5 most important rules
1. Decide effect vs fill up front; `update_shader` kind must match the existing shader's type.
2. Never stop after create — replace the scaffold's `main.ts` completely; read authoring.md before writing it.
3. Keep metadata honest: `isAnimated: true` only when the source reads `frame.time`/`deltaTime`/`frame`; `usesMouse: true` only when it reads `frame.mousePosition`; update_shader syncs these to the fixed features.json manifest.
4. Prefer `frame.time` (absolute ms clock, `* 0.001` for seconds) over frame counts so skipped frames do not change output; expose tunable controls, keep ranges bounded.
5. On capability errors (animation/mouse unavailable) do not retry or bypass — offer a static shader with keyframable properties instead; on build errors fix minimally once, then surface.

## Risks / owner needs
Requires a Figma plan seat; shaders consume account library slots. WebGPU support varies — the skill treats unsupported capabilities as hard gates rather than risks to engineer around.

## Category and tags
Category: design. Tags: figma, mcp, shaders, webgpu, wgsl, generative.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
