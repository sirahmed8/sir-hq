# bulk-create

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\skills\bulk-create\SKILL.md`
- SKILL.md size: 5277 chars

## What it does

Bulk-create Canva designs from tabular data using a brand template with autofill fields, producing one design per row. Use when users say "bulk create designs from this CSV", "generate one design per row", "create a design for each product", "batch generate from a template", or "autofill a template from a spreadsheet". Accepts any tabular data source — uploaded files, pasted tables, JSON, or URLs.

## Structure (headings inside SKILL.md)

- Canva Bulk Design Creation
- Workflow
- Step 1: Get the Data
- Step 2: Select the Brand Template
- Step 3: Inspect the Template Schema
- Step 4: Map CSV Columns to Template Fields
- Step 5: Bulk Create — One Design per Row
- Step 6: Report Results
- Notes
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Image fields require a Canva asset ID — see **Image Field Handling** below
2. - Chart fields require structured data — treat as advanced and ask the user for clarification
3. - Autofill requires a Canva Enterprise plan.
4. - For large CSVs (50+ rows), warn the user upfront that this will make N API calls and may take a while. Offer to do a test run on the first 3 rows before proceeding with the full batch.
5. - If some rows fail, continue with the rest — don't abort the whole batch.

## Files inside the skill

- (SKILL.md only)
