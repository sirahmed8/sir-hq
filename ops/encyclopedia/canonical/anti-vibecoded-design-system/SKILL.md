---
name: anti-vibecoded-design-system
description: "Use when a UI looks generic or AI-generated and needs a bespoke, high-contrast, tactile design that avoids purple gradients and pill-button clichés."
---

# Anti-"Vibe-Coded" Design System & Aesthetic Standard

This skill establishes visual and architectural discipline to ensure user interfaces look bespoke, intentionally designed, and completely free of low-effort AI tropes.

---

## 1. Prohibited Aesthetic Clichés (The Blacklist)

- **NO Purple-to-Blue Neon Gradients**: Avoid default AI pastel blobs, vibrant cyan/magenta glows, and rainbow border meshes.
- **NO Gradient Hero Headlines**: Headings must be clean, legible solid type (`text-foreground` or high-contrast token).
- **NO Emoji Headers**: Never place emojis inside headings or feature badges (`🚀 Supercharge`, `✨ Magic Features`).
- **NO Universal Pill-Shaped Buttons**: Avoid `rounded-full` on standard controls, inputs, and form buttons. Use purposeful geometric hierarchy:
  - Cards/Modals: `rounded-2xl` (16px) or `rounded-xl` (12px)
  - Inputs & Buttons: `rounded-lg` (8px-10px)
  - Badges & Status Indicators: `rounded-full` (pills only for status)
- **NO "Three Identical Icon Boxes in a Row"**: Avoid three generic cards with left colored borders and Lucide icons on every surface.
- **NO Fake Testimonials or Fabricated Metrics**: Strictly avoid stock headshots with fake quotes or fake live visitor counters ("3 people bought this 2 minutes ago").
- **NO "Made with AI" Tags**: Never retain AI badges or boilerplate browser titles ("Vite + React", "Create Next App").
- **NO Intrusive Micro-Gimmicks**: No cursor-following lines, heavy canvas grain textures, harsh white glassmorphism borders, or scroll-hijacking animations.

---

## 2. Enforced Visual Standards

- **The 60-30-10 Color Rule**:
  - **60% Dominant Canvas**: Clean neutral background (`bg-background`).
  - **30% Structural Contrast**: Distinct surfaces, cards, and borders (`bg-card`, `border-border`).
  - **10% High-Intent Accent**: Single focused primary action color (`bg-primary`, `text-primary`).
- **Tactile Physics**:
  - Micro-interactions must feel physical with instantaneous feedback: `active:scale-[0.98]`.
  - Spring transitions under 200ms using physics curves (`cubic-bezier(0.16, 1, 0.3, 1)`).
- **High-Contrast Dark Mode**:
  - True high-contrast dark mode passing WCAG AA/AAA. Avoid muddy low-contrast grey-on-dark-grey text.
- **Typographic Discipline**:
  - High-signal sans-serif (Geist Sans, Inter, Plus Jakarta Sans) paired with monospace for metrics/code.
  - Balanced headings (`text-wrap: balance`) and readable body text (`text-wrap: pretty`).
