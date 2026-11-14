# figma-use

## Summary
The foundational skill for executing arbitrary JavaScript against Figma files through the `use_figma` MCP tool (Plugin API). It defines the operating contract — return-based output, no console.log, sequential mutations, page-context resets, font-loading recipe, sizing-mode enums, color ranges — plus efficient APIs (`node.query` CSS-like selectors, `node.set` batching, `createAutoLayout`, `placeholder` shimmer, inline `node.screenshot`), the incremental build workflow, error recovery, and a 12-reference-doc library covering patterns, variables, components, styles and the full Plugin API typings.

## When to use / when NOT
Load before ANY `use_figma` call; every domain addendum (figma-use-figjam, -slides, -motion) and builder skill (generate-design, generate-library, swiftui, spec) depends on it. For visible design changes it MANDATES also loading figma-generate-design; for reusable library assets, figma-generate-library. Read-only calls need neither. Works in design/FigJam/Slides editor modes with different node-type availability (editor type is readable from the URL).

## Inputs, outputs, tools
- Inputs: fileKey (+ optional sessionId from `create_session`), JavaScript plugin-API script.
- Outputs: ONLY the `return` value (JSON-serialized); console.log is invisible; errors auto-captured; MUST return all created/mutated node IDs.
- Tools: `use_figma`, `get_screenshot`, `get_metadata` (Design only), `node.screenshot()`, `node.query`, `node.set`, `figma.createAutoLayout`, `figma.loadFontAsync`, `figma.listAvailableFontsAsync`; 12 reference docs incl. plugin-api-standalone.d.ts (grep, don't bulk-load).

## 5 most important rules
1. Output contract: plain JS with top-level await + `return`; never wrap in IIFE, never call closePlugin/notify; await EVERY promise; pass IDs across calls as string literals (no state persists).
2. Page discipline: context resets to first page every call; `await figma.setCurrentPageAsync(page)` at most ONCE per call — fan multi-page work into N parallel use_figma calls in ONE message; never loop pages inside a script.
3. Text recipe is canonical and universal: load font (node's CURRENT fonts via getStyledTextSegments for edits, verified style strings via listAvailableFontsAsync — never guess "SemiBold" vs "Semi Bold") → await → mutate → return IDs; covers characters, appendChild, setBoundVariable, etc.
4. Layout/sizing enums: `layoutSizing*` (child) = FIXED/HUG/FILL vs `*AxisSizingMode` (frame) = FIXED/AUTO — never cross; append to auto-layout parent BEFORE setting HUG/FILL; resize() before sizing modes; related children belong in createAutoLayout; top-level nodes placed away from (0,0); colors 0–1 with paint color {r,g,b} only.
5. Evidence-driven batching: size calls for safe retry, not validation cadence — return IDs+counts+bounds as structural evidence; one composition screenshot after building, one post-fix shot max; obey `safeToRetryWithoutCanvasRead` on errors; discover file conventions (names, variables, components) before creating anything.

## Risks / owner needs
Mutates live Figma files — wrong scripts create real damage; cleanup must target ledger IDs, never name-prefix guesses. Requires authenticated Figma MCP. Design-mode node set differs from FigJam/Slides (see per-mode skill).

## Category and tags
Category: design. Tags: figma, plugin-api, mcp, automation, design-automation, core-skill.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
