# alloydb-postgres-replication

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-replication\SKILL.md` (3.4 KB; gemini revision; runnable scripts in `scripts/`).

## Summary
Google-published skill for watching AlloyDB for PostgreSQL replication. Six runnable scripts report database server state, single instance details, instance listings, publication tables and replication slots, and per-replica lag metrics.

## When to use / when NOT
Use when the question is about replication health, sync state between nodes, or high availability and data distribution of an AlloyDB cluster. Do NOT use for cluster provisioning or routine database administration; those belong to the sibling alloydb-postgres-admin skill.

## Inputs, outputs, tools
- Inputs: script name (database_overview, get_instance, list_instances, list_publication_tables, list_replication_slots, replication_stats) plus its parameters; the GCP project is pre-configured and must not be asked for unless the user names another one.
- Outputs: server version, uptime and connection usage; instance details; slot and WAL data; per-replica lag sizes.
- Tools: `node <skill_dir>/scripts/<script>.js '{"<param_name>": "<param_value>"}'`; PowerShell needs the quotes escaped; env vars load from .env files automatically.

## 5 most important rules
1. Never ask for the GCP project ID; it is pre-configured and only overridden on explicit user request.
2. Use the shipped scripts only; do not hand-write queries against the cluster.
3. Pass parameters as a JSON object; on PowerShell escape the quotes.
4. Do not ask the user to set env vars in advance; the scripts load them from .env files.
5. get_instance requires location, cluster and instance; list_instances defaults to all regions and clusters when the filters are omitted.

## Risks / things needing the owner
Running the scripts needs the Gemini toolbox server via npx and working GCP credentials; auth failures should be surfaced rather than worked around.

## Category / tags
Category: data. Tags: alloydb, postgres, replication, gcp, high-availability, wal, lag.

## Revisions
Single gemini copy (v1, Apache-2.0). No competing revisions.
