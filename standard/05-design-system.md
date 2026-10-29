# 05 — Design system and UX

**One family, many personalities.** Every SIR product shares the same structure, components, flows and quality. Each has its own seed color, palette, typography pairing, illustration style and layout accents.

- **Shared information architecture:** the same navigation model everywhere. Bottom tabs on phones; a sidebar or navigation rail on tablets, foldables, desktop and web; the same destinations in the same order.
- **Identical shared screens** (from `@sir/settings` and `@sir/legal`), branded only through tokens:
  - Onboarding: language → welcome (3 screens maximum) → consent gate → just-in-time permission primers → sign in or continue as guest → personalization.
  - Profile: avatar (Cloudinary), name, key stats.
  - Settings, always in this order: Account · Appearance (theme, text size) · Language · Notifications · Privacy & data (consents, export, delete account) · Security (biometric lock, sessions) · AI preferences · Subscription & billing · Help & feedback · Legal (Terms, Privacy, EULA, open-source licenses) · About (version, what's new).
- **Color:** 60% calm neutral canvas, 30% structural surfaces with subtle borders, 10% accent reserved for primary actions, active states and key numbers. Palettes are generated from the product's seed color (light, dark, high-contrast). WCAG 2.2 AA minimum: 4.5:1 for body text, 3:1 for large text and UI parts.
- **Typography:** a deliberate pairing per product, plus an Arabic face designed for screens (IBM Plex Sans Arabic, Cairo, Tajawal, Noto Kufi Arabic or similar, chosen per product). Clear type scale. `tabular-nums` on prices, totals, timers, tables and counters.
- **Layout:** 4/8 pt grid. Window-size classes (compact < 600 dp, medium 600–839, expanded ≥ 840; larger classes for desktop). Layouts adapt; they don't just stretch. No horizontal overflow from 320 px to ultra-wide.
- **Every screen and zoom level:**
  - Browser zoom up to 400% with reflow; never disable pinch-zoom.
  - OS display scaling (Windows 100–250% and above, Android display size).
  - Text scaling to 200% (Android font scale, iOS Dynamic Type including accessibility sizes).
  - High-DPI assets: vector icons, `srcset` images.
  - Every kind of screen: small phones to ultra-wide monitors, foldables, tablets, TVs, round and square watches, car displays.
- **Platform feel:**
  - **iOS/iPadOS:** native navigation and controls; Liquid Glass materials for bars, sheets and controls through SwiftUI components (`@expo/ui`, expo-glass-effect); SF Symbols. Respect Reduce Transparency and Increase Contrast.
  - **Android:** Material 3 Expressive components, shapes and motion (through `@expo/ui` Jetpack Compose components); optional dynamic color with the brand palette as fallback.
  - **Web and desktop:** the brand UI, with glass or material effects used sparingly. Desktop adds keyboard shortcuts, menus, context menus, drag and drop, and remembered window size and position.
- **The 5 states**, built for every data-driven view:
  1. First use: guidance and a clear first action.
  2. Loading: skeletons that match the final layout (no layout shift, no lone spinners for content).
  3. Empty: a specific illustration, a helpful line, a direct action.
  4. Error: a human explanation, Retry, and a graceful fallback (cached data when possible).
  5. Populated: correct with 1 item and with 10,000+ (pagination or virtualization), long text truncated cleanly, no broken alignment.
- **Motion:** purposeful, never decorative noise. Micro-interactions 100–150 ms; standard transitions 200–300 ms; large transitions 300–500 ms; springs for direct manipulation; shared-element transitions between list and detail. Animate only transform and opacity, timed by duration rather than frame counts, so motion stays smooth at every refresh rate from 60 Hz to 120–144 Hz and beyond. Haptics on meaningful moments (mobile). Respect reduced-motion everywhere. Optimistic feedback within 100 ms of a tap.
- **Accessibility:** labels and roles for VoiceOver, TalkBack and NVDA; logical focus order; visible focus; text scaling to 200% without breaking; touch targets ≥ 44 pt (iOS) and ≥ 48 dp (Android); never color alone; captions for video.
- **Languages** (default locales `ar`, `en`, `zh-Hans`, `hi`, set in `.sir/project.yml`):
  - Every string goes through `@sir/i18n` with ICU MessageFormat; never concatenate strings. Plural rules differ: Arabic has six forms, English and Hindi two, Chinese one.
  - Arabic: full RTL mirroring (directional icons flip; media controls and numbers don't); correct bidirectional text; Hijri dates where relevant.
  - Scripts and fonts: Arabic, Latin, Simplified Chinese and Devanagari each need a screen font at matching weight and size (for example Noto Sans SC and Noto Sans Devanagari as fallbacks beside the Arabic and Latin faces). Subset web fonts; Chinese fonts are large. Arabic and Devanagari need taller line heights than Latin.
  - Text expansion: layouts survive strings about 40% longer and taller scripts. Test with pseudo-localization.
  - Formatting: locale-aware dates, numbers and currencies through `Intl` (EGP by default; Hindi uses lakh/crore digit grouping).
  - A language picker in onboarding and settings that defaults to the system language; per-app language on Android 13+ and iOS.
  - Workflow: the team writes English and Arabic source strings; the `localizer` drafts Chinese and Hindi through Gemini/OpenCode using a project glossary; CI checks for missing keys and mismatched placeholders; a native speaker reviews store listings and key screens before launch. Unreviewed machine translation never goes on public SEO pages.
- **Copy:** sharp and domain-specific. Natural Egyptian Arabic for friendly consumer copy, MSA for formal, legal and religious text, natural English, and natural contemporary Chinese and Hindi (not word-for-word translations). No lorem ipsum, no generic marketing filler. Honest and plain: no hype or superlatives ("revolutionary", "game-changing", "best-in-class", "world-class", "seamless", "unleash", "supercharge", "next-level", "magic", "ultimate", "#1") unless a claim is proven and sourced. Use numbers only when they're real.
- **Banned (instant rejection):** generic purple-to-blue gradients; sparkle "AI" icons and floating robot badges; emoji-stuffed headings; pill-shaped buttons on rectangular data inputs; stock filler copy; AI-generated images of real people; unlicensed assets.
- **Icons:** each app has a unique icon with a distinctive silhouette that reads at 16 px. The family shares a grid, stroke weight and corner language (pipeline in module 15).
- **Themes** (rebuild them; the existing ones are broken):
  - Every color, shadow and elevation comes from tokens (`@sir/tokens`). A lint rule forbids raw hex or rgb values in components.
  - Modes: light, dark, follow-system and high contrast. The choice persists and applies everywhere: web, desktop, mobile, watch, TV.
  - No flash of the wrong theme: on web, set the theme before first paint (inline script or cookie); on mobile, splash screens for light and dark; on desktop, the window background matches before content loads.
  - Native chrome follows the theme: status and navigation bars, title bars, scrollbars, form controls (`color-scheme`), keyboard appearance.
  - Images, illustrations, charts and maps adapt or have variants. App icons get dark and tinted variants on iOS and a themed monochrome icon on Android.
  - Test: screenshot every screen in light, dark and high contrast for every locale; contrast checks in CI.
- **Keyboard shortcuts** (every product):
  - One shortcut map for the whole family, defined in the shared UI packages:
    - Ctrl/Cmd+K: command palette and search
    - Ctrl/Cmd+,: settings
    - Ctrl/Cmd+N: new item
    - Ctrl/Cmd+F: find
    - Esc: close
    - `?` or Ctrl/Cmd+/: the shortcut help screen, which also lists each product's own shortcuts
  - Web and desktop: menus show accelerators, focus is always visible, full keyboard navigation (Tab order, arrow keys in lists and grids).
  - iPad, Android tablets and Chromebooks with keyboards: the same shortcuts, discoverable through the iPad menu bar or shortcut overlay and Android's keyboard shortcuts helper.
  - TV: D-pad and remote focus navigation with a clear focus state and no dead ends.
  - Accessibility: never override screen-reader or OS shortcuts; single-key shortcuts can be turned off or remapped (WCAG 2.1.4); arrow-key behavior mirrors correctly in RTL.
