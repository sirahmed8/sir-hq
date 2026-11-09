# DESIGN FAMILY: One Family, Separate Faces
**Standard**: SIR Master Directive & Gemini Quality Charter  
**Scope**: All 17 Workspace Projects (`D:\Projects`)  
**Design Philosophy**: Unified Architectural Craft, Bespoke Brand Identities  
**Version**: 1.0.0 (Strictly enforced)

---

## 1. The Shared SIR Family DNA

### 1.1 Core Philosophy: One Family, Separate Faces
Every application and interface in the SIR ecosystem belongs to a single cohesive engineering dynasty. They share the same uncompromising standards of craftsmanship, performance, and tactile responsiveness. Yet, **no two products look identical**: each possesses its own distinct brand personality, color palette, typographic rhythm, and domain-tailored ergonomics. A student opening `SIR Study` feels scholarly focus; a cashier touching `SIR Business` feels lightning-fast transaction reliability; Ahmed using `AHome` feels intimate sanctuary.

### 1.2 Dynamic Island Spring Motion Architecture
All animation throughout the SIR portfolio adheres to the **Dynamic Island** physics paradigm:
- **Spring Constants**: Transitions use natural spring curves:
  - CSS equivalent: `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);`
  - Spring physics: Stiffness `300–400`, Damping `28–30`, Mass `1.0`.
- **Active-Only Tab Label Expansion**:
  - Inactive tabs display only their crisp monochrome SVG icon (occupying minimal horizontal footprint).
  - The currently active tab smoothly expands to reveal both icon and localized text label with fluid spring interpolation.
  - **Zero White Outline Glitches**: Tab switching must never produce jarring browser focus ring flashes or white outline jumps. Focus rings use subtle semantic color rings (`box-shadow: 0 0 0 2px rgba(..., 0.4)` on `:focus-visible` only).
- **Trigger Morphing & Sheet Continuity**:
  - Dialogs, popovers, and bottom sheets expand smoothly from the bounding box of the trigger element.
  - Backdrops use soft gaussian blur (`backdrop-filter: blur(12px)`) with gradual opacity fade; **never an abrupt pitch-black overlay**.
- **Tactile Active Press Feedback**:
  - All interactive buttons and cards compress subtly on pointer down: `transform: scale(0.98);` with rapid recovery on release.
- **Accessibility & Reduced Motion**:
  - Strictly respects `@media (prefers-reduced-motion: reduce)`: collapses spring translations to clean, instant opacity fades.

### 1.3 Computed, Fluid Layouts (320px Ultra-Mobile to 4K Displays)
- **Zero Fixed-Width Breakdowns**: Layouts are dynamically computed via CSS Flexbox and Grid with automatic wrapping (`flex-wrap: wrap; gap: 0.75rem;`).
- **No Button Spilling**: Action buttons must never overflow or clip outside card containers on narrow viewports (320px–390px).
- **Minimum Touch Targets**: Every interactive button, pill, and tab maintains at least a **44x44px** touch target boundary.
- **Safe Keyboard Viewports (`100dvh`)**: Mobile chat composers and forms use `visualViewport` listeners driving custom height variables (`--vvh`), ensuring the input field glides precisely above the virtual keyboard without fixed-bottom positioning glitches.

### 1.4 Semantic Color Discipline: Zero Yellow Buttons
- **Semantic Palette Invariant**:
  - **Primary Action**: Brand signature token (Sapphire, Emerald, Indigo, Crimson, Violet).
  - **Neutral / Secondary**: Slate / Titanium (`#475569` / `#64748B`).
  - **Success / Completed**: Forest Emerald (`#10B981` / `#059669`).
  - **Danger / Destructive**: Ruby Crimson (`#EF4444` / `#DC2626`).
  - **Attention / Pending**: Amber Ochre (`#F59E0B` / `#D97706`).
- **Zero Yellow Buttons**: Jarring yellow buttons (`#EAB308`) are strictly prohibited across all dialogs, modals, and primary actions.

### 1.5 Executive Typography & Strict Zero-Emoji Rule
- **Typographic Pairings**:
  - Primary Arabic: `Cairo` (weights 400, 600, 700).
  - Primary English / Numbers: `Inter` / `SF Pro Display`.
  - Code, Hex Hashes, Telemetry & Currencies: `JetBrains Mono`.
- **Zero Emoji Mandate**: Emojis are strictly banned from UI views, notifications, Telegram bots, AI replies, and terminal logs. Interfaces communicate authority through crisp, monochrome SVG icons and elegant typography.

