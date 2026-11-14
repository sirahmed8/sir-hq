# bigquery-graph-query

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills\bigquery-graph-query\SKILL.md`
- SKILL.md size: 22016 chars
- Identical content to: `encyclopedia/gemini-plugin/data-agent-kit-plugin--bigquery-graph-query.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/gemini-plugin/data-agent-kit-plugin--bigquery-graph-query.md`. Read that digest for full details.

Description: Provides guidelines and best practices for querying BigQuery property graphs and semantic graphs: native GQL (Graph Query Language) pattern matching, multi-hop and variable-length paths, aggregation, top-N, path extraction, output formatting (graph visualization with TO_JSON vs tabular), GRAPH_TABLE relational SQL integration, and semantic graph querying via the GRAPH_EXPAND TVF with starting-node view selection and AGG() measures. Also covers hybrid semantic search, combining `VECTOR_SEARCH` candidate generation with graph traversal when a node carries an embedding-backed property. Use when querying graph topology, node/edge connections, paths, or semantic measures over an existing BigQuery graph. Don't use for Cypher or non-BigQuery graph databases, or for creating/modifying a graph schema.