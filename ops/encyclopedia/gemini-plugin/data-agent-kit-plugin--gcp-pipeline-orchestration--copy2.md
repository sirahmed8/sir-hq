# gcp-pipeline-orchestration

## Summary
gcp-pipeline-orchestration is a Google-published skill for generating, validating, deploying, and triggering orchestration pipelines on Google Cloud Composer using the `gcloud beta orchestration-pipelines` CLI. It manages two files: an orchestration YAML (pipeline logic, tasks, schedule — camelCase fields, mandatory tags per IDE) and `deployment.yaml` (environment configs: project, region, Composer environment, artifact storage bucket, pipeline sources, variables). Workflow: check for existing deployment.yaml; if missing, init with `gcloud beta orchestration-pipelines init`; fetch Dataproc clusters and Composer environments via gcloud to avoid placeholders; generate/update both files; mandatory validation with `gcloud beta orchestration-pipelines validate --environment=<ENV>` per environment; optional deploy (`deploy --local` returns bundle ID, defaults to paused); optional trigger (Deploy → Poll 30s+15s×2min → Trigger → Verify run). References: orchestration-pipelines-schema.md (YAML structure, camelCase mapping, required tags, deployment.yaml template). Scripts: trigger/airflow_trigger.py fallback.

## When to use / when NOT
Use when creating or updating declarative orchestration pipelines for Cloud Composer to schedule/coordinate dbt, Spark, Dataform, Python, or BigQuery SQL pipelines. Do NOT use for general Airflow DAG authoring (use gcp-composer-troubleshooting for debugging, gcp-managed-airflow-migrations for upgrades), for provisioning infrastructure (use gcp-pipeline-resource-provisioning), or for running pipelines locally without orchestration.

## Inputs, outputs, tools
- Inputs: Pipeline name, environment name (default dev), project/region (from gcloud or user), artifact bucket, Composer environment, Dataproc clusters, schedule (cron, must have endTime), pipeline tasks (dbt, pyspark, bq, etc.).
- Outputs: orchestration-pipeline.yaml, deployment.yaml, validation pass, deploy bundle ID, trigger run confirmation, run list output.
- Tools: `gcloud beta orchestration-pipelines` (init, validate, deploy, list, trigger, runs list, pause/unpause), `gcloud dataproc clusters list`, `gcloud composer environments list/describe`. References: orchestration-pipelines-schema.md. Scripts: trigger/airflow_trigger.py.

## 5 most important rules
1. Always check for existing deployment.yaml first; if absent, init with `gcloud beta orchestration-pipelines init` (ask for pipeline name, default env=dev).
2. YAML uses camelCase (proto snake_case → YAML camelCase); mandatory `tags` field at top level (e.g., ["job:datacloud:kilo"] for this harness).
3. Every schedule MUST include endTime; startTime defaults to current date; never include Z suffix (use YYYY-MM-DDTHH:MM:SS).
4. Validate per environment with `gcloud beta orchestration-pipelines validate --environment=<ENV>`; fix errors and re-validate until exit code 0 before deploy/trigger.
5. Deploy → Poll → Trigger flow: deploy with `--local` (extract bundle ID), poll `list --bundle` every 15s up to 2min, then trigger with bundle ID and pipelineId; verify run appears in `runs list`.

## Risks / things needing the owner
User must provide artifact storage bucket name (init creates placeholder). Composer environment must have compatible image version (composer-3-airflow-3.1.7-build.x, composer-2.16.11-airflow-2.11.1, etc.) and orchestration-pipelines PyPI package. gcloud beta commands require appropriate IAM. Fallback trigger script needs project/region/composer_env from deployment.yaml.

## Category / tags
cloud · gcp, composer, orchestration, orchestration-pipelines, declarative, yaml, dataproc, scheduling

## Revisions
Single revision in `C:\Users\a7med\.gemini\skills\gcp-pipeline-orchestration\SKILL.md` (Google-published, Apache-2.0, v1). Only gemini has this skill; 1 reference file, 1 script (trigger/airflow_trigger.py). No divergent copies.