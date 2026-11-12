# gdocs

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\gdocs\SKILL.md`
- SKILL.md size: 41620 chars

## What it does

Read, create, edit, and manage Google Docs. Use when the user shares a docs.google.com URL, asks to summarize or extract content from a doc, wants a doc drafted, edited, formatted, or commented on, wants tables, images, or smart chips inserted, wants markdown imported or synchronized with a doc, or wants a doc exported. Requires a known document ID — to find documents, use the gdrive skill from the Google Drive plugin; if it isn't installed, ask the user for the doc link. Don't use for Google Sheets, Slides, or Drive file management.

## Structure (headings inside SKILL.md)

- Google Docs
- Setup and Authentication
- Windows (PowerShell)
- Interactive Entity and Metadata Retention
- Content Standards
- Inspecting Documents Accurately
- Recipes
- Efficiency: Automatic Batching
- Output:
- Batched 3 table cell operations in 1 API call.
- Replaced 5 occurrences of "old text".
- Batched 2 replace operations in 1 API call.
- Commands
- Choosing the Right JSON Dump Command
- Working with Tabs
- Preserving Metadata (Comments, Anchors, and Suggestions)
- Updating Existing Documents
- Generating UI Links for Humans
- Supported Formatting
- Tips
- Document-Wide Styling (Named Styles)
- Images in Google Docs
- Reading and Downloading Images
- Inserting and Replacing Images
- Image Storage Lifecycle
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **PNG export of pageless docs**: pageless docs still produce multiple pages

## Key rules (verbatim lines from SKILL.md)

1. -   `--quote` must be an **exact substring of a single line**, free of markdown
2. -   **Safe exporting (avoiding workspace clutter)**: always specify the target
3. 3.  Google Docs hosts its own internal copy of the image. You do not need to

## Files inside the skill

- `references/batch_operations.md` — "Batch Operations"
- `references/commands.md` — "Full List of Commands"
- `references/diagrams.md` — "Diagrams in Google Docs"
- `references/markdown_sync.md` — "Markdown and Google Docs Synchronization"
- `references/metadata_retention.md` — "Metadata & Interactive Entity Retention in Google Docs"
- `references/recipes.md` — "gdocs Recipes"
- `references/styling.md` — "GDocs Styling Reference"
- `references/tabs.md` — "Working with Tabs in Google Docs"
- `references/updating.md` — "Updating Existing Google Docs"
- `scripts/gdocs`
- `scripts/gdocs.cmd`
