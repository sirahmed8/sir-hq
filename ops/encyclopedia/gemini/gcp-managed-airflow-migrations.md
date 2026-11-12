# gcp-managed-airflow-migrations

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\gcp-managed-airflow-migrations\SKILL.md`
- SKILL.md size: 11695 chars

## What it does

Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers migration to Airflow 2.11.1 (MSAA Gen 2 and 3) and Airflow 3 (MSAA Gen 3), including environment inspection, GCS download/upload and scanning patterns for breaking changes.

## When to use (from skill text)

- *   **Change:** DAGs scheduled on datasets only trigger if events occur while
- catch events, or plan manual triggers for catch-up.

## Structure (headings inside SKILL.md)

- Managed Service for Apache Airflow (formerly Cloud Composer) Migration Guide
- Phase 1: Discovery & Download
- Phase 2: Target Version & Dependency Mapping
- 2.1 Airflow 2.11.1+ Dependency Mapping
- Composer 2.10.0 (Airflow 2.10.2)
- Composer 2.15.3 (Airflow 2.10.5)
- Composer 2.16.1 (Airflow 2.10.5)
- Composer 2.17.0 (Target Airflow 2.11.1)
- 2.2 Airflow 3 Migration
- Phase 3: Analysis & Remediation (Scanning Downloaded Files)
- 3.1 Airflow 2.11.1 Core & Dependency checks
- 3.2 Path A: Airflow 2.11.1 Provider Package Scan
- 3.3 Airflow 3 Migration checks
- Phase 4: Deployment & Verification
- 4.1 Static Verification (when migrating to Airflow 3)
- 4.2 Deployment to MSAA
- 4.2 Upload Modified DAGs and Bucket Dependencies (Only when requested)
- 4.3 Verify DAGs via Airflow CLI
- 4.4 Verify in Cloud Logging
- Appendix: Local Environment Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. *   **Remediation:** You MUST document that these DAGs must remain unpaused to
2. *   **Change:** Teardowns always run when a DAG is marked failed.

## Files inside the skill

- `references/airflow-3.md` — "Airflow 3 migration"
- `references/environment-inspection.md` — "Environment inspection & downloading files"
- `references/local-development-environment.md` — "Local Development Environment Verification"
