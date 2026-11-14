# Cross-Project Lessons (HQ)

Every complaint the owner makes about one product becomes a general rule with a "how to apply to other products" line. The verifier and scouts check every project against this list.

Updated: 2026-11-12

---

## L1: Active Tab Must Scroll Into View
**Source:** r33 item 1 (AHome "حياتنا" tab bar)
**Rule:** When a page opens or a tab changes, the active tab must be fully scrolled into view. Never leave the active tab cut off or require horizontal scroll to see it.
**Apply to all:** Every project with horizontal tab bars (SIR Jobs, SIR Study, SIR Laptop Manager, SIR AI, SIR Portfolio, Control Room). Add `scrollIntoView({ behavior: 'smooth', inline: 'center' })` on mount and on tab change.

---

## L2: Merge Duplicate Destinations
**Source:** r33 item 2 (AHome "حياتنا" and "يومنا")
**Rule:** If two navigation entries open the same or semantically overlapping content, merge them into one coherent page. Remove duplicate names.
**Apply to all:** Audit every project's navigation for duplicate destinations (Control Room had Menu + More opening same sidebar - r35 item 1). Keep one entry point per destination.

---

## L3: Matching Spring Open AND Close for Every Sheet/Panel
**Source:** r33 item 3 (AHome "more tabs" bottom sheet), r35 item 3 (Control Room/Laptop Manager sidebar), r38 item 6
**Rule:** Every bottom sheet, side panel, modal, drawer, and overlay must have a matching spring close animation back into its trigger. No open-only animations.
**Apply to all:** Audit every project for panels/sheets with open animation but missing/janky close. Use the same spring config (stiffness/damping) for both directions.

---

## L4: Panel Content Never Clipped
**Source:** r33 item 4 (AHome right-aligned panel), r35 item 2 (Control Room/Laptop Manager table columns)
**Rule:** Any sliding panel, sidebar, or overflow menu must open fully on screen. Content must never be clipped, require horizontal scroll to read its own labels, or wrap character-by-character. Narrow tables at phone width must use card layout, not cramped tables.
**Apply to all:** Test every panel/sidebar at 320px and 390px. Fix CSS: remove fixed narrow widths, add `word-break: keep-all`, `overflow-wrap: anywhere`, or card layout for tables on mobile.

---

## L5: Keyboard Dismiss Returns to Latest Message
**Source:** r33 item 5 (AHome AI chat)
**Rule:** In any chat view, dismissing the keyboard must return the view to showing the latest message (bottom of list). No manual scroll required.
**Apply to all:** SIR Study (study chat), SIR Jobs (job chat), any project with chat interfaces.

---

## L6: Consistent Input Box Styling Across Chat Types
**Source:** r33 items 6, 7 (AHome AI chat input vs normal chat, voice recorder)
**Rule:** All input boxes across the app (normal chat, AI chat, voice recorder, search) must share the same compact, polished styling and spring transitions. No oversized rectangles.
**Apply to all:** Create a shared InputBox component used everywhere. Voice recorder should grow out of the input box with spring animation.

---

## L7: Reply Preview Background Matches Input Box
**Source:** r33 item 8 (AHome)
**Rule:** Reply preview, quote preview, and any inline preview must use the exact same surface color/theme token as the message input box.
**Apply to all:** Use a design token (e.g., `surface-input`) consistently.

---

## L8: Real-Time Bidi Detection Per Character
**Source:** r33 items 9, 10 (AHome chat inputs), r34 item 3 (SIR Jobs), OWNER_DEFAULTS.md item 15
**Rule:** Every text input must detect Arabic vs Latin per character as the user types and set direction/caret side live (Arabic starts/types from right, Latin from left). Mixed content must render with `<bdi>` or `unicode-bidi: isolate` per run. Never show literal "(RTL)"/"(LTR)" to users.
**Apply to all:** Every project with text inputs (all of them). Add bidi detection hook/component. Audit all message rendering for bdi isolation.

---

## L9: Premium Tab Bar Sizing and Centering
**Source:** r33 item 11 (AHome emoji/stickers/GIFs panel)
**Rule:** Tab bars must have adequate touch targets (min 44px), active tab label/icon centered in the active pill, consistent sizing across the app.
**Apply to all:** SIR Jobs, SIR Study, SIR Laptop Manager, Control Room, SIR AI, SIR Portfolio.

---

