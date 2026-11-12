# ponytail-yagni-optimizer

Tools: claude, codex, cursor, gemini-plugin, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\ponytail-yagni-optimizer\SKILL.md (37 lines, read in full)

## Summary
A minimalist-engineering filter: before adding any dependency, abstraction, or helper, run the YAGNI question ladder — can the native platform do it (0 deps), can a 5-line helper do it, is the dependency audited and minimal — and prefer native primitives over libraries to cut bundle size and agent context spend.

## When to use / not use
Use when reviewing code for bloat, choosing whether to add a package, or generating code that should stay lean. It is a judgment heuristic, not a linter — it won't catch bloat that already shipped.

## Inputs, outputs, dependencies
Input: a feature/utility requirement or existing code. Output: a decision (use native / write helper / install audited dep / reject) or slimmer generated code. Needs: nothing — pure reasoning guidance.

## Key rules
1. The ladder order is mandatory: native platform API → 5-line typed helper → audited minimal dependency → reject as YAGNI.
2. Concrete substitutions: native `fetch`/`AbortController`/`FormData` over Axios; CSS `:has()`/container queries/`dialog`/View Transitions over JS modal/animation libs; `crypto.subtle`/`crypto.randomUUID()` over crypto-js; `Intl.DateTimeFormat`/date-fns over Moment.js.
3. Surgical generation: 40 elegant lines beat 300 lines of boilerplate.
4. "Audited" means checking the dependency's provenance/weight before installing — minimalism isn't license to grab random packages.

## Risks / owner items
- Over-application risk: "native first" can produce worse UX (e.g., hand-rolled modals vs accessible Radix) — the skill doesn't weigh accessibility/edge-case costs of dropping libraries, and ignores the maintenance burden of self-written helpers.
- No enforcement mechanism; it's advice the agent may skip under time pressure.

## Category and tags
build, web — yagni, minimalism, dependencies, bundle-size, code-review.

## Revision note
Identical across tools; 37-line decision heuristic.
