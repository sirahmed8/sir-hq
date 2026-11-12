# accidental-data-loss-prevention

- Tool: `claude`
- Category: data
- Source: `C:\Users\a7med\.claude\skills\accidental-data-loss-prevention\SKILL.md`
- SKILL.md size: 1316 chars

## What it does

| **STOP AND VERIFY**: Before running any command or tool that results in irreversible data loss, you MUST obtain explicit user consent. When in doubt, ask. It is better to wait for confirmation than to accidentally delete production data or critical project assets. Use this for: - SQL: DROP TABLE/VIEW/SCHEMA/DATABASE, TRUNCATE, or broad DELETE (missing WHERE or using 1=1). - Cloud Storage: gsutil rm or gcloud storage rm targeting production data or critical buckets. - Infrastructure: gcloud projects delete, deleting Spanner/BigQuery/Dataproc resources, deleting secrets, or KMS key destruction.

## Structure (headings inside SKILL.md)

- Accidental Data Loss Prevention
- Mandatory Procedure
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  **Halt Execution**: Do **not** execute the command.
2. 2.  **Request Consent**: Explain clearly to the user:
3. -   The **impact** of this deletion.

## Files inside the skill

- (SKILL.md only)
