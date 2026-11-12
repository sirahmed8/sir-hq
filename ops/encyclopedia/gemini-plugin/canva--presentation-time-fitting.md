# presentation-time-fitting (canva-presentation-time-fitting)

Tools: gemini-plugin (canva plugin, inactive-skills folder). Source: C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\presentation-time-fitting\SKILL.md (94 lines, read in full)

## Summary
Fits an existing Canva presentation to a target speaking duration using presenter notes ONLY: resolve the design, clone it via resize-design (same dimensions, never touch the original), read per-slide text, split total time equally (or weighted on request) at ~150 wpm, generate speaker notes per slide, write them back through the Canva editing transaction, and commit. Visible slide text is read for context but never modified.

## When to use / not use
Use for "make this a 10-minute presentation", "generate speaker notes", "fit my deck to [duration]". Not for editing slide content itself — if the user wants to cut/pad slides, this skill declines and points to Canva editing.

## Inputs, outputs, dependencies
Input: a design link/URL/ID/name plus total speaking duration. Output: a cloned design with per-slide presenter notes and a time-allocation recap. Needs: Canva MCP tools (resolve-shortlink, search-designs, resize-design, get-design-content, get-design-pages, editing transaction trio).

## Key rules
1. Collect design + duration BEFORE any Canva tool call; ask and wait if either is missing.
2. Always clone with resize-design at the same dimensions — the original is never modified.
3. Time split: total ÷ slide count, ~150 wpm word budget per slide; show the user the allocation table; state weighting assumptions.
4. Notes generation happens in-session (no external API); notes stay faithful to visible slide messages — no invented facts; visual-heavy slides get descriptive narration notes.
5. Write ONLY via the notes operation type — never replace_text/find_and_replace; batch operations, commit the transaction.

## Risks / owner items
- Lives in `inactive-skills/` — the plugin considers it disabled; may need reactivation to use.
- `start-editing-transaction` times out on large decks — retry once, open the transaction earlier, and keep a manual paste-notes fallback ready.
- Can't add/remove slides — unrealistic time targets get flagged with suggestions, not silent stretching.

## Category and tags
media, business — canva, presentation, speaker-notes, mcp-plugin, inactive.

## Revision note
Single plugin revision; note the inactive-skills location — status may differ from active skills.
