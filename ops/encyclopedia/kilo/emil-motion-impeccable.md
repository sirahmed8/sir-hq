# emil-motion-impeccable

## Summary
Combines Emil Kowalski's spring-physics motion doctrine with the Impeccable 23-heuristic design system. Motion rules: ban linear `ease` transitions, use spring tokens (micro: stiffness 400/damping 30/mass 0.8 <180ms; layout morphing: 300/28/1.0 <300ms), `active:scale-[0.98]` press feedback, 30–50ms stagger on mount, shared-layout morphing between trigger and expanded card. Design rules: fluid `clamp()` typography, 1–2px optical icon alignment, strict 4/8px spacing tokens, heading/body line-height proportions, `text-wrap: balance/pretty`.

## When to use / when NOT
Use when adding animations, micro-interactions, drawers/modals, or doing visual polish passes. Do NOT use for information architecture or UX flow (cognitive-product-intuition) or for non-UI code.

## Inputs, outputs, tools
- Inputs: the UI components/pages being polished.
- Outputs: spring-based transitions, staggered mounts, layout morphs, typography/spacing fixes.
- Tools: examples assume Framer Motion / Motion One / Tailwind; CSS `clamp()`, `text-wrap` are native.

## 5 most important rules
1. Replace linear ease transitions with spring physics tuned to the interaction size.
2. Press feedback `scale-[0.98]` on all tactile controls; responses under ~180ms for micro-interactions.
3. Stagger mounted items 30–50ms; never pop everything at once.
4. Spacing only from the 4/8px token scale — no arbitrary px.
5. Fluid type via `clamp()`, `text-wrap: balance` on headings, `pretty` on paragraphs.

## Risks / things needing the owner
Spring-heavy UIs can jank on low-end devices — keep animations transform/opacity-based. Reduced-motion preferences should be respected (skill doesn't mention it; implementer should add `prefers-reduced-motion`).

## Category / tags
design · motion, springs, ui-polish, typography, micro-interactions

## Revisions
Six tools hold it; bodies byte-identical, only `description` differs. Claude copy preferred for trigger-style description.
