# cloud-sql-postgres-vectorassist

## Summary
Google-published skill for standing up pgvector workloads on Cloud SQL PostgreSQL through intent capture: `define_spec` turns a description of the vector-search workload (table, columns, dimensionality, embedding model, prefilter columns, expected vector count) into an ordered set of SQL recommendations; `modify_spec` revises a spec; `apply_spec` executes the recommendations in sequence; `generate_query` produces optimized similarity-search SQL (top_k, filters, target recall, iterative index search); `execute_sql` runs statements.

## When to use / when NOT
Use for "set up vector search on this table", "generate the embedding/index SQL", "write the similarity query". Do NOT use for generic schema work (postgres-data) or performance monitoring. It presumes the pgvector extension and an embedding pipeline exist or will be created by the spec.

## Inputs, outputs, tools
- Inputs: spec params — `table_name` (required for define), `schema_name`, `vector_column_name`, `text_column_name`, `vector_index_type`, `embeddings_available`, `num_vectors`, `dimensionality`, `embedding_model`, `prefilter_column_names`; for queries: `search_text`/`search_vector`, `top_k`, `filter_expressions`, `target_recall`, `iterative_index_search`; `spec_id` links the steps.
- Outputs: ordered SQL recommendation sets, generated search queries, execution results.
- Tools: `scripts/{define_spec,modify_spec,apply_spec,generate_query,execute_sql}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. Follow the pipeline order: define_spec → review recommendations → modify_spec if needed → apply_spec → generate_query → execute_sql.
2. apply_spec runs real DDL/DML in sequence against the database — only after the user has reviewed the generated recommendations.
3. Unspecified optional spec params fall back to internal workload-optimized defaults — state assumptions when reporting the spec.
4. `spec_id` is the thread connecting all steps; keep it consistent.
5. `project` is pre-configured; never ask unless the user names another.

## Risks / things needing the owner
apply_spec provisions indexes/tables that cost storage and can lock tables; embedding choices (model, dimensionality) are hard to reverse. execute_sql is write-capable. Requires pgvector-capable instance + credentials.

## Category / tags
cloud · gcp, cloud-sql, postgres, vector-search, pgvector, ai

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-vectorassist\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
