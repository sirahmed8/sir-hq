# figma-generate-design

## Summary
The heavyweight "build a screen in Figma from the design system" skill: translate an app page/view/modal/sidebar into a Figma composition by REUSING the published design system (component instances, bound variables, text/effect styles) instead of drawing hardcoded primitives. Six steps: understand the deliverable (identify product font first), discover components/variables/styles (Code Connect first, then library search, then existing-screen inventory), create a wrapper frame, build sections inside it with instances + token bindings, validate with read-back evidence plus ONE composition screenshot, and handle image transfer from a parallel `generate_figma_design` capture.

## When to use / when NOT
Use for composed multi-section views (pages, modals, drawers, panels, dashboards, forms) destined for a Figma file that has (or can get) a published design system. NOT for reusable library primitives/tokens (use figma-generate-library) or Code Connect mapping files (use figma-code-connect). For raw/static HTML input or brand-new design-from-prompt with no rendered UI, `html_to_figma` is the exception path. For web apps with content images, the parallel `generate_figma_design` capture is MANDATORY.

## Inputs, outputs, tools
- Inputs: target fileKey (create via figma-create-new-file if needed), source code or description of the screen, product font identified from source.
- Outputs: wrapper frame with component instances bound to variables/styles; componentized repeated elements; validated screenshot.
- Tools: `use_figma` (mandatory companion skill figma-use), `create_session`, `get_libraries`, `search_design_system` (component/variable/style entities), `importComponentSetByKeyAsync`, `importVariableByKeyAsync`, `importStyleByKeyAsync`, `setBoundVariable`/`setBoundVariableForPaint`, `setProperties`, `figma.createNodeFromSvg`, `generate_figma_design` (parallel capture), `generate_image`/`upload_assets` for placeholders; refs: componentization.md, discover-product-font.md, plus figma-use reference docs.

## 5 most important rules
1. HARD GATE: output must be editable text/components/icons/hierarchy — a screenshot or flattened UI raster anywhere in the deliverable (even as wrapper fill) is a failure; remove and rebuild semantically.
2. Discovery order is fixed: Code Connect files (`*.figma.ts(x)`, `@FigmaConnect`, `FigmaConnect`) first → `get_libraries` scope → whole-view + existing-screen inventory → targeted gap searches only; one intent per query, never OR-packed strings; `getLocalVariableCollectionsAsync` sees only local vars — library variables need `search_design_system` with `entity:"variable"`.
3. Never hardcode hex colors/pixel spacing when tokens exist — bind variables for fills/strokes/padding/radii, apply text/effect styles by id; always search before building.
4. Build inside a pre-created wrapper frame (never reparent later — appendChild across calls silently orphans); batch independent imports in Promise.all; return node IDs + counts as structural evidence; componentize repeated elements on the first pass.
5. Validation: read back descendant/type/image-fill inventory, take ONE full-view screenshot, fix targeted defects, take ONE post-fix shot; explicitly assert the font family (Inter-by-default is a silent failure); icons come from codebase SVG via `createNodeFromSvg` with viewBox+width/height (never rebuilt from rotated primitives, never currentColor left black).

## Risks / owner needs
Requires Figma MCP + a file with/for a published design system; Org features may gate libraries. `generate_figma_design`/`generate_image` consume Figma AI credits (must inform user). Long multi-phase scripts risk partial state — phases are designed retry-safe but page-context boundaries still split work.

## Category and tags
Category: design. Tags: figma, design-system, screen-build, mcp, components, variables, tokens.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
