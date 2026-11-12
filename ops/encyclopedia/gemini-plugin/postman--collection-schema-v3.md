# collection-schema-v3

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\collection-schema-v3\SKILL.md`
- SKILL.md size: 3676 chars

## What it does

Use when writing or debugging local Postman v3 collection, environment or globals files, including collection lint failures. Preserves the per-entity files, inherited context, and schema shapes that make API changes reusable and reviewable in Git. Use for requests such as "fix this request YAML".

## Structure (headings inside SKILL.md)

- Collection Schema (v3, Git-Native)
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1. Edit the entity that owns the change. Top-level directories under
2. 2. Preserve inherited auth, variables, and scripts when changing a request.
3. 3. Consult the reference section for the entity being changed:

## Files inside the skill

- `reference/environment.md` — "Environment Schema (v3)"
- `reference/globals.md` — "Globals"
- `reference/http.md` — "HTTP collection files"
- `reference/other_protocols.md` — "Other protocol schemas"
