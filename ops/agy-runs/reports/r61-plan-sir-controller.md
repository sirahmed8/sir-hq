# r61-plan-sir-controller - Report (PLANNING ONLY)

Task: r61 PLANNING ONLY, SIR Controller (slug sir-controller). Owner order: free tools must NOT build. Brief allows writes only under D:/Projects/_SIR (plans/, ops/competitors/, ops/briefs/, ops/research/). No code, no folder/repo changes, no TickTick edits. Completed 2026-11-12 (~19:42-19:50 local).

## What I read first
- D:/Projects/AGENTS.md, ops/WORKER_PREAMBLE.md, plans/PRODUCT_DIRECTION_2026-11-12.md, plans/sir-controller.md, plans/sir-controller-DEEP.md, ops/briefs/sir-controller-tasks.md, ops/competitors/sir-controller.md, ops/TICKTICK_MAP.md (SIR Controller rows), ops/bus/team.md.
- Project folder read-only: D:/Projects/SIR Controller (AGENTS.md, .sir/CHECKPOINT.md, .sir/TASKS.md; legacy tree listing; docs/THIRD_PARTY.csv exists from an earlier audit pass). Nothing executed from the project; nothing edited inside it.
- ops/SKILLS_INDEX.md skill names used in the new tasks file (exact names verified against the index).

## What I did (all under D:/Projects/_SIR)

1. `ops/competitors/sir-controller.md` - rewritten. New section 0 "Platform facts verified 2026-11-12":
   - ViGEmBus (github.com/nefarius/ViGEmBus, fetched 2026-11-12): archived 2023-11-02, "THIS PROJECT HAS BEEN RETIRED", BSD-3-Clause; 1.22.0 is the production line, Win10/11 only.
   - Successor Nefarius VirtualPad is commercial, partner-only (docs.nefarius.at/projects/VirtualPad/, fetched 2026-11-12). No open successor exists; DS4Windows/PadForge still depend on ViGEmBus.
   - Windows timer resolution is per-process since Windows 10 2004; on Windows 11, occluded/minimized window-owning processes do not get high resolution (learn.microsoft.com timeBeginPeriod, fetched 2026-11-12). Consequence baked into the plan: the legacy "0.5 ms timer for your games" claim is false and was cut.
   - Nagle's algorithm is TCP-only; most games use UDP. Kept only as an optional, clearly-labelled "TCP games only" toggle with undo; never a headline.
   - DS4Windows fragmentation: Jays2Kings archived 2021-10-24; Ryochan7 gone; live options ds4windowsapp/DS4Windows (GPL-3.0, pushed 2026-03-01, 239 stars) and CircumSpector/DS4Windows (505 stars, 2025-02-03). ds4windows.org advertises v3.3.3 and links an archived fork; treated as untrusted.
   - PadForge (hifihedgehog/PadForge): .NET 10, SDL3+HIDMaestro+HidHide, pushed 2026-11-12, 325 stars, licence NOASSERTION. Added as a watch row.
   - x360ce/x360ce: active (pushed 2026-11-11), ~2,949 stars, NO licence file via API. The matrix's old "MIT" row is now "(unsourced, verify)"; the M0 licence audit is a hard gate.
   - ExitLag pricing page was JS-rendered; no numbers captured; all prices stay "(unsourced, verify)". Paymob reachable (200); Fawry pricing returned 403 via curl.
   - Complaints section explicitly tagged unverifiable; 12 sourcing tasks listed with links, each under 2 hours.

2. `plans/sir-controller.md` - rewritten (still the plan of record; DEEP plan reconciled):
   - Status header: PLANNING ONLY per owner order 2026-11-12.
   - New section 4: research findings 2026-11-12 (the five load-bearing facts above).
   - Rules extended: rule 11 (ViGEmBus is a pinned, hash-verified prerequisite, never vendored), rule 12 (timer-resolution honesty: diagnostics only, never a game-wide claim).
   - Features: false 0.5 ms headline cut; GPU/DWM flip-model tweaks demoted to experimental+off by default+VM-tested; rapid-fire labelled single-player accessibility only, disabled in safe mode.
   - New sections: 7 screens (11 desktop + 7 portal, five states each), 8 Firestore data model (10 collections; local-only `.reg` deltas; 90-day TTL on scanRuns; 30-day on errorReports), 9 API list (10 endpoints), 10 AI features (fallback chain via ai-proxy; assistant grounded only in a cited catalog), 11 security/privacy, 12 monetisation (EGP-first, Paymob+Fawry, "Launching soon"), 13 launch/marketing (12-week organic $0 plan, GEO/SEO, no superlatives), 14 platform matrix retained, 17 milestones M0-M6 each with an acceptance test, 18 pointer to task file, 19 risks R1-R12 + open questions Q1-Q5 every one with a recommended answer.
   - Plans/PRODUCT_DIRECTION_2026-11-12.md honored: SIR Controller remains in the final product list; GLOBAL; shared kit; owner-only analytics; EGP/USD pricing; dual-host Firebase+Vercel; Firebase project and repo named sir-controller (to be created only when build is authorized).

