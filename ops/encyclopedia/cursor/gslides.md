# gslides

Source read: `C:\Users\a7med\.codex\skills\gslides\SKILL.md` (29 KB; codex revision; `scripts/gslides`, `scripts/gslides.cmd` present). Tail covered the 27-op batch reference.

## Summary
Google Slides control through a Go CLI: `readonly` (read/read-all as text or `--json` presentation AST, info, list-slides, list-elements, get-page, get/set notes, extract-images, export pdf/pptx, export-thumbnail) and `mutate` (create, copy, add/duplicate/delete/reorder slides, textboxes, text, images by URL or file, tables + cells, shapes, backgrounds, notes, element move/resize/style, share, batch). The batch mode supports 27 ops in one JSON file with placeholder IDs (`"id":"SLIDE_1"`) resolved at runtime, `resolved_ids` returned for follow-ups, deferred `set-notes` on new slides, and design tips (header+body card combos, accent dividers, stat call-outs). Auth mirrors gsheets/gmail (`auth status`, background `auth login`).

## When to use / when NOT
Use for creating, reading, editing, styling, or exporting decks from a `slides.google.com/d/<ID>` link. Do NOT use for Docs/Sheets/Drive management; never scrape slide URLs with web tools.

## Inputs, outputs, tools
- Inputs: presentation ID, slide object IDs (0-based index for listing, object ID for export-thumbnail), batch JSON ops, image URLs/files.
- Outputs: text/AST reads, PNG thumbnails, PDF/PPTX exports, `resolved_ids` maps.
- Tools: bundled `gslides` CLI over the Slides API; OAuth via `gslides auth login`.

## 5 most important rules
1. `auth status` first; bare `gslides` afterwards; user cannot run CLI commands themselves.
2. Never delete a slide/element the user did not ask for — speaker notes and layout die with it.
3. Edit only the elements requested; rebuilding a slide loses theme, placeholders, and notes.
4. `reorder-slide --position` is evaluated BEFORE removal: moving later needs `target+1`, earlier needs `target`.
5. Use `export-thumbnail` to visually verify layout before sharing; new decks ship a default title slide — delete placeholder elements `i0`/`i1` in batch JSON to start blank; prefer `add-text` over `update-text` on empty placeholders.

## Risks / owner notes
Destructive deletes are permanent. `share` defaults must stay narrow. Custom layout IDs are deck-specific (discover via `readonly info --json`).

## Category and tags
Category: automation. Tags: google-slides, cli, presentations, batch-ops, oauth, design-tips.
