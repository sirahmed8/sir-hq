# gcp-managed-spark-upgrades

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\gcp-managed-spark-upgrades\SKILL.md`
- SKILL.md size: 24983 chars

## What it does

Upgrades Spark workloads on Google Cloud Managed Service for Apache Spark (formerly known as Dataproc) clusters and Serverless to a newer image or runtime version. Supports static compatibility analysis, code upgrade, build checks against the target version, and optional verification runs. Use when: - Upgrading Managed Spark versions (major, minor, or sub-minor) or assessing upgrade readiness. Example prompt: "Upgrade Managed Spark job [job_id] in project [project_id], region [region] to target version [target_version]. Code location: [local path or GCS path]. Target GCS path: [gcs_target_path]" Don't use when: - Writing new Spark code. - Migrating non-Spark workloads (e.g., Hive/Flink to Spark). - Troubleshooting a failed Spark job that is not part of an upgrade. Limitation: This skill does not support data/result validation currently.

## Structure (headings inside SKILL.md)

- Scope gate
- Terminology
- Rules
- Inputs
- Workflow
- Step 1: Analyze & Upgrade (mandatory)
- Step 2: Verify on GCP (optional)
- Step 3: Handover (mandatory)
- Definition of Done
- IAM Requirements

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 7.  **One token per flag.** Write each long option that takes a value as a
- 1.  **Confirm the production paths are untouched.** Diff the original and final
- -   the recommended production configuration (pinned image version or
- -   [ ] **Handover:** the diff confirms that production paths are untouched, and

## Key rules (verbatim lines from SKILL.md)

1. 3.  **Edit a local working copy.** Never overwrite the source objects in GCS,
2. 4.  **Isolate verification output.** A verification run must never write to
3. 5.  **Approvals.** There are two checkpoints: applying code changes (before Step
4. -   **Project ID, Region**: Cluster: Required. Serverless: Required. Needed
5. -   **Subnet**: Cluster: Required. Serverless: Required. Needed before: Step 2.

## Files inside the skill

- `references/cluster_input_validations.md` — "Cluster Input Checks & Source Discovery"
- `references/cluster_verifications.md` — "Managed Spark Cluster Verification Guide"
- `references/pyspark_analysis.md` — "PySpark Compatibility Analysis Guide"
- `references/serverless_input_validations.md` — "Serverless Input Checks & Source Discovery"
- `references/serverless_verifications.md` — "Managed Spark Serverless Verification Guide"
- `references/spark_migration_reference.md` — "Common Spark Migration Reference"
- `scripts/resolve_version.py`
