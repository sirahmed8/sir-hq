# gdrive

- Tool: `gemini-plugin` (plugin: `gdrive`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\gdrive\skills\gdrive\SKILL.md`
- SKILL.md size: 12120 chars

## What it does

Browse, search, upload, download, and manage.

## Structure (headings inside SKILL.md)

- Google Drive
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
- -   `mutate` uploads, edits, creates, deletes, and changes permissions.

## Key rules (verbatim lines from SKILL.md)

1. -   **Reach for `readonly` first, and never run a `mutate` command the user did
2. -   **Check where a file is going before you move it.** Moving a file out of a
3. -   Always pass `--mime_type` when watching one kind of document, so discovery

## Files inside the skill

- `scripts/gdrive`
- `scripts/gdrive.cmd`
