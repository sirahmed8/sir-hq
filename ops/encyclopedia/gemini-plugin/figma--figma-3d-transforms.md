# figma-3d-transforms

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-3d-transforms\SKILL.md`
- SKILL.md size: 16113 chars

## What it does

Add or edit 3D transforms — depth, perspective, z-axis rotation, tilt, isometric, and parallax looks that flat 2D rotation cannot express. Use whenever a request reaches into the third dimension — "make it 3D", "add depth/perspective", "tilt/rotate it back", "z-plane", "isometric", "flip it like a card", "parallax", "vanishing point", "receding into the distance", "make it pop out".

## When to use (from skill text)

- Use this skill when a request needs the third dimension and plain 2D rotation can't express it: perspective, depth, z-axis tilt, isometric layouts, card flips, parallax stacks, "make it pop out of the screen."
- - Don't grep the plugin API docs for 3D transforms — use this skill; the shapes above are the full surface.

## Structure (headings inside SKILL.md)

- Adding / editing 3D transforms
- Animating 3D transforms
- Runtime
- User-facing language
- The three fields
- transform3d — the per-element pose
- scene3d — the shared 3D space (containers only)
- transformOrigin — the pivot
- Setting perspective
- Filled parent? Isolate the 3D children (do this by default)
- Never put `scene3d` perspective and `transform3d` on the same layer
- Interpreting the ask
- Workflow
- Recipes
- Gotchas
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP resources

## Risks / cautions found in text

- 1. Make any static (non-3D) design changes first; don't create or delete nodes unless the user asked.
- - If `node.transform3d` reads back `undefined`, the 3D transform capability isn't enabled in this environment. Don't silently produce nothing — tell the user 3D transforms aren't available here. `scene3d` exists only on FRAME, COMPONENT, and INSTANCE containers; `null` there means no scene is config

## Key rules (verbatim lines from SKILL.md)

1. - Talk in plain terms: "adding perspective", "tilting it back", "giving the scene depth". Don't name these fields or the plugin API to the user, and don't surface raw error text.
2. - `translateZ` and all three `rotate*` are **required** on write; `backfaceVisible` and `visible` are optional and default to `true`.
3. - **There is no X or Y translation** — `transform3d` only translates along Z. To move a node horizontally or vertically, set the node's own position (`node.x` / `node.y`); don't reach for a transform. So a scene of several children at different X/Y spots is built by positioning each node, then apply
4. - `perspective` and `preserve3d` are both **required** on write; `visible` is optional and defaults to `true`.
5. - Reads return `null` when unconfigured — and an all-default scene reads back as `null`, so don't treat `null` as an error.

## Files inside the skill

- `references/carousels.md` — "Ring / 3D carousel"
- `references/cubes.md` — "Cube recipes"
