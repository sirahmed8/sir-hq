# cloud-sql-postgres-data

## Summary
Google-published skill for exploring and querying a Cloud SQL for PostgreSQL database: execute a single SQL statement, list schemas (with owner, grants, object counts), tables (full JSON detail: columns, constraints, indexes, triggers, owner), views, indexes (with usage stats and unused detection), sequences, stored procedures, and triggers. Node-script JSON-param wrapper.

## When to use / when NOT
Use for "show the schema", "list indexes/views/sequences", "run this SELECT", "which indexes are unused". Do NOT use for instance/user provisioning (admin), monitoring/PromQL (monitor/health), backups (lifecycle), or MySQL.

## Inputs, outputs, tools
- Inputs: `sql` for execute_sql; filters `schema_name`, `table_name(s)`, `index_name`, `only_unused`, `role_name`, `sequence_name`, `limit`, `output_format` for the list_* scripts.
- Outputs: JSON schema metadata, query results, index usage statistics.
- Tools: `scripts/execute_sql.js`, `list_indexes.js`, `list_schemas.js`, `list_sequences.js`, `list_stored_procedure.js`, `list_tables.js`, `list_triggers.js`, `list_views.js`; Node + JSON; auto-loads .env; project pre-configured.

## 5 most important rules
1. execute_sql runs one real statement — destructive SQL needs explicit user confirmation first.
2. list_indexes reports scans/tuples-read per index and `only_unused` filtering — the evidence base for index cleanup decisions; report, don't drop.
3. All listers exclude system schemas (pg_catalog, information_schema) by design.
4. `project` is pre-configured; never ask unless the user names another.
5. Do not ask about env vars unless a script fails on missing env.

## Risks / things needing the owner
execute_sql is write-capable against whatever the credentials reach. Unused-index findings can be wrong if stats are stale — verify before recommending drops. Requires DB credentials in env.

## Category / tags
cloud · gcp, cloud-sql, postgres, sql, schema, database

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-data\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