## L10: Real GIF/Sticker Content (No Placeholders)
**Source:** r33 items 12, 13 (AHome)
**Rule:** GIF and sticker tabs must fetch and show real content from legitimate free providers (Tenor, Giphy). Failed loads must be hidden, not shown as errors. Stickers must use real popular packs.
**Apply to all:** Any project with emoji/GIF/sticker pickers.

---

## L11: Real Ringing State for Calls
**Source:** r33 item 14 (AHome voice call)
**Rule:** Outgoing calls must show a real ringing/ringback state (sound + UI) before connecting. No immediate "connected" screen.
**Apply to all:** Any project with call features.

---

## L12: Video Call Opens Video UI
**Source:** r33 item 15 (AHome)
**Rule:** Tapping "video call" must open the video call UI, not fall back to voice call screen.
**Apply to all:** Any project with call features.

---

## L13: User-Choosable Notification/Call Sounds
**Source:** r33 item 16 (AHome)
**Rule:** Provide distinct user-choosable sounds for notifications and incoming calls, on top of OS defaults.
**Apply to all:** Any project with notifications/calls.

---

## L14: Dynamic Island Continuous Morph (No Fade Swaps)
**Source:** r33 item 17, r38 items 5, 9 (AHome)
**Rule:** Every Dynamic Island state change must be one continuous spring grow/shrink. Never fade-out/fade-in swaps. Only one island visible at a time. Never covers composer or tab bar.
**Apply to all:** Any project using Dynamic Island pattern (Control Room, SIR Laptop Manager if adopted).

---

## L15: Games/Interactives Playable Inside Chat
**Source:** r33 item 18 (AHome)
**Rule:** Game invites and interactive features must render and be playable directly inside the chat bubble/thread (like Telegram/Messenger game cards). No separate navigation required.
**Apply to all:** Any project with games or interactive messages.

---

## L16: Poll/Question Messages Get Distinct Card UI
**Source:** r33 item 19 (AHome)
**Rule:** Poll-style messages must render as a well-designed card with options, vote counts/avatars, clear visual difference from normal text messages.
**Apply to all:** Any project with polls/questions in chat.

---

## L17: Biometric Lock Register Once, Works Forever
**Source:** r33 item 20, r38 item 1 (AHome)
**Rule:** After enabling biometric lock and registering once, reopening the app must never require re-registering. Fix credential ID/relying-party mismatch, stale references, or race conditions. Add regression test: register in settings, kill and relaunch, verify unlock works without re-registering.
**Apply to all:** Any project with biometric/passkey auth (SIR Laptop Manager, SIR AI, SIR Jobs if they add it).

---

## L18: Native-App Feel (Disable Browser Defaults)
**Source:** r33 item 21, r34 item 6, r35 item 5, OWNER_DEFAULTS.md items 14, 15
**Rule:** Site-wide: disable default browser text selection and right-click context menu. Provide app's own context menu with relevant in-app actions + generic refresh. Must not block normal input field editing (select/copy/paste inside inputs still works). Every text input must do bidi detection per character. Auto-detect currency/region from visitor locale/IP.
**Apply to all:** Every public web product (SIR Jobs, SIR Study, SIR AI, SIR Portfolio, Control Room, SIR Laptop Manager web dashboard).

---

## L19: Click-Target Audit (No Covered/Zero-Size Hit Areas)
**Source:** r34 item 1 (SIR Jobs)
**Rule:** Every interactive element must have a real, unobstructed hit area (min 44px). No absolutely-positioned element may sit on top of a button without intentional `pointer-events`. Browser test: tab-click every visible button/link on each route, assert real click handler fires.
**Apply to all:** Every project. Add automated click-target audit to CI.

---

## L20: Compact Toolbar (No Cluttered Top Bars)
**Source:** r34 item 2 (SIR Jobs)
**Rule:** Top bars must be compact: one toolbar, numbers in labelled chips of consistent height/radius, connection status as small dot+label. No loose text of different heights/weights.
**Apply to all:** Control Room, SIR Laptop Manager, SIR AI, SIR Portfolio, SIR Study.

---

## L21: No Literal "(RTL)"/"(LTR)" in Copy
**Source:** r34 item 3 (SIR Jobs), r35 item 4, OWNER_DEFAULTS.md item 15
**Rule:** Language toggles and any direction labels must show only "English" / "العربية" (or equivalent). Never technical suffixes.
**Apply to all:** Every project with language selection.

---

