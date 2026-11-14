# bigquery-graph-author

- Tool: `gemini-config`
- Category: security
- Source: `C:\Users\a7med\.gemini\config\skills\bigquery-graph-author\SKILL.md`
- SKILL.md size: 10817 chars

## What it does

Provides an end-to-end journey for authoring a BigQuery property graph from your tables or from a model document/diagram (an ER diagram, an ontology, a semantic model): dataset discovery, candidate relationships verified against the data, a readable plan, and `CREATE PROPERTY GRAPH` DDL with schema best practices and semantic measures/dimensions, plus an opt-in verification suite for the landed graph. Use when creating or replacing a property graph, authoring a graph from a dataset or a document, or verifying relationships or suspicious edge counts. Don''t use for querying an existing graph, for non-BigQuery graph databases, or for drawing/rendering diagrams.'

## Structure (headings inside SKILL.md)

- Authoring a BigQuery Property Graph — the Journey
- The journey (one trunk, every request)
- Plan-to-execute operating notes
- Non-negotiable rules

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   **One statement per execution.** Never append anything after a semicolon.
2. -   **Never invent a schema, a job-history result, or a catalog result.** If
3. -   **Never present an untested inference as a design, and never present a
4. -   **Announce each data source before you read it, and the announcement is a

## Files inside the skill

- `OWNERS`
- `references/data-discovery.md` — "Data discovery — the discovery station, data side"
- `references/ddl/best-practices.md` — "BigQuery Graph Schema Best Practices"
- `references/ddl/ddl-advisor.md` — "BigQuery Graph Schema Advisor"
- `references/ddl/ddl-reference.md` — "BigQuery Property Graph DDL Reference"
- `references/ddl/feature-parity.md` — "BigQuery Graph Limitations & Feature Parity"
- `references/document-source.md` — "Document sources — the user brings a description of their model"
- `references/graph-verification.md` — "Graph Verification"
- `references/relationship-verification.md` — "Relationship verification — the relationship-verification station"
- `references/semantic-enrichment.md` — "Semantic Enrichment — decided in the plan, landed in the first DDL"
