# Task Plan: Round 11 Addendum (Control Room)

Goal: Consolidate top-bar settings controls into a single smooth Settings modal/popover, replace top tab bar with a responsive collapsible side menu (drawer on mobile, collapsible rail on desktop), ensure bidirectional LTR/RTL logical property mirroring, and eliminate all CMD/console window flashing via CREATE_NO_WINDOW across all subprocesses.

## Files Touched
- `D:\Projects\_SIR\plans\generate_dashboard.py`: Add `CREATE_NO_WINDOW = 0x08000000` to all `subprocess.run` calls (`git`, `gh`) to prevent CMD window flashes.
- `D:\Projects\_SIR\plans\dashboard_template.html`:
  - Add Settings Modal/Popover (`#settings-modal`) grouping Theme, Language, Density, Telemetry Refresh, and Remote Endpoints.
  - Implement single Settings button in top header (`#settings-btn`).
  - Implement Collapsible Side Menu / Rail (`#side-menu` / `#side-drawer`) with mobile drawer toggle (`#menu-toggle-btn`) and desktop rail with tooltips and active item highlights.
  - Keep 4 primary anchor pills visible on mobile header (`Now`, `Handover`, `CI`, `Projects`), while full 10 sections live in the side menu.
  - Mirror all CSS with logical properties (`inset-inline`, `margin-inline`, `padding-inline`, `border-inline`), directional transforms, and bidirectional number isolation (`unicode-bidi: isolate;`).
- `D:\Projects\_SIR\.sir\MASTER_PLAN.md`: Update master plan with Round 11 feature states and next 10 detailed tasks.
- `D:\Projects\_SIR\ops\agy-runs\reports\r11-control.md`: Final Round 11 engineering report.

## Steps in Order
1. Complete Console Window Silencing (Item 5):
   - In `generate_dashboard.py`, inject `CREATE_NO_WINDOW` into `git()` (lines 355-364), `gh` in `archived_count()` (line 528), `gh` in `get_ci_status()` (line 565), and `get_git_short_hash()` (line 683).
   - Verify on screen by triggering `refresh-control-room.py` and watching for 0 CMD flashes.
2. Build Consolidated Settings Window (Item 1):
   - Replace separate `#lang-btn` and `#theme-btn` in header with a single unified Settings button `#settings-btn`.
   - Implement Dynamic Island style compact modal/popover growing smoothly from the button (`cubic-bezier(0.16, 1, 0.3, 1)`).
   - Group settings into clear categories:
     - *Appearance*: Dark / Light theme toggle, Compact / Normal density.
     - *Localization*: English / Arabic toggle with instant RTL/LTR flip.
     - *System & Sync*: Telemetry refresh trigger button, Claude artifact sync hash indicator.
     - *Security & Remote*: Tailnet endpoint status.
   - Support keyboard navigation (`Esc` closes, focus trap, smooth backdrop blur).
3. Implement Collapsible Side Menu & Navigation Drawer (Item 2):
   - Build desktop collapsible side rail and mobile off-canvas drawer.
   - On desktop: clean rail showing icon + label, active item highlighted with `var(--accent)`.
   - On phones: keep top 4-5 quick access pills visible, with `#menu-toggle-btn` (hamburger icon) opening full 10-section drawer from logical start (left in LTR, right in RTL).
   - Dynamic Island spring transitions on open/close and hover.
4. Bidirectional RTL & LTR Polish (Item 3):
   - Refactor CSS using logical properties (`margin-inline-start`, `padding-inline-end`, `border-inline-start`).
   - Drawer slides from right in Arabic, left in English.
   - Isolate numbers, ports, git hashes, and paths with `direction: ltr; unicode-bidi: isolate;` to prevent punctuation reversals.
   - Mirror chevron and directional icons with `[dir="rtl"] .icon-flip { transform: scaleX(-1); }`.
5. Self-Improvement & Polish (Item 4):
   - Fluid spring physics on all interactive elements (`scale(0.97)` on active press, staggered lists).
   - Verify HTTP 200/304 conditional ETag revalidation.
   - Verify 0 privacy leaks with build assertion.
6. Verification & Visual Evidence:
   - Compile all scripts with `python -m compileall`.
   - Capture desktop and mobile screenshots in English and Arabic RTL (1440px and 390px).
   - Commit directly to `main` and verify green GitHub Actions CI.
   - Signal `agy-done.py r11-control ok`.

## Acceptance Checks (What will be seen on screen)
- Zero black CMD flashes or console popups when `refresh-control-room.py` or Task Scheduler triggers.
- Top bar displays single elegant Settings button (`Settings` / `الإعدادات`) opening a smooth popover with Appearance, Language, and System groups.
- Navigation organized into a collapsible side menu/rail, with mobile drawer sliding from right (AR) or left (EN) without white outline glitches.
- Numbers, git hashes, and ports display in proper order in both Arabic and English without punctuation inversion.
- Full responsive fidelity across 320px, 390px, 768px, 1024px, 1440px.

## Risks & Mitigations
- *Drawer backdrop click bleed*: Backdrop overlay will trap touch events and close drawer smoothly.
- *Layout shift when drawer opens*: Use fixed overlay drawer on mobile and flex layout on desktop to prevent content reflow.
- *Privacy leak*: Assertive regex guard in `generate_dashboard.py` prevents any accidental leaks.
