# PLAN: SIR ModPack (Wave 6, GLOBAL product, rebuild from zero)

**Version 1.0.0.** Rewritten 2026-11-12 (round r52, HQ). Supersedes the r44 text of this file. The canonical competitor study with dated links is `D:/Projects/_SIR/ops/competitors/sir-modpack.md` (sources opened 2026-11-12). The first ten build tasks for the free agents are in `D:/Projects/_SIR/ops/briefs/sir-modpack-tasks.md`.

**Truth rule for this plan.** Nothing here is called working unless a reviewer saw it today. **The product has never been built.** `D:\Projects\SIR ModPack` holds the kit files, the Desktop folder kit and one legacy project, and nothing that runs. Verified today (2026-11-12): the private GitHub repo `sirahmed8/sir-modpack-source` exists, default branch `main`, last update 2026-11-09 18:37 UTC (`gh repo view`). Verified today: the legacy public repo `sirahmed8/SIR-ModPack` exists and is still **public**, last update 2026-10-30. Not verified: the Firebase project for this product does not exist (no `.firebaserc` in the product folder, and the Firebase CLI was not on the PATH today).

**Product class: GLOBAL.** Anyone in the world can use it, accounts and subscriptions exist, every platform is planned, the owner has an owner-only analytics page, the site is hosted twice (Firebase Hosting and Vercel), and a paid subscription gives the owner every permission inside the product.

**What is still true from the old plan and is carried over:** the mission (a curated, high-performance modpack with a launcher that runs it on a laptop), the hard legal rules (never redistribute the game files, never rewrite the game JAR, verify every download, never store a Minecraft password), the platform reading that a Minecraft launcher is desktop-first, the pricing shape (free core with an optional EGP tier), and the dual-hosting rule.

---

## 1. Who it is for, and the promise

**For the player.** The player in Cairo, Giza, Alexandria or anywhere else who downloaded a modpack once, hit a wall of "Exit Code 1" with a 500-line log, and gave up. They have a laptop, not a gaming PC, and they want the game to run smoothly without reading forum threads about JVM flags.

> One click installs a tuned modpack on your laptop, and when something breaks, the app tells you in one Arabic or English sentence what to do.

**For the friend with the server.** The player who hosts for their friends and loses every session to a crash, a corrupted world or a backup they forgot to take.

> Your own server, on your own machine, with world backups and a crash answer before the group chat starts asking questions.

**The end state we sell.** A player downloads SIR ModPack, signs in with Microsoft, presses one button, and the launcher downloads the exact tuned pack, verifies every file against a signed manifest, picks the right Java, writes the right memory settings for the RAM the machine actually has, and starts the game at a frame rate we measured on that hardware class. Two weeks later something breaks: the launcher reads the crash log, names the mod responsible in one sentence in Arabic, offers the one-click fix, and the player is back in the world. On a second machine, the same signed-in account restores the pack, the settings and the worlds.

**Not in v1:** no ads, no "144+ FPS" without a named benchmark, no Minecraft game file in our repository, no redistribution of a mod whose licence forbids it, no fake players, no invented server counts, no cracked launcher, no shared or modified game account.

---

## 2. The ten competitors, and where we win

Full table with dated sources: `D:/Projects/_SIR/ops/competitors/sir-modpack.md`.

| Competitor | What it proves about the market | Our edge |
|---|---|---|
| CurseForge | The catalogue is where players already look; the desktop app and the auto-update are table stakes | One tuned pack instead of 344,660 projects, no ads, no Overwolf process, hash-checked downloads, Arabic first |
| Modrinth | Open source, an API others build on, and hosting bundled with one-click install; but its Linux app is unstable by its own admission | We do not compete as a catalogue: we compete on a pack tuned for a named laptop class, a crash answer in plain Arabic, and EGP pricing |
| Prism Launcher | The reference for instance isolation, account handling and free redistributability | The same correctness with the setup decisions made for the player; Prism stays GPL-3.0 and unmerged |
| ATLauncher | A long-lived pack catalogue with one-click install still works; the interface is from another decade | Modern motion, fast verification, a server manager, an Arabic guide |
| MultiMC | Predictability and stability are the launcher user's real requirement | The curation and the crash answer on top of a known-good instance model |
| HMCL | Depth of auto-install is respected by power users, and its density is the reason beginners quit | One decision screen for a first-time player, the full depth behind it |
| PojavLauncher | Phones are a real audience for Java Minecraft; running the game on a phone is a different job from controlling your PC | The phone is a remote for the PC launcher and the server, not a pretend laptop |
| GDLauncher | One-click install from both catalogues, no premium upsell, and instance sharing by code | The shared code carries a tuned pack and a server; the phone controls and monitors |
| Feed The Beast | The curated-house model is proven and the most useful business model to copy | The performance promise is a reproducible benchmark, the server is the player's own machine, Arabic first |
| Lunar Client | Frame rate is the headline players care about, and a free client with paid cosmetics converts | A benchmark on named hardware instead of a marketing number, an open configurable pack, the player owns the server |

**Category truth from the sources read today (2026-11-12):** the free tier is expected, CurseForge's ad-supported free tier is the price anchor ($2.99/month for Premium), Modrinth Plus is $4.99/month, Modrinth Hosting starts at $10/month for 4 GB, Aternos proves that free server hosting has a very large audience (142,800,357 users claimed), FTB proves that a curated house can win, and the Mojang rules decide what may be charged for. Our plan follows that truth instead of fighting it.

---

## 3. Features

### 3.1 Parity with the best in the category (must ship)

