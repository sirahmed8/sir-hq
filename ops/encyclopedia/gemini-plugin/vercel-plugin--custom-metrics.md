# custom-metrics (Vercel)

## Summary
Skill for emitting and querying Vercel Custom Metrics: call `metric(name, value, tags?)` from `@vercel/functions` inside a Function at the point an outcome is known, deploy and invoke it, then discover schema and query via `vc metrics` (sum/avg/percentiles, `--group-by` tags, `--since`). Includes modeling rules — stable dotted names with unit suffixes, bounded tag cardinality, no PII in tags — and a decision table for which signal to use (metrics vs Web Analytics events vs OTel spans vs logs).

## When to use / when NOT
Use for numeric business/application measurements you want to aggregate and trend (orders.created, durations, queue sizes). Do NOT use for user-interaction events (Web Analytics), traces (OTel), or per-request diagnostics (logs). Requires Observability Plus on the team.

## Inputs, outputs, tools
- Inputs: metric name, numeric value, optional string tags; `vc metrics schema|query` commands.
- Outputs: aggregated metric series in Vercel Observability.
- Tools: `@vercel/functions` `metric()` (sync, no-op off-runtime), Vercel CLI `vc metrics` / `vercel metrics`, project/team scope flags.

## 5 most important rules
1. Emit at the point the outcome is known; `metric()` is synchronous — never await it.
2. Stable dotted names with unit suffix (`orders.duration_ms`); variable data goes in tags, never in the name.
3. Tag cardinality must be bounded — outcome/plan/provider yes; user IDs, request IDs, emails, raw URLs never.
4. Match aggregation to emission: count events → emit 1 → `sum`/`persecond`; durations → emit value → `avg`/`p95`/`max`.
5. Verify via a deployed Function invocation — local runs are no-ops; check `vc metrics schema <name>` after deploy + ingestion delay.

## Risks / things needing the owner
Custom Metrics querying needs Observability Plus (paid tier) — confirm availability. High-cardinality tags can blow up cost; the skill's rules exist to prevent that. `vercel.` prefix is reserved.

## Category / tags
cloud · vercel, metrics, observability, instrumentation

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\custom-metrics\SKILL.md`. Only gemini-plugin holds it.
