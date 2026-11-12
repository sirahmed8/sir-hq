# gslides

- Tool: `gemini-plugin` (plugin: `gslides`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\gslides\skills\gslides\SKILL.md`
- SKILL.md size: 29611 chars

## What it does

Read, create, and edit Google Slides presentations. Use when creating presentations, when the user shares a slides.google.com URL, asks to summarize or extract content from a deck, wants slides drafted or updated, or wants a presentation exported. Don't use for Google Docs, Sheets, or Drive file management.

## When to use (from skill text)

- `add-text`                    | `element`, `textbox`, `text`                                                                                                                                                                                             | Insert text into element. Use this to safely inse

## Structure (headings inside SKILL.md)

- Google Slides
- Setup
- Windows (PowerShell)
- Authentication
- Usage
- Recipes
- Commands
- Tips
- Placeholder IDs (Single-Batch Workflows)
- Batch `--json` Response
- Card Design Tips (from Testing)
- Batch Operations Reference
- Key Features
- Slide Creation Recipe
- Complete Batch JSON Example
- Global Flags
- Generating UI Links for Humans
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   A 403 that names a missing permission or scope is not a sign-in problem.
- -   **Never delete a slide the user did not ask you to delete.** A removed slide

## Key rules (verbatim lines from SKILL.md)

1. -   **Never delete a slide the user did not ask you to delete.** A removed slide
2. -   **CRITICAL:** Never attempt to scrape Google Slides URLs (e.g.,

## Files inside the skill

- `references/styling.md` — "GSlides Styling Reference"
- `scripts/gslides`
- `scripts/gslides.cmd`
