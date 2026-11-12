# figma-code-connect

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-code-connect\SKILL.md`
- SKILL.md size: 26772 chars

## What it does

Create and maintain Figma Code Connect.

## When to use (from skill text)

- | Method | Use when |

## Structure (headings inside SKILL.md)

- Code Connect
- Overview
- Prerequisites
- Step 1: Parse the Figma URL
- Step 2: Discover Unmapped Components
- Step 3: Fetch Component Properties
- Step 4: Identify the Code Component
- Step 5: Create the Template File (.figma.ts)
- File location
- Template structure
- Property mapping
- Exhaustive variant handling
- Interpolation in tagged templates
- Finding descendant layers
- Nested configurable instances
- Nested component example
- Conditional props
- Step 6: Validate
- Inline Quick Reference
- `instance.*` Methods
- InstanceHandle Methods
- TextHandle Properties
- SelectorOptions
- Export Structure
- Rules and Pitfalls
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tools, MCP client, MCP tool

## Risks / cautions found in text

- 1. **Never string-concatenate template results.** `executeTemplate().example` is a `ResultSection[]` object, not a string. Using `+` or `.join()` produces `[object Object]`. Always interpolate inside tagged templates: `` figma.code`${snippet1}${snippet2}` ``

## Key rules (verbatim lines from SKILL.md)

1. - **Figma MCP server must be connected** — verify that Figma MCP tools (e.g., `get_code_connect_suggestions`) are available before proceeding. If not, guide the user to enable the Figma MCP server and restart their MCP client.
2. - **Components must be published** — Code Connect only works with components published to a Figma team library. If a component is not published, inform the user and stop.
3. - **Organization or Enterprise plan required** — Code Connect is not available on Free or Professional plans.
4. - **URL must include `node-id`** — the Figma URL must contain the `node-id` query parameter.
5. - **TypeScript types** — for editor autocomplete and type checking in `.figma.ts` files `@figma/code-connect/figma-types` must be added to `types` in `tsconfig.json`:

## Files inside the skill

- `references/advanced-patterns.md` — "Code Connect Examples"
- `references/api.md` — "Code Connect Template API Reference"