| Feature | Why it is in the list | Source of the requirement |
|---|---|---|
| One-click install of a named modpack with SHA-256 verification on every file | The core action of every launcher that works | CurseForge, ATLauncher, GDLauncher, FTB App |
| Isolated instances (one pack, one settings folder, one worlds folder, no cross-talk) | The model the whole category copied | MultiMC, Prism Launcher, GDLauncher |
| Official Microsoft account sign-in, no password ever stored | Non-negotiable for a launcher people trust | Prism Launcher, legacy `auth_service.py` and `loopback_service.py` |
| Correct Java handling: detect the installed runtimes, choose the right one, tell the player in words | The number one cause of a failed launch | Legacy `java_service.py` (PE header architecture inspection, HKLM and HKCU registry probing, semver parsing) |
| Memory and JVM settings computed from the machine, with a slider that explains the trade-off | Wrong RAM settings cause crashes and stutter | Legacy `RamSlider` idea in `.sir/MASTER_PLAN.md` |
| A mod list with a licence row for every single mod | Legal baseline and trust | Legacy `docs/MOD_LICENSES.csv` plan, Minecraft Usage Guidelines |
| Mods can be enabled, disabled and updated without reinstalling the pack | Power-user expectation | ATLauncher, HMCL |
| A crash screen that reads the real log and names the cause in one sentence, in Arabic and English | The failure nobody solves | Legacy `crash_analyzer_service.py` (Mixin conflicts, Java mismatch, OutOfMemory variants, native `hs_err` logs, dependency conflicts, corrupted region files, shader compile failures) |
| A server manager: start, stop, logs, players, TPS, RAM, world backup and restore | The session the player actually runs | Legacy `server_core`, `rcon_service.py`, `worlds_service.py` |
| World backups with a restore that is proven by comparing hashes | The thing players lose | Legacy `worlds_service.py` |
| Share a setup with a friend using one code | Proved to work and to be wanted | GDLauncher instance sharing by code |
| Live performance view: FPS, frame time, RAM, CPU, GPU, with the hardware named | Turns a promise into a measurement | Lunar Client, legacy `hardware_monitor_service.py` |
| A guide in Arabic and English that a first-time player can follow with no technical words | Nobody in the category does this well | FTB, legacy `README_AR.md` |
| Updates: the launcher, the pack and the mods update themselves, with a rollback | Table stakes | CurseForge, Modrinth, Prism |
| A clean, fast, native desktop app (no Electron bloat), with the pack catalogue searchable | The daily-use surface | Prism Launcher, Modrinth App, legacy `.sir/MASTER_PLAN.md` |
| Five states on every screen, Arabic RTL first, English second, four themes | House standard | `plans/SHARED_PLATFORM_KIT.md` |
| One-tap data export and one-tap account deletion | Legal baseline | Mojang and Microsoft rules, house standard |
| A website with the download, the mod list with licences, the guide, the legal pages and a support assistant | The trust surface and the discovery surface | FTB, legacy `website-next` |

### 3.2 The owner's own ideas, carried forward from the legacy project and TickTick

Every line says where it came from, so nothing gets silently rebuilt thinner than what he already asked for.

| Idea | Source | Status in this plan |
|---|---|---|
| A performance pack for a laptop class: Sodium, Lithium, FerriteCore, Iris, ModernFix, entity culling, plus 185 curated mods | `legacy/SIR ModPack (v1)/mods` (185 jars; sodium, lithium, ferritecore, iris, modernfix and entityculling present) | M1, the pack itself, each mod with a licence row |
| Crash analyzer that reads the real Java stack trace, the native `hs_err_pid*.log` and the shader error | `legacy/.../development/launcher_core/crash_analyzer_service.py` | M2, the signature feature of the product |
| A one-click video preset engine that writes three layers at once: the vanilla `options.txt`, the Sodium or Embeddium options file, and the Iris or OptiFine shader options, across five tiers (Ultra, Balanced, Performance, Competitive, Potato) for both the modern and the legacy version | `legacy/.../video_preset_service.py` | M3, the same five tiers |
| A plain-language Java discovery that inspects the PE header architecture and probes both HKLM and HKCU | `legacy/.../java_service.py` | M1 |
| An asset integrity verifier with parallel SHA-256 hashing, ZIP CRC validation and quarantine | `legacy/.../repair_service.py` | M1 |
| A live hardware telemetry daemon at 1 second intervals with CPU, RAM and GPU | `legacy/.../hardware_monitor_service.py`, `.sir/MASTER_PLAN.md` item 10 | M2 |
| A controller and gamepad bridge for Xbox and PS5 controllers | `.sir/MASTER_PLAN.md` item 7, legacy `controlify_compat.py`, `controls_service.py` | M4 |
| World backup with rolling snapshots and a restore that compares hashes | `.sir/MASTER_PLAN.md` item 8, legacy `worlds_service.py` | M2 |
| Discord rich presence showing the dimension, biome and elapsed play time | `.sir/MASTER_PLAN.md` item 17, legacy `discord_service.py` | M4 |
| A screenshot gallery that reads the real F2 screenshots and makes a shareable link | `.sir/MASTER_PLAN.md` item 22, legacy `gallery_service.py`, `screenshot_tools_service.py` | M4 |
| A skin studio with a 3D preview | Legacy `skin_studio_service.py`, `website-next/components/Skin3DViewer.tsx`, `/skins` and `/capes` pages | M5, behind the account and the legal pages |
| Shader packs for the modern and the legacy version, tuned separately | `legacy/shaderpacks/SIR Modern Shader.zip`, `SIR Legacy Shader.zip` | M3 |
| A server manager that shows live TPS and RAM and takes automatic world snapshots | Legacy `server_core`, `server_ui` | M2 |
| A silent background updater that never flashes a console window | `legacy/.../installer_core/installer_bridge.py` (uses `creationflags=0x08000000`), `.sir/MASTER_PLAN.md` item 21 | M3, a Windows background task that pauses while a game runs |
| A nightly backup of the user's keybindings, shader options and server list, encrypted | `.sir/MASTER_PLAN.md` item 23 | M4 |
| A local server latency probe with a live player count | `.sir/MASTER_PLAN.md` item 12, legacy `satellite_service.py` | M4 |
| One-click duplication of an instance for testing an experimental mod | `.sir/MASTER_PLAN.md` item 14, legacy `clone_service.py` | M4 |
| A differential sync that repairs only the changed files instead of downloading everything again | Legacy `syncer_service.py`, `.sir/MASTER_PLAN.md` item 5 | M1 |
| An in-product assistant that explains crashes and Fabric setup in Arabic | `.sir/MASTER_PLAN.md` item 13, legacy `website-next/app/crash-analyzer` and `AiChatWidget.tsx` | M5, grounded, with a free quota and a local fallback |
| A weekly visibility check script for the AI answer engines | `.sir/MASTER_PLAN.md` item 18 | M5 |
| A turnkey setup guide in plain Arabic and English for the owner | `.sir/MASTER_PLAN.md` item 24 | M3 |
| A Playwright end-to-end launcher smoke test: launch, verify mods, check the JVM flags, check the ping | `.sir/MASTER_PLAN.md` item 25 | M2 |

**Explicitly dropped from the legacy, with the reason:**

| Legacy thing | Why it goes |
|---|---|
| The 5-pass ASM and namespace auto-remapper that rewrote third-party mod JARs and stripped the Mojang signature | It modifies other people's mods and removes a signature. Mojang's usage guidelines do not allow commercial exploitation of their assets, and shipping a remapper invites both a legal problem and a malware problem. **Not in v1. Not in any version.** |
| "144+ FPS", "100% PASS, zero bugs", "Verified & Signed" | Unprovable claims. The rule is a benchmark with the hardware named, or the sentence does not exist. |
| A custom "SIR Platform License" for the public repo | A public repository needs a licence a normal person can read. The new repo is private and the release artefacts carry a clear proprietary notice with a mod credits page. |
| The two `accounts.json` files that were tracked in history | Account data never goes into git, in this build or in the next. The legacy history was rewritten on 2026-10-29 and a backup bundle kept; the legacy public repo goes private or archived at M6. |
| A copy of Prism Launcher (GPL-3.0) inside `development/` | GPL code must not be copied into a proprietary launcher. Prism stays a separate unmodified tool or is not used at all. |
| A copy of the full Minecraft server and 16.9 GB of assets in the repository | Builds and packs live in release storage, never in git. |

