# generate-editor-search-query

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\generate-editor-search-query\SKILL.md`
- SKILL.md size: 6977 chars

## What it does

Generates Unity Search queries and opens the Search window to find assets or scene objects. Use when the user asks to find, filter, or list assets, GameObjects, components, or references in the Editor, not on disk.

## When to use (from skill text)

- If the user asks for a general explanation, project overview, folder-structure summary, architecture walkthrough, gameplay-system summary, or "how do I" programming answer, do not use this skill unless the prompt explicitly asks for Unity Search, a Search query, or opening the Search window.

## Structure (headings inside SKILL.md)

- Default Behavior
- Scope
- References
- Passing C# to `script eval`
- Query Generation Rules
- Opening Unity Search
- Response Format
- Validation Checklist
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 3. Show the query in the response before or while opening Search.
2. - **Types must be fully qualified.** A bare `SearchService` does not resolve (`CS0246`), and a
3. - For requests that mix Search with repair work, generate and open the query first; do not modify results unless the user explicitly confirms a separate follow-up action.
4. - Do not invent unsupported filters for uncertain requests. If a request cannot be expressed reliably with Unity Search syntax, open the closest safe query and state the limitation.
5. 5. Never claim Search opened if the command failed.

## Files inside the skill

- `references/open-search-window.md` — "Open Unity Search Window"
- `references/query-patterns.md` — "Unity Search Query Patterns"
- `SECURITY.md` — "Security notes: generate-editor-search-query"
