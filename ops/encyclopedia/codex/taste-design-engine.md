# taste-design-engine (claude/codex/kilo/cursor/windsurf/opencode copies)

## Summary
taste-design-engine is a SIR-authored design-quality skill with four parts: (1) the "Taste Doctrine", a banned-vs-enforced table of AI-slop patterns (purple-blue gradients, pill-everything, emoji headers, floating AI badges, three identical icon cards, plastic stock photos) against premium alternatives (monochrome canvas with brand accents, purposeful radii, typographic hierarchy, asymmetric layouts); (2) design tokens and geometry — the 60-30-10 color rule, type scale (Geist/Inter/Plus Jakarta + Geist Mono/JetBrains Mono), `text-wrap: balance/pretty`, Emil Kowalski spring motion (`active:scale-[0.98]`, stiffness 400/damping 30, 30-50ms staggers), fluid `clamp()` type and 1-2px optical alignment; (3) a self-audit checklist (WCAG contrast 4.5:1/3:1, 4px/8px spacing grid, one dominant CTA per viewport, 5-state completeness); (4) an image-to-code workflow (analyze spatial grid, extract tokens, recreate with native primitives) and a live browser verification protocol via Chrome DevTools MCP or Playwright (screenshot + console check).

## When to use / when NOT
Use when a UI needs premium visual polish, when auditing a UI against AI-slop patterns, or when replicating a mockup/screenshot into code. Do NOT use it for backend work, for establishing brand-new design systems from scratch (that is modern-ui-ux-design-system), or as a substitute for the premium-code-bar law — it operationalizes part of it.

## Inputs, outputs, tools
- Inputs: an existing UI to audit/polish, or a reference image/mockup to replicate.
- Outputs: audited/polished UI code, token extractions, and browser-verified screenshots.
- Tools: Chrome DevTools MCP (`new_page`, `navigate_page`, `take_screenshot`, `list_console_messages`) or Playwright CLI; Tailwind/React conventions assumed.

## 5 most important rules
1. The banned list is absolute: no neon gradients, no `rounded-full` on standard controls, no emoji headers, no "AI-powered" badges, no identical icon-card rows, no plastic stock imagery.
2. Radii are purposeful: 8-10px controls, 14-16px cards; spacing sticks to the 4/8px grid.
3. Every interactive element gets tactile `active:scale-[0.98]` and sub-200ms spring motion, never linear transitions.
4. Self-audit before declaring done: contrast, spacing grid, single dominant CTA, all 5 states.
5. Never assume the design works without looking: screenshot it and check the console for zero errors.

## Risks / things needing the owner
Verification requires a running dev server and a browser tool; leaked browser processes are a known SIR incident (audio read aloud), so browser rules apply (headless, muted, closed in finally). The skill pushes a specific aesthetic (Geist/Inter, monochrome+accent) that may not fit every brand; the owner picks the brand direction. Nothing else needs the owner.

## Category / tags
design · ui-polish, anti-ai-slop, design-tokens, motion, verification

## Revisions
Six copies exist (claude, codex, kilo, cursor, windsurf, opencode); the claude copy (used here) is representative — copies differ only in frontmatter description wording. Content identical.
