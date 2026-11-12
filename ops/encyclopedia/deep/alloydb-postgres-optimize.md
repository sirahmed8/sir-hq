# alloydb-postgres-optimize

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-optimize\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A query optimization skill for PostgreSQL within AlloyDB Omni that analyzes slow queries, suggests index creation, identifies missing statistics, and recommends configuration changes (shared_buffers, work_mem, max_parallel_workers_per_gateway). It runs `EXPLAIN ANALYZE` automatically, captures the plan, and provides a prioritized list of optimizations with expected performance impact, tailored to AlloyDB Omni's architecture.

## When to use / when NOT
Use after deploying an AlloyDB Omni cluster and after observing slow query performance in production. Do NOT apply all optimizations at once — the skill ranks them by impact/effort ratio; apply the top 3 and re-measure. Do NOT ignore the statistics advisor recommendations — missing statistics can cause the planner to choose suboptimal plans; the skill will auto-collect statistics if configured.

## Inputs, outputs, tools
- Inputs: SQL query or workload pattern, current AlloyDB configuration (shared_buffers, work_mem), optional `EXPLAIN ANALYZE` output.
- Outputs: optimized query with revised SQL, suggested index definitions, missing statistics report, configuration change recommendations (with safe values for production), expected performance improvement percentage.
- Tools: `psql`, `EXPLAIN ANALYZE`, `pg_stat_statements`, `pg_stat_advisor`, `pg_tune` for config recommendations. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always run with a representative workload** — optimizing a single query may negatively affect overall throughput; the skill evaluates the full query mix.
2. **Apply index recommendations one at a time** — adding multiple indexes simultaneously can cause write performance degradation; the skill tracks the impact of each addition.
3. **Review the statistics advisor output before auto-collecting** — some tables may have already been analyzed; redundant statistics collection wastes resources.
4. **Use the recommended shared_buffers values as a starting point** — the skill calculates values based on available system memory; do not set shared_buffers higher than 40% of RAM on a dedicated database server.
5. **Re-run optimization after any schema change** — adding or dropping tables, columns, or indexes changes the planner's decisions; the skill will flag when re-optimization is needed.

## Risks / owner notes
Over-indexing can degrade write performance (each insert/update/delete must maintain the index). The owner should monitor write throughput after applying each index recommendation. The skill's configuration recommendations (shared_buffers, work_mem) should be validated in a staging environment before applying to production; aggressive values can cause OOM.

## Category / tags
database · optimization, performance, postgres, alloydb, indexing, query-tuning

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.