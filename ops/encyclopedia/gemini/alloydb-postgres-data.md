# alloydb-postgres-data

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-data\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A data management skill for AlloyDB Omni that handles bulk data operations, including import/export, data copying between schemas, point-in-time recovery, and data archiving. It uses `COPY` protocol for high-throughput bulk loads, `pg_dump`/`pg_restore` for logical backups, and `pg_resetwal` for recovery when the WAL log is corrupted. The skill also validates data integrity after any bulk operation using row counts and checksums.

## When to use / when NOT
Use for bulk data moves, schema migrations, or recovery operations on AlloyDB Omni clusters. Do NOT use `pg_resetwal` without a recent backup — the skill will warn that this operation can cause data loss if the WAL files are missing. Do NOT import CSV files with more than 10 million rows in a single `COPY` command — the skill recommends batching into chunks of 100K-500K rows for reliability.

## Inputs, outputs, tools
- Inputs: operation type (import, export, backup, recover, copy), source/target connections, file paths (for COPY), batch size (recommended 100K-500K rows).
- Outputs: operation status (success/failed/rows_affected), data integrity checksum, row count, backup ID for recovery operations.
- Tools: `psql`, `pg_dump`, `pg_restore`, `gsutil` (for GCS backups), `COPY FROM/TO`, `wal-e` for continuous archiving. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always use batch-sized COPY imports** — the skill recommends 100K-500K row batches; importing 10M+ rows in one command risks timeout and partial loads.
2. **Validate data integrity after any bulk operation** — the skill compares row counts and MD5 checksums between source and target; never skip this step.
3. **Keep a recent backup before running pg_resetwal** — the skill will refuse to proceed if the last backup is older than 24 hours; this is a safety guard.
4. **Use `pg_dump --no-owner --no-acl` for cross-cluster exports** — this avoids transferring ownership and ACL dependencies that may not exist in the target cluster.
5. **Schedule point-in-time recovery tests quarterly** — the skill can generate a recovery plan; the owner should test a PITR restore on a staging cluster at least once per quarter.

## Risks / owner notes
The most common data loss scenario is using pg_resetwal without a recent backup, or importing large CSVs in a single command that times out and leaves the database in an inconsistent state. The owner should always follow the batch size recommendations and maintain regular backups. Cross-cluster role and ACL migration requires manual review after the dump/restore; the skill's `--no-owner --no-acl` flags reduce but do not eliminate this need.

## Category / tags
database · data-management, postgres, alloydb, import-export, backup, recovery, bulk-data

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.