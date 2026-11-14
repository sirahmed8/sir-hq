---
name: modern-ui-ux-design-system
description: "Use when designing or implementing a UI/UX design system with tokens, micro-interactions, and visual hierarchy."
---

# Modern UI/UX Design System & Ergonomics Guide

This skill provides comprehensive, scientifically and psychologically backed guidelines for crafting world-class, modern user interfaces that delight users and eliminate visual, layout, and ergonomic bugs.

---

## Core Pillars & Detailed References

Read the corresponding reference guide for deep mathematical models, token sets, and code templates:

1. [Psychological Laws & Cognitive Ergonomics (Hick's, Fitts's, Miller's, Gestalt)](./references/psychological_laws_and_ergonomics.md)
   - Detailed HCI laws, mathematical formulas for decision time and movement time, and practical visual hierarchy rules.
2. [Fluid Spring Animations & Design Tokens (Tailwind CSS v4 + OKLCH)](./references/fluid_spring_animations_and_tokens.md)
   - Spring physics easing curves, curvature hierarchy (`--radius: 0.75rem`), and CSS `@starting-style` entry transitions.
3. [Color Theory, OKLCH Dynamics & Flawless Theming](./references/color_theory_and_theming.md)
   - 60-30-10 distribution rules, OKLCH perceptual lightness color spaces, WCAG AAA contrast compliance, and zero-FOUC theme switching.
4. [Complete 5-State UI Implementation Patterns](./references/5_state_ui_patterns.md)
   - Drop-in implementations for Initial, Shimmer Skeleton, Empty State with CTA, Error Boundary with retry, and Partial/Overflow edge cases.

---

## Quick Design System Rules

- **Curvature Hierarchy**: Cards `rounded-2xl` (16px), Inputs/Buttons `rounded-lg` (8px-10px), Pills `rounded-full`. $\text{radius}_{\text{inner}} = \max(0, \text{radius}_{\text{outer}} - \text{padding})$.
- **Micro-Interactions**: Tactile spring press feedback (`active:scale-[0.98]`), smooth hover transitions (`transition-all duration-200 ease-[var(--ease-spring)]`).
- **Typography**: High-signal sans-serif (Geist, Inter, Plus Jakarta Sans) paired with monospace for metrics/code. Apply `text-wrap: balance` to headings and `text-wrap: pretty` to body text.
