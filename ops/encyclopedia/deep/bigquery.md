# bigquery

**Source:** `C:\Users\a7med\.gemini\skills\bigquery\SKILL.md` (+ `references/`)
**Category:** data
**Tags:** bigquery, sql, bigframes, bqml, ai-functions, graph-analytics, gql, google-cloud

## Summary
A Google-published BigQuery skill (metadata version v4, Apache-2.0) that acts as a routing table for four BigQuery areas: SQL query optimization, BigFrames (BigQuery DataFrames) Python code, BigQuery ML and AI functions (BQML SQL), and Graph Analytics (property graphs and GQL). The SKILL.md itself is short and points to about 24 reference files; the real guidance lives in those references.

## When to use / when not to
Use it for any BigQuery work, especially query optimization, BigFrames code generation, BQML/AI function syntax, or GQL graph queries. Do not use it for non-Google data warehouses or for general Python and ML work unrelated to BigQuery.

## Inputs, outputs, tools
Inputs: the BigQuery task, the data size, and SQL or Python code. Outputs: optimized SQL, BigFrames code, BQML function usage, GQL queries, and a "Summary of Optimizations" section. Tools: BigQuery, BigFrames and GoogleSQL GQL. No MCP.

## Five most important rules
1. Always check the data size before choosing libraries, and justify the choice with that size.
2. Treat BigFrames as the default library over the BigQuery Python client; avoid `.to_pandas()` on full datasets, avoid `read_gbq()` for SQL, and prefer built-in accessors over UDFs and lambdas.
3. For BQML, table-valued functions (`AI.GENERATE_TABLE`, `AI.FORECAST`, `AI.EVALUATE`, `AI.GENERATE_EMBEDDING`) belong in the `FROM` clause; use `=>` for named optional arguments and `'DEFAULT'` as the remote connection.
4. For graphs, use BigQuery GoogleSQL GQL only; never generate Cypher.
5. Route to the specific reference file for the function or feature instead of answering from memory.

## Risks and owner actions
The skill is a router, so the reference files are large and detailed; the main risk is answering from memory instead of loading the right reference. No owner action is needed beyond GCP access.

## Revisions
Only one copy exists (`.gemini/skills/bigquery`, 3851 bytes, dated 2026-07-12).
