# gcp-spark-observability

- Tool: `gemini-config`
- Category: security
- Source: `C:\Users\a7med\.gemini\config\skills\gcp-spark-observability\SKILL.md`
- SKILL.md size: 8736 chars

## What it does

Monitors, inventories, and assesses Google Cloud Managed Service for Apache Spark (Dataproc Serverless and Dataproc on Compute Engine) environments, clusters, batches, jobs, sessions, metrics, logs, costs, and configurations across single and multiple regions. Use when listing active or historical Spark workloads, discovering failed batches or jobs, auditing multi-region fleet inventory, calculating Serverless compute (DCU-Hours) and shuffle storage consumption, detecting idle or zombie clusters, inspecting scheduled pipeline cadence health, investigating failed cluster operations or stockouts, checking quotas and alerting coverage, or querying Cloud Monitoring and Cloud Logging telemetry. Don't use for deep root-cause analysis or performance optimization of a specific job or batch (use gcp-spark-troubleshooting), authoring new PySpark code (use gcp-spark), or upgrading Spark versions (use gcp-managed-spark-upgrades).

## When to use (from skill text)

- * Handoff: if no `batch_id` or `job_id` is given (for example, *"Why did my last Spark batch fail?"*), use this skill first to find the latest failed ID, region, and `stateMessage`/`status.details`, then hand off to `@skill:gcp-spark-troubleshooting`.
- * Handoff: use this skill first to identify top DCU consumers, regressed schedules, or saturated clusters, then hand off one workload at a time with its ID, region, usage/runtime metrics, and `runtimeConfig`/`softwareConfig` properties. Do not propose Spark property tuning from fleet metrics alone.

## Structure (headings inside SKILL.md)

- Google Cloud Spark & Dataproc Observability
- Skill Routing & Handoff
- Non-Obvious CLI & API Gotchas (Read First)
- Where to Look (Quick Map)

## Tools / MCPs it needs

- MCP mentions: MCP field, MCP list

## Risks / cautions found in text

- * $\text{DCU-Hours} = \text{milliDcuSeconds} / 3{,}600{,}000$; $\text{Shuffle-GB-Months} = \text{shuffleStorageGbSeconds} / 2{,}592{,}000$. DCU-hours measure compute usage, not dollar spend (use Cloud Billing export for dollars; never fabricate dollar amounts).
- * Audit log entries with a non-empty `protoPayload.status` (such as `PERMISSION_DENIED`) are rejected API calls, not cluster operations.
- * Never cancel, kill, stop, or delete any workload or cluster without explicit user confirmation.
- * **Idle / zombie clusters:** `clusters list --filter="status.state=RUNNING" --limit=100` (always report `metrics.yarnMetrics`, `config.lifecycleConfig` TTLs `idleDeleteTtl`/`autoDeleteTime`/`idleStopTtl`, and recent `jobs list --cluster=<NAME> --limit=5`; recommend `gcloud dataproc clusters update 

## Key rules (verbatim lines from SKILL.md)

1. * Handoff: use this skill first to identify top DCU consumers, regressed schedules, or saturated clusters, then hand off one workload at a time with its ID, region, usage/runtime metrics, and `runtimeConfig`/`softwareConfig` properties. Do not propose Spark property tuning from fleet metrics alone.
2. * `sessions` and `session-templates` require the `beta` track and `--location=<REGION>` (`gcloud beta dataproc sessions list --location=<REGION>`).
3. * Always pass `--quiet` to `asset`, `metastore`, `composer`, and `scheduler` commands so disabled APIs do not hang on interactive prompts. Never enable APIs.
4. 3. **Always specify `--limit` & respect server-side `--filter` restrictions:**
5. * Always pass an explicit `--limit` (for example `--limit=20` to `--limit=200`) on every `gcloud ... list`, `gcloud asset search-all-resources`, and `gcloud logging read` query so list calls stay bounded.

## Files inside the skill

- `references/gcloud_observability_reference.md` — "gcloud Dataproc & Spark Observability Reference"