3. `ops/briefs/sir-controller-tasks.md` - expanded 10 -> 48 tasks. Section A keeps the original first 10 ready-to-hand tasks (same order, sharpened acceptance tests). New sections: B (B11-B16 licence/legal/governance), C (C17-C30 driver and engine, incl. ViGEmBus guided install, HidHide, Raw Input reader, virtual 360 bridge, deadzone/curves/trigger labs, test pad, process watcher, hotplug, DualSense extras, DirectInput templates), D (D31-D38 optimizer: scan v1, honest timer diagnostics, fix engine with .reg undo, restore_all_defaults.ps1, anti-cheat safe mode, Nagle toggle, 24h watchdog, autostart), E (E39-E43 portal: downloads with SHA-256 manifest, pricing + email capture, Paymob/Fawry webhooks with idempotency, /owner with real metrics, Firestore rules isolation tests), F (F44-F48 AI assistant, AI explainer, full quality sweep, honest-claims sweep, release with checksums + dual-host deploy + legacy retirement). Every task carries Files, an acceptance test and exact skills from ops/SKILLS_INDEX.md. Header states PLANNING ONLY clearly.

4. `plans/sir-controller-REFRESH-LOG.md` - created; records this refresh, the date, every source fetched and every change.
5. `ops/bus/team.md` - START line appended (19:42) and DONE line appended (19:45).
6. `ops/bus/sir-hq.md` - one line appended.

## Commit note
- `ops/competitors/sir-controller.md` (my rewrite) was swept into parallel commit 9818a2d (r58 skeletons round) before I committed; `git show HEAD:ops/competitors/sir-controller.md` confirms the refreshed content landed. My commit fb0b4ad carries the other 6 files.

## Commands run (real)
- `git status --short; git log --oneline -5` (start of round; tree had many pre-existing modifications from other processes; none of mine touched, none reverted)
- `wc -l plans/sir-controller.md plans/sir-controller-DEEP.md ops/briefs/sir-controller-tasks.md ops/competitors/sir-controller.md`
- Web: webfetch ViGEmBus repo, End-of-Life page, VirtualPad page, timeBeginPeriod doc, ds4windows.org (untrusted, ignored for sourcing), GitHub REST API via curl (repo search + licence endpoints), Bing/DuckDuckGo scrape attempts (no usable results), Paymob/Fawry reachability checks.
- `grep -n "controller" ops/TICKTICK_MAP.md`, `grep` over ops/SKILLS_INDEX.md for skill names.
- No builds, no tests run (planning-only round; no code exists for this project).

## What is unsure / honestly open
- x360ce licence never read directly (needs repo clone; queued as task B11). Until then the controller's sellability is UNKNOWN; recommendation: mapper stays free regardless.
- ExitLag / Hone / Razer Cortex / CCleaner prices unverified (JS-rendered pages / 403); all tagged "(unsourced, verify)".
- sircontroller.app and signing-certificate prices unverified; owner must buy.
- Legacy "298/298 MSTest pass" claim never verified; no test run this round (nothing to run).
- Whether Windows 12 changes timer/ViGEm behavior: unknowable now; the plan treats driver breakage as a monitored risk (R2) with an honest "unsupported OS" fallback.
- Claims in the competitor matrix about user complaints are illustrative, not evidence; sourcing tasks 5-6 exist for that.

## Recommendation for the owner / HQ
1. Do not authorize build yet; the M0 licence gate (B11/B12/A1/A2) should run first when build is approved.
2. When approved, suggested order: A1 -> A2 -> A4 -> B11/B12 -> C17 onwards. Never skip the licence gate.
3. Owner-only actions remain: decide sell-or-not after licence note; buy domain + signing cert; create Paymob/Fawry accounts; plug real controllers for acceptance; Egyptian attorney review of the legal pack; confirm whether "SIR Systems LLC" exists (recommend: remove the name).
4. TickTick: no changes made this round; the map still points SIR Controller at the old plan; HQ should refresh the row after this lands.

## Definition of done check
- Every brief item 1-5 addressed: research done and added to plan (section 4); plan expanded (screens, data model, API list, AI, security/privacy, monetisation, launch/marketing); tasks expanded to 48 with acceptance tests and skills; risks and open questions listed with recommended answers (section 19); refresh log written with date. Report complete. CI not applicable (planning-only; no code changed).
