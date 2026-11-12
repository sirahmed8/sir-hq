# generate-deck (canva-branded-presentation)

## Summary
Canva plugin skill (lives under `inactive-skills/` in the canva plugin) for generating branded marketing/sales presentation decks via the Canva app's `generate-design` tool with `design_type: "presentation"`. Core rule: call `generate-design` DIRECTLY — never route through `prepare-design-generation`/`_prepare_design_generation` or outline-review helpers; if direct generation can't proceed without a prepare step, STOP and tell the user. Deck-focused doctrine: audience/objective inferred from brief (8-12 slides default), persuasive commercial narrative arcs (problem→insight→solution→value→proof→next step), scannable slide titles over vague labels, per-slide visual direction. Brand kits are mandatory ceremony: always call `list_brand_kits`, present options, and REQUIRE the user to choose — never auto-select even if one kit exists; pass selection as `brand_kit_id`. Template tools are explicitly out of scope (search-brand-templates, autofill-design, create-design-from-brand-template). After generation, present candidates and use create-from-candidate to return the editable design link.

## When to use / when NOT
Use for NEW Canva AI presentation drafts (sales/marketing/pitch decks). NOT for docs/reports/proposals/posters (other design types), NOT for editing existing designs, translating, resizing, brand-checking, or template-based generation — those route to different Canva skills/workflows.

## Inputs, outputs, tools
- Inputs: user brief/outline/notes; inferred audience, length, tone, objective.
- Outputs: presentation candidates → user picks → editable Canva design link.
- Tools: Canva app `generate-design` (`design_type:"presentation"`), `list_brand_kits`, create-from-candidate flow; references in SKILL body only (no scripts dir).

## 5 most important rules
1. Direct `generate-design` only — never prepare-design-generation or outline helpers; stop and report if blocked rather than calling prepare tools.
2. ALWAYS list brand kits and make the USER choose before generation — no auto-select, even with a single obvious kit; missing `brandkit:read` scope → tell user to reconnect the Canva app.
3. Generation prompt must be a deck brief: title, audience, objective, slide count, narrative arc, brand/product/positioning, pain points, proof, slide-by-slide outline with visual direction per slide, CTA.
4. Commercial narrative over informational outline — buyers/prospects framing, concise messaging, specific benefits and proof points.
5. If no brand kits exist, say so and ask whether to continue kit-less; if user opts out, stay brand-aware from supplied materials without inventing brand rules.

## Risks / owner needs
Requires the Canva app connected with proper OAuth scopes; brand kit choice is a user decision the skill refuses to automate. Note: skill sits in `inactive-skills/` — it may not be loaded by default in the current plugin revision.

## Category and tags
Category: business. Tags: canva, presentations, decks, branding, marketing, slides, ai-generation.

## Revisions
Single gemini-plugin canva copy (inactive-skills path); no competing revisions.
