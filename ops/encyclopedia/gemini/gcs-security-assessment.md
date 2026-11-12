# gcs-security-assessment

- Tool: `gemini`
- Category: security
- Source: `C:\Users\a7med\.gemini\skills\gcs-security-assessment\SKILL.md`
- SKILL.md size: 6803 chars

## What it does

Assesses security posture, evaluates risks, and checks SAIF compliance for Google Cloud Storage buckets or projects. Use when the user requests security scans, vulnerability checks, or SAIF assessments. Don''t use when: The user is asking about non-GCS resources (Compute Engine, GKE, etc.), investigating a live production outage, or asking general security questions not tied to a specific project or bucket.'

## Structure (headings inside SKILL.md)

- Security Posture Assessment Skill
- Philosophy
- Phase Summary Table
- Workflow Execution
- Error Handling
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP Server

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 2.  **Do not skip phases**: You must complete Phase N before proceeding to Phase
2. 3.  **Strict adherence**: Follow all steps defined in each phase. Do not
3. 4.  **Gating & analysis scope**: Only a failed **required** preflight check

## Files inside the skill

- `examples/sample_assessment.md` — "Sample Assessment Output"
- `references/baseline_security.md` — "Baseline Security"
- `references/bucket_classification.md` — "Bucket Classification"
- `references/phases/baseline.md` — "Phase 3: Baseline Security Evaluation"
- `references/phases/classification.md` — "Phase 2: Bucket Classification"
- `references/phases/discover.md` — "Phase 1: Discover Scope and Telemetry"
- `references/phases/output.md` — "Phase 5: Output"
- `references/phases/toxic_analysis.md` — "Phase 4: Toxic Combination Analysis"
- `references/saif_risk_factors.md` — "SAIF Risk Factors"
- `references/telemetry_signals.md` — "Telemetry Signals Reference"
- `references/toxic_combinations.md` — "Toxic Combination Archetypes"
- `scripts/cloud_rest_helpers_nodeps.py`
- `scripts/evaluate_project_security_posture.py`
- `scripts/fetch_bucket_telemetry.py`
- `scripts/fetch_object_telemetry.py`
- `scripts/list_datasets.py`
- `scripts/preflight_permissions.py`
- `scripts/validation.py`
