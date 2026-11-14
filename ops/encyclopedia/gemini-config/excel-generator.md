# excel-generator

## Summary
A Python/openpyxl playbook for generating executive-grade .xlsx workbooks: navy/slate headers with white bold text, zebra striping, alignment rules per data type, native dynamic formulas (XLOOKUP, SUMIFS, COUNTIFS, AVERAGEIFS) instead of hardcoded values, and accounting-style total rows with thin-top/double-bottom borders. Identical content ships in codex, cursor, kilo, opencode and windsurf copies.

## When to use / when NOT
Use when a task needs a real, styled Excel deliverable (reports, models, trackers) generated programmatically. Do NOT use for reading/analyzing existing spreadsheets (that is data work, not generation), for CSV-only needs, or when the user just wants formulas explained without a file.

## Inputs, outputs, tools
- Inputs: the data model (headers, rows, which columns are text/numbers/dates/status), target filename.
- Outputs: a saved `.xlsx` via `openpyxl` (Workbook/Worksheet, styles, column auto-width).
- Tools: Python 3 with `openpyxl`; no MCP or external service.

## 5 most important rules
1. Never emit raw unstyled grids — every workbook follows corporate executive styling.
2. Header row: `#0F172A`/`#1E293B` fill, white bold 11pt Segoe UI/Calibri/Aptos, height ~28.
3. Zebra striping: odd rows `#F8FAFC`, even white; alignment by type — text left, numbers right, dates/status/IDs center.
4. Always write live formulas (XLOOKUP over VLOOKUP, SUMIFS family for rollups), never precomputed constants.
5. Total rows get bold text, a thin top border and a double bottom accounting line; auto-size columns with `get_column_letter`.

## Risks / owner needs
None beyond a Python env with openpyxl. Number-format strings and fonts are Windows-friendly defaults; verify output opens correctly in Excel before delivery.

## Category and tags
Category: data. Tags: excel, xlsx, openpyxl, python, reporting, automation.

## Revisions
Byte-identical across codex, cursor, kilo, opencode and windsurf (kilo digest states identical to codex). Any copy is equivalent; kilo used as source.
