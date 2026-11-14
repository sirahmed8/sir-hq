# google-cloud-storage-bucket-architect

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\google-cloud-storage-bucket-architect\SKILL.md`
- SKILL.md size: 10422 chars

## What it does

Creates Cloud Storage (Google Cloud Storage, or GCS) buckets. Analyzes the workload (sensitive data, media hosting, ingestion, web hosting, archiving, backup, logging, analytics, AI/ML, or general-purpose), validates project-level security settings, and designs a secure-by-default, cost-effective configuration (location, storage class, uniform bucket-level access, public access prevention, soft delete, lifecycle) before creating it. Use whenever a user wants to create, make, set up, provision, or spin up a bucket, or needs object storage for an app, service, pipeline, or dataset — even a "simple" or "default" bucket, or when bucket creation is one step in a larger workflow. Outputs or executes the creation via gcloud, the JSON/REST API, Terraform, or SDK client libraries (C++, Java, Python, Go). Don't use for anything other than creating new buckets — for uploads, downloads, access changes, or reconfiguring existing buckets, use google-cloud-storage-basics.

## When to use (from skill text)

- between commands. Use this append form verbatim. It keeps any attribution

## Structure (headings inside SKILL.md)

- Google Cloud Storage Bucket Architect
- Philosophy
- Attribution
- Phase Summary Table
- Workflow Execution
- Error Handling
- References
- Phases
- Bucket Use Cases
- Provisioning & Output Formats
- SDK Language-Specific Guides

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. *   **gcloud**: Prefix every `gcloud` invocation you execute or output
2. *   **REST (cURL)**: Set the `User-Agent` header verbatim:
3. 1.  **Start at Phase 1 (Preflight/Project Checks)**: Assess project-level

## Files inside the skill

- `references/archiving_compliance.md` — "Long-Term Archive & Regulatory Compliance"
- `references/backup_dr.md` — "Backup and Disaster Recovery"
- `references/gcloud.md` — "gcloud Command Generation Guide"
- `references/log_storage.md` — "Log Storage"
- `references/media_hosting.md` — "Media Hosting & Content Delivery Network (CDN)"
- `references/phase_draft_plan.md` — "Phase 2: Draft Bucket Create Plan"
- `references/phase_output.md` — "Phase 3: Output Based on User Intent"
- `references/phase_project_checks.md` — "Phase 1: Project-Level Security Checks"
- `references/rest.md` — "Cloud Storage JSON API Reference"
- `references/sdk.md` — "Cloud Storage SDK Reference"
- `references/sdk_cpp.md` — "C++ SDK Examples"
- `references/sdk_go.md` — "Go SDK Examples"
- `references/sdk_java.md` — "Java SDK Examples"
- `references/sdk_python.md` — "Python SDK Examples"
- `references/sensitive_data.md` — "Sensitive Data & Compliance (PII, HIPAA, Finance)"
- `references/static_website.md` — "Static Website Hosting"
- `references/storage_for_ai.md` — "AI & Machine Learning (Storage for AI)"
- `references/terraform.md` — "Terraform Google Provider Cloud Storage Reference"
- `references/ugc_ingestion.md` — "Direct User-Generated Content (UGC) Ingestion"