### 1.6 Bidirectional Parity (Arabic RTL & English LTR)
- **Logical CSS Properties**: Directional properties use logical equivalents (`margin-inline`, `padding-inline`, `inset-inline`, `border-inline-start`).
- **Mirrored Drawer Transitions**: Mobile side drawers slide from the right in RTL and from the left in LTR. Directional chevrons mirror automatically via `transform: scaleX(-1);`.
- **Bi-Directional Isolation**: Git hashes, IP addresses, ports, version stamps, and file paths are wrapped in `<bdi>` or `unicode-bidi: isolate;` to prevent punctuation inversion in Arabic sentences.

### 1.7 The Five Mandatory UI States
Every view, data card, and table must explicitly handle:
1. **Idle / Populated**: Clean spacing, balanced typographic hierarchy, responsive wrap.
2. **Loading Skeleton**: Shimmering wireframe geometries matching final content dimensions; zero spinner freezes.
3. **Empty State**: Thoughtful, encouraging localized copy, custom bespoke SVG emblem, and a single prominent 1-tap call-to-action button.
4. **Error State**: Non-technical, plain-language explanation, error reference badge, and an animated Retry button.
5. **Overflow / Truncation**: Graceful text ellipsis (`text-overflow: ellipsis`), informative tooltips, and responsive layout wrapping.

---

## 2. Per-Project Identity Table (All 17 Projects)

