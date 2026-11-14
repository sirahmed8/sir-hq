---
name: taste-design-engine
description: "Use when a UI needs premium visual polish, a self-audit against AI-slop patterns, or an image-to-code visual replication."
---

# Taste Design Engine & Visual Verification Suite

Inspired by the Claude Code `taste-skill`, `awesome-design-md`, and live headless browser testing, this skill ensures every interface looks like a $10,000 custom build rather than generic AI slop.

---

## 1. The "Taste" Doctrine: Premium vs. AI Slop

| AI Slop (Strictly Banned) | Premium Craftsmanship (Enforced) |
| :--- | :--- |
| Purple-to-blue neon gradients and pastel meshes | Monochromatic canvas with intentional, high-contrast brand accents |
| `rounded-full` pill buttons on every control | Purposeful radii: 8–10px (`rounded-lg`) for controls; 14–16px (`rounded-2xl`) for cards |
| Cliché emoji headers (`🚀 Supercharge your...`) | Clean, balanced typographic hierarchy (`text-wrap: balance`) |
| Floating headline badge (`✨ AI-Powered Magic`) | Clear, declarative value proposition answering *What does this do?* |
| Three identical icon cards in a row | Asymmetric, editorial layouts reflecting real content hierarchy |
| Blurry glassmorphism with harsh white borders | Solid surfaces with subtle borders (`border-border/60`) and layered shadows |
| Generic stock photography with plastic faces | Authentic product screenshots, data visualizations, or curated vector art |

---

## 2. Design System Tokens & Geometry (Awesome Design)

- **Color Distribution (60-30-10 Rule)**:
  - `60%`: Canvas foundation (`bg-background`).
  - `30%`: Structural cards, sidebars, borders (`bg-card`, `border-border`).
  - `10%`: Primary high-intent action token (`bg-primary`, `text-primary-foreground`).
- **Typographic Scale**:
  - UI Sans: Geist Sans, Inter, or Plus Jakarta Sans.
  - Metrics / Code: Geist Mono or JetBrains Mono.
  - Heading Balance: `text-wrap: balance` on all `h1`-`h3`; `text-wrap: pretty` on paragraphs.
- **Micro-Interactions & Tactile Physics (Emil Kowalski Motion)**:
  - Tactile press feedback: `active:scale-[0.98]` on all buttons and cards.
  - Motion tokens: Sub-200ms spring physics (`stiffness: 400, damping: 30`) over mechanical linear transitions.
  - Staggered entrances: 30-50ms stagger on grid/list items; shared spatial morphing across state changes.
- **Impeccable Design Heuristics**:
  - Optical alignment: 1-2px compensation on arrows, icons, and badges.
  - Fluid typography clamp: `clamp(min, preferred, max)` for seamless viewport scaling without jarring media query jumps.

---

## 3. Web Design Guidelines Self-Auditor

Before declaring any UI task complete, the agent must self-audit against this checklist:
- [ ] **Contrast Compliance**: Normal text >= 4.5:1; large text >= 3:1 (WCAG AA/AAA).
- [ ] **Spatial Consistency**: Spacing strictly adheres to a 4px/8px grid (`gap-2`, `gap-4`, `p-6`).
- [ ] **Hierarchical Clarity**: Exactly one dominant primary CTA per viewport; secondary actions are visually subordinate (ghost or outline).
- [ ] **5-State Completeness**: Does the view gracefully render Initial, Loading (geometric skeletons), Populated, Error (with retry), and Empty states?

---

## 4. Image-to-Code Workflow

When given a mockup, screenshot, or design reference:
1. **Analyze Spatial Grid**: Break down the reference into container flex/grid rows and columns.
2. **Extract Design Tokens**: Sample primary background, card surface, border color, typography size, and radii.
3. **Recreate with Native Primitives**: Write modular, semantic code (Tailwind CSS, React/Next.js, or native framework) without unneeded wrapper divs.
4. **Preserve Polish**: Replicate padding, subtle drop shadows, and hover transitions.

---

## 5. Live Browser Verification Protocol

Never assume a design works without looking at it:
1. **Launch & Navigate**: Use Chrome DevTools MCP (`new_page` → `navigate_page`) or Playwright CLI to open the local development URL.
2. **Inspect Visual Rendering**: Call `take_screenshot` to verify layout alignment, typography rendering, and mobile responsiveness.
3. **Verify Console Health**: Run `list_console_messages` to ensure zero uncaught runtime errors, missing CSS variables, or hydration mismatches.
