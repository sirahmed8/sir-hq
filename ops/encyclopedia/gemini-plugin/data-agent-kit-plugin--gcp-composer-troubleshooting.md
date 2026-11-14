# gcp-composer-troubleshooting

## Summary
gcp-composer-troubleshooting is a Google-published skill for performing Root Cause Analysis (RCA) on failed Cloud Composer (Apache Airflow) pipelines. It provides a structured, evidence-based workflow: gather context (DAG ID, run ID), fetch logs via `gcloud logging read`, download the actual remote DAG code from GCS using `gcloud storage` (never assume local code matches), correlate logs with code to pinpoint the failure, and produce an RCA report. It emphasizes read-only analysis first, prohibits hallucination, and includes templates for declarative pipeline files (deployment.yaml, orchestration-pipeline.yaml) with environment-specific configs. Reference files in the skill folder cover environment inspection and local development.

## When to use / when NOT
Use when a Composer/Airflow DAG fails and the user wants an RCA, or when debugging DAG import errors, task failures, or performance issues in a managed Airflow environment. Do NOT use for general GCP troubleshooting unrelated to Composer, for writing new DAGs from scratch (use gcp-data-pipelines or gcp-pipeline-orchestration instead), or for modifying code without first proving the root cause with logs and remote code.

## Inputs, outputs, tools
- Inputs: DAG ID, approximate failure time or run ID, optional task ID; user may provide vague error ("my DAG failed") requiring log search.
- Outputs: Root Cause Analysis report with specific log entries, code snippets, line numbers, and proposed fix; optionally a fixed DAG file if user requests.
- Tools: `gcloud` CLI (composer environments list/list-dags/run, logging read, storage cp), gcs buckets. No scripts/references in skill folder; references exist externally (environment-inspection.md, local-development-environment.md).

## 5 most important rules
1. Always gather context first (DAG ID, run ID, task ID) — if user gives vague error, ask for identifiers or time range.
2. Use `gcloud logging read` with filters: severity="ERROR", resource.type="cloud_composer_environment", logName/text containing DAG ID; broaden time window if needed.
3. Download remote DAG code from GCS bucket (logs provide bucket/path) — never assume local code matches; remote is source of truth.
4. Correlate logs with code to pinpoint exact line/config causing failure; do not modify code during RCA phase.
5. Produce RCA report citing specific log entries and code; only propose fix after root cause is proven.

## Risks / things needing the owner
Log access requires appropriate GCP IAM roles (Logging Viewer, Storage Object Viewer). Secrets in logs must be redacted. Syncing local-to-remote or downloading remote DAGs needs explicit user confirmation. The skill is read-only until user explicitly requests a fix and points to the correct git repo.

## Category / tags
cloud · gcp, composer, airflow, rca, troubleshooting, logging, gcloud, data-pipelines

## Revisions
Single revision in `C:\Users\a7med\.gemini\skills\gcp-composer-troubleshooting\SKILL.md` (Google-published, Apache-2.0, v1). No divergent copies on other tools (only gemini has this skill).