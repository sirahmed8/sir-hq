# cloud-sql-sqlserver-data

## Summary
Minimal Google-published skill for Cloud SQL SQL Server data access: exactly two scripts — `execute_sql` (run one statement) and `list_tables` (schema info for user tables). The smallest member of the cloud-sql family; no views/indexes/sequences/procedure listers unlike the Postgres counterpart.

## When to use / when NOT
Use only for "run this T-SQL" or "list tables". For anything richer (indexes, views, query plans, monitoring) this skill does not cover it — pair with cloud-sql-sqlserver-monitor for metrics or run queries via execute_sql directly.

## Inputs, outputs, tools
- Inputs: `sql` for execute_sql; table filters/output format for list_tables.
- Outputs: query results and JSON table schema details.
- Tools: `scripts/execute_sql.js`, `scripts/list_tables.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. execute_sql runs one real statement — destructive T-SQL needs explicit user confirmation.
2. There is no query-plan or index-inspection script here; do not pretend coverage exists.
3. `project` is pre-configured; never ask unless the user names another.
4. Do not ask about env vars unless a script fails on missing env.
5. Keep statements single — the tool executes one SQL statement per call.

## Risks / things needing the owner
Write-capable execute_sql against production credentials. Requires GCP/DB credentials in env.

## Category / tags
cloud · gcp, cloud-sql, sqlserver, sql, database

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-sqlserver-data\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