### 3.3 Explicitly out of scope for v1

A cracked or offline-mode launcher, any redistribution of Mojang or Microsoft assets, a mod marketplace where we take a cut, a PvP client that gives an unfair gameplay advantage, a hosting business (we point players at their own machine, and the paid tier is a supporter tier, not a server rental), any "hit registration" or combat-automation mod, and a Minecraft server in our own infrastructure.

---

## 4. Platform matrix

Standing rule (owner, 2026-11-12, `PRODUCT_DIRECTION_2026-11-12.md` section 6): every product ships on every platform. Web, Windows, macOS, Linux, Android and iOS are required. Wear OS, watchOS, TV and car are not in that list, so they are skipped in v1 with a written reason, not left in silence.

| Platform | v1 | What v1 includes | Later |
|---|---|---|---|
| Web (browser) | Required | The whole hub: download, the mod list with licences, the Arabic guide, the support assistant, the pricing page, the legal pages, the owner dashboard | Facts page and `llms.txt` for the answer engines |
| PWA (installable, offline) | Required | Install from the browser, the guide and the mod list work with no signal, the download page works offline | Richer offline actions |
| Windows | Required (M3) | The launcher itself, as a real installer, with the Microsoft sign-in and self-update; plus the hub as an installable PWA from day one | Signed installer (the owner buys the certificate) |
| macOS | Required (M3) | The launcher, unsigned DMG, from the same Rust core as Windows; plus the hub PWA from day one | Signed build when the owner has an Apple account |
| Linux | Required (M3) | The launcher as AppImage and .deb with a .desktop entry, from the same core; plus the hub PWA from day one | Signed package |
| Android phone and tablet | Required (M4) | The companion app: the signed-in account, the download of the pack, a remote control for the PC launcher, the server status and log tail, the crash assistant. **It does not try to run Java Minecraft on the phone** | A Pojav-style on-device launcher is a separate project with its own licence review |
| iPhone and iPad | Required (M4) | The same companion app, same account, same data, tablet layouts | App Store or SideStore (needs a paid Apple account, the owner decides) |
| Wear OS | Skipped in v1 | Nothing | A server-status glance widget, decided with an ADR |
| watchOS | Skipped in v1 | Nothing | Same ADR as Wear OS |
| TV (Android TV and Apple TV) | Skipped in v1 | Nothing | A living-room screen that shows the server status, only if a real user asks |
| Car (Android Auto and CarPlay) | Skipped in v1 | Nothing | Nothing in the launch path; a car is the wrong place for a launcher |
| Widgets and live activities | Part of M4 | Android Glance and iOS WidgetKit: the server status and the last frame time | Richer surfaces later |
| Browser extension | Skipped | Nothing | No browser use case that justifies the store review |
| Docker and self-host | Skipped | Nothing | The server manager runs on the player's own machine, which is the point |

**Rule:** every platform shares one Firebase project, one account and one dataset. The Windows, macOS and Linux launchers come from **one Rust core** with a thin webview shell, so a fix reaches all three at once and the memory footprint stays small. The Android and iOS companion comes from **one Expo app**. No platform ever carries its own copy of the rules.

**Stack decision, to be confirmed by a two-hour spike in M0 with an ADR:** the launcher shell is Tauri v2 (Rust core plus a React and TypeScript interface) rather than the legacy Python and pywebview, because the product needs a native file watcher, a real memory governor and a small idle footprint, and Tauri v2 gives one codebase for the three desktop platforms. The web hub is Next.js 15+ App Router with React 19, TypeScript strict and Tailwind v4 tokens, on Firebase Hosting and Vercel. The engine work (manifest, downloader, hash verifier, crash parser) is Rust in `crates/`, so the same verified code serves the desktop app, the CI and the tests.

---

## 5. Architecture on the shared kit

