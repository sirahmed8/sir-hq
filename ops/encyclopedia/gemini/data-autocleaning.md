# data-autocleaning

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\data-autocleaning\SKILL.md`
- SKILL.md size: 12118 chars

## What it does

Automated data quality and transformation capabilities for Dataform/dbt/BigQuery pipelines. Processes data sourced from BigQuery or Cloud Storage (GCS), applying best practices for data ingestion, movement, schema mapping, and comprehensive data cleaning.

## When to use (from skill text)

- > You **MUST** use this skill for **ANY** task where the source is BigQuery or

## Structure (headings inside SKILL.md)

- Data Autocleaning Skill
- When to Use
- Task Execution Workflow
- Step 1: Preliminary Checks (Before Implementation Planning)
- Step 1.5: Implementation Plan Requirements
- Profiling Evidence
- Step 2: Generate Transformations
- Step 3: Quality Review & Profiling
- Step 3.5: Quality Review Evidence Requirements
- Quality Review Profiling Evidence
- Step 4: Documentation
- Definition of Done
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **Garbage Values**: Drop or convert to `NULL` only for malformed data (e.g.,
- -   **Schema Alignment**: Populate missing fields with `NULL` and drop fields

## Key rules (verbatim lines from SKILL.md)

1. -   **Never skip** Dataplex profiling (Steps 1 and 3). Always use Dataplex —
2. 1.  **Check Eligibility** — You MUST confirm the source is a BigQuery table or
3. -   **GCS sources**: For GCS sources, you MUST create an external table
4. -   **Wait for results**: You **MUST NOT** proceed until the Dataplex
5. 4.  **[!IMPORTANT]** The location MUST be a specific Google Cloud region

## Files inside the skill

- `scripts/dataplex_scanner.py`
