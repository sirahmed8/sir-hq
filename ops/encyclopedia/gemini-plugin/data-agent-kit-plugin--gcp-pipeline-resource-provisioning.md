# gcp-pipeline-resource-provisioning

## Summary
gcp-pipeline-resource-provisioning is a Google-published skill for declarative GCP resource creation (BigQuery datasets/tables, Dataform, Dataproc, BigQuery Data Transfer Service) via `deployment.yaml` using `gcloud beta orchestration-pipelines`. It enforces mandatory `datacloud` label on every resource definition (value: antigravity/vscode/other per IDE), requires explicit destination dataset for BigQuery DTS transfers, and mandates secrets via Secret Manager references (`secrets:` block, `{{ VAR }}` substitution) — never hardcode secrets, never create secrets (ask user). Workflow: list supported resource types with `gcloud beta orchestration-pipelines resource-types list`; discover project/region/commit SHA/env via gcloud/git; generate/update deployment.yaml using reference spec; validate per environment; deploy with `deploy --local`. References: gcp_pipeline_resource_provisioning_spec.md (template with sample resource blocks).

## When to use / when NOT
Use when creating/modifying deployment.yaml for pipeline infrastructure, resolving env-specific variables, or provisioning supported resources via orchestration pipelines. Do NOT use if resources already exist, for unsupported resource types, for general cloud infra (VMs, networks, K8s, IAM — use Terraform), for multi-cloud, or if already using Terraform for target resources.

## Inputs, outputs, tools
- Inputs: Target environment (dev/stage/prod), resource types and configs, existing deployment.yaml (if any).
- Outputs: deployment.yaml with actual values (no placeholders), validated config, successful deployment (exit code 0).
- Tools: `gcloud beta orchestration-pipelines` (resource-types list, validate, deploy), `gcloud config get project`, `gcloud projects describe`, `gcloud config get-value compute/region`, `git rev-parse HEAD`. References: gcp_pipeline_resource_provisioning_spec.md. No scripts folder.

## 5 most important rules
1. Always populate `datacloud` label under `definition.labels` for every resource (hardcode: antigravity/vscode/other).
2. For BigQuery DTS transfer configs, MUST also define target `bigquery.dataset` in same file with datacloud label, even if dataset exists.
3. Secrets: store in Secret Manager, reference in `secrets:` block, substitute as `{{ VAR }}`; never create secrets, never read/print secret values.
4. Validate with `gcloud beta orchestration-pipelines validate --environment=<ENV>` before deploy.
5. Deploy with `gcloud beta orchestration-pipelines deploy --environment=<ENV> --local`; do not remove DTS transfer resource after run completes.

## Risks / things needing the owner
User must create secrets manually in Secret Manager if missing; agent only references them. Project/region discovery via gcloud requires auth. Deployment modifies live GCP resources — user should review deployment.yaml before deploy. No direct owner actions beyond secret creation.

## Category / tags
cloud · gcp, provisioning, orchestration-pipelines, bigquery, dataform, dataproc, dts, declarative, secrets

## Revisions
Single revision in `C:\Users\a7med\.gemini\skills\gcp-pipeline-resource-provisioning\SKILL.md` (Google-published, Apache-2.0, v1). Only gemini has this skill; 1 reference file. No divergent copies.