# LESSONS_UI: Portfolio-Wide Modern UI/UX Engineering Rules

Derived from owner testing on real physical hardware (iPhone 15 Safari/PWA and Android Xiaomi). These principles apply to every product across the SIR portfolio (AHome, SIR Business, SIR Hagoozat, SIR Education Hub, SIR Study, SIR Jobs, etc.).

---

## 1. Shared Swipe Pager Architecture (Tabs Everywhere)

Every tabbed group, category bar, and sub-navigation in the application must support horizontal finger swiping and desktop mouse drag. Never invent bespoke per-screen swipe logic.

- **Unified Component**: Use a single shared `SwipeablePager` component across all views.
- **Pure Gesture Math**:
  - Distance threshold: commit swipe when displacement $|dx| > 56\text{px}$ (`COMMIT_PX`).
  - Velocity threshold: commit quick flicks when velocity $|v| > 0.45\text{px/ms}$ (`VELOCITY_PX_MS`), even on short drags.
  - Axis locking: lock to horizontal only when $|dx| > 6\text{px}$ and $|dy| \le |dx| \times 1.1$. If vertical motion dominates, immediately release ownership to let the page scroll naturally.
  - Edge resistance: apply an elastic dampening factor ($0.18$) at the first and last tabs. Never wrap around tabs silently.
- **Direction Mirroring (RTL)**:
  - When `document.documentElement.dir === "rtl"`, invert displacement mapping ($dx \times -1$). In RTL, dragging from left-to-right pulls the next tab, and dragging from right-to-left moves to the previous tab.
- **Visual Continuity (Zero White Flash, Zero Stale Text)**:
  - Do not unmount outgoing panels prematurely. Keep the active panel and recently visited panels mounted during the spring transition.
  - Apply `inert={!active}` and `aria-hidden={!active}` to inactive panels.
  - For complex interactive panels (e.g. chat feeds), support a `keepIds` property so scroll position and draft state survive switching.

---

## 2. One Custom Picker Set (Zero Native System Pickers)

Never use browser-native form pickers (`<select>`, `<input type="date">`, `<input type="time">`, `<input type="datetime-local">`, bare checkboxes).

- **Why**: Native inputs invoke OS-level bottom sheets and modal wheel pickers on iOS and Android that break layout springs, distort viewport height calculations, ignore dark/light design tokens, and crash standalone PWA frames.
- **Standard Suite**:
  - **`Select`**: Dropdown with accessible portal sheet, animated spring emergence, and tactile option selection.
  - **`BuiltinTimePicker`**: Bespoke time sheet with discrete hour and minute grids (12h/24h format).
  - **`BuiltinDateTimePicker`**: Integrated calendar month grid and time picker.
  - **`Switch`**: Smooth toggle for binary settings and preference channels.
  - **`Checkbox`**: Accessible custom checkbox for multi-item selection only.

---

## 3. Software Keyboard Viewport & Composer Technique (Mobile WebKit / Safari)

Mobile Safari and mobile browsers overlay the software keyboard without resizing `100vh` or `100dvh`, completely occluding bottom composers and inputs.

- **No `position: fixed; bottom: 0`**: Fixed bottom elements either get covered by the iOS form accessory bar or produce visual rubber-band stutter during scroll.
- **Deterministic VisualViewport Sizing**:
  - Monitor `window.visualViewport` on `resize` and `scroll` events, throttled to `requestAnimationFrame`.
  - When an editable element (`input`, `textarea`, `contenteditable`) is focused and visual viewport drops by $>120\text{px}$ (`KEYBOARD_MIN_PX`), activate `html[data-keyboard-open="true"]`.
  - Export CSS custom variables: `--vvh` (visible viewport height), `--vvtop` (scroll offset), and `--kb` (keyboard height).
- **Flex Column Shell**:
  - Size the main chat shell using `height: min(var(--vvh, 100dvh), 100dvh); min-height: 0; padding-bottom: 0 !important;`.
  - The shell acts as a flex column: content area takes `flex: 1; min-height: 0; overflow-y: auto;`, and the composer sits firmly as the last flex row.
- **Dock Suppression**:
  - While keyboard is active, smoothly slide out and hide bottom navigation bars:
    ```css
    html[data-keyboard-open] .dock-frame,
    html[data-keyboard-open] .app-bottom-nav {
      opacity: 0 !important;
      pointer-events: none !important;
      transform: translateY(100%) !important;
    }
    ```
- **Body Scroll Lock**:
  - Apply `overflow: hidden; overscroll-behavior: none;` to `html[data-keyboard-open]` and `body` to prevent rubber-band drift while typing.
- **Scroll Active Input into View**:
  - Invoke `scrollIntoView({ block: "nearest", behavior: "instant" })` on the focused composer to keep the cursor centered above the keyboard.

---

## 4. Compact Tab Bar Rules

- **Dimensions**: Target a compact baseline: $40\text{px}$ minimum block size, $18\text{px}$ icons.
- **Label Discipline**: In compact tab rails, show label text only for the active tab; keep inactive tabs icon-only with clear accessible `aria-label`.
- **Zero Label Clipping**: Audit all viewports from $320\text{px}$ to $1920\text{px}$. Long localized strings (such as Arabic multi-word labels) must never clip or trigger horizontal scrollbars.
- **Dynamic Slot Allocation**: Use `ResizeObserver` on the tab container to dynamically calculate how many tabs fit (`splitTabs`), placing remaining tabs into an accessible "More" sheet.
- **Route Single-Source of Truth**: Navigation shows only consolidated primary routes. Legacy or merged routes remain in code purely as URL redirects, never as duplicate visible tabs.

---

## 5. Device & Person-Aware Guidance & Checklists

- **Runtime Modality Detection**:
  - Discriminate accurately between platforms: iOS vs. Android vs. Desktop.
  - Discriminate accurately between modalities: Standalone PWA (`display-mode: standalone`) vs. Native APK (`isCapacitorNative`) vs. Web Browser.
- **Tailored Checklists**:
  - iOS PWA: Guide Add to Home Screen, Safari Web Push permissions, Focus Mode alerts, and background execution realities.
  - Android APK: Guide battery optimization exemption, autostart permission, and exact alarm access.
- **Personalized Grammar & Tone**:
  - Address users with accurate localized grammatical forms (e.g. Arabic masculine vs. feminine imperatives and verbs according to authenticated viewer).
- **Brand Name Orthography**:
  - Enforce standard Arabic orthography for device brands (e.g. «شاومي» for Xiaomi, never «شياومي»).

---

## 6. Network & Telemetry Hygiene

- **Visibility-Aware Polling**:
  - Every recurring poll interval (e.g. media player status, background sync, companion heartbeats) must pause immediately when `document.visibilityState === "hidden"`.
- **Deduplicated Cache**:
  - Memoize rapid consecutive queries through shared stores with short TTL caches.
  - Implement exponential backoff with randomized jitter on network failure.
- **Transparent Counters**:
  - Always explain what telemetry metrics represent (e.g. "Total requests answered since local server started", alongside the current per-minute rate).
