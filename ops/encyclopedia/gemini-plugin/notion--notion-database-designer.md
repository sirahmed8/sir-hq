# notion-database-designer

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-database-designer\SKILL.md (+ reference/schema-migrations.md, examples/)

## Summary
Designs and builds Notion trackers from scattered notes or described workflows — request queues, content calendars, team trackers. It inspects existing databases first, chooses properties and views around the actual decisions people need to make, migrates data safely when schemas change, and verifies that the tracker answers the original questions.

## When to use / not use
Use for "set up a tracker" or "make this tracker easier to follow" requests, including converting notes into records. Not for routine record updates inside an existing tracker, and not when the user only wants design advice — a design request produces a proposal, not a database.

## Inputs, outputs, dependencies
Input: notes/lists/links or a described workflow; optional existing database to improve. Output: a Notion database (or improved schema/views) with populated records and verified filters. Needs Notion MCP tools; loads schema-migrations.md before changing property types or moving records.

## Key rules
1. One coherent entity per data source; typed properties only for values reused in filtering/sorting/grouping — narrative stays in page bodies.
2. Link to records owned by another database via relations; never copy an independent version.
3. Views organize, they do not secure: a filtered view is not an access boundary.
4. Cost discipline: plan the whole build before the first write, skip unneeded searches/access checks, batch rows sharing a parent, and embed working views inline via `parent_page_id` rather than leaving only database links.
5. Migration safety: check for matching records before importing notes (no duplicates from repeated mentions), keep unknown owners/dates unset, label suggestions vs commitments, preserve source notes, and read schema-migrations.md before type changes.

## Risks / owner items
- Formulas, rollups, templates, and view types vary by connection — describe manual steps for unsupported features instead of claiming they exist.
- No write access → return a usable design and state what remains unbuilt; never work around a denied write.

## Category and tags
ops, build — notion, database, tracker, schema-design, migration, mcp.

## Revision note
Single plugin revision; notable for its explicit "few tool calls" latency guidance unique among the Notion skills.