Base: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`. That file is the shared standards kit every product builds against; SIR Platform was cancelled as a project on 2026-11-12, so there is no extraction target any more. SIR ModPack is a GLOBAL product, so it adopts all twenty sections of the kit as internal `packages/*` with the kit names and interfaces, and when it hardens a piece that other products need, that piece goes back into the kit file and HQ queues the adaptation for the others.

### 5.1 Shape

```
apps/hub            Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 tokens
                    routes: /  /download  /mods  /guide  /support  /pricing  /legal/*  /owner
apps/desktop        Tauri v2 shell (Windows, macOS, Linux) around the same React interface
apps/companion      Expo app (Android, iOS): remote, server status, crash assistant
packages/core       domain types and zod schemas: Pack, Mod, Manifest, Instance, Profile, Server, Backup, Finding
packages/engine     Rust crate: signed manifest, downloader with resume and SHA-256, crash-log parser,
                    JVM argument compiler, options.txt writer, instance manager
packages/kit        owner-auth, billing-fallback, ai-proxy, signed-webhook, legal-pack, help-center,
                    i18n, ui/styles/hooks, design-tokens, motion, notifications, changelog, security-baseline
packages/data       Firestore access layer, repositories, indexes, emulator tests
crates/             the Rust workspace that packages/engine builds on (one workspace, one lockfile)
docs/               MOJANG_RULES.md, MOD_LICENSES.csv, guide/, help/, data-model.md, adr/
scripts/            verify, audit, benchmark, make-icons-and-desktop
```

Layer rule: `apps` depend on `packages`, `packages` never depend on `apps`, `packages/core` depends on nothing. Files under 300 lines, absolute imports, no `any`, typed everywhere.

### 5.2 Accounts (`owner-auth`)

Two identities, kept apart on purpose:
1. **The SIR account** (email, Google sign-in, Firebase Auth): the hub, the owner dashboard, the supporter tier, the companion app and the settings sync. The ID token is verified on the server with JWKS, the session lives in an HttpOnly, Secure, SameSite=Strict cookie, and the owner and admin allow-list fails closed. A forged token gets 403; a client-side flag flip grants nothing.
2. **The Minecraft account** (Microsoft device code): the launcher never asks for a password, never stores one, and never sends the token to our servers. The token stays in the Windows Credential Manager on the player's machine, and the hub only ever sees a display gamertag.

Rule: our server never receives a Microsoft refresh token, and the launcher never asks the user for a Minecraft password. Test: a grep over the repository finds no `accounts.json` and no password field, and the credential store test shows the token is written to the OS store and nowhere else.

### 5.3 Owner-only analytics page

Route `/owner`, gated by a server-verified owner token that fails closed. Real metrics only, each read from an aggregate and never from a whole collection: downloads, installs that completed, launch count, average FPS on the named hardware classes, crash count by cause, server starts, backup success rate, supporter revenue in EGP and in the visitor currency, AI cost, and the error rate. A metric with no data shows a dash with the reason, never a zero dressed as a fact. A non-owner token gets 403 and a forged token gets 403.

### 5.4 AI with the fallback chain

One feature uses AI: the crash explainer. The crash parser is deterministic code and produces the finding (the offending mod, the conflict, the missing dependency); AI only turns that finding into a sentence in Arabic or English, and it only runs after the user presses the explain button. The log itself is parsed **on the player's machine** and only the sanitised finding is sent, never the raw log, unless the user explicitly attaches it.

Chain (`plans/AI_FALLBACK_CHAIN.md`): Gemini `flash-lite-latest`, then `flash-latest`, then any other Gemini text model, then OpenRouter free models, then the other free providers, then the local model on this PC. One Gemini key and one OpenRouter key for this product, both created on **this product's own** Firebase/GCP project, both in the ignored env file and in the Vercel project settings, never in git. Free quota 5 per rolling 24 hours with a visible badge, the owner unmetered, `AI_ENABLED` as the kill switch, a daily cost cap in `config/limits.json`, and the evals written in Arabic and English with the runner exiting non-zero below the threshold. The evals include crash logs where the correct answer is "no mod is at fault", so the model may not invent a culprit.

### 5.5 Data and money

Firestore holds the accounts, the packs and their versions, the mod catalogue with licences, the supporter subscriptions, the crash findings the user chose to share, the support conversations and the leads. The rules deny by default, scope every document to its owner, and are tested in the emulator with a cross-tenant read that must fail. A user's crash findings, worlds and screenshots never leave the player's machine unless the user sends them.

Billing uses `billing-fallback`: the pricing page shows the EGP prices with the currency auto-detected from the visitor locale and IP with a manual override on top, "Subscriptions launching soon" with an email capture while the gateway keys do not exist, Paymob and Fawry in test mode with the keys in the environment only, and a webhook signed with a timestamp inside the payload, verified server-side, idempotent, with ten negative tests. A subscription grants the owner every permission inside the owner dashboard.

### 5.6 Hosting and delivery

The hub is hosted on **Firebase Hosting** (primary, clean Google sign-in screen) **and** on **Vercel** (the GitHub repo imported with the Vercel CLI), same build, same environment variables set in both places, both addresses curl-checked with one retry on timeout, and both written in the project checkpoint. The launcher ships as a signed release feed with a manifest hash, a rollback and a self-update. Operations: a health endpoint at `/api/health`, a nightly backup of Firestore to private storage with a monthly restore test, a nightly manifest verification of the pack, a nightly error digest, a status JSON, and a weekly Telegram report at a round hour.

### 5.7 Security baseline

Firestore rules deny by default. Server-side checks on every mutation. zod validation at every boundary. No secrets in git, gitleaks in CI and pre-commit. A CSP without `unsafe-inline` and without `unsafe-eval`. Analytics load only after consent with Reject All as prominent as Accept. Rate limits on sign-in, downloads, AI and webhooks. One-tap data export and one-tap deletion. Every mod file is verified against a signed manifest before it reaches the instance folder; a mismatch is quarantined, not installed. The licence audit runs in CI and fails the build when a mod has no licence row. No fake data in any path a user can see.

---

## 6. Premium quality bar

This is the floor from `D:/Projects/_SIR/standard/23-premium-code-bar.md` and `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`, written for this product.

**Motion, Apple level.**
- One shared spring config across the app: stiffness 300 to 400, damping 28 to 30, transform and opacity only, no layout thrashing, 120 Hz safe.
- Every sheet, drawer, modal and panel opens and closes with the same spring. An open-only animation is a defect.
- The signature interaction is the **launch sequence**: the download, the verification, the Java choice and the memory choice happen as one continuous surface that grows from the press, and each stage is real progress, never a fake percentage.
- Micro-interactions 100 to 150 ms, standard 200 to 300 ms, large 300 to 500 ms. Press scale 0.98. A reduced-motion path for every animation.
- The active tab shows its label and the others show an icon only, the active tab scrolls into view on load and on change, and the bottom bar never vanishes when the keyboard opens.
- Skeletons match the final geometry, optimistic feedback lands under 100 ms, and there is no white flash on a theme change.

**Two languages, one layout.**
- Egyptian Arabic first for the player, English second for the international market, MSA only in the legal pages. Both ship together, never one as a partial translation.
- RTL designed first: logical CSS properties only, flipped directional icons, Arabic line heights, never a mirrored afterthought.
- Every text input detects Arabic or Latin per character as the user types and moves the caret and the direction live. Every mixed run is isolated with `<bdi>` or `unicode-bidi: isolate`. The words "RTL" and "LTR" never appear to the user.
- Currency auto-detected from the visitor locale and IP, with a manual override on top. Dates and times formatted with `Intl`.

**Five states on every screen.**
Idle, loading skeleton, empty with exactly one action, error with a retry, populated. The empty state never shows a fake mod, a fake server or a fake number.

**Accessibility.**
WCAG 2.2 AA. Every control has an accessible name. Touch targets at least 44 px with no covered hit area. A full keyboard path on every screen, visible focus, zoom from 80 to 200 percent, no horizontal scroll from 320 px to 3840 px, reduced motion honoured, and a colour pair that passes contrast in light, dark, system and high-contrast themes.

**The look.**
One design system: tokens for colour, spacing on a 4 and 8 px grid, radii, shadows, type and motion. The seed is the Emerald Matrix of the legacy (`#10B981`) on Bedrock Obsidian (`#0B0F14`), with Redstone Ruby (`#EF4444`) for danger only. No purple-blue gradients, no emoji headings, no pill buttons on data inputs, no stock filler, no hype words, no em dashes in copy. One component per control, never two. Arabic screen face: Cairo or Tajawal for Arabic, Inter for Latin, JetBrains Mono for the frame-time numbers.

**Native app feel.**
The browser's text selection and the right-click menu are disabled site-wide and replaced by the app's own menu with in-app actions and a refresh. Normal select, copy and paste inside real input fields still work.

**Evidence before the word done.**
Screenshots at 320, 390, 768, 1280 and 1920 px, in Arabic and English, in light and dark, plus 3840 px once. Playwright on the critical journeys. Lighthouse mobile 90 or better. A click-target audit in CI. The self-audit loop runs until two clean cycles.

---

## 7. Free tier and fair pricing (EGP and USD)

These are **test prices**, not published prices. They are the outline the owner confirms against the official gateway fee schedule and against the Mojang rules before anything is charged. The EGP/USD column uses **53.55 EGP for 1 USD**, read from `open.er-api.com/v6/latest/USD` on 2026-11-12, and the pricing page recomputes the conversion from the live rate. The anchor points come from the competitor file: CurseForge Premium $2.99/month, Modrinth Plus $4.99/month, Modrinth Hosting from $10/month for 4 GB.

**The Mojang rule that decides the shape.** The Minecraft Usage Guidelines (read 2026-11-12) allow money for access to a server when the cost is the same for everyone, when everyone who pays gets access to all the mods the server owner enabled, when the owner owns and controls the server the whole time they charge, and when the entitlements do not ruin other players' experience or give a competitive advantage. Cosmetics may be sold, except anything that acts like a player cape. So our paid tier is **a supporter tier for the launcher and the pack**, never a paywall on the pack, never a gameplay advantage, and never a rented server in v1.

| Plan | Who | EGP | USD | What it includes | Rule |
|---|---|---|---|---|---|
| Player Free | Any player | 0 | 0 | The whole launcher, the whole pack, every mod, every shader preset, the crash explainer (5 per day), the local server manager, world backups, the guide in Arabic and English, the account, the settings sync | The core action is never behind a plan |
| Supporter | A player who wants to fund it | 49 per month or 490 per year (test) | about 0.91 per month or about 9.15 per year | Name on the supporters page, an early build channel, a supporter badge in the launcher, and the AI quota raised from 5 to 30 a day. **No gameplay advantage, no mod is locked, no server perk** | Cosmetic and supporter perks only, never gameplay |
| Team | A small group that plays together | 149 per month or 1,490 per year (test) | about 2.78 per month or about 27.85 per year | Everything in Supporter, plus the shared setup code that syncs one player's pack and settings to the others, plus a shared server profile | The share code is a convenience, not a gate |
| Owner | The product owner | 0 | 0 | Everything, unlimited AI, every permission in the owner dashboard | The owner pays nothing and a subscription grants the owner all permissions |

**Fairness rules written into the product.**
1. The launcher, the pack, the mods and the crash explainer are never behind a plan. No mod is locked. No gameplay item is sold.
2. Nothing that affects gameplay is sold, so the Mojang rule about competitive advantage can never be broken by our pricing.
3. Every price on screen is in the visitor's currency, auto-detected, with the original EGP amount next to it.
4. No ads in any tier, ever. The owner sets an ad spend cap of 0 until he changes it.
5. The pack never ships a Minecraft game file. The launcher downloads the game from the official source on the player's machine.
6. A mod whose licence forbids redistribution is downloaded from its author at install time, and the licence row on the website says so.
7. The owner of the product gets every paid feature free.

**Still open and blocking publication:** the official Paymob and Fawry fee schedules for Egypt, the tax treatment of a supporter subscription for an individual in Egypt, the exact refund wording, the code-signing certificate cost, and the lawyer review of every legal page. Each is tagged "(unsourced, verify)" in `ops/competitors/sir-modpack.md` and in `docs/ENV.md` when the project starts.

---

## 8. Milestones M0 to M6, with acceptance tests

Every exit check is something a reviewer can run or click. "Green" means the output was seen, not assumed.

### M0: Foundations, the kit and the honest map of the legacy

Work: create the product's own Firebase project named `sir-modpack` (free Spark plan) and keep it separate from every other product; write the legacy parity matrix over `legacy/SIR ModPack (v1)`; scaffold the monorepo (apps, packages, crates, docs, scripts) with strict TypeScript and Tailwind v4 tokens; make the launcher shell decision with a two-hour spike and an ADR; write `docs/MOJANG_RULES.md` and `docs/MOD_LICENSES.csv`; design the token set; **recreate the Desktop folder kit from scratch for the new build** (the old kit belonged to the legacy build).

Exit checks:
1. `D:/Projects/SIR ModPack` contains `folder.ico` (named exactly that, never `icon.ico`) and the Desktop folder `SIR Projects/SIR ModPack` holds `folder.ico`, `SIR ModPack.lnk`, `Start SIR ModPack dev.lnk`, `Stop SIR ModPack dev.lnk`, `Open project folder.lnk` and `Versions.txt` reading version 1.0.0 and a plain status.
2. `.sir/reports/parity.md` lists every module of the legacy `launcher_core` (37 services), the installer, the server manager, the 32-route `website-next` (the legacy `PROJECT.md` claims 38 routes; the real count is 32 `page.tsx` files), the PyInstaller packaging, the 185 mod jars and the six instance tiers, each with a keep, port, drop or drop-with-reason verdict and the file that proves it. The four drops named in section 3.2 are in that file with their reasons.
3. The verify script runs typecheck, lint, tests, build and gitleaks, and the output was seen green.
4. The Firebase project `sir-modpack` exists, `.firebaserc` names it, and the GitHub repo `sirahmed8/sir-modpack-source` is its only remote.
5. `docs/adr/001-launcher-shell.md` compares Tauri v2 and the legacy Python and pywebview with a measured installer size and a measured start time for each, and `docs/MOJANG_RULES.md` carries the URL and the read date.
6. `docs/MOD_LICENSES.csv` has a row for every mod in the pack with its licence and its source URL, and the licence audit script fails when a row is missing.

### M1: The pack and the verified installer

Work: the signed manifest schema and the generator; the downloader with resume and SHA-256 verification; the instance manager; the Java discovery; the differential sync; the licence audit in CI; the first run of the tuned pack.

Exit checks:
1. A corrupted file is rejected by the installer, the file is quarantined, and the test output is pasted into the report.
2. A download that stops halfway resumes and finishes without re-downloading the completed files, and the test says how many bytes were re-fetched.
3. The pack installs into a temporary folder and every file matches its manifest hash, with the count of files verified printed.
4. `docs/MOD_LICENSES.csv` covers every mod in the pack and the audit exits non-zero when a row is removed.
5. The Java discovery finds the installed runtimes on a real machine and reports the architecture it read from the PE header.
6. The differential sync repairs a changed file without re-downloading the whole pack, and the byte count is printed.

### M2: The crash answer and the server manager

Work: the crash-log parser (Java stack trace, native `hs_err_pid*.log`, OutOfMemory variants, Mixin conflicts, dependency conflicts, corrupted region files, shader compile errors); the plain-language explanation in Arabic and English; the server manager with start, stop, logs, TPS and RAM; world backup and restore; the Playwright launcher smoke test.

Exit checks:
1. The parser names the offending mod for each of 20 real-shaped crash logs in Arabic and English, and a log with no fault is reported as "no mod is at fault" rather than a guess.
2. The server manager starts a test server, the log tail shows its output, the server stops cleanly, and the port is closed afterwards.
3. A world backup is restored and the restore compares hashes to the original, with the comparison printed.
4. The launcher smoke test passes: launch, verify the mods, check the JVM flags, check the ping.
5. Screenshots of the launch sequence and the crash screen exist in `.sir/evidence/` at 390 px and 1280 px in Arabic and English, light and dark.

### M3: The desktop launchers and the twin hubs

Work: the Tauri shell for Windows, macOS and Linux from one Rust core; the self-update and the signed release feed; the Next.js hub with the download, the mod list with licences, the Arabic guide, the pricing page and the legal pages; the Firebase Hosting and Vercel deployments; the Windows background task that checks for updates silently and pauses while a game runs.

Exit checks:
1. The installer installs, starts, signs in with the same account, updates itself, and shows the version and the size on the Download page.
2. The same account on Windows and on the hub sees the same supporter state and the same settings.
3. Both hosts answer: the Firebase URL and the Vercel URL were curl-checked, and both addresses are written in the project checkpoint.
4. The Windows background task updates without flashing a console window, and it does not run while a game is running.
5. The macOS build runs on a macOS runner and the Linux build runs on a Linux runner, with the output pasted in.

### M4: The companion app and the social layer

Work: the Expo companion for Android and iOS (remote control of the PC launcher, server status and log tail, crash assistant, the pack download); the widgets and live activities; the Discord rich presence; the controller and gamepad bridge; the screenshot gallery; the instance sharing by code; the local server latency probe; the nightly backup of the player's own configuration.

Exit checks:
1. The APK builds and installs on a real device, and the same account sees the same state as the desktop app.
2. The remote starts and stops the PC launcher and shows the real state, not a stale one.
3. The instance sharing by code reproduces the same pack and settings on a second machine, verified by comparing the manifest hashes.
4. The Discord presence shows the real dimension and the elapsed time inside the game.
5. The nightly configuration backup restores correctly and the restore hash is logged.

### M5: AI, the guide and the quality pass

Work: the grounded crash explainer with the fallback chain; the support assistant grounded in `docs/help`; the full guide in Arabic and English; the weekly AI visibility check; the self-audit loop.

Exit checks:
1. The AI eval set passes with Arabic and English crash logs, and the assistant refuses a question that is not in `docs/help`.
2. A free user gets the 5-a-day badge and the sixth request is refused with a clear message.
3. When the primary provider is forced to fail, the chain falls through and the answer still arrives, and the log shows which provider answered.
4. The guide is finished in both languages with no missing keys, and a first-time reader follows it with no technical words.
5. Screenshots exist at 320, 390, 768, 1280 and 1920 px in both languages and in light, dark and high contrast, with the five states visible.
6. The accessibility audit passes WCAG 2.2 AA with an accessible name on every control, no covered hit area, and no horizontal scroll from 320 px.
7. Lighthouse mobile is 90 or better and the JSON is saved in `.sir/evidence/`.

### M6: Release, the legal pack and the legacy handover

Work: the launch package (domain, accounts, the code-signing certificate, the lawyer review); the release feed with checksums; the legacy public repo made private or archived; the legacy handover.

Exit checks:
1. A release build carries a checksum, the Download page shows the version and the size, and the rollback restores the previous build.
2. The legacy public repo `sirahmed8/SIR-ModPack` is private or archived and verified with `gh repo view`.
3. Every legal page exists under `/legal/*`, each marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch", and the privacy policy matches what the product really collects.
4. The Mojang rules file has been re-read on the release date and the pack still complies.
5. Each legacy folder moves from `legacy/` to `D:\Projects\old projects\` only after the parity matrix shows every kept feature is ported and verified, keeping the git history. `legacy/` is never deleted from the repository history.
6. The two hosts answer the day of the release, checked with curl.

---

## 9. The first ten tasks for the free agents

Ready to queue, each with its own brief: `D:/Projects/_SIR/ops/briefs/sir-modpack-tasks.md`.

1. Legacy parity matrix over the whole legacy project, read-only, into `.sir/reports/parity.md`.
2. Monorepo scaffold, tokens, RTL, the health route and the verify pipeline.
3. The product's own Firebase project and the `owner-auth` package with negative tests.
4. The signed manifest schema, the licence table and the licence audit.
5. The downloader with resume and SHA-256 verification, and the quarantine of a bad file.
6. The Java discovery, the JVM argument compiler and the `options.txt` writer.
7. The crash-log parser and the plain-language finding in Arabic and English.
8. The shared UI kit: tokens, the four themes, the five states, the spring components.
9. The hub: the download page, the mod list with licences and the Arabic guide.
10. The server manager with start, stop, logs, world backup and a restore that compares hashes.

---

## 10. Skills from the library that this build uses

Picked from `D:/Projects/_SIR/ops/SKILLS_INDEX.md` and the digests in `D:/Projects/_SIR/ops/encyclopedia/deep/`. Every path below was checked to exist on 2026-11-12.

**Design and UI**
- `anti-vibecoded-design-system` - keeps the launcher away from generic AI styling and purple gradients.
- `taste-design-engine` - the self-audit against AI patterns before the screens ship.
- `emil-motion-impeccable` - the spring physics for the launch sequence, the sheets and the tab bar.
- `modern-ui-ux-design-system` - tokens, micro-interactions and hierarchy for one design system.
- `high-conversion-copywriting` - the promise line and the download page copy that sell the end state without hype.
- `commercial-app-blueprint` - `llms.txt`, the trust signals and the sticky call to action on the hub.
- `a11y-debugging` - the accessibility audit with Chrome DevTools against WCAG 2.2 AA.
- `modern-web-guidance` - the current web APIs, container queries and dialog behaviour, run before any client-side work.
- `react-best-practices` and `nextjs` - the hub's App Router structure, Server Components, rendering and performance.
- `mobile-ergonomics-polish` - touch targets, no horizontal scroll and tap feedback in the companion app.

**Desktop, Rust and the engine**
- `modern-app-engineering` - the shared architecture for the Tauri v2 desktop shell and the Expo companion.
- `binary-reverse-engineer` - reading the Java stack trace format and the JAR metadata the manifest needs.
- `graphify-ast-memory` - mapping the 16.9 GB legacy tree into a deterministic AST graph so the parity matrix is not guesswork.

**Security and legal**
- `firestore_rules_creation` - the deny-by-default rules for every collection.
- `firebase_security_rules_auditor` - the audit that finds a cross-tenant read before a user does.
- `zero-trust-security-hardening` - server-side role checks, secure cookies and rate limiting.
- `owasp-vulnerability-shield` - the OWASP pass over the download endpoints, the manifest and the webhook.
- `vibe-auth-hardening` - the five auth flaws a fast build introduces, including the owner route.
- `legal-compliance-shield` - the legal pack that matches what is actually collected.
- `cookie-debugging` - the consent banner behaviour and the cookie audit on the hub.

**AI**
- `gemini-api-dev` - the Gemini calls and the structured output for the crash explanation.
- `ai-gateway` and `omniroute-resilience-gateway` - the fallback chain and the failover on quota errors.
- `firebase_ai_logic_basics` - Firebase AI Logic when it becomes cheaper than a direct call.

**Automation and operations**
- `chat-sdk` - the Telegram bot for the weekly report and the crash digest.
- `verification` - the end-to-end check before the word done.
- `pc-storage-guardian` - the disk checks around the downloads, the cache and the backups, protecting the SSD.
- `direct-action-shield` - the short, factual messages to the owner.

**Data, hosting and growth**
- `firebase_firestore` - queries, indexes and the data model.
- `database-reliability-transactions` - the atomic manifest and entitlement writes with idempotency keys.
- `firebase_hosting_basics`, `vercel-cli`, `deployments-cicd` and `env-vars` - the two hosts with the same build and the same variables.
- `open-seo-auditor` and `google-preferred-sources` - Arabic search visibility, JSON-LD and the AI answer check.
- `system-design-architect` and `production-engineering-standards` - the zero-mock persistence and the production bar.
- `production-engineering-standards` also covers the zero-mock rule for the crash parser and the downloader: no fake progress, no invented results.

---

## 11. Risks and the defaults we take

- **Mojang and Microsoft rules decide what can ship.** Default: read `docs/MOJANG_RULES.md` again at M6, keep the launcher free, keep the pack free, sell a supporter tier with cosmetic perks only, and never redistribute the game files.
- **Mod licences decide what can be packaged.** Default: a mod whose licence forbids redistribution is downloaded from its author at install time, and the licence row says so on the website.
- **The legacy repo is 16.9 GB and the public repo is still public.** Default: the new repo holds source only; the legacy public repo goes private or archived at M6; the legacy history is never deleted.
- **The performance promise is the easiest way to be wrong.** Default: no FPS number exists in any user-facing path unless a benchmark script produced it on named hardware, and the benchmark output is stored next to the claim.
- **A launcher is a security product.** Default: the launcher holds a credential, so the credential stays in the OS store, the download is hash-verified against a signed manifest, and the manifest is the only source of files.
- **The old ASM remapper is tempting and must not return.** Default: it is dropped for good, with the reason written in the parity matrix so a later agent does not "restore" it.
- **Java and Minecraft move fast.** Default: the pack is versioned per Minecraft release, the launcher supports the current version and the one before, and the update watcher tells the player when a new version exists.
- **Every platform at once is a lot.** Default: one Rust core for the three desktop platforms and one Expo app for the two mobile platforms, so the platform count costs builds, not duplicated code.

---

## 12. Only the owner can do

Buy the domain and point it at both hosts. Sign in once on the Google OAuth screen so the branding is right. Create the Microsoft Azure application for the device-code sign-in and paste the client id into the ignored env file. Buy the code-signing certificate for the Windows installer. Create the Paymob and Fawry business accounts and paste the keys. Create the Apple developer account and the Play Console accounts when the reinstallment ladder allows. Lawyer review of the legal pages. Rotate the legacy keys.

Everything else is an agent's job.

---

## 13. Sources and files

- Canonical competitor study with dated links: `D:/Projects/_SIR/ops/competitors/sir-modpack.md`
- The ten build briefs: `D:/Projects/_SIR/ops/briefs/sir-modpack-tasks.md`
- Shared kit: `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`
- AI chain: `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md`
- Quality charter: `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md`
- Desktop and Windows standard: `D:/Projects/_SIR/plans/WINDOWS_APP_STANDARD.md`
- Product direction: `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md`
- Legacy sources, read-only: `D:/Projects/SIR ModPack/legacy/SIR ModPack (v1)`
- Legacy facts and red flags: `D:/Projects/_SIR/ops/inventory/SIR-ModPack-and-GTA-V-mods.md`
- Legacy project kit: `D:/Projects/SIR ModPack/.sir/` (`MASTER_PLAN.md`, `PLAN.md`, `DESIGN.md`, `PLATFORMS.md`, `TASKS.md`)
- Owner ideas: `D:/Projects/_SIR/ops/TICKTICK_MAP.md` and `plans/PROJECT_MERGE_RECORD.md`
- Rules read on 2026-11-12: Minecraft Usage Guidelines (`https://www.minecraft.net/en-us/usage-guidelines`)

---

## 14. Plan refresh r61 (2026-11-12): rescan findings, new research, risks and open questions

Rescan per `ops/WORKER_PREAMBLE.md` rule 20: re-read the product folder read-only (`.sir/PLAN_REFRESH.md`, `CHECKPOINT.md`, `AGENTS.md`, kit files), this plan, `sir-modpack-DEEP.md`, `ops/briefs/sir-modpack-tasks.md`, `ops/competitors/sir-modpack.md`, `ops/inventory/SIR-ModPack-and-GTA-V-mods.md`, `ops/TICKTICK_MAP.md` (the "Rotate secrets, Day 1" row names this product) and `PRODUCT_DIRECTION_2026-11-12.md`, then ran fresh web research. Log of the rescan: `plans/sir-modpack-REFRESH-LOG.md`.

### 14.1 What the 2026-11-12 research changed

1. **Minecraft abandoned `1.x` numbering.** Since 2026 Java Edition uses `YY.N` (year, then drop number, then optional hotfix `YY.N.H`): 26.1 "Tiny Takeover" (2026-03-24, the first release under the scheme, replacing what would have been 1.22), 26.1.1, 26.1.2, 26.2 "Chaos Cubed" (2026-06-16), 26.3 "Wilderness Bound" (2026-09-15); the last `1.x` release was 1.21.11 in December 2025. **Java 25 or newer is required from 26.1 onward** (Mojang version files declare it; performance packs like Fastly Optimised already ship 26.4 snapshots). The Java discovery, the JVM compiler and the pack versioning must treat `26.N` as a first-class version family, not a snapshot, and must never parse it as a pre-release string. Written into task T11 and the version-matrix rule below.
2. **PojavLauncher is dead; Amethyst is the live successor.** PojavLauncher was archived on 2025-09-23 and points to `AngelAuraMC/Amethyst-Android` (LGPL-3.0, ~2.4k stars, still committing in October 2026, supports up to 26.3-snapshot-1, ships its own OpenJDK 21 mobile port and is adding Java 25). A flood of fake "PojavLauncher" APK mirror sites is documented. This validates the plan's M4 choice: our Android companion **remotely controls the PC launcher** and never emulates a laptop; it also adds a warning to the companion's store listing and docs never to link APK mirrors.
3. **New launcher competitors the matrix did not name.** Dawn (dawn.gg: free, ad-supported, Fabric/Forge/NeoForge profiles, Windows/macOS/Linux, modpack install as a profile), Millida Launcher (free, sign-in by nickname, Modrinth packs one click, explicitly targets low-end PCs and Pojav-class devices), Modgrade (modpack security and privacy grading per file, "all 63 mods checked"), and Fastly Optimised (a pack tuned for PojavLauncher-class devices, already on 26.4 snapshots). All added to `ops/competitors/sir-modpack.md` with what we copy and where we still win.
4. **Microsoft sign-in has a gate we must plan for.** Device-code flow against `login.microsoftonline.com/consumers` still works, but the Azure application (client) ID must be submitted to Mojang for approval (`aka.ms/mce-reviewappid`) before it can call Minecraft Services; unapproved IDs fail with "Invalid app registration". XSTS errors `2148916233` (account does not own Java Edition) and `2148916238` (Xbox Live unavailable in the user's country) are the two real failure modes to design the Arabic/English error copy around. Refresh tokens enable silent re-auth for roughly 90 days of inactivity. The Azure registration and the Mojang approval submission are owner steps (section 12) plus a documented engineering task (T45).
5. **Modrinth API v2 is official and has had a real outage.** API v2 is the supported surface (PAT and OAuth2; CORS open). In April 2025 the API went read-only during a database incident and Prism Launcher broke for a day. Lesson written into the plan: every catalogue fetch goes through one adapter with cache, retry and a "catalogue unreachable, your installed pack still works" state, and we never hard-depend on a live API for an already-installed pack.
6. **The `.mrpack` format is the interop standard.** Modrinth packs are a zip with `modrinth.index.json` plus `overrides/`; supporting import (not hosting) costs little and instantly makes thousands of packs installable through our verified pipeline. CurseForge packs use a different manifest; supporting read-only import of both is now a planned task (T12, T13), still with the rule that we never redistribute files whose licence forbids it.

### 14.2 Version-support rule added to the plan

- The pack is versioned per Minecraft release. v1 supports **the current Java release and the one before it** (today that is 26.3 and 26.2), plus the last `1.x` line (1.21.11) for players on older hardware, because loader and mod ecosystems lag new drops by weeks. Each pack version names its exact game version, loader and Java requirement (Java 25 for 26.x).
- A `YY.N` version must never be treated as a snapshot or beta by the parser, the manifest or the UI. Snapshot and preview builds are supported only behind an explicit "preview" flag, never in the default pack.
- The Java discovery probes for Java 8, 17, 21 **and 25** runtimes and reports which one each installed pack needs.

### 14.3 New risks and the default taken

- **Risk: Mojang rejects or delays the Azure client approval.** Default: the owner submits the app registration in M0 (it is a form plus the `aka.ms/mce-reviewappid` request); the launcher ships with the device-code flow behind a feature flag, and the error screen for "Invalid app registration" explains the state in plain words instead of crashing. Microsoft sign-in is the only account path; no offline/cracked mode ever ships.
- **Risk: Mojang changes auth again.** Default: the auth layer is one Rust module behind a trait; a second provider (e.g. a future flow) plugs in without touching the UI; the parity matrix records every auth call site.
- **Risk: Java 25 adoption lags on players' machines.** Default: the launcher downloads the correct Mojang runtime build for the pack's version (the same mechanism vanilla uses), so the player never installs Java by hand; the "find Java" screen only appears when auto-download fails.
- **Risk: `.mrpack`/CurseForge import becomes a piracy or licence vector.** Default: import means "read the pack index, verify each file's hash where the index provides one, download from the original source"; files whose source licence forbids redistribution are fetched from the author at install time and the licence row says so; nothing is hosted or re-served by us.
- **Risk: new competitors (Dawn, Millida, Amethyst ecosystem) ship faster.** Default: our differentiation stays the same three things no competitor combines: a pack tuned for a named laptop class with a reproducible benchmark, the plain-language crash answer in Arabic and English, and EGP pricing with a local server manager. The competitor file is re-read at every milestone.

### 14.4 Open questions and the recommended answer for each

| Question | Recommended answer |
|---|---|
| Which game versions does v1 support? | 26.3 and 26.2 (current and previous drop), plus 1.21.11 as the legacy line for older hardware. Each pack pins its loader and Java requirement. |
| Does the Android app ever run the game on the phone? | No. It is a remote and monitor for the PC launcher plus the server status; on-device Java is a separate project (Amethyst proves it is possible, LGPL-licensed) and is not in this plan. |
| Do we support `.mrpack` and CurseForge pack import in v1? | `.mrpack` import yes (cheap, huge interop win); CurseForge manifest import yes in read-only form; we never host or re-serve third-party files. |
| What happens while the Azure app awaits Mojang approval? | Ship behind the flag; the sign-in screen shows a clear "sign-in is being enabled" state. There is no offline or cracked account path (Mojang requires a genuine account and our rules forbid one), so approval is an M0 owner step, not optional. |
| Should the launcher offer CurseForge/Modrinth browsing inside the app? | No in v1. The pack is curated; power users get mod enable/disable/update inside the instance, and a link out to the catalogues for browsing. A catalogue is a different product. |
| How do we handle the April-2025-style Modrinth API outage? | One catalogue adapter with cache and retry; installed packs never depend on the live API; the hub shows "catalogue unreachable" honestly. |
| Is a supporter tier still legal under the Mojang rules? | Yes, per the 2026-11-12 reading: cosmetic/supporter perks only, no gameplay advantage, no locked mods, cost-equal-for-everyone if any server feature is ever sold. Re-verify at M6. |

### 14.5 Task list

`ops/briefs/sir-modpack-tasks.md` now holds **50 tasks** (T1 to T50), each with files, steps, an acceptance test and the skills from `ops/SKILLS_INDEX.md` that fit. T1 (parity matrix) is done; T2 to T10 are unchanged; T11 to T50 cover the version matrix and Java 25, `.mrpack`/CurseForge import, instances, presets, shaders, mods UI, server UI, backups, crash AI, assistant, all three desktop builds, self-update, hub pages, dual hosting, Firestore, billing, companion, sharing, Discord, gamepad, gallery, skins, config backup, benchmark harness, latency probe, device-code auth, i18n/a11y, launch and handover. The first ten stay ready to hand to agents.
