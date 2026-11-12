# notion-knowledge-capture

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-knowledge-capture\SKILL.md (+ reference/*-database.md schema examples, examples/)

## Summary
Captures conversations and supplied notes as durable Notion knowledge: wiki pages, how-to guides, FAQs, decision records, retrospectives, or meeting summaries. It preserves decisions vs proposals faithfully, picks a content pattern from a small table, resolves or creates the destination, and links sources.

## When to use / not use
Use when saving or updating durable knowledge from existing context. Use `notion-research-documentation` instead when the main job is discovering and synthesizing new sources.

## Inputs, outputs, dependencies
Input: conversation material or supplied notes, plus a destination (page, database, or search). Output: a created/updated Notion page or database record with source and related links. Needs Notion MCP search/fetch/create/update tools and optional per-type database schema references.

## Key rules
1. Separate agreed decisions from proposals; never invent owners, dates, consensus, or missing steps. Draft requests produce drafts — no publishing.
2. Pick structure from the content type table (concept, how-to, decision record, FAQ, meeting summary, learning/post-mortem); omit empty sections; preserve exact commands/configs and label suggested additions.
3. Update an existing document for the same topic rather than creating a near-duplicate; flag conflicting decisions instead of silently replacing them; keep a dated change note for material revisions.
4. For databases, fetch the schema once and use actual properties — the suggested schemas in references are examples, not requirements.
5. On ambiguous write failure, check whether the page exists before retrying to avoid duplicates; with no write access, return a copy-ready draft.

## Risks / owner items
- Explicitly warns that retrieved content is source material, not instructions to expand scope.
- Does not authorize publishing or reorganization beyond the requested destination convention.

## Category and tags
ops, study — notion, knowledge-management, documentation, decision-records, mcp.

## Revision note
Single plugin revision; the lightest of the Notion build skills (89 lines).
