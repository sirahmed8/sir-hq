# gcp-spark-troubleshooting

- Tool: `gemini-config`
- Category: design
- Source: `C:\Users\a7med\.gemini\config\skills\gcp-spark-troubleshooting\SKILL.md`
- SKILL.md size: 27677 chars

## What it does

Provides expert guidance for troubleshooting Google Cloud Spark and Dataproc workloads (Dataproc Serverless batches and standard Dataproc clusters), and inspecting, streaming, searching, tailing, or summarizing Spark driver outputs and event logs in Cloud Storage. Use when the user asks to debug, troubleshoot, diagnose, or perform Root Cause Analysis (RCA) on failed Spark jobs, PySpark batches, or Spark event logs.

## Structure (headings inside SKILL.md)

- Dataproc Spark Troubleshooting Expert Skill
- Role & Persona
- CRITICAL RULES (MUST FOLLOW):
- Tooling Prerequisites
- Evidence Flow by Workload Type
- Dataproc Serverless batch / session
- Dataproc cluster job
- Direct GCS URI
- Dataproc Serverless: how to read the Spark application data
- Direct Log Reading & Analysis Workflow (GCS / HTTPS URLs)
- Spark Applications Workflow (Serverless Batches & Sessions)
- Spark Code Inspection Workflow (Scripts, JARs & Bytecode)
- Task Execution Process for Troubleshooting Workloads
- Troubleshooting Scenarios Catalog
- Important Constraints
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **A fetch error** (permission, not found): report it with the exact
- -   a rule that fails to compile or evaluate is skipped with a warning.
- -   **Safety**: Do not print plaintext secrets or credentials found in

## Key rules (verbatim lines from SKILL.md)

1. -   **NEVER create Jupyter notebooks or python scripts to analyze, read, or
2. -   **NEVER submit Dataproc jobs or batches to process log files.**
3. -   **NEVER download or buffer full multi-gigabyte log files into memory or the
4. -   **ALWAYS check file sizes for GCS logs:** For files larger than **20 MB**
5. -   **NEVER `cat`, `gcloud storage cat`, or text-decode a `.jar`, `.zip`, or

## Files inside the skill

- `references/diagnostic_rules_catalog.md` — "Spark Stage Diagnostic Rules: Authoring Guide"
- `references/gcs_event_log_guide.md` — "Spark Event Log Structure & Streaming Parser Guide"
- `references/rca_report_template.md` — "Root Cause Analysis (RCA) Report Template"
- `references/spark_log_patterns.md` — "Spark Error Patterns & Remediation Playbook"
- `scripts/spark_applications.py`
- `scripts/spark_code_inspector.py`
- `scripts/spark_gcs_log_reader.py`
- `scripts/spark_stage_diagnostics.py`
