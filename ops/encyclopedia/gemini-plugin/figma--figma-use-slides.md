# figma-use-slides

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-use-slides\SKILL.md`
- SKILL.md size: 21982 chars

## What it does

Use Figma's use_figma MCP tool in the Slides.

## When to use (from skill text)

- **`use_figma` + this skill (default):** Handles any Slides task — new decks, edits to existing decks, brand-matched designs, reference-file styling, iterative refinement, speaker notes, and full creative control over layout, color, and typography. Use this for most requests.
- How closely to follow the reference depends on what the user asked for. "Make it look like this" means replicate the design language with new content. "Use this for inspiration" means echo the character but make it your own. "Here's our brand deck" means extract the brand system and apply it consist
- When building a new deck of 5 or more slides, use this two-phase workflow. It replaces the general incremental workflow from [figma-use](../figma-use/SKILL.md) Section 6 for deck-building specifically — the principles still apply, but the cadence changes.

## Structure (headings inside SKILL.md)

- use_figma — Figma Plugin API Skill for Slides
- Choosing How to Build a Slides Deck
- When to use which
- Pick one and commit
- Critical Rules (Slides-specific)
- Design Thinking
- New deck design process
- Reading a reference file
- Deck-Building Workflow
- Phase 1 — Design & Plan
- Phase 2 — Build
- Sections
- When asked to organize a deck
- Naming + scoping
- Renaming a section
- Speaker Notes
- When to write speaker notes
- What good speaker notes look like
- What to avoid in speaker notes
- Formatting
- Inspecting Slides Files
- Quick inspection scripts
- Reference Docs
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool, MCP as, MCP resource

## Risks / cautions found in text

- 1. **Newly created Slides files have a default light theme.** When a Slides file is created via `create_new_file`, a default light theme is automatically initialized. This theme is structural scaffolding — you should overwrite the theme's color variables and text styles with your own design directio
- 6. **Never delete existing slides to rebuild them.** When asked to improve, redesign, or restyle a deck, modify the existing slides in place. Only delete slides when the user explicitly asks to "start over" or "redo from scratch."
- 1. **Read the brief.** What is the deck communicating, and to whom? An investor pitch, a team retrospective, a product launch, and a technical deep-dive all demand different visual treatments. The design should be inseparable from the content.
- - **3–5 slides per `use_figma` call.** Structurally similar slides (e.g. a series of product feature slides) can go in the same batch. Each slide is an isolated subtree — cross-slide dependencies don't exist, so large batches are safe.

## Key rules (verbatim lines from SKILL.md)

1. 1. **Newly created Slides files have a default light theme.** When a Slides file is created via `create_new_file`, a default light theme is automatically initialized. This theme is structural scaffolding — you should overwrite the theme's color variables and text styles with your own design directio
2. 3. **SLIDE_GRID and SLIDE_ROW are opaque nodes** — do not access `.fills`, `.effects`, or layout properties on them. Only `SLIDE` nodes (type `'SLIDE'`) extend `BaseFrameMixin`. **Exception:** `SLIDE_ROW.name` IS settable — that's how plugins rename slide sections (e.g. `slideRow.name = "Intro"`). S
3. 6. **Never delete existing slides to rebuild them.** When asked to improve, redesign, or restyle a deck, modify the existing slides in place. Only delete slides when the user explicitly asks to "start over" or "redo from scratch."
4. 3. **Layout variety check.** Read through the slide plans in sequence. If the layout descriptions feel repetitive — "two-column, two-column, grid, two-column" — rearrange before building. This is the cheapest moment to diversify. See [slide-design.md](references/slide-design.md) for anti-patterns.
5. 4. **Code preamble.** Write out the reusable preamble you'll paste at the top of every build script: a `const C = { ... }` color palette object, a `Promise.all([...])` font-loading block, and the `addFrame`/`addText`/`addRect` helpers from [slide-gotchas.md](references/slide-gotchas.md#position-afte

## Files inside the skill

- `references/slide-content.md` — "Slide Content"
- `references/slide-design.md` — "Slide Design Principles"
- `references/slide-gotchas.md` — "Slide Gotchas & Common Mistakes"
- `references/slide-grid.md` — "Slide Grid"
- `references/slide-lifecycle.md` — "Slide Lifecycle"
- `references/slide-properties.md` — "Slide-Specific Properties"