## L22: Currency Auto-Detection with Manual Override
**Source:** r34 item 5 (SIR Jobs), OWNER_DEFAULTS.md item 16
**Rule:** Default currency display auto-detected from visitor's locale/IP. Manual picker available as override, never as only way.
**Apply to all:** SIR Jobs, SIR AI (if billing), SIR Portfolio, any project showing prices.

---

## L23: Full Visual Redesign to Premium Standard
**Source:** r34 item 7 (SIR Jobs), OWNER_DEFAULTS.md item 1
**Rule:** Simplify information density, align spacing to 4/8px grid, consistent card/button radii, consistent chip styles, spring animations. Remove duplicate navigation entries.
**Apply to all:** Every project. Use shared design tokens and component library.

---

## L24: Biometric Lock Card Centered Vertically/Horizontally
**Source:** r38 item 1 (AHome)
**Rule:** Lock/auth screens must center the main card in the viewport. Localized labels with bdi isolation (e.g., "افتح بالبصمة أو الوجه" not mixed English).
**Apply to all:** Any project with lock/auth screens.

---

## L25: Voice Recording Bar Grows with Spring (No Clipping)
**Source:** r38 items 2, 3 (AHome)
**Rule:** Voice recording bar must grow from input field with spring animation, same height as controls (cancel, timer, pause, send). No clipping, overflow, z-index issues, or safe-area padding problems. AI chat voice must use SAME component as normal chat.
**Apply to all:** Any project with voice recording.

---

## L26: Local Voice Transcription (Five States)
**Source:** r38 item 4 (AHome)
**Rule:** Voice messages must have Transcript button using local model only (whisper.cpp/faster-whisper via local AI service). Five states: idle, working, done, error with retry, empty. Correct Arabic/English per detected language.
**Apply to all:** Any project with voice messages.

---

## L27: Dynamic Island Single Instance, Continuous Morph
**Source:** r38 items 5, 9 (AHome)
**Rule:** Only one Dynamic Island at a time. Continuous spring morph between states. Never two pills visible. Never covers composer or tab bar.
**Apply to all:** Any project using Dynamic Island.

---

## L28: Bottom Tab Bar Never Vanishes
**Source:** r38 item 8 (AHome)
**Rule:** Bottom tab bar must never disappear, page must not zoom unexpectedly, taps must always work. Fix root cause: viewport/visualViewport handling, keyboard, fixed positioning, transform on parent, pinch-zoom. Add regression test.
**Apply to all:** Every project with bottom tab bar (all mobile web apps).

---

## L29: Profile System (Per-User, Local Storage)
**Source:** r38 item 10 (AHome)
**Rule:** Profile: upload photo, display name, nickname, bio, small customizations. Photo and name show in chat headers/person references. Tapping opens profile. Per-user, stored in app's own storage only (never outside service). Five states, photo crop, size limit.
**Apply to all:** Any project with user profiles (SIR Jobs, SIR Study, SIR AI, SIR Laptop Manager).

---

## L30: Card Spacing on 8px Grid (No Sticking)
**Source:** r38 item 11 (AHome calm/wellness page)
**Rule:** Every card must have proper spacing on 8px grid. No content stuck to neighbours. Button labels must have padding and wrap correctly.
**Apply to all:** Every project. Audit all card layouts.

---

## L31: Professional Game Cards (Clean Cover, Title, Action, Score Chip)
**Source:** r38 item 12 (AHome games hub)
**Rule:** Game cards: one clean cover, one title, one primary action, one short secondary line, high score as small chip. Group into clear sections. Proper game logic: scores, levels, pause, restart, sounds off by default. 3D games evaluated for three.js/WebGL upgrade.
**Apply to all:** Any project with games.

---

## L32: Developer Strings Behind Disclosure
**Source:** r35 item 6 (Control Room/Laptop Manager)
**Rule:** Raw IPs, PIDs, "DAEMON: OK" style text must not appear on screens the owner views casually. Move behind a "developer" disclosure if useful.
**Apply to all:** Control Room, SIR Laptop Manager, any dashboard/project with dev/debug info.

---

## L33: Self-Audit Loop (Two Clean Cycles at 4 Widths, 2 Languages, 2 Themes)
**Source:** r33 item 22, r34 item 8, r35 item 7, r38 item 7, OWNER_DEFAULTS.md item 1
**Rule:** Before marking done: open every page/tab/sheet at 320/390/768/1280, Arabic and English, light and dark. Find and fix at least 10 defects nobody listed. Before/after evidence in project's `.sir/evidence/` folder.
**Apply to all:** Every project, every round.

