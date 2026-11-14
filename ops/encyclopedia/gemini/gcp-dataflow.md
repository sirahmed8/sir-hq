# gcp-dataflow

## Summary
gcp-dataflow is a Google-published skill for authoring, packaging, executing, and troubleshooting Apache Beam pipelines on Cloud Dataflow. It covers the full lifecycle: check for existing Google-provided templates (Classic or Flex) matching source/sink before building custom; create new pipelines from scratch with language confirmation (Java/Python/Go) and consistent Beam SDK versioning; package as Flex Templates using Cloud Build (prefer over local Docker); configure Google templates with strict parameter validation (all non-optional params required); pre-create target sinks (BigQuery tables, error tables) to prevent runtime mismatches; execute with mandatory pre-launch confirmation of the full gcloud command; monitor jobs with staged polling; and deep diagnostics for streaming/batch jobs using Dataflow REST API, Monitoring, and Logging with transform-name-to-stage/ptransform mapping. References folder contains 8 detailed guides (python_flex_template_reference, dataflow_diagnostics_reference, bottlenecks_and_parallelism_context, streaming_job_health, streaming_horizontal_autoscaling_analysis, SSL cert guide, UDF guide, deadletter schema).

## When to use / when NOT
Use for creating Dataflow pipelines (custom or from templates), configuring Flex Templates, debugging job failures, analyzing streaming job health/bottlenecks/autoscaling, or batch job performance. Do NOT use for general GCP resource management, non-Dataflow services (GCE, GCS, BigQuery unless directly impacting Dataflow), or non-Beam pipeline technologies.

## Inputs, outputs, tools
- Inputs: Source/sink identification, pipeline requirements, existing codebase (Java Gradle, Python, Go), template selection, job ID for diagnostics.
- Outputs: Pipeline code (Java/Python/Go), cloudbuild.yaml, Flex Template artifacts, launch commands, monitoring URLs, diagnostic reports with root causes and file:/// code links.
- Tools: `gcloud` (dataflow flex-template run, jobs describe, logging read), `gcloud storage ls` for templates, Dataflow REST API, Monitoring REST API, Cloud Build. References: 8 .md files in `references/`. No scripts folder.

## 5 most important rules
1. Always check for existing Google Dataflow templates (Classic in gs://dataflow-templates/latest, Flex in gs://dataflow-templates/latest/flex) before writing custom pipeline.
2. Package new pipelines as Flex Templates using Cloud Build; use Single Docker Image Configuration for Python; never bake secrets into images — fetch from Secret Manager at runtime.
3. Strict parameter validation: any template metadata param without "isOptional": true is REQUIRED, even if description suggests default.
4. Pre-create target BigQuery table and error/bad-records table before launch; derive error schema from DataflowTemplates GitHub source.
5. Mandatory pre-launch confirmation: present entire gcloud command with all params explained; do not execute until explicit approval. Monitor with staged polling (30s×2min, then 3min).

## Risks / things needing the owner
GCP project/region/permissions must be verified; `gcloud config get-value project` used to avoid placeholders. Secrets via Secret Manager need `roles/secretmanager.secretAccessor` on worker SA. Regional restrictions may apply. No direct owner actions (sign-in, payment) but user must approve launch commands.

## Category / tags
cloud · gcp, dataflow, apache-beam, flex-templates, streaming, batch, diagnostics, troubleshooting, cloud-build

## Revisions
Single revision in `C:\Users\a7med\.gemini\skills\gcp-dataflow\SKILL.md` (Google-published, Apache-2.0, v4). Only gemini has this skill; 8 reference files in `references/`. No divergent copies.