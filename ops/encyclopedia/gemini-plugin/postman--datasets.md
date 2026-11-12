# datasets

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\datasets\SKILL.md`
- SKILL.md size: 5975 chars

## What it does

Use when creating or repairing dataset manifests, or when a collection needs queried or joined test inputs, a reusable named view, spreadsheet worksheet data, live database rows, or script access through pm.datasets(). Chooses between a simple iteration file and a dataset while preserving query semantics, portability, and credential boundaries. Use for requests such as "run this collection over database rows".

## Structure (headings inside SKILL.md)

- Datasets
- Choose the data and execution path
- Build a portable, queryable artifact
- Interpret failures and results
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. Choose credentials before choosing a database connector. JDBC variables

## Key rules (verbatim lines from SKILL.md)

1. 3. Choose credentials before choosing a database connector. JDBC variables

## Files inside the skill

- `reference/schema.md` — "Dataset YAML"
- `reference/spreadsheets.md` — "Spreadsheet sources"