---

## L34: Five States on Every View
**Source:** OWNER_DEFAULTS.md item 1, r38 items 4, 10
**Rule:** Every screen/view must handle: idle, loading skeleton, empty with one action, error with retry, populated.
**Apply to all:** Every project.

---

## L35: Spring Motion (Transform/Opacity Only, 120Hz Safe)
**Source:** OWNER_DEFAULTS.md item 1, r33, r35, r38
**Rule:** All animations use spring physics, transform and opacity only (120Hz safe). No layout-thrashing animations.
**Apply to all:** Every project.

---

## L36: RTL-First with Logical CSS Properties
**Source:** OWNER_DEFAULTS.md item 1, r33, r34, r38
**Rule:** Use logical CSS properties (margin-inline-start, padding-inline-end, etc.). RTL-first design. Bidi isolation for mixed content.
**Apply to all:** Every project.

---

## L37: Design Tokens (Light, Dark, System, High Contrast)
**Source:** OWNER_DEFAULTS.md item 1, standard/23-premium-code-bar.md
**Rule:** Themes: light, dark, system, high contrast. All colors, spacing, radii, shadows via tokens.
**Apply to all:** Every project.

---

## L38: Own Firebase Project and Repo Per Product
**Source:** OWNER_DEFAULTS.md item 2, WORKER_PREAMBLE.md item 13
**Rule:** Every SIR product has its own Firebase project and GitHub repo named exactly after the product. Never reuse AHome's project. Never reuse another product's project.
**Apply to all:** SIR AI, SIR Portfolio, SIR Jobs, SIR Study, SIR Laptop Manager, SIR Controller, SIR Business, etc.

---

## L39: Dual Hosting (Firebase + Vercel)
**Source:** OWNER_DEFAULTS.md item 2, WORKER_PREAMBLE.md item 15
**Rule:** Every public web product hosted on both Firebase Hosting and Vercel. Same build, same env vars on both. Both addresses curl-checked.
**Apply to all:** SIR AI, SIR Portfolio, SIR Jobs, SIR Study, SIR Laptop Manager web dashboard, Control Room.

---

## L40: Version Stays 1.0.0
**Source:** WORKER_PREAMBLE.md item 10, AGENTS.md
**Rule:** Every project and app stays at version 1.0.0 while under development. Never bump, tag, or release a higher version.
**Apply to all:** Every project.

---

## L41: No Secrets in Git, Private Data Stays Local
**Source:** AGENTS.md, OWNER_DEFAULTS.md items 4, 5
**Rule:** No secrets in git. AHome and Habiba data never leaves AHome/local systems. Private exports only in `_local/` (gitignored).
**Apply to all:** Every project.

---

## L42: Messages to Owner Format
**Source:** OWNER_DEFAULTS.md item 6, WORKER_PREAMBLE.md item 12
**Rule:** Title, at most 5 one-fact lines, one action or nothing. Buttons for questions. Egyptian Arabic. End with "المطلوب منك: لا شيء" or single tap needed.
**Apply to all:** Every agent/project sending Telegram messages.

---

## L43: Windows Background Tasks (Pause During Games, Low Priority)
**Source:** OWNER_DEFAULTS.md item 7, WORKER_PREAMBLE.md item 11
**Rule:** Automation runs as Windows background tasks, pauses during games (game-mode snapshot), low priority while owner works. Independent of any chat. Test browsers headless, muted, always closed in finally block.
**Apply to all:** Every project with background automation.

---

## L44: Initiative - Adapt Improvements Across Projects
**Source:** OWNER_DEFAULTS.md item 8
**Rule:** Agents suggest and advise. Capture new ideas into the right plan in the same turn. Adapt improvements from one project to others (new component, new rule, new fix) and record them in this LESSONS.md file.
**Apply to all:** Every agent, every project.

---

## L45: College Work - Practice Sets Only
**Source:** OWNER_DEFAULTS.md item 8, AGENTS.md
**Rule:** Help learn (summaries, practice sets, worked examples, flashcards, mock quizzes). Never solve graded work for submission.
**Apply to all:** SIR Study, any educational content.

---

## L46: Jobs Auto-Apply (Vetted, Truthful, Cap 10/Day)
**Source:** OWNER_DEFAULTS.md item 9, AGENTS.md
**Rule:** Apply automatically to vetted truthful matches (cap 10/day). Report every application and every first answer. Vibe Coder profile only.
**Apply to all:** SIR Jobs only.

