# alloydb-postgres-health

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-health\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A health monitoring skill specifically for the PostgreSQL layer within AlloyDB Omni. It checks PostgreSQL-level metrics such as deadlock detection, WAL growth, buffer cache hit ratio, and concurrent transaction limits. The skill integrates with the broader AlloyDB health framework and can generate PostgreSQL-specific alerts that feed into the overall AlloyDB Omni monitoring dashboards.

## When to use / when NOT
Use for deep PostgreSQL-level health investigation when AlloyDB-level metrics are insufficient. Do NOT ignore PostgreSQL-specific warnings (e.g., too many deadlocks, WAL disk full) — these can cause transaction failures and data corruption if left unaddressed. Do NOT run this skill simultaneously with the general alloydb-omni-health skill on the same cluster, as they may conflict on metric collection intervals.

## Inputs, outputs, tools
- Inputs: PostgreSQL connection string, alert thresholds (deadlock count, WAL growth rate, cache hit ratio), check interval.
- Outputs: PostgreSQL health status, deadlock report, WAL growth metrics, cache hit ratio, long-running transaction list, recommended actions.
- Tools: `psql`, `pg_stat_activity`, `pg_stat_wal`, `pg_stat_bgwriter`, `deadlock detection` queries, `pglogminer` (for WAL analysis). MCP: gemini-plugin connector.

## 5 most important rules
1. **Always investigate deadlock warnings immediately** — the skill detects deadlock candidates; the owner must choose which transaction to abort and ensure application code handles deadlocks gracefully.
2. **Monitor WAL growth rate** — if WAL is growing faster than it is being archived, the skill will flag it as a critical risk; increase archive_command frequency or expand WAL disk capacity.
3. **Set a cache hit ratio alert at 95%** — below this threshold, the buffer cache is not effective and query performance will suffer; the skill recommends increasing shared_buffers or optimizing queries.
4. **Track long-running transactions** — any transaction running longer than 5 minutes should be reviewed; the skill can generate a KILL script with safety checks.
5. **Do not run VACUUM during peak hours** — the skill will suggest optimal VACUUM windows based on connection patterns; running VACUUM during high usage can cause performance degradation.

## Risks / owner notes
Deadlocks are often a symptom of application-level locking issues; the skill can detect them but cannot fix the root cause in application code. The owner should work with developers to ensure transactions are kept short and that deadlock handling is implemented. WAL full conditions can cause the database to shut down; the skill's early warning on growth rate helps prevent this.

## Category / tags
database · health, postgres, alloydb, monitoring, deadlock, wal, performance

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.