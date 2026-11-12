# modern-ui-ux-design-system

Source read: `C:\Users\a7med\.claude\skills\modern-ui-ux-design-system\SKILL.md` (2.1 KB; claude revision; codex/cursor/kilo/opencode/windsurf listed; `references/` has 4 deep guides).

## Summary
UI/UX design-system doctrine with four reference pillars: (1) psychological laws & cognitive ergonomics (Hick's, Fitts's, Miller's, Gestalt — with formulas for decision/movement time and visual hierarchy rules); (2) fluid spring animations & tokens (spring easing curves, curvature hierarchy `--radius: 0.75rem`, CSS `@starting-style` entry transitions, Tailwind v4 + OKLCH); (3) color theory & theming (60-30-10 distribution, OKLCH perceptual lightness, WCAG AAA contrast, zero-FOUC theme switching); (4) complete 5-state UI patterns (idle, shimmer skeleton, empty+CTA, error boundary+retry, partial/overflow — drop-in implementations). Quick rules: curvature hierarchy (cards 16px, controls 8-10px, pills full; inner radius = outer − padding), tactile `active:scale-[0.98]` spring press, high-signal sans (Geist/Inter/Plus Jakarta Sans) + monospace for metrics, `text-wrap: balance/pretty`.

## When to use / when NOT
Use when designing or implementing a design system, theme, or polishing UI states/motion. Not for backend work or for projects with an established different token system (match the codebase first).

## Inputs, outputs, tools
- Inputs: UI surfaces needing tokens, states, motion, or theming.
- Outputs: token values, CSS/Tailwind snippets, 5-state component patterns, theme-switch code.
- Tools: Tailwind CSS v4, OKLCH colors, CSS `@starting-style`, spring easings; references hold templates.

## 5 most important rules
1. Curvature hierarchy: outer radius − padding = inner radius; controls 8-10px, cards 12-16px.
2. Every data view implements all 5 states (idle/loading-skeleton/empty+CTA/error+retry/populated-overflow).
3. Colors in OKLCH for perceptual consistency; 60-30-10 distribution; WCAG AAA contrast; zero-FOUC theme switching.
4. Motion is spring physics on transform/opacity only — `active:scale-[0.98]` tactile press.
5. Typography: signal sans + monospace metrics; `text-wrap: balance` headings, `pretty` body.

## Risks / owner notes
Pairs with anti-vibecoded-design-system and emil-motion-impeccable (overlapping coverage — check for contradictions before mixing). Reference files must be read for actual token values; SKILL.md alone is summary-level.

## Category and tags
Category: design. Tags: design-system, tokens, okLCH, spring-motion, 5-states, accessibility, tailwind.
