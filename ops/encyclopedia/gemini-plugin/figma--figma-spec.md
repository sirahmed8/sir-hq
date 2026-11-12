# figma-spec

## Summary
Guide for working with native Figma specs — GitHub-Flavored Markdown documents living under `SPEC_BLOCK` nodes, accessed through `figma.spec.*` plugin-API methods inside `use_figma`. A standalone spec file holds one spec; Design/FigJam files can embed several. Covers discovery (resolve `SPEC_BLOCK`/`DOCUMENT` nodes by URL node-id or page search), creation on canvas, and three content operations: `getContent` (read `markdown`), `setContent` (destructive full replace), `editContent` (surgical find/replace), plus anchored comments via `figma.spec.comments.*`.

## When to use / when NOT
Use for reading, creating, reviewing or commenting on Figma specs. HARD GATE: must call `whoami` first and confirm the target file's plan has `specs_enabled: true`; if unclear which plan owns a file, ask — never infer from the file key. If specs are unavailable, stop the workflow. Do NOT edit ordinary canvas text nodes as a fallback.

## Inputs, outputs, tools
- Inputs: spec node id (from URL or discovery), markdown content/edits, comment anchor text.
- Outputs: verified markdown reads, applied edits/comments; every write is verified by re-reading `getContent`.
- Tools: `whoami`, `figma.getNodeByIdAsync`, `findAllWithCriteria`, `page.loadAsync`, `figma.spec.createOnCanvasAsync/getContent/setContent/editContent`, `figma.spec.comments.create/getThread/reply` — all inside `use_figma`.

## 5 most important rules
1. Confirm `specs_enabled` via `whoami` before any spec API; resolve the DOCUMENT-type SPEC_BLOCK root and pass its id to every call (omitting throws when multiple specs exist).
2. Default to surgical `editContent` — each `oldText` must match exactly once (add context to disambiguate); `setContent` only for empty drafts or explicit full replacement.
3. Pass markdown as plain strings — never base64/Buffer for text (base64 only for image data URLs); keep markdown and node traversal strictly separate.
4. Preserve `[comment:<uuid>]…[/comment:<uuid>]` marker pairs around the same text or threads detach; verify every write by re-reading getContent, never by screenshots.
5. Comments need `anchorText` matching rendered text exactly once (use `contextText` for repeats) and replies must use the root comment UUID, never a reply's.

## Risks / owner needs
Plan-gated feature (`specs_enabled`); wrong-plan inference is explicitly banned. Shared specs must use portable links (GitHub permalinks), never localhost paths.

## Category and tags
Category: design. Tags: figma, specs, markdown, mcp, documentation, comments.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
