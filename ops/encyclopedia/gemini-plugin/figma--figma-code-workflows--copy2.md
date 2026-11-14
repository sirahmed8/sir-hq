# figma-code-workflows (import a project into Figma)

## Summary
An Figma MCP workflow that imports a local running app or static HTML project into Figma — either as editable Design layers or as a runnable Code Layer / standalone Code (Make) output. It is essentially a routing skill: first resolve WHAT output the user wants (and never guess — ask "editable design layers or a code layer?" and end the turn), then pick the tool (`generate_figma_design`, `html_to_figma`, or `send_code_to_figma`) and follow each response's `nextStep` instructions exactly through preparation, validation, upload and import completion.

## When to use / when NOT
Use only for an explicitly requested Figma output or a given Figma file link as destination; generic "make a code project" requests do NOT trigger it. Static HTML or a running app are the inputs. Do NOT use it to decide output intent yourself — ambiguity must be resolved by asking the user once.

## Inputs, outputs, tools
- Inputs: local project (running app or self-contained static HTML), optional destination file URL/link, user's plan choice for new files.
- Outputs: a Figma Design file with layers, or a Code Layer / standalone Code import; final file/layer link plus honest report of import and preview outcomes.
- Tools: Figma MCP tools `whoami` (checks `code_layers_enabled`), `create_new_file`, `send_code_to_figma`, plus `generate_figma_design` / `html_to_figma` for the editable-layers path (handled by sibling skills).

## 5 most important rules
1. Output intent is mandatory: if unclear, ask "Editable design layers or a code layer?" and STOP — a Design link chooses destination, not output.
2. Check `whoami.code_layers_enabled` before choosing a runnable destination; fall back to standalone Code/Make or explain the limit.
3. Screen-count heuristic only when no explicit choice: fewer than 10 screens (or unknown) → Code Layer in a Design file; 10+ → standalone; never ask the user to count.
4. Follow each tool response's `nextStep` verbatim, pass continuation arguments unchanged, and never invent recovery steps; report pending imports as pending.
5. Keep the user updated at each stage (preparing/validating, uploading, completing) and finish only with the returned link and confirmed outcomes.

## Risks / owner needs
Requires an authenticated Figma MCP connection and a plan that permits file creation; code-layer availability depends on account flags. Uploads project source to Figma — confirm no secrets in the bundle before sending.

## Category and tags
Category: design. Tags: figma, mcp, import, code-layer, design-to-code, workflow.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
