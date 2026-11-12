# notion-build-my-engineering-wiki

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-build-my-engineering-wiki\SKILL.md (+ reference/design.md, reference/release-overview-layout.md, examples/webhook-release.md)

## Summary
Builds a populated Notion "engineering home" from technical docs, project context, and connected sources: a wiki or project dashboard with getting-started, architecture, development, and operations sections, optional delivery tracking, and a designed first screen. It is a setup/reorganization skill, not for routine edits.

## When to use / not use
Use for "set up my engineering wiki / project home" requests or reorganizing this domain. Do not use for single record edits, pure research, or when an issue tracker (GitHub/Linear) already owns delivery work — link to it instead of duplicating.

## Inputs, outputs, dependencies
Input: conversation context plus supplied docs/links; optional Notion parent destination. Output: Notion pages/databases with real content, relations, views, and a verified read-back. Needs: Notion MCP tools (search, fetch, create-pages, update-page, notion-page-panel), current tool schemas, and reference/design.md before composing.

## Key rules
1. Start from conversation context; never ask the user to repeat it or design a schema. Bounded discovery only for info that changes structure.
2. Reuse existing pages/databases after inspecting schemas; never replace an established workflow with a template.
3. Separate current implementation, accepted decisions, and proposals; cite code/spec/issue evidence; newer drafts do not auto-supersede accepted decisions.
4. No empty departments: only sections with real material or an explicit next step. Keep secrets out — link to credential instructions, never copy values.
5. Verify by read-back (row coverage, relations, filters, sorts, undated work); disclose when visual appearance was not verified. After uncertain writes, inspect before retrying.

## Risks / owner items
- Creates real Notion content; does not authorize publishing, sharing changes, or code/issue/deploy changes.
- Warns against claiming live sync to external trackers — relations are manual links.
- SQL DDL relation targets need the bare data-source UUID, not the `collection://` prefix.

## Category and tags
ops, build, study — notion, wiki, documentation, knowledge-base, mcp.

## Revision note
Single plugin revision (mtime 2026-11-12); part of the Notion plugin family sharing one boilerplate skeleton.
