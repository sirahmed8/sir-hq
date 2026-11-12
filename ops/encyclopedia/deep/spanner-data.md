# spanner-data

## Summary
spanner-data is a Google-published (Apache-2.0, publisher google, v1) skill for working with Google Cloud Spanner databases. It is a thin wrapper: a SKILL.md that documents four Node.js helper scripts in `scripts/` (`execute_sql.js` for DML, `execute_sql_dql.js` for DQL/SELECT, `list_tables.js` and `list_graphs.js` for schema discovery). Each script is invoked as `node <skill_dir>/scripts/<script>.js '{"param": "value"}'`, auto-loads credentials from .env files (and from Gemini/Claude plugin env conventions), and shells out to the prebuilt `spanner` gcloud/CLI tooling (`--prebuilt spanner`) to run the query or listing. Output for listings can be `simple` (names only) or `detailed` (full information schema as JSON).

## When to use / when NOT
Use when a project uses Cloud Spanner and the agent needs to inspect tables/graph schemas or run SQL against it. Do NOT use for Firestore (use firestore-data / firebase_firestore skills), for Postgres/MySQL (use the cloud-sql-* skills), or when no Spanner instance/credentials are configured.

## Inputs, outputs, tools
- Inputs: a JSON argument object per script (e.g. `{"sql": "SELECT ..."}`, `{"table_names": "users,orders", "output_format": "detailed"}`).
- Outputs: query result sets or JSON schema listings printed to stdout.
- Tools: Node.js runtime, the scripts themselves, the `spanner` prebuilt binary (gcloud CLI component), and Spanner credentials in environment/.env files (`SPANNER_DIALECT` is an optional var that gets omitted when empty). Requires an authenticated gcloud session and network access to the instance.

## 5 most important rules
1. DML goes through `execute_sql`; reads/SELECT go through `execute_sql_dql` (the skill insists on the googlesql interface for Spanner).
2. Scripts auto-load env vars from .env files; do not ask the user for vars unless execution actually fails on a missing one.
3. Schema discovery first: `list_tables` / `list_graphs` with `output_format=detailed` before writing queries against an unknown schema.
4. Graph support is explicit: Spanner Graph schemas are listed separately via `list_graphs`.
5. PowerShell needs escaped quotes in the JSON argument; Bash does not.

## Risks / things needing the owner
These scripts execute real SQL against a production-grade database: DML can mutate or delete data, so destructive statements need the usual care (and the accidental-data-loss-prevention skill applies). First-time setup needs `gcloud auth` / Spanner IAM credentials, which only the owner can grant. Costs: Spanner queries consume instance capacity (RU/CPU), relevant on paid instances.

## Category / tags
data · spanner, google-cloud, sql, database, gcloud

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\skills\spanner-data\` (SKILL.md plus four scripts). No divergent copies.