| Slug | Product Name | Brand Aesthetic | Primary & Secondary Tokens | Canvas & Surface Tokens | Typography | Motion Signature | Bespoke Logo Motif | Signature Screen Element |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`ahome`** | **AHome** | Warm Midnight Sanctuary | Soft Rose `#F43F5E`<br>Lavender `#A78BFA` | Obsidian `#0B0F17`<br>Slate Glass `rgba(30,41,59,0.7)` | `Cairo`<br>`SF Pro` | Intimate breathing springs, morphing voice island | Interlocking hearth arches | Dynamic Island partner presence & care summary |
| **`sir-study`** | **SIR Study** | Academic Royal Codex | Sky Sapphire `#0284C7`<br>Beacon Cyan `#38BDF8` | Deep Navy `#0A0F1D`<br>Slate Glass `rgba(30,41,59,0.75)` | `Cairo`<br>`Inter`<br>`JetBrains Mono` | Crystalline focus, active recall card flip | Codex gate with celestial star | Interactive Simplex & DFD visual simulation labs |
| **`sir-jobs`** | **SIR Jobs** | Royal Sapphire Career Command | Royal Sapphire `#2563EB`<br>Cobalt `#60A5FA` | Executive Navy `#0B1120`<br>Slate Glass `rgba(30,41,59,0.7)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Decisive tactile spring, roving modal tab traps | Sovereign briefcase with compass | 13,475 EGP target calculator & Kanban pipeline |
| **`sir-laptop-manager`** | **SIR Laptop Manager**| Obsidian Cybernetic Console | Performance Emerald `#10B981`<br>Telemetry Cyan `#06B6D4` | Cybernetic Obsidian `#080C14`<br>Smoked Glass `rgba(17,24,39,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Surgical real-time telemetry stream, tactile relief | Hardware core aperture & circuit node | Live hardware telemetry & 1-click Game Mode |
| **`sir-hq`** | **SIR Control Room** | Command Radar Obsidian | Command Indigo `#6366F1`<br>Telemetry Cyan `#38BDF8` | Command Obsidian `#090D16`<br>Indigo Glass `rgba(15,23,42,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Authoritative radar sweep, sub-ms ETag transitions | Radar aperture with crosshair sweep | Attention queue & single-source artifact |
| **`sir-ai`** | **SIR AI** | Cybernetic Neural Obsidian | Neural Violet `#8B5CF6`<br>Electric Cyan `#06B6D4` | Deep Obsidian `#070A12`<br>Slate Glass `rgba(17,24,39,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Dynamic morphing voice waveform, active listening | Neural iris aperture | Jarvis voice assistant morphing visualizer |
| **`sir-negm-furniture`**| **SIR Negm Furniture** | Luxury Artisanal Atelier (FROZEN)| Bronze Gold `#D97706`<br>Warm Sand `#F59E0B` | Charcoal Obsidian `#0F1115`<br>Bronze Glass `rgba(22,25,30,0.8)` | `Cinzel`<br>`Cairo`<br>`Inter` | Fluid architectural 3D camera pan | Carpenter's square & golden spiral | 3D room floor plan canvas studio |
| **`sir-obour-hub`** | **SIR Obour Hub** | Academic Prestige & Campus Beacon | Campus Emerald `#059669`<br>Gold Beacon `#D97706` | Forest Obsidian `#06110D`<br>Emerald Glass `rgba(12,30,23,0.75)` | `Cairo`<br>`Inter` | Vibrant campus rhythm, lecture pulse | Academic gate & open scroll | Live lecture hall timetable ticker & GPA simulator |
| **`sir-hagoozat`** | **SIR Hagoozat** | Night Match Stadium & Pitch Emerald | Turf Emerald `#10B981`<br>Floodlight Cyan `#06B6D4` | Stadium Obsidian `#080F0C`<br>Turf Glass `rgba(14,26,21,0.75)` | `Inter`<br>`Cairo`<br>`Teko` | Athletic high-energy spring, score ticker | Pentagon ball & floodlight beacon | Interactive pitch slot lock grid & 5v5 lobby |
| **`sir-business`** | **SIR Business** | Merchant Ledger Emerald & Brass | Merchant Emerald `#059669`<br>Brass Gold `#D97706` | Ledger Obsidian `#07100D`<br>Slate Glass `rgba(12,29,24,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Lightning-fast numpad tactile, receipt cut pulse | Hexagonal seal & balance scale | Sub-50ms barcode checkout terminal |
| **`sir-content-creation-studio`**| **SIR Content Creation Studio**| Neon Cyber Studio & Kinetic Crimson | Kinetic Crimson `#E11D48`<br>Neon Violet `#8B5CF6` | Studio Obsidian `#0A060E`<br>Studio Glass `rgba(19,13,27,0.75)` | `Bebas Neue`<br>`Inter`<br>`Cairo` | Kinetic bouncy spring scrub, video timeline | Camera aperture & play prism | Multi-track video timeline scrubber & captions |
| **`sir-controller`** | **SIR Controller** | Cybernetic Apex & Electric Indigo | Electric Indigo `#6366F1`<br>Neon Amber `#F59E0B` | Apex Obsidian `#06080F`<br>Indigo Glass `rgba(13,17,30,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | 60fps deflection stick response, sub-ms timer | Gamepad silhouette & latency wave | 3D real-time gamepad deflection tester |
| **`sir-modpack`** | **SIR ModPack** | Emerald Pixel Vanguard & Bedrock | Emerald Matrix `#10B981`<br>Redstone Ruby `#EF4444` | Bedrock Obsidian `#0B0F14`<br>Emerald Slate `rgba(17,24,34,0.75)` | `Minecraftia`<br>`Inter`<br>`Cairo` | Live FPS gauge spring, delta downloader | Faceted emerald crystal cube | 120 FPS performance tuning slider & modlist |
| **`sir-mods-for-gta-v`**| **SIR Mods for GTA V** | Vinewood Sunset & Neon Noir | Sunset Amber `#F59E0B`<br>Neon Cyan `#06B6D4` | Vinewood Obsidian `#080A10`<br>Sunset Glass `rgba(14,18,29,0.75)` | `Pricedown`<br>`Inter`<br>`Cairo` | Redline tachometer needle sweep | Tachometer gauge & golden palm | 3D vehicle handling physics tuner |
| **`sir-odysseus`** | **SIR Odysseus** | Archived Academic Gray | Muted Slate `#64748B`<br>Cool Steel `#94A3B8` | Archive Gray `#1E293B`<br>Solid Slate `#334155` | `Inter` | Static archival, zero active animations | Compass Rose | Read-only archival digest & retirement notice |
| **`sir-life`** | **SIR Life** | Tranquil Serenity & Sacred Horizon | Tranquil Teal `#0D9488`<br>Amethyst `#8B5CF6` | Twilight Obsidian `#060F0E`<br>Teal Glass `rgba(12,24,23,0.75)` | `Cairo`<br>`Inter` | Breathing organic pulse, gentle chime | Blooming lotus & crescent horizon | Cairo prayer countdown hero & habit rings |
| **`sir-platform`** | **SIR Platform** | Sovereign Keystone & Titanium | Keystone Titanium `#475569`<br>Electric Indigo `#6366F1` | Keystone Obsidian `#080C14`<br>Titanium Glass `rgba(14,20,34,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Architectural foundation snap | Keystone arch & diamond prism | Interactive component token gallery & CLI |
| **`sir-portfolio`** | **SIR Portfolio** | Sovereign Luminary & Void Obsidian | Sovereign Platinum `#F8FAFC`<br>Royal Sapphire `#2563EB` | Void Obsidian `#06080D`<br>Slate Glass `rgba(15,23,42,0.75)` | `Inter`<br>`Cairo`<br>`JetBrains Mono` | Staggered card entrance, live commit ticker | Monogram SA & celestial compass | Live verified product wall & architecture modals |

---

## 3. Comprehensive Resilience, Edge Cases & Operational Depth

### 3.1 Missing Pieces & Anticipated Future Demands
- **Push Notification Cascades**: When an alert fires (e.g. high-fit job, exam in 2h, thermal spike >85°C), the system dispatches via Web Push API on desktop and Telegram bot on iPhone simultaneously, with automatic deduplication.
- **Bi-Directional CalDAV Bridge**: Integration between `SIR Study`, `SIR Obour Hub`, `SIR Life`, and iPhone native calendar without cloud middle-men.
- **Automated P2P Local Wi-Fi Mesh**: Direct mDNS device pairing allowing offline synchronization between phone and laptop when away from cellular networks.

