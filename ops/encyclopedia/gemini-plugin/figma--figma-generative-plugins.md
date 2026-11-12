# figma-generative-plugins

## Summary
Workflow for creating and updating account-library "generative plugins" in Figma via MCP tools (`create_generative_plugin`, `get_generative_plugin`, `update_generative_plugin`). A plugin is `code.ts` (plugin logic with `figma.showUI(__html__)`) plus `ui.html` (controls); the create call only produces a square-drawing scaffold that MUST then be replaced with the real authored files. Deep authoring rules (PropsKit controls, fonts, relaunch, bounded work, geometry, API gotchas) live in references/authoring.md.

## When to use / when NOT
Use before every `create_generative_plugin` or `update_generative_plugin` call. Plugins run in the Figma Design editor and must have functional UI even with no configurable inputs. Do NOT use for one-off canvas edits (that is `use_figma` / figma-use), and never embed secrets — plugin source is readable by anyone with access.

## Inputs, outputs, tools
- Inputs: requested workflow and controls, planKey (user-supplied or via `whoami`), plugin id for updates.
- Outputs: a plugin with name/description/version; completion requires a "try in new file" URL `figma.com/file/new?try-tool-resource-content-id=<id>&try-tool-resource-type=gen_tool&type=design&mode=design` plus an offer to open it in an existing file.
- Tools: Figma MCP `whoami`, `create_generative_plugin`, `get_generative_plugin`, `list_generative_plugins`, `update_generative_plugin` (replaces `code.ts`/`ui.html` only — cannot touch `manifest.json` or add files); reference doc references/authoring.md.

## 5 most important rules
1. Never stop after `create_generative_plugin` — the scaffold is not the deliverable; read every returned source URI, then replace with complete authored files.
2. `update_generative_plugin` takes complete file replacements (not diffs); unspecified files are preserved, and `manifest.json` can never be replaced.
3. Every plugin needs a clear primary action and validation/status feedback; avoid destructive canvas changes unless that is the explicit purpose.
4. On a build error, make the smallest correction from compiler output and retry once, then surface the error — do not rewrite blindly.
5. A non-error update result is success (version may be omitted); report name, id, version and the try-in-Figma link, then ask about opening in an existing file.

## Risks / owner needs
Needs a Figma plan seat for plugin creation; source is visible to file collaborators so no secrets/tokens/OAuth in code — for authenticated integrations stop and propose static data or a public endpoint instead.

## Category and tags
Category: design. Tags: figma, mcp, plugins, generative, ui-authoring.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
