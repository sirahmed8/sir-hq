# figma-swiftui

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-swiftui\SKILL.md`
- SKILL.md size: 3438 chars

## What it does

Bi-directional translation between SwiftUI.

## When to use (from skill text)

- | Direction | Trigger | Reference |

## Structure (headings inside SKILL.md)

- Figma ↔ SwiftUI
- Pick the direction
- Shared context (applies to both directions)
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. **iOS HIG semantic colors are tokens, not hex.** `var(--backgrounds/primary, …)`, `var(--labels/secondary, …)`, `var(--separators/non-opaque, …)` etc. map to `Color(.systemBackground)`, `Color.secondary`, `Color(.separator)` in SwiftUI, and to variables in a semantic collection in Figma. Keep the

## Key rules (verbatim lines from SKILL.md)

1. 2. **The React+Tailwind in `get_design_context` output is a structural reference, not a literal source.** It approximates the visual. Never transliterate `position: absolute` / pixel frames / `mix-blend-mode` stacks into SwiftUI or into Figma — the screenshot is the source of truth in both direction
2. 6. **For code → design, `use_figma` is the API.** Always load [`figma-use`](../figma-use/SKILL.md) before any `use_figma` call. If the task involves building a full screen, also load [`figma-generate-design`](../figma-generate-design/SKILL.md); if it involves building components or a design system, 

## Files inside the skill

- `references/code-to-design.md` — "SwiftUI → Figma (code → design)"
- `references/design-to-code.md` — "Figma → SwiftUI (design → code)"
