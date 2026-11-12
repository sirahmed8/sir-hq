# cloud-sql-mysql-data

## Summary
Google-published skill for working inside a Cloud SQL for MySQL database: executing arbitrary SQL, listing table schemas with full detail (columns, constraints, indexes, triggers), and getting MySQL's query plan (EXPLAIN) to analyze performance and index effectiveness. Same Node-script wrapper pattern as the other cloud-sql-* skills.

## When to use / when NOT
Use for "run this query", "show me the tables/schema", "why is this query slow / which indexes help". Do NOT use for instance/user/database provisioning (cloud-sql-mysql-admin) or backup/restore operations (cloud-sql-mysql-lifecycle).

## Inputs, outputs, tools
- Inputs: `sql` statement (execute_sql), `sql_statement` (get_query_plan), `table_names` comma list + `output_format` simple|detailed + `min_duration_secs`/`limit` (list_tables, list_active_queries).
- Outputs: query results, JSON schema descriptions, EXPLAIN plans, and top-N longest-running queries from processlist + innodb_trx.
- Tools: `scripts/execute_sql.js`, `get_query_plan.js`, `list_tables.js`, `list_active_queries.js` via `node <skill_dir>/scripts/<name>.js '{...}'`; auto-loads .env.

## 5 most important rules
1. execute_sql runs real statements against the database — treat it as a write-capable tool and confirm destructive SQL with the user first.
2. Use get_query_plan before recommending index changes; it shows how MySQL will execute the statement.
3. list_active_queries reveals long-running transactions (wait duration, rows locked/modified) — the first stop for "database is slow" triage.
4. `project` is pre-configured; never ask for it unless the user names another.
5. Do not ask about env vars unless a script actually fails on missing env.

## Risks / things needing the owner
execute_sql can mutate or drop production data — no dry-run guard in the skill itself. Requires DB credentials in env. Query plans reflect current stats, not guaranteed future plans.

## Category / tags
cloud · gcp, cloud-sql, mysql, sql, database, monitoring

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-mysql-data\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
