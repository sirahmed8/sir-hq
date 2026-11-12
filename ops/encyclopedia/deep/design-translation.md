# design-translation (canva-translate-design)

## Summary
Canva plugin skill that translates all text in a design into another language as a NEW copy: resolve the design (direct ID — never search by ID — URL parse, or search-designs by name), duplicate via `Canva:resize-design` (same dims, original untouched), open `start-editing-transaction`, translate each text element preserving formatting/proper nouns, batch all `replace_text` ops in one `perform-editing-operations`, update the title, show preview, get explicit approval, then `commit-editing-transaction`.

## When to use / when NOT
Use for "translate my design to X" / localization requests. Do NOT modify the original — always work on a copy. Not for redesigning layouts or non-Canva files.

## Inputs, outputs, tools
- Inputs: design ID/URL/name + target language.
- Outputs: a translated copy design + link.
- Tools (MCP): Canva:search-designs, resize-design, start-editing-transaction, perform-editing-operations, commit-editing-transaction.

## 5 most important rules
1. Never modify the original — always duplicate first via resize-design.
2. Design IDs go straight through; search-designs is for titles only.
3. Batch ALL text replacements into a single perform-editing-operations call.
4. Preserve line breaks/emphasis; keep brand names/proper nouns/technical terms.
5. Explicit user approval before commit; warn that longer translations may break layout.

## Risks / things needing the owner
Machine translation quality needs human review; layout overflow is likely with longer target languages. Skill sits under canva `inactive-skills/` — may be disabled.

## Category / tags
design · canva, translation, localization, mcp

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\canva\inactive-skills\design-translation\SKILL.md`. Only gemini-plugin holds it, currently inactive.
