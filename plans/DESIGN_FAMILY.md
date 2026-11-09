# DESIGN FAMILY: One Family, Separate Faces
**Standard**: SIR Master Directive & Standards 23–27  
**Scope**: All 17 Workspace Projects (`D:\Projects`)  
**Design Philosophy**: Unified Architectural Craft, Bespoke Brand Identities  
**Version**: 1.0.0 (Strictly enforced)

---

## 1. The Shared SIR Family DNA

### 1.1 Core Philosophy: One Family, Separate Faces
Every application and interface in the SIR ecosystem belongs to a single cohesive engineering dynasty. They share the same uncompromising standards of craftsmanship, performance, and tactile responsiveness. Yet, **no two products look identical**: each possesses its own distinct brand personality, color palette, typographic rhythm, and domain-tailored ergonomics. A student opening `SIR Study` feels scholarly focus; a cashier touching `SIR Business` feels lightning-fast transaction reliability; Ahmed using `AHome` feels intimate sanctuary; a homeowner customizing furniture in `SIR Negm Furniture` feels luxury craftsmanship.

### 1.2 Dynamic Island Spring Motion Architecture
All animation throughout the SIR portfolio adheres to the **Dynamic Island** physics paradigm:
- **Spring Constants**: Transitions use natural spring curves:
  - CSS equivalent: `transition: all 0.38s cubic-bezier(0.16, 1, 0.3, 1);`
  - Spring physics: Stiffness `350`, Damping `30`, Mass `1.0`.
- **Active-Only Tab Label Expansion**:
  - Inactive tabs display only their crisp monochrome SVG icon (occupying minimal horizontal footprint).
  - The currently active tab smoothly expands to reveal both icon and localized text label with fluid spring interpolation.
  - **Zero White Outline Glitches**: Tab switching must never produce jarring browser focus ring flashes or white outline jumps. Focus rings use subtle semantic color rings (`box-shadow: 0 0 0 2px rgba(..., 0.4)` on `:focus-visible` only).
- **Trigger Morphing & Sheet Continuity**:
  - Dialogs, popovers, and bottom sheets expand smoothly from the bounding box of the trigger element.
  - Backdrops use soft gaussian blur (`backdrop-filter: blur(14px)`) with gradual opacity fade; **never an abrupt pitch-black overlay**.
- **Tactile Active Press Feedback**:
  - All interactive buttons and cards compress subtly on pointer down: `transform: scale(0.975);` with rapid recovery on release.
- **Accessibility & Reduced Motion**:
  - Strictly respects `@media (prefers-reduced-motion: reduce)`: collapses spring translations to clean, instant opacity fades.

### 1.3 Computed, Fluid Layouts (320px Ultra-Mobile to 4K Displays)
- **Zero Fixed-Width Breakdowns**: Layouts are dynamically computed via CSS Flexbox and Grid with automatic wrapping (`flex-wrap: wrap; gap: 0.75rem;`).
- **No Button Spilling**: Action buttons must never overflow or clip outside card containers on narrow viewports (320px–390px).
- **Minimum Touch Targets**: Every interactive button, pill, and tab maintains at least a **44x44px** touch target boundary.
- **Safe Keyboard Viewports (`100dvh`)**: Mobile chat composers and forms use `visualViewport` listeners driving custom height variables (`--vvh`), ensuring the input field glides precisely above the virtual keyboard without fixed-bottom positioning glitches.

### 1.4 Semantic Color Discipline: Zero Yellow Buttons
- **Semantic Palette Invariant**:
  - **Primary Action**: Brand signature token (Sapphire, Emerald, Indigo, Crimson, Violet, Bronze).
  - **Neutral / Secondary**: Slate / Titanium (`#475569` / `#64748B`).
  - **Success / Completed**: Forest Emerald (`#10B981` / `#059669`).
  - **Danger / Destructive**: Ruby Crimson (`#EF4444` / `#DC2626`).
  - **Attention / Pending**: Amber Ochre (`#F59E0B` / `#D97706`) - text and warning badge only, **never as a primary button background**.
- **Zero Yellow Buttons**: Jarring yellow buttons (`#EAB308` / `#FACC15`) are strictly prohibited across all dialogs, modals, and primary actions.

