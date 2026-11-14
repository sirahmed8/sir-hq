# bigtable-basics

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\bigtable-basics\SKILL.md`
- SKILL.md size: 5225 chars

## What it does

>- Provisions instances and tables, designs performant schemas, and queries data in Bigtable. Use when designing Bigtable row keys, configuring column families, writing SQL queries or client library code (Java, Go, Python) for Bigtable, or diagnosing performance/hotspotting issues. Also use when provisioning Bigtable clusters using gcloud or cbt CLIs. Don't use for generic Cloud SQL administration.

## Structure (headings inside SKILL.md)

- Bigtable Basics
- Core Principles
- Quick Recipes
- 1. Querying Data
- 2. Manipulating Data
- 3. Data Model Definition (DDL)
- Reference Guides
- Common Workflows
- Schema Evolution (DevOps)
- External Resources
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **Client Selection:** For production use cases, prefer **Java** or **Go**
- 1.  **Prefer Terraform** for production schema changes to prevent accidental

## Key rules (verbatim lines from SKILL.md)

1. -   **Observability:** When diagnosing performance or hotspotting, **always**
2. 2.  For manual `cbt` changes, first check the existing state by listing the table's column families and GC policies before proposing any modifications:

## Files inside the skill

- `assets/row_key_schema.yaml`
- `references/client_libraries.md` — "Bigtable Client Library User Guide"
- `references/cli_data_access.md` — "Bigtable CLI Data Access"
- `references/dataplex.md` — "Dataplex Catalog Search for Bigtable"
- `references/infrastructure_management.md` — "Bigtable Infrastructure and Administration"
- `references/schema_design.md` — "Bigtable Schema Design Guide for Agents"
- `references/sql_guide.md` — "Bigtable SQL Guide for Agents"
