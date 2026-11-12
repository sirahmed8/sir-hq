# a11y-debugging

- Tool: `gemini-plugin` (plugin: `chrome-devtools-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\chrome-devtools-plugin\skills\a11y-debugging\SKILL.md`
- SKILL.md size: 5810 chars

## What it does

Uses Chrome DevTools MCP for accessibility.

## Structure (headings inside SKILL.md)

- Core Concepts
- Workflow Patterns
- 1. Automated Audit (Lighthouse)
- 2. Browser Issues & Audits
- 3. Semantics & Structure
- 4. Labels, Forms & Text Alternatives
- 5. Focus & Keyboard Navigation
- 6. Tap Targets and Visuals
- 7. Color Contrast
- 8. Global Page Checks
- Troubleshooting
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Parsing**: Do not read the entire file line-by-line. Use a CLI tool like `jq` or a Node.js one-liner to filter for failures:
2. 3.  **Check Heading Levels**: Ensure heading levels (`h1`, `h2`, `h3`, etc.) are logical and do not skip levels. The snapshot will include heading roles.
3. 4.  If a modal opens, focus must move into the modal and "trap" within it until closed.

## Files inside the skill

- `references/a11y-snippets.md` — "Accessibility Debugging Snippets"
