# branded-presentation

Tools: claude (canva connector). Source: C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\branded-presentation\SKILL.md (62 lines, read in full)

## Summary
Creates on-brand Canva presentations from an outline or brief. Resolves the content source (text, design ID, link, or named doc), lists brand kits (auto-selects if one), then calls Canva:generate-design with a structured query (brief, narrative arc, slide plan), shows candidates, and finalizes via create-design-from-candidate. Inactive skill — must be enabled before use.

## When to use / not use
Use when the user asks to create a branded presentation, make an on-brand deck, turn an outline into slides, or generate a presentation from a brief. NOT for checking an existing design against brand (use brand-check) or for non-Canva output; autofill requires a Canva Enterprise plan.

## Inputs, outputs, dependencies
Input: outline/brief text, or a Canva design ID/link/name as content source. Output: an editable Canva presentation design (link to new design). Needs: Canva connector, brand kit (list-brand-kits), generate-design, create-design-from-candidate; Enterprise plan for autofill.

## Key rules
1. Resolve content source correctly: raw design ID → start-editing-transaction directly (never search-designs); link → extract ID; name → search-designs first.
2. If one brand kit exists, use it automatically; if multiple, ask the user to select before generating.
3. Query must follow the format: Presentation Brief (title, topic, key messages, style), Narrative Arc paragraph, Slide Plan (title, goal, 3-6 bullets, visuals, speaker notes).
4. Expand sparse outlines into a complete slide plan with reasonable content; extract key points from narrative briefs.
5. Use clear, action-oriented slide titles; confirm candidate choice before creating the final design.

## Risks / owner items
- Skill is inactive — must be enabled in the plugin before invocation.
- Autofill requires Canva Enterprise plan; flag to user if unavailable.
- Multiple brand kits require user selection; do not guess.

## Category and tags
canva, presentation, content — canva, brand-kit, slides, deck-generation.

## Revision note
Single skill file, 62 lines, no references. Inactive status noted; enable before use.