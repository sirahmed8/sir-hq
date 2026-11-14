# gdocs

## Summary
gdocs is a Google-published skill for creating, editing, and managing Google Docs documents via the `gdrive` CLI or programmatically. It supports read-only access (viewing content) and write operations (creating new docs, appending text, inserting tables, formatting). The skill handles document lifecycle: create new documents with optional initial content, read existing doc content, insert content at cursor position or append, add tables with specified rows/columns, replace placeholder text with structured data, and export to Markdown or PDF. All operations require a known document ID or title search.

## When to use / when NOT
Use when users need to create or edit Google Docs, add tables, replace placeholders, or export docs. Do NOT use for non-Google-Doc document types, for creating large documents without structure, or for document types better suited to other tools (Slides for presentations, Sheets for tabular data).

## Inputs, outputs, tools
- Inputs: Document ID, operation type (create, read, insert, append, table, replace, export), content to insert, table dimensions, export format.
- Outputs: Document content (text), newly created doc ID, export file path, table data confirmation.
- Tools: `gdrive` CLI (doc create, doc open, doc append, doc insert table, doc replace text, doc export), `gdrive` search by title. No scripts folder.

## 5 most important rules
1. Always ask for document ID when user references an existing doc; use `gdrive` search to find by title if ID unknown.
2. Insert content using `{{PLACEHOLDER}}` pattern replacement rather than raw appending for structured docs.
3. Tables: specify rows and columns; never assume default dimensions.
4. Export: ask user preferred format (markdown vs pdf); markdown preserves structure better.
5. Never expose or log document content beyond what's needed for the operation.

## Risks / things needing the owner
Document access requires appropriate Google Drive permissions (reader/writer). Large documents may have paragraph limits. Export format choice affects downstream consumers. No direct owner actions (sign-in, payment) but user must confirm doc operations.

## Category / tags
google · docs, document-editing, text-replacement, tables, export, markdown, pdf

## Revisions
Single revision in `C:\Users\a7med\.config\kilo\skills\gdocs\SKILL.md` (Google-published, Apache-2.0, v1). Only kilo has this skill; scripts/references folders exist (scripts=True, refs=True per earlier check).