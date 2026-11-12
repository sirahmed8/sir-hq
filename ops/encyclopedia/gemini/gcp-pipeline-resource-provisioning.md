# gcp-pipeline-resource-provisioning

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\gcp-pipeline-resource-provisioning\SKILL.md`
- SKILL.md size: 6528 chars

## What it does

| Automates declarative resource creation and provisioning for data pipelines, supporting BigQuery, Dataform, Dataproc, BigQuery Data Transfer Service (DTS), and other resources. It manages environment-specific configurations (dev, staging, prod) through a deployment.yaml file. Use when: - Modifying or creating deployment.yaml for deployment settings. - Resolving environment-specific variables (e.g., Project IDs, Regions) for deployment. - Provisioning supported infrastructure like BigQuery datasets/tables, Dataform resources, or DTS resources via deployment.yaml. Do not use when: - Resources already exist. - Managing resources not supported by `gcloud beta orchestration-pipelines resource-types list`. - Managing general cloud infrastructure (VMs, networks, Kubernetes, IAM policies), which are better suited for Terraform. - Infrastructure spans multiple cloud providers (AWS, Azure, etc.). - Already uses Terraform for the target resources.

## When to use (from skill text)

- ## How to use this skill

## Structure (headings inside SKILL.md)

- How to use this skill
- Mandatory labels
- Step 1: Supported Resource Types
- Step 2: Discover Environment Parameters
- Step 3: Generate or update deployment.yaml
- Step 4: Validation
- Step 5: Deployment
- Definition of Done
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 5.  **Environment Name**: If initialization is needed, you MUST ask the user for

## Files inside the skill

- `references/gcp_pipeline_resource_provisioning_spec.md` — "e"