### 1.5 Executive Typography & Strict Zero-Emoji Rule
- **Typographic Pairings**:
  - Primary Arabic: `Alexandria` & `Cairo` (weights 400, 600, 700; line-height minimum 1.6 to avoid diacritic clipping).
  - Primary English / Numbers: `Inter` / `SF Pro Display`.
  - Code, Hex Hashes, Telemetry & Currencies: `JetBrains Mono`.
- **Zero Emoji Clutter**: Professional interfaces use crisp monochrome SVG icons (Heroicons / Lucide); zero emojis in production UI views, modals, and receipts.

---

## 2. Per-Project Brand Identity & Visual Signatures

| Project | Signature Primary / Accent | Primary Hex | Surface Theme | Distinct Atmosphere & Personality |
|---|---|---|---|---|
| **AHome** | Rose Quartz / Warm Amber | `#E11D48` / `#F59E0B` | Deep Cocoa Charcoal | Sanctuary, intimate, deeply private, warm glow |
| **SIR Study** | Scholar Indigo / Gold Amber | `#4338CA` / `#D97706` | Deep Inkwell Navy | Scholarly, academic rigor, distraction-free |
| **SIR Jobs** | Executive Emerald / Teal | `#059669` / `#0D9488` | Deep Forest Slate | Corporate, high-stakes, sharp, career momentum |
| **SIR Laptop Manager**| Titanium Steel / Cyan | `#475569` / `#0891B2` | Gunmetal Industrial | Hardware control, precision, telemetry, silent power |
| **SIR AI** | Cyber Violet / Electric Cyan | `#7C3AED` / `#06B6D4` | Obsidian Space | Frontier intelligence, crystalline, fluid cognition |
| **SIR Hagoozat** | Pitch Turf Emerald / Lime | `#10B981` / `#84CC16` | Pitch Charcoal | Athletic, pulse-raising, immediate, outdoor turf |
| **SIR Business** | Commercial Sapphire / Mint | `#2563EB` / `#10B981` | Clean Ledger Slate | High-trust, ultra-fast transaction, cashier tactile |
| **SIR Obour Hub** | Academic Navy / Coral Sunset| `#1E3A8A` / `#F97316` | Campus Slate | Vibrant, youthful, campus community, collegiate |
| **SIR Negm Furniture**| Artisan Bronze / Warm Sand | `#D97706` / `#F59E0B` | Deep Charcoal Obsidian| Luxury Artisanal Atelier, bespoke craftsmanship, 3D |
| **SIR Content Studio**| Creator Crimson / Neon Pink| `#DC2626` / `#EC4899` | Dark Studio Matte | High-impact, viral, cinematic timeline editor |
| **SIR Controller** | Cyber Neon Green / Steel | `#16A34A` / `#64748B` | Hard Anodized Alloy | Low-latency, esports weapon, mechanical precision |
| **SIR ModPack** | Deep Moss Green / Obsidian | `#15803D` / `#334155` | Minecraft Stone | Gaming craft, clean blocky accents, lightweight |
| **SIR Mods for GTA V** | Sunburst Orange / Slate | `#EA580C` / `#475569` | High-Contrast Dark | High-octane action, safe mod sandbox |
| **SIR Life** | Sage Green / Calming Teal | `#0D9488` / `#14B8A6` | Clean Ceramic Dark | Mindful serenity, healthy habits, spiritual focus |
| **SIR Portfolio** | Founder Platinum / Sapphire| `#2563EB` / `#94A3B8` | Architectural Dark | Executive authority, verifiable truth, GEO engine |
| **SIR Platform** | Monorepo Neutral / Indigo | `#6366F1` / `#64748B` | System Foundry | Universal parent tokens, high-performance base |
| **_SIR** | Command Azure / Emerald | `#0284C7` / `#10B981` | Mission Control | Real-time operations truth, autonomous oversight |

---

## 3. Resilience & Edge-Case Architecture

1. **RTL Directional Intelligence**: Full logical property enforcement (`margin-inline-start`, `border-start-start-radius`); navigation icons flip 180deg in RTL; media players and timers remain directional invariant.
2. **Offline-First Tactile States**: When network connection drops, apps render an organic amber offline banner with local cache indicators. Buttons enter optimistic pending states with automatic retry queues.
3. **Empty States with Dignity**: Zero fake reviews, zero mock placeholder numbers. Empty states explain the feature clearly with a single primary action button to get started.
4. **Accessible Error Dialogs**: User-facing errors state: (1) What happened in plain human words, (2) Why it happened, (3) Exactly what action to take (e.g. "Check connection" or "Retry in 30s").
