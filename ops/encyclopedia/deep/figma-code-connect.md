# figma-code-connect

## Summary
End-to-end procedure for creating Figma Code Connect template files (`.figma.ts`) that map published Figma components to real code components: parse the Figma URL, discover unmapped components via `get_code_connect_suggestions`, fetch property definitions via `get_context_for_code_connect`, locate the matching code component, then author a parserless template whose default export uses `` figma.code`...` `` with `getString`/`getBoolean`/`getEnum`/`getInstanceSwap`/`getSlot`/`findInstance` extraction and `executeTemplate()` for nested instances.

## When to use / when NOT
Use when given a Figma URL and asked to connect components to code. Prerequisites are strict: Figma MCP connected, components published to a team library, Organization/Enterprise plan, URL must contain `node-id`. Do NOT write `.figma.tsx` or use `figma.connect()` — that parser-based format is a different artifact and is rejected here; leave existing `.figma.tsx` files untouched and add `.figma.ts` alongside.

## Inputs, outputs, tools
- Inputs: Figma URL (fileKey + nodeId, hyphens→colons), target codebase (`figma.config.json` paths/importPaths/include, tsconfig types), optionally a specified code component.
- Outputs: `ComponentName.figma.ts` files beside existing Code Connect files, validated against a checklist.
- Tools: Figma MCP `get_code_connect_suggestions`, `get_context_for_code_connect`; project file reads; references api.md and advanced-patterns.md.

## 5 most important rules
1. Output is ALWAYS `.figma.ts` + `` figma.code`...` `` tagged template — never `.figma.tsx`/`figma.connect()`; the default export needs `example` and `id`, optional `imports`/`metadata`.
2. Map Figma properties exhaustively: every VARIANT value must appear in `getEnum` (unmapped = silent undefined); combine multiple variants into exhaustive conditional branches when output differs; omit properties with no code-prop equivalent — never invent props.
3. Never hardcode slot/children content: resolve INSTANCE_SWAP via `getInstanceSwap`, children via `findInstance`/`findConnectedInstance`/`findText`, always `executeTemplate()`; check `type === 'INSTANCE'` first (finders return truthy ErrorHandle on failure) and skip `hasCodeConnect()` guards.
4. Interpolation wrapping matters: strings quoted, instance/section results in braces, slot sections interpolated as snippet sections, booleans via ternary; never string-concatenate ResultSection[] (`[object Object]`), never `.map().join()`.
5. Prefer `getInstanceSwap` over `findInstance` when a property exists (survives icon swaps); `getSlot` only for SLOT-type properties; `traverseInstances: true` + `path` needed to reach inside nested instances — but only reach in when the parent code component takes the child as a prop.

## Risks / owner needs
Plan-gated (Org/Enterprise only) and requires published components — unpublished selections stop the flow. Wrong mappings silently produce broken snippets; Step 6 self-review is the only gate.

## Category and tags
Category: design. Tags: figma, code-connect, design-to-code, typescript, mcp, component-mapping.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
