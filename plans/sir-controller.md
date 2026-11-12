# PLAN: SIR Controller (Wave 8, GLOBAL product, PLANNING ONLY since 2026-11-12)

Audited 2026-11-12 (r61 refresh, rule 20). Replaces `SIR Controller (v1)` and `SIR Optimizer` (both in `legacy/`, kept until M6). The controller part is derived from the open-source x360ce project, so it is not Ahmed's own work; the optimizer part is his. Whether to sell any of it is decided at M0 by the licence audit.

**Status 2026-11-12: PLANNING ONLY.** Owner order: free tools must NOT start building. No code, no repo, no folder changes until the owner says build. Current projects allowed to build: SIR Study, SIR Jobs, SIR AI, SIR Laptop Manager, SIR Portfolio (see plans/PRODUCT_DIRECTION_2026-11-12.md and ops/bus/team.md rule 22).

## 1. Purpose (plain words) and Promise

SIR Controller is a game controller mapper and PC gaming optimizer for Windows gamers. It makes PlayStation, Switch and wheel controllers work as Xbox controllers in any game, and it scans a Windows laptop explaining in plain words what slows it down. **One-sentence promise**: Enable any gamer, anywhere, to use any controller with zero setup and zero anti-cheat risk, while their PC stays honest about what it can and cannot speed up. Arabic and English first, five states, Apple-level motion, no fake claims.

Honesty rule baked into the promise: we never claim FPS boosts. Every performance claim ships with a reproducible benchmark on named hardware, or it does not ship.

## 2. Names and IDs

| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Controller` |
| GitHub (private) | `sirahmed8/sir-controller` (legacy repos `sirahmed8/SIR-Controller`, `sirahmed8/sir-optimizer`) |
| Stack (planned) | Mapper: keep existing .NET core (Engine, tests); UI decided by spike ADR (WinUI 3 vs Tauri v2). Optimizer: .NET 8 or PowerShell engine + Tauri UI. Web portal: Next.js 15+ on Cloudflare Pages |
| Domain | Old plan used `sircontroller.app` and `siroptimizer.com`: neither resolved when last checked (2026-10-29); owner checks and buys; price "(unsourced, verify)" |
| Platforms | **GLOBAL:** Windows ✅ (both tools first); Web portal ✅; macOS ⏭️; Linux ⏭️; Android ⏭️; iOS ⏭️; TV/watchOS/Car ⏭️. All share the Firebase project and auth |
| Money | Free core mapping. Pro in EGP for profile sync + optimizer suite; 249 EGP/month and 1,999 EGP/year appear in legacy strings; test prices only, "(unsourced, verify)". EGP first, USD/SAR/AED toggle auto-detected with manual override. "Launching soon" + email capture until keys exist. Owner gets all Pro features free |

## 3. Current state

Not started. `.sir/CHECKPOINT.md` is the HQ setup note; 9 commits, setup and plan only. PORTFOLIO.md: 2 of 20 tasks. Legacy facts (inventories 2026-10-29, nothing run): Controller is a WinForms app on .NET Framework 4.6.2 with ~410 vendored engine files and a commit claiming "298/298 MSTest pass" (unverified); ~20 binaries tracked in git; LGPL-3.0 text beside a proprietary EULA naming "SIR Systems LLC" (no evidence this company exists: remove the name unless the owner confirms a real registered entity); three identical generic agent files; download button pointed at a private repo; unsigned webhook and client-side owner gate with a hard-coded email. Optimizer: client-side owner flag flip, AI keys in the web bundle, open CORS chat route with no auth, simulated owner transactions, nested `public_repo/.git`, tracked .exe/.zip files.

## 4. Research findings 2026-11-12 (rule 20 refresh, load-bearing)

Full detail and links in `ops/competitors/sir-controller.md` (section 0) and `plans/sir-controller-REFRESH-LOG.md`. The ones that change the plan:

1. **ViGEmBus is retired.** github.com/nefarius/ViGEmBus archived 2023-11-02, BSD-3-Clause, "THIS PROJECT HAS BEEN RETIRED". Successor **Nefarius VirtualPad** is commercial, partner-only. DS4Windows releases still install ViGEmBus 1.22.0. Plan impact: depend on ViGEmBus 1.22.0 as a pinned, hash-verified prerequisite; never vendor the driver into git; show honest install state; track migration.
2. **Windows timer resolution is per-process since Windows 10 2004**, and Windows 11 does not grant high resolution to fully occluded or minimized window-owning processes. `timeBeginPeriod(1)` in our daemon does NOT speed up games. The legacy "0.5 ms timer" claim must be reworded: the optimizer can only (a) request high resolution for its own process, (b) detect whether a game raised its own resolution, (c) document it. Any public claim of game-wide 0.5 ms is false and must never ship. Source: learn.microsoft.com timeBeginPeriod (fetched 2026-11-12).
3. **Nagle's algorithm is TCP-only; most games use UDP.** `TcpAckFrequency=1`/`TCPNoDelay=1` are harmless but mostly irrelevant to ping. Keep them as an optional, clearly-labelled "TCP games only" toggle with undo; never as a headline feature or marketing claim.
4. **DS4Windows ecosystem is fragmented** (Jays2Kings archived 2021; ds4windowsapp/DS4Windows GPL-3.0, active 2026-03; Ryochan7 gone). **PadForge** (hifihedgehog, .NET 10, SDL3, pushed 2026-11-12, licence unknown) is the strongest new open entrant. x360ce is alive (pushed 2026-11-11) but shows no licence file via the API. The M0 licence audit is a hard gate on the whole product, not a formality.
5. **No competitor ships Arabic RTL-first UI**, honest no-boost claims, or one-installer ViGEm onboarding. That is the defensible wedge.
6. ExitLag pricing numbers were JS-rendered and not captured; all prices in the matrix stay "(unsourced, verify)" until the sourcing tasks in the competitor file are done with links and dates.

## 5. Rules (each needs a test or command)

1. **Licence audit first (M0):** every vendored component with licence in `docs/THIRD_PARTY.csv`; LGPL-3.0 parts stay replaceable (dynamic link or source offered); EULA must not contradict the licence; x360ce licence file read directly and recorded. Selling allowed only if the audit says so; otherwise the controller stays free and only the optimizer is Pro. Legal reading is the lawyer step.
2. **Driver-level changes are risky:** ship a read-only scan first. Any change to Windows settings is a dry run with an undo (restore point or saved registry export), tested on a VM.
3. **No binaries in git:** releases hold installers; CI check fails on files over 5 MB.
4. **Server-side owner and Pro checks only** (verified ID token, allow-list), using `owner-auth` from SHARED_PLATFORM_KIT. Test: client flag flip changes nothing.
5. **No AI key in any bundle:** chat route authenticated, rate-limited, CORS locked, using `ai-proxy` from SHARED_PLATFORM_KIT.
6. **Webhooks signed with timestamp inside the payload**; idempotent; using `signed-webhook` from SHARED_PLATFORM_KIT.
7. **No fake transactions or numbers in the owner dashboard:** empty states are honest.
8. **"OP mode"** exists only server-verified for the owner account.
9. **No performance claim without a reproducible benchmark script on named hardware.** No "boosts FPS by X percent" anywhere, including README, store listings, site and press.
10. **Owner-only analytics page:** separate route, server-verified owner token, real metrics only (downloads, installs, scan runs, errors). No other user sees it.
11. **ViGEmBus is a prerequisite, never a vendored binary.** Installer downloads 1.22.0 from the official GitHub release with SHA-256 verification; failure shows honest recovery steps; uninstall removes only what we added.
12. **Timer-resolution honesty:** the optimizer may only report the resolution of the calling process and whether the foreground game requested one; it must never claim game-wide 0.5 ms.

## 6. Features list

**Mapper features:**
- One-click guided install of ViGEmBus 1.22.0 (hash-verified) and optional HidHide
- Per-game profile editor: button remapping, analog stick deadzone calibration, trigger saturation, sensitivity curves (linear/exponential/S-curve)
- Live test pad for verifying mappings in real time
- Profile per-game switching based on active window detection (process watcher)
- Settings and Profile tabs with save/load; profile export/import (file) for sharing
- Gyro/motion support and DualSense lightbar/rumble (M2+, after core ships)
- Multi-controller player-slot assignment (up to 4 pads)
- DirectInput to XInput auto-mapper for generic retro pads (M2+)

**Optimizer features (read-only first):**
- Read-only scan of startup items, disk free space, power plan, network adapter config, background services; plain-language findings in Arabic and English
- Fix with preview and undo (`.reg` delta backups before any system modification)
- Standalone `restore_all_defaults.ps1` reverting every tweak to Windows defaults
- Timer-resolution diagnostics: report resolution of our process and of the foreground game; no false game-wide claims (see rule 12)
- Optional Nagle toggle clearly labelled "TCP games only" with undo
- Safe-mode anti-cheat guard: detects competitive game processes; restricts actions to user-mode, certified-safe operations
- Daemon budget: under 25 MB RAM, 0.1% CPU idle, `CREATE_NO_WINDOW = 0x08000000`

**Owner ideas from TickTick and legacy:**
- Arabic RTL-first UI with English; bidi-isolated mixed text inputs
- Five states on every screen; spring physics motion; high-contrast tactile UI with zero yellow buttons
- Device list with one-click install and profile preview
- Dashboard showing scan findings, fix history, per-game profile
- "Why is my game stuttering?" support assistant grounded in a cited known-issues catalog (no AI improvisation on system fixes)

**Explicitly cut or demoted after 2026-11-12 research:**
- "Sub-millisecond Windows timer resolution for your games" as a headline claim: cut (per-process since Win10 2004; see rule 12)
- GPU pre-render queue / DWM flip-model registry tweaks: demoted to "experimental, off by default, undo required, VM-tested" — weak evidence, high risk
- Rapid-fire/macro remapping: single-player accessibility only, clearly labelled; never advertised for competitive play; disabled in safe mode

## 7. Screens (desktop app) and portal (web)

**Desktop app screens (each: five states, Arabic RTL + English, 44 px targets):**
1. Onboarding/install wizard (driver check, hash verify, HidHide optional, first game detection)
2. Home/dashboard (connected devices, active profile, last scan summary, one-click scan)
3. Devices (detected pads, install/configure, HidHide hide toggles)
4. Test pad (live visualization: buttons, sticks with deadzone rings, triggers, gyro)
5. Calibration lab (radial deadzone, anti-deadzone, per-axis curves)
6. Trigger lab (hair trigger, actuation point)
7. Profiles (list, per-game auto-switch rules, duplicate/export/import, default)
8. Optimizer scan (findings list with risk labels: safe/caution/avoid, Arabic + English explanations)
9. Fix preview + undo history (`.reg` delta viewer, one-click restore)
10. Settings (theme light/dark/system/high-contrast, language, daemon autostart, update channel)
11. About/diagnostics (versions, driver state, timer resolution report, export diagnostics bundle)

**Web portal screens:** Landing, Downloads (hash-verified, version history), Pricing (Launching Soon + email capture), Privacy/Terms/Refunds, Help center, `/owner` analytics (server-gated), status page.

## 8. Data model (Firestore, GLOBAL shared project)

Collections (owner-only where marked; never store personal file contents):

- `users/{uid}` — profile, locale, createdAt, plan (free|pro), proUntil
- `devices/{uid}/items/{deviceId}` — controller VID/PID, name, connection (usb|bt), lastSeen; no input data stored
- `profiles/{uid}/items/{profileId}` — name, gameMatch (exe list), mapping JSON, curves, deadzones; export/import supported
- `scanRuns/{uid}/items/{runId}` — timestamp, findings summary (counts, not full registry contents), app version; 90-day TTL
- `fixHistory/{uid}/items/{fixId}` — fixId, appliedAt, regDeltaRef (local, never uploaded), undoneAt
- `licenses/{uid}` — plan, source (paymob|fawry|manual), activatedAt, webhookEventId (idempotency)
- `leads/{email}` — launch-notification signups, source, createdAt
- `analyticsDaily/{date}` — owner-only aggregates: downloads, installs, scanRuns, errors, proActivations
- `errorReports/{id}` — owner-only, opt-in crash payloads, 30-day TTL, no personal paths
- `aiUsage/{uid}/{day}` — counters for free-tier rate limits (5/day)

Local-only (never synced): `.reg` deltas, diagnostics bundles unless user taps "send".

## 9. API list (portal, Next.js route handlers / server actions)

- `POST /api/auth/session` — Firebase ID token -> HttpOnly session cookie (SameSite=Strict), rate-limited
- `GET /api/me` — verified session -> profile; 401 otherwise
- `POST /api/leads` — email capture, validated, deduped, rate-limited
- `GET /api/downloads/latest` — signed URL + version + SHA-256 manifest
- `POST /api/webhooks/paymob` — signed (timestamp in payload), idempotent, activates license
- `POST /api/webhooks/fawry` — same, Fawry payload shape
- `POST /api/ai/chat` — authenticated, `ai-proxy` chain, free 5/24h, CORS locked
- `GET /api/owner/metrics` — owner allow-list only; aggregates from analyticsDaily; 403 otherwise
- `GET /api/health` — public, no data
- Portal pages are static where possible; `/owner` is server-rendered with middleware gate

Desktop app talks to Firebase directly (Auth + Firestore) with offline persistence; no always-on server needed for mapping.

## 10. AI features (fallback chain via `ai-proxy`)

1. "Why is my game stuttering?" assistant — grounded ONLY in `docs/help/*.md` + a cited known-issues catalog; refuses system-destructive suggestions; free tier 5/day
2. Plain-language explanation of scan findings (rules first; AI only to rephrase, never to decide safety)
3. Profile suggestion from a game title (maps to a starter template; user confirms)
4. Support drawer shared component across products (KIT `help-center`)
5. Evals: Arabic + English sets run in CI before each release; no answer may advise registry edits outside the safe catalog

## 11. Security and privacy

- Server-side owner/Pro checks only; client flags are cosmetic
- Secrets in env only; gitleaks in CI; no keys in bundles (rule 5)
- Signed webhooks; idempotent activation; replay rejection
- Least-privilege Firestore rules; per-user isolation; owner analytics reads aggregates only
- Telemetry: opt-in, anonymous, counts only; no file paths, no document names, no keystrokes (impossible by design: we never read input content beyond mapping)
- Privacy policy + terms: AI-drafted, marked for Egyptian attorney review before commercial launch; delete-my-data flow deletes `users`, `profiles`, `scanRuns`, `aiUsage` for the uid
- Driver install: SHA-256 pinned ViGEmBus; no self-update without signature check; failure = honest error + manual steps
- AHome/Habiba data: never touched, never leaves local systems

## 12. Monetisation

- Free forever: mapping core, deadzone/curve calibration, test pad, basic scan (read-only), Arabic/English UI
- Pro (EGP first, USD/SAR/AED toggle): profile cloud sync, optimizer fix engine, fix history, priority support, launch-notification perks; test prices 249 EGP/month or 1,999 EGP/year "(unsourced, verify)"; alternative one-time 199 EGP lifetime under evaluation (DEEP plan); decide at M0 with licence audit outcome
- Payment: Paymob + Fawry (Egypt) test mode first; Stripe later if international; activation via signed webhook only
- "Subscriptions launching soon" + email capture until gateway accounts exist
- Owner account: all Pro features free, server-verified

## 13. Launch and marketing

- Pre-launch (weeks -2..0): Arabic gaming forums teaser, Discord presence, demo GIFs (mapping a DualSense in 60 seconds)
- Launch (weeks 1..4): Reddit r/pcmasterrace + r/DS4Windows + Arabic gaming communities blitz; honest comparison page (vs x360ce manual setup) with benchmarks on named hardware
- Weeks 5..8: Arabic YouTube/Twitch small-creator outreach with benchmark kits; Steam-free distribution via site + GitHub releases
- Weeks 9..12: tournament/community giveaway; collect install counts for honest case studies
- GEO/SEO: `llms.txt`, SoftwareApplication JSON-LD, pre-rendered metadata, target queries (Arabic: "تسريع ويندوز 11 للألعاب", "تشغيل دراع بلايستيشن على الكمبيوتر"; English: "Windows PC gaming optimizer", "virtual Xbox 360 controller mapper")
- Content rule: zero superlatives without a linked benchmark; no "best", "fastest", "guaranteed FPS"
- 12-week calendar owned by the marketing duty; budget US$0 (organic only) until owner decides otherwise

## 14. Platform matrix (unchanged)

| Platform | v1 inclusion | Notes |
|---|---|---|
| Windows | ✅ Both tools | Primary; .NET 8 / Tauri v2 desktop client |
| Web portal | ✅ Landing, Downloads, Pricing, legal, /owner | Next.js 15+, Cloudflare Pages; dual-hosted Firebase + Vercel |
| macOS / Linux | ⏭️ skipped | Windows-driver tools |
| Android / iOS | ⏭️ skipped | Not v1 scope |
| Wear/watch/TV/Car | ⏭️ skipped | Not applicable |

## 15. Architecture on the shared kit (plans/SHARED_PLATFORM_KIT.md)

Reuses the kit entirely; only controller/optimizer features differ. `owner-auth`, `ai-proxy`, `billing-fallback`, `design-tokens`, `motion`, `signed-webhook`, `changelog`, `help-center` as specced in the kit; five states everywhere; RTL-first; 120 Hz-safe motion; high-contrast themes.

## 16. Premium quality bar

Themes: light/dark/system/high-contrast (WCAG 2.2 AA). Motion: spring physics, transform+opacity only. RTL-first with logical CSS properties; bidi-isolated mixed text; no "(RTL)" suffixes. Five states on every screen. Accessibility: 44 px targets, AA contrast, real SVG icons, no emoji headers, no gradient hero text, no pill-everything. Proof: screenshots at 320/390/768/1280/1920 px, LTR/RTL, light/dark, Lighthouse mobile 90+, zero horizontal overflow.

## 17. Milestones (M0-M6) with acceptance tests

- **M0 Foundations:** licence audit complete (`docs/THIRD_PARTY.csv`, `docs/LICENSE_DECISION.md`); ViGEmBus dependency decision ADR; folder/repo per kit; CI green (typecheck, lint, test, build, gitleaks, size check). Acceptance: audit lists 100% vendored components; zero unlicensed in the sell path; build green.
- **M1 Core slice:** ViGEmBus detection + guided install; one controller read live; profile load/save + test pad; portal scaffold with server-side owner gate. Acceptance: real DualSense/DS4 detected on a clean VM; mapping applied and verified in a test harness; client flag flip -> 403.
- **M2 Parity:** full mapping engine (curves, deadzones, triggers), optimizer read-only scan + fix engine with undo, process-watcher auto-switch. Acceptance: legacy feature parity checklist 100%; undo restores byte-identical registry state on VM.
- **M3 Security/legal/billing:** SHARED_PLATFORM_KIT gates green (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail); legal pack drafted; billing fallback + email capture live. Acceptance: 10 negative webhook tests pass; owner dashboard shows honest empty states.
- **M4 AI:** stutter assistant + finding explainer on `ai-proxy`; evals Arabic+English green. Acceptance: no answer advises out-of-catalog system edits; 5/day free limit enforced.
- **M5 Quality sweep:** five states everywhere; 4 themes; a11y audit; Lighthouse 90+; screenshots; e2e critical journeys; honest-claims lint green. Acceptance: zero horizontal overflow at 5 viewports; claims lint fails on unsupported claim.
- **M6 Release:** signed installer, checksums, published on Firebase Hosting + Vercel (portal) and GitHub releases (app); legacy retired per MERGE rules; retro published with real numbers. Acceptance: fresh VM install-to-mapped in under 5 minutes; both hosts return 200.

## 18. First 10 tasks (ready to hand, title + brief)

See `ops/briefs/sir-controller-tasks.md`. PLANNING ONLY: do not start until the owner authorizes build.

## 19. Risks and open questions (with recommended answers)

| # | Risk / question | Recommended answer |
|---|---|---|
| R1 | x360ce licence unclear (no LICENSE file via API 2026-11-12); the whole controller is derived from it | M0 hard gate: read the licence file directly; if unclear or incompatible, mapper stays free, open-source, no Pro features gated on it; only optimizer is Pro. Never sell derived code until counsel signs off |
| R2 | ViGEmBus retired (2023-11); driver unmaintained; future Windows update could break it | Pin 1.22.0 + SHA-256; never vendor; show driver health in diagnostics; track PadForge/VirtualPad migration; if ViGEmBus breaks on a future Windows, mapper pivots to "unsupported OS" honest state, not silence |
| R3 | Timer-resolution claim is technically false for games (per-process since Win10 2004) | Reword all copy; diagnostics only; rule 12; no public claim |
| R4 | Anti-cheat flags (Vanguard/EAC/BattleEye) for virtual controllers | We add no kernel driver; ViGEmBus is user-mode virtual device, same class used by DS4Windows for a decade; safe-mode guard restricts tweaks in competitive processes; disclaimer in ToS; monitor vendor statements (sourcing task 10) |
| R5 | Driver install failure rates on real machines (unsigned old driver, Secure Boot) | Guided installer with hash verify + honest recovery page; telemetry (opt-in) tracks install success; never bundle driver; owner tests on his PC |
| R6 | LGPL vs proprietary EULA conflict in legacy ("SIR Systems LLC" unverified entity) | Remove the entity name now; EULA redrafted from actual licence obligations; lawyer reviews before any sale |
| R7 | Bluetooth jitter/disconnects on cheap adapters | Document Microsoft-BT-stack requirement (as DS4Windows does); diagnostics bundle logs BT link quality; honest "use USB for ranked play" guidance |
| R8 | Price sensitivity in Egypt (249 EGP vs free tools) | Keep mapping free forever; Pro only for sync + fix engine; EGP pricing tested; annual discount; owner decides at M0 |
| R9 | "SIR Systems LLC" and ownership/IP clarity | Owner confirms whether a registered entity exists; if not, copyright headers use Ahmed Alaa; remove LLC everywhere |
| R10 | Domain cost (sircontroller.app) + code-signing cert (~US$100-500/yr) | Owner decision; until then "Launching soon" site + unsigned beta clearly labelled; never ship unsigned stable releases |
| R11 | Support load in Arabic + English for driver issues | Help center grounded in docs; assistant refuses out-of-catalog fixes; escalation = GitHub issue template, not DMs |
| R12 | Competitor clones (PadForge already active) | Wedge = Arabic RTL + honest claims + one-installer + owner analytics; do not race features we cannot benchmark |
| Q1 | Sell or not? | Default: mapper free forever; optimizer Pro; final call at M0 after licence audit + owner decision |
| Q2 | Lifetime 199 EGP vs subscription? | Recommend subscription (Paymob supports recurring) for sustainability; lifetime only as launch promo |
| Q3 | Ship optimizer before mapper or together? | Together at M2/M3; mapper alone is undifferentiated vs DS4Windows |
| Q4 | Keep ViGEm install inside our installer? | No; separate signed ViGEmBus installer exe, hash-verified, chained only with user consent |
| Q5 | Which games get first-class tested? | GTA V, CS2, Valorant, Rocket League, EA FC (the legacy DEEP list) on the owner's machine |

## 20. Only the owner can do

Decide to sell or not after the licence note; buy domain and signing certificate; create Paymob/Fawry (and possibly Stripe) accounts; plug in real controllers for acceptance testing; lawyer review of the legal pack; confirm whether "SIR Systems LLC" exists.

## 21. Competitor matrix reference

See `ops/competitors/sir-controller.md` (refreshed 2026-11-12) for the matrix, platform facts, complaint list and sourcing tasks.

## 22. Feature parity target

Match or exceed the best controller tool for: one-click install, per-game profiles, test pad, read-only optimizer with undo, plain-language explanations, Arabic RTL, signed installer, owner analytics, zero fake claims.
