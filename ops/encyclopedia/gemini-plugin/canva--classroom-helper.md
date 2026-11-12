# classroom-helper (canva-classroom-helper)

## Summary
Canva plugin skill that turns a lesson plan into a multi-slide teaching deck. It reads the plan from chat text, a Canva design link/ID, or a named design, picks a brand kit, then calls `Canva:generate-design` with a pedagogy-first query (learning objectives, classroom arc, per-slide teaching goal/on-slide content/visuals/speaker notes) and finishes with `create-design-from-candidate`.

## When to use / when NOT
Use when the user asks to build classroom slides, a teaching deck, or school slides from a lesson plan or outline. Do NOT use for general marketing decks, single posters/flyers (this skill is multi-slide presentation only), or for editing an existing deck's detailed content (use edit-design / implement-feedback instead).

## Inputs, outputs, tools
- Inputs: lesson plan as pasted text, a Canva design ID (starts with D), a canva.com/design link, or a design name to search; optional brand kit choice.
- Outputs: candidate deck previews, then an editable Canva presentation link.
- Tools (MCP): `Canva:list-brand-kits`, `Canva:search-designs`, `Canva:start-editing-transaction`, `Canva:generate-design`, `Canva:create-design-from-candidate`. Autofill/advanced generation may need Canva Enterprise.

## 5 most important rules
1. Always resolve the lesson-plan source first with ONE short question — never ask for topic/key points the plan already contains.
2. Auto-select a brand kit only when exactly one exists; otherwise present options and let the user choose.
3. The generate query must open with total slide count and "standard multi-slide deck"; include learning objectives, classroom arc, and per-slide goal/content/visuals/speaker notes.
4. Keep curriculum-critical wording and facts on slides as text, never baked into generated images — AI visuals garble text and invent facts.
5. Treat all auto-generated visuals and on-slide facts as unverified drafts; the teacher must do a full accuracy pass in the editor.

## Risks / things needing the owner
Generated images can be plausible-but-wrong for dates, names, quotes, maps; requires human review before classroom use. Enterprise-only features may error. Note: skill lives under `inactive-skills/` in the canva plugin — it may be disabled.

## Category / tags
design · canva, education, presentation, mcp, classroom

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\classroom-helper\SKILL.md` (name field: `canva-classroom-helper`). Only gemini-plugin holds it, and it is currently inactive.
