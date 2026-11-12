# discovering-gcp-data-assets

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\discovering-gcp-data-assets\SKILL.md`
- SKILL.md size: 9919 chars

## What it does

| Finds and inspects data assets within Google Cloud. Relevant when any of the following conditions are true: 1. The user request involves finding, exploring, or inspecting data assets in Google Cloud, such as: - BigQuery datasets, tables, or views - BigLake catalog or tables - Spanner instances, databases or tables - etc. 2. You need to retrieve the schema, metadata, or governance policies for a GCP data asset. 3. You have a keyword or topic (e.g., "sales data") but lack the specific table or resource ID. 4. You are attempting to find data using `bq ls`, as this skill offers a superior approach. Don't use when: - Assets are outside Google Cloud

## When to use (from skill text)

- Use this when the user describes the **meaning** or **intent** of the data
- Use this for exact keyword matches or technical strings (e.g., `name:order_v2`).

## Structure (headings inside SKILL.md)

- Instructions
- Step 1: Prioritize Assets from the Conversation
- Step 2: Handle Public Datasets or Proceed to Search
- Step 3: Execute Discovery Search
- A. Semantic Search (Natural Language Intent)
- B. Keyword Search (Technical Strings)
- Step 4: Lookup Context
- Command Execution
- Troubleshooting
- Context Lookup Fails or "Resource not found"
- Search Returns No Results
- Context Lookup Fails with "NOT_FOUND" (despite correct format)
- Breaking the Research Loop
- Search Fails with "--project: Must be specified."
- Search Fails with "PERMISSION_DENIED"
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tools, MCP tool

## Risks / cautions found in text

- -   **Exact vs. Token Match**:
- -   Use `:` for token/substring matches (e.g., `name:sales`).
- -   **`name:x`**: Substring/token match on resource ID.
- -   **`displayname:x`**: Substring/token match on display name.

## Key rules (verbatim lines from SKILL.md)

1. -   **Semantic Search**: Logical operators (`AND`, `OR`) MUST be
2. -   Use `=` for exact matches. REQUIRED for `system`, `type`, and
3. -   **Singular Keywords**: When performing keyword search, ALWAYS convert
4. -   **`createtime[>|<|=]x`**: Match assets created after/before date

## Files inside the skill

- (SKILL.md only)
