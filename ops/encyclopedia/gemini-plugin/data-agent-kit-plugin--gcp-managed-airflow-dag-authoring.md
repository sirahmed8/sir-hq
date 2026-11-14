# gcp-managed-airflow-dag-authoring

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\gcp-managed-airflow-dag-authoring\SKILL.md`
- SKILL.md size: 5891 chars

## What it does

Guides the authoring and validation of Apache Airflow DAGs for Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers environment context discovery, Airflow 2 vs 3 compatibility, authoring best practices, and local/remote validation processes. Use when creating or extending an Airflow DAG. Don't use when authoring Python code unrelated to Airflow DAGs.

## Structure (headings inside SKILL.md)

- GCP Managed Airflow DAG Authoring Guide
- Phase 1: Context Discovery
- 1.1 Identify Target Environment & Access
- 1.2 Identify Development Environment
- 1.3 Inspect Target Environment (if available and requested)
- Phase 2: DAG Authoring Best Practices
- 2.1 General Airflow Best Practices
- 2.2 Airflow 2 vs Airflow 3 Compatibility
- Phase 3: Validation Process
- 3.1 Local Validation (Offline/Pre-deployment)
- 3.2: Target Environment Validation
- 3.2.1 Deploy to GCS
- 3.2.2 Verify via Airflow CLI
- 3.2.3 Monitor Cloud Logging
- Definition of Done

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **Use Airflow Variables/Connections:** Never hardcode credentials or

## Key rules (verbatim lines from SKILL.md)

1. *   **No Top-Level Code Execution:** Do NOT execute database queries, external
2. *   **Explicit Catchup:** Always set `catchup=False` in the DAG definition
3. *   **Use Airflow Variables/Connections:** Never hardcode credentials or

## Files inside the skill

- (SKILL.md only)
