# alloydb-omni-data

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-data\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A data migration and sync skill for AlloyDB Omni that moves data between on-premises PostgreSQL databases and cloud AlloyDB clusters, and vice versa. It handles schema conversion, data type mapping, large object (LOB) migration, and incremental sync via CDC (Change Data Capture). The skill also validates data integrity after migration using checksum comparison and can reverse migration direction if needed.

## When to use / when NOT
Use when migrating an existing PostgreSQL workload to AlloyDB Omni or syncing data bi-directionally between on-prem and cloud. Do NOT attempt a full dump-restore for large databases (over 100GB) without incremental sync — the skill's CDC feature is designed for this. Do NOT skip the schema validation step; migrating with incompatible data types will cause runtime errors in the target cluster.

## Inputs, outputs, tools
- Inputs: source PostgreSQL connection string, target AlloyDB connection string, migration direction (on-prem→cloud, cloud→on-prem, bidirectional), checksum algorithm (md5, sha256), sync interval (for incremental).
- Outputs: migration report (rows migrated, errors, checksum validation), incremental sync status, schema diff, reversed migration flag if applicable.
- Tools: `gsql` or `psql` for source/target, `alloydb-migration` CLI, `etcdctl` for CDC state, `md5sum`/`sha256sum` for checksums. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always test migration on a copy of the database first** — never migrate production data without a recoverable backup and a test run.
2. **Use checksum validation after any data move** — the skill compares row counts and checksums between source and target to confirm integrity.
3. **For incremental sync, configure CDC with a reasonable wal retention period** — too short and changes are lost; too long and CDC consumes excessive storage.
4. **Handle data type mismatches proactively** — AlloyDB Omni may not support all PostgreSQL extensions (e.g., PostGIS, pgvector); map these before migration.
5. **Document the migration rollback plan** — the skill can reverse direction, but you must have the original data available and the rollback logged before starting.

## Risks / owner notes
The biggest risk is data loss during migration if the checksum validation is skipped or if the CDC lag exceeds the retention window. The owner should always run a full checksum comparison after any migration and monitor CDC lag during incremental sync. Rolling back a failed migration can be complex if the original database has been modified since the backup was taken.

## Category / tags
database · data-migration, postgres, alloydb, sync, cdc, checksum, migration

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.