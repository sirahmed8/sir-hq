# gsheets

- Tool: `gemini-plugin` (plugin: `gsheets`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\gsheets\skills\gsheets\SKILL.md`
- SKILL.md size: 19451 chars

## What it does

Read, write, format, and manage Google Sheets. Use when the user shares a sheets.google.com or docs.google.com/spreadsheets URL, asks to read or summarize spreadsheet data, wants cells written, formatted, sorted, merged, or validated, wants rows/columns inserted or deleted, wants charts, pivot tables, or tables added, wants CSV imported, or wants a spreadsheet created, copied, shared, or exported. Don't use for Google Docs, Slides, or Drive file management.

## Structure (headings inside SKILL.md)

- Google Sheets
- Setup
- Windows (PowerShell)
- Authentication
- Usage
- Recipes
- Commands
- Tips
- Global Flags
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   A 403 that names a missing permission or scope is not a sign-in problem.
- -   **Never run a destructive command the user did not ask for.** Deleting a

## Key rules (verbatim lines from SKILL.md)

1. -   **Never run a destructive command the user did not ask for.** Deleting a
2. -   **CRITICAL:** Never attempt to scrape Google Sheets URLs (e.g.,
3. -   Avoid spaces in sheet names when used in range notation; if unavoidable,
4. -   `batch` requires `data` (not `values`) for `write`/`append` ops; unknown

## Files inside the skill

- `scripts/gsheets`
- `scripts/gsheets.cmd`
