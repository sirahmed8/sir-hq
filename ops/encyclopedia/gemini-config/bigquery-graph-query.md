# bigquery-graph-query

- Tool: `gemini-config`
- Category: design
- Source: `C:\Users\a7med\.gemini\config\skills\bigquery-graph-query\SKILL.md`
- SKILL.md size: 22032 chars

## What it does

Provides guidelines and best practices for querying BigQuery property graphs and semantic graphs: native GQL (Graph Query Language) pattern matching, multi-hop and variable-length paths, aggregation, top-N, path extraction, output formatting (graph visualization with TO_JSON vs tabular), GRAPH_TABLE relational SQL integration, and semantic graph querying via the GRAPH_EXPAND TVF with starting-node view selection and AGG() measures. Also covers hybrid semantic search, combining `VECTOR_SEARCH` candidate generation with graph traversal when a node carries an embedding-backed property. Use when querying graph topology, node/edge connections, paths, or semantic measures over an existing BigQuery graph. Don''t use for Cypher or non-BigQuery graph databases, or for creating/modifying a graph schema.'

## When to use (from skill text)

- 4.  **Result Uniqueness**: Use `DISTINCT` in your `RETURN`/`COLUMNS` clause when
- Use when the user wants to see relationships, paths, topology, networks,
- connectivity, or entire entities (nodes/edges) as a whole. **Triggers**:

## Structure (headings inside SKILL.md)

- BigQuery Graph Query Guidelines
- Query Paradigm Decision Guide
- Reference Files (rarely needed — do NOT load for standard queries)
- PART 1: Property Graph Querying (Native GQL)
- Pre-generation Checklist
- Core Directives
- Basic Query Construction
- Aggregation, Grouping, and Top-N (native standalone GQL)
- Existence Checks and Subqueries (essentials)
- Graph Pattern Matching
- Path Extraction Functions
- Output Formatting: Visualization vs. Tabular
- Query Optimization
- PART 2: Semantic Graph Querying (GRAPH_EXPAND TVF)
- 1. Query the Flattened View with `GRAPH_EXPAND`
- 2. Choosing the Starting Node (Avoid Under-counting)
- 3. When No Starting Node Fits — Fall Back to GQL
- 4. Querying Measures with `AGG()`
- 5. Prefer Measures (AGG) over Standard SQL Aggregations
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 2.  **Keyword Escaping**: You **MUST** enforce backticks around any reserved SQL
2. -   `MATCH (a)-[e:Transfers]-(b)`: undirected (any direction) — **avoid**;
3. -   **Limit**: always append `LIMIT 500` unless the user requests a different
4. 3.  **Avoid bidirectional/undirected traversals** (`(a)-[e]-(b)`) — they carry a
5. -   **DO NOT** substitute a different starting node to force a `GRAPH_EXPAND`

## Files inside the skill

- `OWNERS`
- `references/gql-advanced-functions-and-perf.md` — "Advanced Element Functions & Query Optimization"
- `references/gql-subqueries.md` — "GQL Subquery Limitations"
- `references/graph-table-and-sql-integration.md` — "GRAPH_TABLE Syntax and SQL Integration"
- `references/hybrid-vector-graph-search.md` — "Hybrid Semantic + Graph Search"
