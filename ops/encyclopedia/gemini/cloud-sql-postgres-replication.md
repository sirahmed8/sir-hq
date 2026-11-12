# cloud-sql-postgres-replication

## Summary
Google-published skill for auditing Cloud SQL PostgreSQL replication and security posture: server overview (version, replica flag, uptime, connection usage), pg_settings, publication tables, replication slots with retained-WAL size, role inventory with privilege flags, replication_stats showing per-replica lag breakdown (sent/write/flush/replay), and publication membership.

## When to use / when NOT
Use for "is replication healthy", "how far behind is the standby", "which slots are pinning WAL", "audit roles/privileges". Do NOT use for configuring replication itself (not covered), monitoring CPU/PromQL (monitor/health), or backups (lifecycle).

## Inputs, outputs, tools
- Inputs: optional filters `setting_name`, `table_names`/`publication_names`/`schema_names`, `role_name`, `limit`.
- Outputs: lag metrics per replica (bytes at each pipeline stage + total_lag), slot WAL retention sizes, role privilege matrix, publication table lists.
- Tools: `scripts/{database_overview,list_pg_settings,list_publication_tables,list_replication_slots,list_roles,replication_stats}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. list_replication_slots reports the WAL each slot prevents from being removed — a stale slot is a disk-fill risk; report size, don't drop.
2. replication_stats breaks lag into sent/write/flush/replay stages — pinpoint which stage is behind before recommending fixes.
3. list_roles exposes superuser/replication/BYPASSRLS flags — treat findings as a security audit, escalate anything unexpected.
4. `project` is pre-configured; never ask unless the user names another.
5. Do not ask about env vars unless a script fails on missing env.

## Risks / things needing the owner
Read-only audit; acting on findings (dropping slots, revoking roles) needs owner approval. Requires GCP + DB credentials.

## Category / tags
cloud · gcp, cloud-sql, postgres, replication, security, audit

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-replication\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
