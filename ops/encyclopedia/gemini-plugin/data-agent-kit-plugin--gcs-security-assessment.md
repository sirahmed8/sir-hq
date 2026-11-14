# gcs-security-assessment

## Summary
SAIF-grounded security posture assessment for Google Cloud Storage buckets/projects — NOT a generic security chatbot. Runs a strict 5-phase pipeline defined in references/phases/: (1) Discover scope & gather telemetry, (2) classify buckets, (3) baseline security evaluation, (4) toxic-combination analysis, (5) formatted report. Philosophy: correlate multiple signals to find "toxic combinations" — individually low-risk configs that combine into critical exposure (e.g. public bucket + ML training data + no CMEK + no VPC-SC + no audit logs ≠ public marketing PDFs). Every finding must be grounded in actually-gathered telemetry; unverifiable checks are explicitly skipped, never hallucinated.

## When to use / when NOT
Use for GCS security scans, vulnerability checks, SAIF assessments tied to a specific project/bucket. NOT for non-GCS resources (Compute, GKE), live production outages, or general security questions.

## Inputs, outputs, tools
- Inputs: project ID / bucket names / dataset references from user.
- Outputs: phased assessment report (bucket classifications, baseline failures, toxic combos, cross-cutting remediations; keep under ~80 lines, reasoning condensed to 2-3 sentences).
- Tools: Storage Insights datasets, BigQuery telemetry scripts (fetch_bucket_telemetry.py, fetch_object_telemetry.py), evaluate_project_security_posture.py, IAM Recommender, Model Armor API, preflight adc check.

## 5 most important rules
1. Follow phases strictly in order; never skip; only a failed `adc` preflight sets ready_to_proceed=false and stops everything — everything else branches on `analysis_scope`.
2. Multiple Storage Insights datasets → STOP and ask the user to pick one; never auto-select.
3. `project_only` scope (SI unavailable) does NOT bail: run only evaluate_project_security_posture.py, skip SI-backed telemetry scripts, recommend enabling SI.
4. PermissionDenied on a check = mark that status UNKNOWN and use that wording consistently across ALL report sections — never infer the control is present or absent.
5. NEVER execute destructive commands (rm/rb/IAM changes) without printing the exact command and getting explicit Y/N; Model Armor API disabled is a FINDING not an error; untagged/unclassified buckets are treated as potentially sensitive (recommend SDP).

## Risks / owner needs
Read-only assessment by design, but remediation steps may include owner-level decisions (enabling SI, VPC-SC, CMEK). Report must be honest about unknowns — UNKNOWN is a valid status, guessing is not.

## Category and tags
Category: security. Tags: gcs, google-cloud, security-assessment, saif, toxic-combinations, compliance, telemetry.

## Revisions
Single gemini skill copy; no competing revisions.