---

## L47: AI Fallback Chain (Gemini → OpenRouter → Other Free → Local)
**Source:** OWNER_DEFAULTS.md item 11, plans/AI_FALLBACK_CHAIN.md
**Rule:** Every project's AI calls follow: Gemini flash-lite-latest → flash → any Gemini → OpenRouter free → other free providers → local. One key per project on that project's own Firebase/GCP project and its own OpenRouter key.
**Apply to all:** Every project with AI features.

---

## L48: Scheduled Jobs Use Round Times (:00 and :30)
**Source:** OWNER_DEFAULTS.md item 12
**Rule:** Scheduled jobs use round times (:00 and :30), never odd minutes, except prayer-based duties.
**Apply to all:** Every scheduled task, cron, background job.

---

## L49: Windows App Standard (Installer, Firebase Sign-In, Self-Update, Download Page)
**Source:** OWNER_DEFAULTS.md item 13, plans/WINDOWS_APP_STANDARD.md
**Rule:** Every product with Windows app follows: real installer, Google sign-in on Firebase, self-updating to latest build, Download page on site, private repo with production-only release builds, per-project Product Kit folder, entry in Projects-Hub.html.
**Apply to all:** SIR Laptop Manager, SIR AI, SIR Portfolio, SIR Jobs, SIR Controller, etc.

---

## L50: Browser Audit Probe (Translucent Ancestors + Gradient Stops for WCAG)
**Source:** OWNER_DEFAULTS.md "Adopted from SIR Jobs"
**Rule:** Browser audit probe composites translucent ancestor backgrounds AND every gradient stop before computing WCAG contrast. Treats wrapping `<label>`/pseudo-element hit area as real touch target.
**Apply to all:** Every project's audit scripts.

---

## L51: Escaping Discipline (escHtml, escapeJs, safeHref)
**Source:** OWNER_DEFAULTS.md "Adopted from SIR Jobs"
**Rule:** `escHtml()` for every interpolated text/attribute. `escapeJs()` only inside inline handler args. `safeHref()` allowing only http(s) for every external link.
**Apply to all:** Every project with vanilla JS views.

---

## L52: Dialog and Floating Panel Focus (Move In, Restore Out)
**Source:** r83 (SIR Portfolio AI chat focus, scout finding approved by HQ)
**Rule:** Every conditionally mounted dialog, drawer, sheet or floating panel must move focus into the panel when it opens (first input, or the panel container with tabIndex -1 when there is no input) and return focus to the trigger when it closes (close button, Escape, overlay). Focus must never drop to <body> while a panel is open and must never stay stranded after the panel unmounts; the first Tab from a chat panel then walks the panel controls, not the page behind them.
**Apply to all:** Every product with a floating chat, dialog, sheet, drawer or modal (SIR AI, SIR Jobs, SIR Study, SIR Portfolio, Control Room, SIR Laptop Manager dashboards, AHome sheets).

---

## Design principle for every product (owner, research round 43, 2026-11-12)

**Source:** SIR AI competitor research (`SIR AI/.sir/plans/COMPETITOR_MATRIX.md`, `FEATURE_IDEAS.md`).
**Rule:** Every project runs the same competitor research before its plan is accepted: at least 8 competitors or open-source cousins, each with what it is, licence, pricing (mark third-party prices as unverified), 3 strongest features, 3 weakest flaws, what we copy, and what we do better. Keep the result in `<project>/.sir/plans/COMPETITOR_MATRIX.md`, and at least 40 tagged ideas in `<project>/.sir/plans/FEATURE_IDEAS.md` (each idea tagged `cite` or `original`).
**Checks:** Licences and star counts come from the GitHub API, not from aggregator blogs. Do not clone repos over 150 MB or with a non-open licence; reference them through their docs. Refresh the matrix every quarter and whenever a competitor changes owner.
**Apply to all:** Every project, starting with the next plan review.

---

## How to Use This File
1. **Verifier** checks every task against relevant lessons before marking PASS.
2. **Scouts** read this file daily and test their project against every lesson.
3. **HQ Manager** adds new lessons when owner complains about something.
4. **Every project** must have evidence in `.sir/evidence/` showing compliance.
5. When a new lesson is added, append it here and note "Adopted from <project>" in OWNER_DEFAULTS.md.