# figma-use-slides

## Summary
Slides-specific addendum to figma-use for driving Figma Slides decks (`figma.com/slides/...`) through the `use_figma` plugin API. Covers the deck-building workflow (design thinking → slide plan → batched builds of 3-5 slides), the slide grid model (SLIDE_GRID/SLIDE_ROW/SLIDE nodes), sections, speaker notes, and six reference docs. Includes a hard choice rule: use `use_figma` for everything except quick template decks where `generate_deck` suffices — and never both for one deck.

## When to use / when NOT
Use for ANY Slides task: new decks, edits, restyles, speaker notes, brand-matched designs. Always pass `skillNames` including `figma-use-slides` (`resource:`-prefixed when MCP-loaded). `generate_deck` is the only alternative — single-call curated templates, no custom design/brand matching/iteration; pick ONE approach per deck, never mix.

## Inputs, outputs, tools
- Inputs: brief or reference file (Slides or Design), existing deck to edit, brand guidelines.
- Outputs: slides with content, speaker notes, named sections; validated via read-only scripts + screenshots.
- Tools: `use_figma` (with figma-use), `create_new_file`, `get_screenshot`/`node.screenshot()`, `figma.getSlideGrid()`, `slide.speakerNotes`, `slideThemeId`; NO `get_metadata` (Design-only), NO `figma.createPage()` (throws on Slides).

## 5 most important rules
1. Position AFTER appendChild, at every nesting level — new nodes auto-parent at (240,240) slide-grid padding, so setting x/y first lands them at intended−240 (intermittent bug); fix order, never compensate by adding 240.
2. SLIDE_GRID/SLIDE_ROW are opaque (no fills/effects/layout props; only SLIDE extends BaseFrameMixin) — but SLIDE_ROW.name IS settable for section names; `getSlideGrid()` returns plain arrays, not row nodes, so rename via tree traversal.
3. Never delete existing slides to "improve" a deck — edit in place; only rebuild on explicit "start over". New files get a default light theme you must overwrite, not follow.
4. Deck workflow for 5+ slides: Phase 1 = full slide-by-slide spatial plan + shared constants (palette roles, fonts, signature motif) + layout-variety check + reusable code preamble; Phase 2 = batches of 3-5 slides per call, deterministic batch validation (~3s overlap/clipping/bounds check), screenshots only at checkpoints.
5. Design thinking scales: content edits skip it; structural additions inherit the deck's existing design language; new decks get full treatment (brief → design language → position → signature). Speaker notes only when asked or presenter-ready decks — bullets that complement slides, never scripts or slide-repeats.

## Risks / owner needs
Requires Figma MCP + Slides file access; new decks consume plan file slots. The appendChild/x-y ordering bug is the classic failure — follow the helper pattern in slide-gotchas.md.

## Category and tags
Category: design. Tags: figma, slides, presentations, mcp, speaker-notes, deck-building.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
