# figma-generate-design

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-generate-design\SKILL.md`
- SKILL.md size: 38721 chars

## What it does

Translate application pages.

## When to use (from skill text)

- Use this skill to create or update **screens, views, and multi-section UI containers** in Figma by **reusing the published design system** — components, variables, and styles — rather than drawing primitives with hardcoded values. This includes full pages, modals, dialogs, drawers, sidebars, panels,
- - Use this skill when the deliverable is a **composed Figma view** (new or updated) — including a form, dashboard, list, table, card, header, panel, dialog, message preview, or other multi-section container — built from design system component instances. This applies even when the user calls the com
- Because this skill works in retry-safe construction phases, errors are naturally scoped to the current phase. Content from previous successful calls remains intact.

## Structure (headings inside SKILL.md)

- Build / Update Screens and Views from Design System
- HTML-to-Figma Exceptions
- Skill Boundaries
- Prerequisites
- Parallel Workflow with generate_figma_design (Web Apps Only)
- Required Workflow
- Step 1: Understand the Deliverable
- Step 2: Collect Component Keys, Variables, and Styles
- Step 3: Create the Wrapper Frame
- Step 4: Customize Covered Sections and Build Missing Sections
- Step 5: Validate the Full View and Transfer Images
- Step 6: Updating an Existing View
- Reference Docs
- Error Recovery
- Best Practices
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP resource, MCP server, MCP tool

## Risks / cautions found in text

- - If the primary deliverable is a **reusable library primitive or foundation** intended for variants, tokens, or publication, use [figma-generate-library](../figma-generate-library/SKILL.md) with [figma-use](../figma-use/SKILL.md) instead.
- 3. **Once confirmed looking good:** Delete the `generate_figma_design` output — it was only used as a visual reference.
- 4. **Identify the product's font family from the source. Do not default to Inter.** Find *which* typeface the product uses before writing any script. See [references/discover-product-font.md](references/discover-product-font.md) for where to look (CSS variables, component files) and how to resolve m
- 5. **Check whether the view contains any images** (e.g., `<img>`, `<Image>`, background images, product photos, avatars, icons loaded from URLs). If it does and this is a web app, you **must** run the parallel `generate_figma_design` capture workflow — start it immediately alongside Step 2 so the ca

## Key rules (verbatim lines from SKILL.md)

1. - Figma MCP server must be connected
2. - The target Figma file must have a published design system with components (or access to a team library)
3. - User must provide a target Figma file (URL or `fileKey`). If they don't have one yet, invoke `/figma-create-new-file` (or call `create_new_file`) first and reuse the returned file_key. Both `use_figma` and `generate_figma_design` require an existing `fileKey`.
4. - Run `generate_figma_design` against the **same `fileKey`** to capture a pixel-perfect screenshot of the running web app into that file. `generate_figma_design` always requires `fileKey` — if the user does not yet have a Figma file, first invoke `/figma-create-new-file` (or call the `create_new_fil
5. 3. **Once confirmed looking good:** Delete the `generate_figma_design` output — it was only used as a visual reference.

## Files inside the skill

- `references/componentization.md` — "Componentize repeated and reusable elements"
- `references/discover-product-font.md` — "Discover and verify the product font"
