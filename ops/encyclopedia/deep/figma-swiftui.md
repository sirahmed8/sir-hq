# figma-swiftui

## Summary
A router skill for bidirectional translation between Figma designs and SwiftUI code. It holds only the direction table and shared doctrine; actual procedures live in references/design-to-code.md and references/code-to-design.md. Design→code uses `get_design_context` with `clientLanguages: "swift"`/`clientFrameworks: "swiftui"`; code→design uses `use_figma` (plus figma-use, figma-generate-design, figma-generate-library as needed).

## When to use / when NOT
Use when translating a Figma frame into SwiftUI for an iOS project, or pushing SwiftUI views/screens/tokens into Figma. If the request is ambiguous (both a Figma URL and .swift files present, no clear verb), ask which direction before loading a reference.

## Inputs, outputs, tools
- Inputs: Figma file/frame URL (fileKey + nodeId, `-`→`:`) or SwiftUI source; target iOS project or Figma file.
- Outputs: SwiftUI code matching the design, or Figma nodes/variables built from code.
- Tools: Figma MCP `get_design_context`, `use_figma`, `figma.util.getSfSymbolCharacter`; sibling skills figma-use, figma-generate-design, figma-generate-library.

## 5 most important rules
1. The React+Tailwind in `get_design_context` output is a structural approximation, never literal source — do not transliterate absolute positioning or blend-mode stacks into SwiftUI or Figma; the screenshot is truth in both directions.
2. iOS HIG semantic colors are tokens: `var(--backgrounds/primary)` etc. map to `Color(.systemBackground)`/`.secondary`/`Color(.separator)` and Figma semantic variables — keep the mapping, drop literal RGBA.
3. SF Symbols round-trip by NAME only, never codepoints: use the `<SFSymbol>` names verbatim design→code, and `figma.util.getSfSymbolCharacter(name)` code→design.
4. Recognize system patterns, not node names: nav stack chrome = NavigationStack, bottom icon+label row = TabView, repeated same-height rows = List.
5. Branch URLs use `branchKey` as the fileKey argument; ambiguous direction = ask before loading references.

## Risks / owner needs
Requires Figma MCP access and (for code→design) a writable Figma file/plan. iOS semantics mean generated SwiftUI still needs Xcode-side compilation checks.

## Category and tags
Category: mobile. Tags: swiftui, ios, figma, design-to-code, code-to-design, sf-symbols.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
