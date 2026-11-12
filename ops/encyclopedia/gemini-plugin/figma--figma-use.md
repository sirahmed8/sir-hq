# figma-use

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-use\SKILL.md`
- SKILL.md size: 34163 chars

## What it does

Core protocol for running JavaScript in the.

## When to use (from skill text)

- Before anything, load [plugin-api-standalone.index.md](references/plugin-api-standalone.index.md) to understand what is possible. When you are asked to write plugin API code, use this context to grep [plugin-api-standalone.d.ts](references/plugin-api-standalone.d.ts) for relevant types, methods, and

## Structure (headings inside SKILL.md)

- use_figma — Figma Plugin API Skill
- 1. Critical Rules
- 2. Page Rules (Critical)
- 3. `return` Is Your Output Channel
- 4. Editor Mode
- 5. Efficient APIs — Prefer These Over Verbose Alternatives
- `node.query(selector)` — CSS-like node search
- `node.set(props)` — batch property updates
- `figma.createAutoLayout(direction?, props?)` — auto-layout frames
- `node.placeholder` — shimmer overlay for AI-in-progress feedback
- `await node.screenshot(opts?)` — inline screenshots
- 6. Incremental Workflow (How to Avoid Bugs)
- Key rules
- The pattern
- Suggested step order for complex tasks
- What to validate at each step
- 7. Error Recovery & Self-Correction
- When the script succeeds but the result looks wrong
- 8. Pre-Flight Checklist
- 9. Discover Conventions Before Creating
- Quick inspection scripts
- 10. Reference Docs
- 11. Snippet examples
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP resource, MCP tools

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  **Use `return` to send data back.** The return value is JSON-serialized automatically (objects, arrays, strings, numbers). Do NOT call `figma.closePlugin()` or wrap code in an async IIFE — this is handled for you.
2. 2.  **Write plain JavaScript with top-level `await` and `return`.** Code is automatically wrapped in an async context. Do NOT wrap in `(async () => { ... })()`.
3. 3.  `figma.notify()` **throws "not implemented"** — never use it
4. 10. `setBoundVariableForPaint` returns a **NEW** paint — must capture and reassign
5. 16. **Always set `variable.scopes` explicitly when creating variables.** The default `ALL_SCOPES` pollutes every property picker — almost never what you want. Use specific scopes like `["FRAME_FILL", "SHAPE_FILL"]` for backgrounds, `["TEXT_FILL"]` for text colors, `["GAP"]` for spacing, etc. See [va

## Files inside the skill

- `references/api-reference.md` — "Figma Plugin API Reference"
- `references/common-patterns.md` — "Common Patterns"
- `references/component-patterns.md` — "Component & Variant API Patterns"
- `references/effect-style-patterns.md` — "Effect Style API Patterns"
- `references/gotchas.md` — "Gotchas & Common Mistakes"
- `references/plugin-api-patterns.md` — "Plugin API Patterns"
- `references/plugin-api-standalone.d.ts`
- `references/plugin-api-standalone.index.md` — "Plugin API Index"
- `references/text-style-patterns.md` — "Text Style API Patterns"
- `references/validation-and-recovery.md` — "Validation Workflow & Error Recovery"
- `references/variable-patterns.md` — "Variable & Token API Patterns"
- `references/working-with-design-systems/wwds-components--creating.md` — "Working with design systems: Creating Components"
- `references/working-with-design-systems/wwds-components--using.md` — "Working with design systems: Using Components"
- `references/working-with-design-systems/wwds-components.md` — "Components"
- `references/working-with-design-systems/wwds-effect-styles.md` — "Working with design systems: Effect Styles"
- `references/working-with-design-systems/wwds-text-styles.md` — "Working with design systems: Text Styles"
- `references/working-with-design-systems/wwds-variables--creating.md` — "Working with design systems: Creating Variables"
- `references/working-with-design-systems/wwds-variables--using.md` — "Working with design systems: Using Variables"
- `references/working-with-design-systems/wwds-variables.md` — "Working with design systems: Variables"
- `references/working-with-design-systems/wwds.md` — "Working with design systems"
