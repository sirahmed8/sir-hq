# gcp-managed-airflow-migrations

## Summary
gcp-managed-airflow-migrations is a Google-published skill for migrating Apache Airflow DAGs to Managed Service for Apache Airflow (MSAA, formerly Cloud Composer) Gen 2/3 targeting Airflow 2.11.1 or Airflow 3. It provides a 4-phase workflow: Phase 1 — download DAGs from source environment (references/environment-inspection.md); Phase 2 — map target version dependencies with detailed provider/SSH/HTTP version tables and breaking changes for Composer 2.10.0 through 2.17.0 (Airflow 2.11.1) plus Airflow 3 changes (decoupled Task SDK, Asset rename, SubDAG/SLA removal); Phase 3 — scan downloaded DAGs with specific grep commands for core changes (Dataset scheduling, HTML descriptions, Teardown tasks, Pendulum 3) and provider packages (SSH, HTTP, Google providers v11–v20 with exact scan commands and remediation); Phase 4 — optional deployment/verification (static lint with ruff AIR30, upload to target GCS, verify via Airflow CLI `dags list`/`dags list-import-errors`, monitor Cloud Logging). References: environment-inspection.md, airflow-3.md, local-development-environment.md.

## When to use / when NOT
Use when migrating DAGs from an existing MSAA/Composer environment to Airflow 2.11.1 (Gen 2/3) or Airflow 3 (Gen 3), including dependency upgrades and breaking-change remediation. Do NOT use for writing new DAGs, general Composer troubleshooting (use gcp-composer-troubleshooting), or migrations to non-MSAA Airflow deployments.

## Inputs, outputs, tools
- Inputs: Source environment name/region (optional, for inspection), target version (Airflow 2.11.1 or 3), DAG files (local or downloaded).
- Outputs: Remediated DAG files, migration report with scan findings, deployment commands, verification steps.
- Tools: `gcloud composer environments describe/run`, `gcloud storage cp`, grep/sed for scanning, ruff for Airflow 3 static checks. References: 3 files in `references/` (environment-inspection.md, airflow-3.md, local-development-environment.md). No scripts folder.

## 5 most important rules
1. Phase 1: Download and inspect source environment DAGs before any changes; confirm source version only if explicitly requested.
2. Phase 2: Apply all relevant dependency mappings cumulatively — when migrating to Airflow 3, include all Airflow 2.11.1 changes plus Airflow 3 changes.
3. Phase 3: Run exact scan commands provided (grep patterns for each breaking change) and apply specified remediation (e.g., SimpleHttpOperator→HttpOperator, BigQueryExecuteQueryOperator→BigQueryInsertJobOperator, SSHHook timeout→conn_timeout, context manager changes).
4. Phase 4 (optional): Validate with `ruff check --select AIR30`, deploy modified DAGs to target GCS bucket, verify via `gcloud composer environments run dags list` and `dags list-import-errors`, monitor Cloud Logging for errors.
5. Never deploy/upload/verify unless explicitly requested; static verification and deployment are opt-in steps.

## Risks / things needing the owner
Target environment details (name, region, GCS bucket) needed for deployment — user must provide or confirm. Secret values in DAGs must not be exposed during scan. `gcloud` commands require appropriate IAM. Airflow 3 migration is a major upgrade; testing in local Composer dev environment (`composer-dev`) recommended before production deploy.

## Category / tags
cloud · gcp, composer, airflow, migration, msaa, dag, breaking-changes, provider-upgrade

## Revisions
Single revision in `C:\Users\a7med\.gemini\skills\gcp-managed-airflow-migrations\SKILL.md` (Google-published, Apache-2.0, v1). Only gemini has this skill; 3 reference files. No divergent copies.