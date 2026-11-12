# figma-generate-library

## Summary
The design-system builder skill: create or update Figma libraries (tokens/foundations, single components, full libraries, or reconciliations) that faithfully match a codebase's UI. It is scope-driven — four explicit scopes each with a definition-of-done — and enforces a disciplined state ledger (`/tmp/design-system-state-{RUN_ID}.json`), sequential-only `use_figma` calls, token architecture tiers, and an evidence-based validation cadence. Eight helper scripts cover inspection, variable collections, semantic tokens, variant components, binding, docs pages, validation and cleanup.

## When to use / when NOT
Use for reusable library primitives/foundations — tokens, variables, styles, components, variant matrices, documentation pages, Code Connect — anything meant for publication or reuse. NOT for one-off screens/views (use figma-generate-design) or mapping files alone (figma-code-connect). A narrow request must NOT be silently promoted to a full-library project.

## Inputs, outputs, tools
- Inputs: requested scope + inventory, codebase tokens/components (source of truth), target fileKey, existing Figma conventions.
- Outputs: variable collections/modes/scopes/code-syntax, text/effect styles, component sets with properties/bindings, doc pages, Code Connect mappings (full-library scope), state ledger file.
- Tools: `use_figma` (with mandatory figma-use companion), `get_libraries`, `search_design_system`, figma.variables/style APIs, helper scripts in scripts/ (inspectFileStructure, createVariableCollection, createSemanticTokens, createComponentWithVariants, bindVariablesToComponent, createDocumentationPage, validateCreation, cleanupOrphans); 8 reference docs.

## 5 most important rules
1. Lock scope and acceptance checks BEFORE first mutation; communicate proportionally and stop when the scope's definition-of-done passes — no speculative extra work.
2. Foundations before dependents; inspect existing conventions first; every variable gets explicit scopes (never ALL_SCOPES) and WEB code syntax wrapped as `var(--name)`; semantic layer aliases primitives, never duplicates raw values.
3. Components: bind visual properties to variables by default, INSTANCE_SWAP for icons (never variant-per-icon), cap variant matrices at ~30 (split beyond), position variants after combineAsVariants (they stack at 0,0), deterministic naming, idempotent name+ledger-ID existence checks — never duplicate.
4. Execution discipline: `use_figma` calls are strictly sequential (never parallel), page context resets each call (setCurrentPageAsync once per call, split multi-page work), never hallucinate node IDs (read from state ledger), never parallelize, return ALL created IDs every call, and write the state ledger to disk since conversation truncates.
5. Reuse decision: local existing → subscribed library → unsubscribed UI kit → create new; wrap when visual match but API incompatible; ask the user on genuine code-vs-Figma or close-match forks — never silently default, never build on rejected work.

## Risks / owner needs
Mutates a real Figma file (possibly a published library others consume); wrong scope or naming pollutes the system. Code Connect and full QA are Org-plan territory. Requires Figma MCP auth.

## Category and tags
Category: design. Tags: figma, design-system, tokens, components, library, mcp, variants.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
