# figma-generate-library

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-generate-library\SKILL.md`
- SKILL.md size: 24428 chars

## What it does

Build and update Figma design system.

## Structure (headings inside SKILL.md)

- Design System Builder — Figma MCP Skill
- 1. Scope and Completion Contract
- Definition of done
- Scope changes
- 2. Scoped Workflow
- Tokens / foundations
- Single component or family
- Full library / design system
- Reconciliation / update
- 3. Critical Rules
- 4. State Management (Required for Long Workflows)
- 5. Library Discovery and search_design_system — Reuse Decision Matrix
- 6. Decision Forks
- 7. Naming Conventions
- 8. Token Architecture
- 9. Anti-Patterns
- 10. Reference Docs
- 11. Scripts
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP Skill, MCP resource

## Risks / cautions found in text

- 1. **Discovery:** lock the token and component inventory and print the gap analysis.
- 11. **No destructive cleanup** — cleanup scripts identify nodes by name convention or returned IDs, not by guessing.
- - Token binding model is compatible (uses same or aliasable variables)
- - Token model incompatible (hardcoded values, different variable schema)

## Key rules (verbatim lines from SKILL.md)

1. - The final deliverable covers the locked inventory and is materially faithful to the applicable source of truth, including requested variant/state coverage, required assets, and in-scope review examples.
2. - For component tasks, keep main components and construction assets outside the final review frame, and show the requested states as instances in one compact frame. Before stopping, inspect that frame at normal scale and repair clipped, truncated, low-contrast, empty, misplaced, or detached content.
3. - Required variable scopes, aliases, code syntax, component properties, variants, and bindings are verified.
4. - Replace placeholders when the source provides the required asset; remove temporary instances, test frames, captures, abandoned artifacts, and unrelated stray nodes.
5. 1. Inspect and reuse compatible local or library variables, text styles, and effect styles. Create only the missing foundations required by the component. For source-defined, library-standard, or repeated component roles, create or reuse a shared text or effect style and apply it to every matching c

## Files inside the skill

- `references/code-connect-setup.md` — "Code Connect Setup Reference"
- `references/component-creation.md` — "Component Creation Reference"
- `references/discovery-phase.md` — "Discovery Phase Reference"
- `references/documentation-creation.md` — "Documentation Creation Reference"
- `references/error-recovery.md` — "Error Recovery Reference"
- `references/naming-conventions.md` — "Naming Conventions Reference"
- `references/token-creation.md` — "Token Creation Reference"
- `scripts/bindVariablesToComponent.js`
- `scripts/cleanupOrphans.js`
- `scripts/createComponentWithVariants.js`
- `scripts/createDocumentationPage.js`
- `scripts/createSemanticTokens.js`
- `scripts/createVariableCollection.js`
- `scripts/inspectFileStructure.js`
- `scripts/validateCreation.js`
