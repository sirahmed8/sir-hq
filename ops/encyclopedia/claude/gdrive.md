# gdrive

- Tool: `claude`
- Category: data
- Source: `C:\Users\a7med\.claude\skills\gdrive\SKILL.md`
- SKILL.md size: 12761 chars

## What it does

Browse, search, and manage Google Drive files and folders. Use when the user shares a drive.google.com URL, asks what is in a folder, wants a file found, downloaded, uploaded, updated in place, moved, copied, or renamed, wants a Google file exported to PDF, Markdown, or CSV, wants comments read or added, wants sharing and permissions checked or changed, or wants Drive activity watched. Don't use for editing the contents of a Doc, Sheet, or Slides deck.

## Structure (headings inside SKILL.md)

- Google Drive
- Setup and Authentication
- Windows (PowerShell)
- Usage
- Recipes
- Commands
- Tips
- Global Flags
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   `mutate` uploads, edits, creates, deletes, and changes permissions.

## Key rules (verbatim lines from SKILL.md)

1. -   **Reach for `readonly` first, and never run a `mutate` command the user did
2. -   **Check where a file is going before you move it.** Moving a file out of a
3. -   Always pass `--mime_type` when watching one kind of document, so discovery

## Files inside the skill

- `scripts/gdrive`
- `scripts/gdrive.cmd`