### 3.2 Edge Cases & Failure Mode Hardening
- **Windows Socket Resets (`WinError 10054/10053`)**: Web servers on ports 3300, 3456, 8765, 8899, 8900 wrap client reads in try-except blocks, handling sudden mobile network disconnects without raising unhandled traceback errors.
- **Race Condition Prevention on High Concurrency**: Slot booking in `SIR Hagoozat` and checkouts in `SIR Business` utilize row-level database locking with 5-minute atomic reservation leases.
- **Rapid Click & Double-Submit Protection**: All action buttons implement client-side debouncing (minimum 300ms lock) and idempotent transaction keys to eliminate accidental double charges or duplicate database records.
- **Low Disk Space & Quota Exhaustion**: Disk cleaner in `SIR Laptop Manager` enforces a strict 2GB safety reserve buffer; temporary operations abort cleanly if free space on C: drops below 5GB.

### 3.3 Accessibility Standards (WCAG 2.1 AA Compliant)
- **Keyboard Navigation & Focus Traps**:
  - All interactive elements are fully reachable via keyboard `Tab` / `Shift+Tab`.
  - Open modals trap keyboard focus within the dialog container (`aria-modal="true"`); pressing `Escape` dismisses the modal and restores focus smoothly to the triggering element.
- **Screen Reader Announcements**:
  - Dynamic content changes (toasts, status updates, countdown warnings) announce state changes via hidden live regions (`aria-live="polite"`).
- **Contrast Ratios**:
  - Text to background contrast maintains at least **4.5:1** for body copy and **7:1+** for headlines across both dark and daylight themes.

### 3.4 Offline Resilience & Data Synchronization
- **Service Worker Architecture**: Every web interface registers an offline Service Worker caching static shells, CSS tokens, and vector brand assets using a Stale-While-Revalidate caching strategy.
- **Local Transaction Queues**: Write actions executed while offline are staged in IndexedDB transaction queues. Upon network reconnection, updates sync to the central server with deterministic timestamp sequencing.
- **Visual Offline Status Badges**: Interfaces display a subtle amber pill ("Offline Mode - Local Changes Saved") when network connectivity drops, switching to green ("Synced") upon automated reconnection.

### 3.5 Security & Zero-Trust Defense in Depth
- **Zero-Trust Network Ingress**: Services bind strictly to `127.0.0.1` and validate `Tailscale-User-Login: a7medorabe7@gmail.com`. Foreign network requests receive instant HTTP 403 Forbidden responses.
- **RFC 9110 Security Headers**: Every local web server strictly emits:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Content-Security-Policy: default-src 'self' ...; script-src 'self' 'unsafe-inline';`
- **Zero Hardcoded Secrets**: Secrets and private keys are never committed to git repositories; verified via gitleaks pre-commit hooks and CI scans.
- **Private Data Isolation**: AHome and Habiba personal content remain strictly isolated within local SQLite vaults with DPAPI encryption at rest; zero data egress.

### 3.6 Performance Budgets & Hardware Health
- **First Contentful Paint (FCP)**: Sub-100ms first paint on desktop; sub-300ms on 4G mobile devices.
- **Animation Framerate**: 60 FPS minimum on mobile viewports; 120 FPS on 120Hz/144Hz desktop monitors with zero layout thrashing (`will-change: transform`).
- **Memory Lifecycle**: Event listeners and intervals are systematically cleaned up on component unmount; map and canvas objects explicitly call disposal routines to prevent JavaScript heap leaks.
- **Battery Conservation**: Long-running background timers suspend interval polling when the browser tab is hidden (`document.hidden`).

### 3.7 Automated Backups, Rollback & Self-Healing
- **SHA-256 Quarantine Buckets**: Destructive operations (cache purges, broken shortcut repairs, registry edits) stage target files into timestamped quarantine buckets with JSON rollback manifests.
- **Silent Scheduled Startup**: All background daemons boot headlessly via `wscript.exe` and `pythonw.exe` on Windows user login, ensuring zero console CMD window flashes during active gaming or desktop work.
- **Automated Restore Drills**: SQLite databases execute automated daily integrity checks (`PRAGMA integrity_check;`) and automated test restores to in-memory databases.

### 3.8 Onboarding & Empty State Architecture
- **Zero-Friction First Run**: No mandatory setup wizards or tedious onboarding questionnaires; the interface launches directly into a clean, intuitive workspace.
- **Progressive Disclosure**: Advanced controls (calibration, raw telemetry, export settings) are gracefully tucked into Dynamic Island popovers, revealing complexity only when requested.
- **Contextual Empty States**: When lists or tables contain zero items, they present custom vector illustrations, encouraging copy, and a single prominent 1-tap button to create the first record.
