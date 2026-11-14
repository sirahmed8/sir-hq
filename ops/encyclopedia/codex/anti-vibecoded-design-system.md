# anti-vibecoded-design-system

Source read: `C:\Users\a7med\.claude\skills\anti-vibecoded-design-system\SKILL.md` (claude revision; not found in codex/kilo/cursor/windsurf/opencode).

## Summary
A design quality gate that eliminates low-effort AI aesthetic tropes ("vibe-coded" look) and enforces a bespoke, high-contrast, tactile visual standard. Defines a blacklist of 7 prohibited clichés (purple-blue gradients, gradient headlines, emoji headers, universal pill buttons, 3-icon-box layouts, fake testimonials/metrics, "Made with AI" tags, intrusive micro-gimmicks) and enforces 4 positive standards: 60-30-10 color rule, tactile physics (spring transitions, active scale), true high-contrast dark mode, typographic discipline (Geist/Inter/PJSans + mono, balanced headings, pretty body wrap).

## When to use / when NOT
Use for ANY UI work: new screens, redesigns, component libraries, design system audits. Do NOT skip for "quick" UI tasks — the clichés appear fastest there. Not for backend/API/db tasks.

## Inputs, outputs, tools
- Inputs: a UI task, design spec, or existing code to audit.
- Outputs: compliant UI code (Tailwind/React/HTML/CSS), design tokens, or a marked-up audit with fixes.
- Tools: plain file read/write; references Tailwind v4 tokens, CSS custom properties, spring physics (cubic-bezier(0.16,1,0.3,1)).

## 5 most important rules
1. **Zero tolerance for the blacklist**: No purple-blue gradients, gradient headlines, emoji in headings, universal `rounded-full` buttons, 3-icon-box rows, fake social proof, AI badges, or scroll-hijacking gimmicks.
2. **60-30-10 color rule**: 60% neutral canvas (`bg-background`), 30% structural contrast (`bg-card`, `border-border`), 10% single high-intent accent (`bg-primary`/`text-primary`).
3. **Tactile physics mandatory**: Micro-interactions use `active:scale-[0.98]` and spring transitions under 200ms (`cubic-bezier(0.16,1,0.3,1)`).
4. **True high-contrast dark mode**: WCAG AA/AAA pass; no muddy grey-on-dark-grey.
5. **Typography discipline**: High-signal sans (Geist Sans, Inter, Plus Jakarta Sans) + mono for code/metrics; `text-wrap: balance` headings, `text-wrap: pretty` body.

## Risks / owner notes
None operational. The risk is shipping vibe-coded UI that looks like every other AI prototype. Owner should enforce this on every visible screen.

## Category / tags
design · anti-cliché, design-system, tailwind, dark-mode, typography, motion, wcag, tactile-ui

## Revisions
Only the claude copy exists (2.7 KB). Not in the 112-set. This is the canonical version.