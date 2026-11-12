# gsheets

Source read: `C:\Users\a7med\.codex\skills\gsheets\SKILL.md` (21 KB; codex revision chosen over kilo/opencode/windsurf/cursor which share the set; `scripts/gsheets`, `scripts/gsheets.cmd` Go CLI wrappers present).

## Summary
Full Google Sheets control through a Go CLI split into `readonly` (read, read-all, read-links, info, list, list-sheets, named-ranges, filter-views, revisions, comments, settings, inspect-cell, export csv/xlsx/pdf/ods/tsv/png, export-chart) and `mutate` (write, append, clear, create/delete/copy/rename, sheet CRUD, formatting, merge, sort, freeze, borders, conditional-format, row/col insert/delete, copy-paste, auto/smart/formula fill, find-replace, notes, comments, data-validation, protect, settings, charts, pivots, tables, sharing, import-csv, batch/raw-batch). It covers auth setup, A1-range and sheet-id conventions, markdown-links extraction of hyperlinks and smart chips, formula retrieval, template instantiation, and structured batch JSON (`data` field, unknown fields rejected).

## When to use / when NOT
Use for any read/write/format/manage task on a sheet the user links (`docs.google.com/spreadsheets/d/<ID>`). Do NOT use for Google Docs, Slides, or Drive file management, and never scrape sheet URLs with web tools (auth-gated; use the CLI).

## Inputs, outputs, tools
- Inputs: spreadsheet ID from URL, A1 ranges or `--sheet-id`+row/col coords, TSV/`|`/`\n` write data, CSV files, batch JSON files.
- Outputs: plain reads (`--json` for machine output), exports to files, mutation confirmations.
- Tools: bundled `gsheets` CLI (first run via `scripts/gsheets auth status`, then bare `gsheets`); Google Sheets/Drive API underneath; `gsheets auth login` background OAuth flow.

## 5 most important rules
1. `auth status` is the only login check; never hunt for tokens or run ops before it.
2. `readonly` vs `mutate` namespaces are strict; destructive commands (`delete`, `delete-sheet`, `delete-rows/cols`, `clear`) require explicit user request — `delete` additionally needs `--confirm`.
3. Write the narrowest range possible; rewriting whole sheets destroys formatting, formulas, and validation.
4. Never share broadly or publicly unless the user explicitly instructs.
5. Batch JSON uses `data` (2D array), not `values` — unknown fields are rejected to prevent silent no-op writes; comments added via API show "Original Content Deleted" in the grid UI but live in Comment History.

## Risks / owner notes
Destructive mutations are irreversible (no undo). `share` can expose data — default to not sharing. Auth needs the owner's browser sign-in once.

## Category and tags
Category: automation. Tags: google-sheets, cli, readonly-vs-mutate, batch-ops, export, data-validation.
