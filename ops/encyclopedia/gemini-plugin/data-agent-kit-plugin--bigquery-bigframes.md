# bigquery-bigframes

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\bigquery-bigframes\SKILL.md`
- SKILL.md size: 3233 chars

## What it does

Generates Python code using BigQuery DataFrames (BigFrames). Use by default for any Python data task involving BigQuery, including data processing, analysis, and machine learning. Don't use for SQL-first workflows or the google-cloud-bigquery client library — use bigquery-basics.

## Structure (headings inside SKILL.md)

- BigFrames (BigQuery DataFrame) basics
- Generic Coding Guidelines
- Model Development

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. *   **Avoid `.to_pandas()`**: You MUST NOT use `.to_pandas()` to download the
2. *   **Avoid `read_gbq()` for SQL**: Do not write SQL queries and execute them
3. *   **Use BigFrames ML package for Machine Learning Tasks**: Do not use
4. *   **Do not use lambdas** with `Series.map()` or `DataFrame.apply()`.
5. *   **Schema Verification**: Do not assume schema of intermediate outputs.

## Files inside the skill

- (SKILL.md only)
