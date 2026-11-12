# dataform-bigquery

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\dataform-bigquery\SKILL.md`
- SKILL.md size: 12258 chars

## What it does

Expertise in generating clean, correct, and efficient Dataform pipeline code for BigQuery ELT. Use this when creating or modifying Dataform pipelines, actions, or source declarations, when Dataform, SQLX, or BigQuery are mentioned in a transformation, when data needs to be ingested from GCS into BigQuery via Dataform, or when setting up a new Dataform project or configuring workflow_settings.yaml.

## Structure (headings inside SKILL.md)

- Dataform Expert Skill for BigQuery
- Role & Persona
- Task Execution Workflow
- Step 0: Environment Verification
- 1. Understand the Current State
- 2. Gather Information
- 3. Apply Automatic Data Cleaning and SQL Optimizations
- 4. Planning guidelines
- 5. Implement Changes
- 6. Validate & Compile
- 7. Iterate
- Credentials for `dataform run` and `dataform run --dry-run`
- Incremental / Append Operations
- Coding Standards
- BigQuery Source Declarations
- GCS Ingestion
- Schema & Metadata
- Readability
- BigLake Iceberg Support (4-Part Naming)
- Concatenating Catalog and Namespace Into Schema
- Unit Testing
- Security
- Operational Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2.  **Assumptions** — Numbered list of risky assumptions.
- -   If `.df-credentials.json` is successfully set up (from Step 1), run
- -   If `.df-credentials.json` could not be initialized, fall back to using

## Key rules (verbatim lines from SKILL.md)

1. -   Prioritize **technical accuracy** over agreement — investigate before
2. -   **Execution Rule**: MUST NOT execute a real `dataform run` without explicit
3. -   **Always** fetch schema for source and destination tables before working
4. -   **Always** add table and column descriptions.
5. -   **State assumptions clearly** — don't ask for unnecessary clarifications.

## Files inside the skill

- (SKILL.md only)
