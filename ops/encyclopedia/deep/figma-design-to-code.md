# figma-design-to-code

## Summary
The core Figma-to-code implementation discipline: pull a frame's context and screenshot via `get_design_context`, then translate it into the project's real stack — reusing design-library components and Code Connect mappings, placing every static asset exactly where the design uses it, and verifying the rendered result matches the screenshot. It is less a tool guide than a strict contract for HOW to implement from Figma output without producing a brittle pixel replica.

## When to use / when NOT
Use whenever implementing a Figma frame/screen into code. Do NOT use the screenshot as an implementation asset (it is only the visual target), and do NOT skip `get_design_context` — sparse responses must be expanded by batch-requesting visible child nodes.

## Inputs, outputs, tools
- Inputs: a Figma node/frame (via file key + node id), the target project's component library and conventions.
- Outputs: implemented, interactive code matching the design; verified assets and geometry.
- Tools: Figma MCP `get_design_context` (must pass `skillNames` including `figma-design-to-code`, prefixed `resource:` when loaded via MCP resource), `get_screenshot` fallback, `get_design_context` batch calls for sparse responses; project build/render for verification.

## 5 most important rules
1. Always request a screenshot in the first `get_design_context` call; if none returns, call `get_screenshot` before editing — the render is the visual target, never a code asset.
2. Sparse responses are forbidden as implementation source: correlate child node IDs with the screenshot and batch-request the visible children for high-fidelity context.
3. Adapt returned code to project conventions: translate absolute positioning into native layout, implement intended interactivity, and inspect project paths plus installed design-library deps BEFORE editing.
4. Reuse Code Connect components at their mapped nodes and reuse/composed design-library assets; only modify when they cannot express the design. Never omit, redraw, inline, or substitute static assets; download every asset to a local non-temporary path and never leave Figma URLs in code; do not override root width/height on SVGs.
5. Verify only the requested screen/component: every visible asset's local file, design slot, callsite and rendered geometry must be correct — one substituted or misproportioned asset is a FAIL; note but do not fix out-of-scope mismatches.

## Risks / owner needs
Requires Figma MCP access to the file. Asset downloads and component reuse reduce drift but the skill cannot guarantee pixel parity — visual verification against the screenshot is the gate.

## Category and tags
Category: design. Tags: figma, design-to-code, mcp, implementation, assets, code-connect.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
