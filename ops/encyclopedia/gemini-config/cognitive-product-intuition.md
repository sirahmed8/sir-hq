# cognitive-product-intuition

## Summary
A UX doctrine skill that stops agents from producing clone-like, high-friction interfaces. It defines two distinct mental models that must never share a layout — linear setup wizards (locked future steps, revisitable past steps, one dominant CTA) vs exploratory manager/inventory dashboards (search, filters, bulk actions, density) — plus a friction checklist (no premature success, destructive confirmations, no dead clicks, no dead ends, single primary CTA).

## When to use / when NOT
Use when reviewing or building wizards, onboarding flows, dashboards, or any UI that "feels off" or templated. Do NOT use as a visual-style guide (colors, spacing — that is emil-motion-impeccable / taste-design-engine) or for backend logic.

## Inputs, outputs, tools
- Inputs: the flow/screens under design or audit.
- Outputs: corrected IA and interaction rules applied to the UI; a friction audit.
- Tools: none — pure reasoning protocol applied while writing markup/components.

## 5 most important rules
1. Never reuse one layout across different mental models; wizard ≠ dashboard.
2. In linear steppers, future steps are strictly locked until prior steps validate; past steps may be revisited with invalidation warnings.
3. Only the active step shows inputs and the primary validation button.
4. No "Done!" while background work (downloads, writes, indexing) still runs.
5. Exactly one primary CTA per viewport; every hover/pointer element must have a real handler; every error state needs Back/Retry/Cancel.

## Risks / things needing the owner
None operational — it shapes UI decisions. Over-applying "locked steppers" to legitimately non-linear flows would be a misuse; the skill itself warns the models differ.

## Category / tags
design · ux, mental-models, wizard, anti-patterns, review

## Revisions
Six tools hold it; bodies are byte-identical — only the `description` frontmatter differs. The claude copy is preferred: its trigger-style description ("Use when a UI or flow feels confusing...") matches how skills are selected, unlike the codex/cursor/kilo/opencode/windsurf one-line summaries.
