# COMPETITOR MATRIX: SIR Laptop Manager

**Version:** 1.0.0 (stays 1.0.0 while under development)  
**Research Date:** 2026-11-12  
**Owner:** SIR Laptop Manager project  
**Method:** Official product pages and official pricing pages where they loaded, plus GitHub REST API for open-source licence and stars. Third-party figures marked "unverified". Nothing here claims SIR Laptop Manager works; project status only in `.sir/CHECKPOINT.md`.

---

## 1. Direct and Best-in-Class Competitors (10 products)

| # | Product | What It Is | Licence | Pricing (Source Quality) | Strongest 3 | Weakest 3 | Copy into SIR Laptop Manager | Do Better |
|---|---------|------------|---------|---------------------------|-------------|-----------|------------------------------|-----------|
| 1 | **Microsoft PC Manager** | Free Windows 10/11 cleanup & health suite: health checkup, storage analysis, startup manager, process manager, pop-up blocker, deep uninstall, Windows Update & Security shortcuts | Closed, free | Free (official page, 2026-11-12). No paid tier on official site. | 1. One-click health checkup scans junk, risks, startup in one pass<br>2. Disk analysis with duplicate & large-file views<br>3. Deep uninstall removes leftovers | 1. Shallow advanced control<br>2. No undo for cleanup<br>3. Recommends its own auto-start<br>4. No battery health<br>5. No developer tooling | The one-screen health score and prioritized fix list; the storage breakdown | Real weighted score with visible inputs; every destructive action behind dry-run + quarantine; no self-promotion; owner-only data |
| 2 | **CCleaner** | Long-running PC cleaner with health check, software updater, driver updater, performance optimizer, disk analyzer, duplicate finder, scheduled cleaning | Closed, freemium | Free tier; Professional USD 44.95/yr; Professional Plus USD 64.95/yr (3 devices); Premium bundle listed USD 89.95, promoted USD 64.95 (5 devices) — official plans page 2026-11-12; regional prices differ | 1. Software updater closes security holes<br>2. Scheduled cleaning<br>3. Disk & duplicate analyzers | 1. Paid wall around core health<br>2. Upsell-heavy<br>3. Closed source<br>4. Past bundling/telemetry complaints<br>5. Registry cleaning risky | Software update check with clear "check only, never install" promise; scheduled maintenance | Free internal tool; local-only; quarantine before delete; no upsell; no account |
| 3 | **Glary Utilities Pro** | All-in-one suite with 20+ tools: one-click maintenance, disk cleanup, startup manager, duplicate finder, disk analyzer, privacy eraser, file recovery | Closed, freemium | Pro USD 39.95/yr (up to 3 PCs); Nov 2026 discount USD 19.97/yr — official store page 2026-11-12 | 1. One-click maintenance bundles cleanup/repair/privacy<br>2. Broad module set<br>3. Scheduled automatic maintenance | 1. Aggressive upsell<br>2. Dated interface<br>3. Registry repair risk<br>4. Telemetry/bundle complaints<br>5. Low transparency | The "one score, then one action" pattern; module breadth | No upsell; modern interface; dry-run + undo on every module; no registry mutation by default |
| 4 | **Razer Cortex** | Gaming optimization & launcher: game booster, auto boost, FPS counter, system booster cleanup, game library, deals, game clips | Closed, free | Free; optional Razer account for sync & rewards — official pages & FAQ 2026-11-12 | 1. Auto game detection with pause/restore of background apps<br>2. FPS & system telemetry<br>3. Game library + deals in one place | 1. Gaming-only scope<br>2. Account & rewards layer<br>3. Background service & telemetry<br>4. No startup, driver, or battery care | Game detection with graceful pause/restore (already in project); telemetry overlays | Full PC care not a game launcher; no account; local-only; no rewards manipulation |
| 5 | **MSI Center** | OEM control center for MSI laptops: user scenarios, thermal modes, battery master with charge thresholds, system diagnosis, hardware monitoring, Mystic Light, Live Update | Closed, free | Free, MSI hardware only — official pages 2026-11-12 | 1. Battery Master with charge thresholds & calibration<br>2. Hardware monitoring & SSD health<br>3. Performance & thermal profiles | 1. Locked to MSI hardware<br>2. Module bloat<br>3. Opaque automation<br>4. No quarantine/undo<br>5. Poor portability | Battery health card with capacity, wear, charge guidance; hardware health readouts | Works on any Windows 11 PC; transparent thresholds; no vendor lock; no module store |
| 6 | **Dell Optimizer** | OEM AI optimization: ExpressResponse, ExpressCharge, thermal modes, intelligent audio, presence-based lock, network priority | Closed, free | Free, Dell hardware only — official pages 2026-11-12 | 1. Battery charge policy & runtime extension<br>2. Thermal & power profiles<br>3. Presence-based security | 1. Locked to Dell hardware<br>2. Custom charge thresholds removed in 6.x, moved to BIOS<br>3. Opaque AI decisions<br>4. No cleanup or startup control | Battery care detail & thermal guidance | Owner-visible thresholds & reasons; cross-vendor; no BIOS trip |
| 7 | **BleachBit** | Open-source cleaner & privacy tool (Windows/Linux): application cleaners, free-space wipe, file shredder, CLI | GPL-3.0 | Free (official site). 7,465 stars (GitHub API 2026-11-12) | 1. Deep application & privacy cleaning<br>2. Portable mode & CLI<br>3. No ads, telemetry, or account<br>4. CleanerML & winapp2 support | 1. Dated interface<br>2. Permanent deletion, no undo<br>3. No startup/power/driver/health modules<br>4. Manual review needed | Granular cleaner categories; privacy focus; CLI-friendly design | Quarantine before delete; restore path; modern interface; integrated health score |
| 8 | **Bulk Crap Uninstaller** | Open-source bulk uninstaller: leftover cleanup, orphan detection, batch automation, startup manager, application data export | Apache-2.0 | Free (official site). 22,429 stars (GitHub API 2026-11-12) | 1. Thorough app & leftover detection<br>2. Batch uninstall with safety checks<br>3. Huge exportable metadata<br>4. Startup manager | 1. Uninstall-only scope<br>2. Technical interface<br>3. No real-time care<br>4. No health score or battery | Leftover detection; application metadata export; startup management | Safe uninstall flow with restore point + quarantine first; plain-language impact; one clear primary action |
| 9 | **Windhawk** | Open-source customization marketplace for Windows: injects reviewed mods for taskbar, Start menu, Explorer, other programs | GPL-3.0 | Free (official site). 9,792 stars (GitHub API 2026-11-12) | 1. Source-available mods, one-click install<br>2. Active catalogue<br>3. Engine stability focus | 1. Technical audience<br>2. Global injection risk<br>3. No cleanup or startup<br>4. Mod quality varies | Mod manager UI with backup/restore; versioned catalogue; source review | Per-mod permissions; no global injection by default; snapshot before every change |
| 10 | **Sysinternals Autoruns** | Microsoft's exhaustive startup/autorun inspector: registry, services, tasks, shell extensions, signature & VirusTotal checks, CLI | Free, no redistribution licence (Microsoft Learn 2026-11-12) | Free | 1. Most complete autorun coverage<br>2. Signature & VirusTotal checks<br>3. CLI & offline scan<br>4. Hide Microsoft entries | 1. Technical & unsafe for novices<br>2. No undo<br>3. No cleanup or health<br>4. No automation | Startup location coverage; signature status; CLI parity | Plain-language impact; safe disable with backup; owner-only; one-tap restore |

---

## 2. Open-Source Cousins & Adjacent Tools (Reviewed, Not Cloned)

| Product | Licence (GitHub API or Official) | Stars (API) | Strongest 3 | Weakest 3 | Use for SIR Laptop Manager |
|---------|----------------------------------|-------------|-------------|-----------|----------------------------|
| BleachBit | GPL-3.0 | 7,465 | Cleaner definitions, shredder, portable, CLI | No undo, dated UI, cleaning only | Cleaner category model & privacy copy |
| Bulk Crap Uninstaller | Apache-2.0 | 22,429 | Leftover detection, batch uninstall, metadata export | Uninstall-only, technical, no care loop | Future uninstall module data model & safety checks |
| Windhawk | GPL-3.0 | 9,792 | Mod catalogue, source review, injection engine | Technical, risky global injection, no care | Look manager backup & restore discipline |
| Sysinternals Autoruns | Free, no redistribution licence | N/A | Autorun coverage, signature checks, CLI | Technical, no undo, no automation | Startup inventory & signature status vocabulary |
| PowerToys | MIT (official repo) | Not checked this round | Keyboard-first utilities, FancyZones, PowerToys Run | Not a PC-care suite, separate install, no health/cleanup | Command palette & keyboard shortcut patterns |

---

## 3. What to Build First (Ranking from Feature Gaps)

| Rank | Feature | Competitor Evidence | Why First |
|------|---------|---------------------|-----------|
| 1 ✅ | **Weighted health score** with one-click check & prioritized fix list | PC Manager health checkup; CCleaner Health Check; Glary one-click maintenance | Without a score the dashboard is a wall of numbers |
| 2 ✅ | **Battery care card** with design capacity, full charge capacity, wear, cycle count, plain recommendation | MSI Center Battery Master; Dell Optimizer ExpressCharge; CCleaner Health | Battery is the #1 laptop degradation factor; owner needs actionable guidance |
| 3 ✅ | **Update checker** that only checks winget + NVIDIA driver, never installs | CCleaner Software Updater; MSI Center Live Update; PC Manager Windows Update card | Security hygiene without risk; owner controls installs |
| 4 | **Uninstall manager** with leftover detection, restore point, quarantine | BCUninstaller (leftover detection, batch, metadata export); PC Manager deep uninstall | Removing apps still means Windows Settings + manual folder checks |
| 5 | **Duplicate file finder** with dry-run selection & quarantine | PC Manager disk analysis; CCleaner duplicate finder; Glary duplicate finder | Users cannot find duplicate downloads or project copies today |
| 6 | **Largest files browser** | PC Manager large files; Glary disk analyzer; TreeSize class | No way to see which files consume disk beyond category totals |
| 7 | **Startup impact legend, filter, delayed start** | Task Manager startup impact; Autoruns categories; CCleaner startup manager | Table shows High/Medium/Low but no legend, filter, or per-item delay |
| 8 | **Privacy & telemetry report** with per-area toggles | BleachBit privacy cleaners; O&O ShutUp10 class; PC Manager pop-up/browser protection | No screen explains what leaves machine or lets owner audit it |
| 9 | **Scheduled maintenance plan** (round times :00/:30) | Glary automatic maintenance; CCleaner scheduled cleaning; PC Manager smart boost | Cleanup/startup scans exist but no weekly plan with visible report |
| 10 | **Disk SMART & SSD health readout** | Speccy hard disk health; MSI System Diagnosis SSD status; CCleaner Health | App shows capacity but not drive health |

---

## 4. Facts That Must Not Be Claimed

- Every price above is a snapshot from the official page on 2026-11-12 and can change by region, promotion, or bundle. Third-party prices marked unverified must not appear in product copy.
- Star counts are GitHub API snapshots from 2026-11-12, not claims about SIR Laptop Manager.
- No SIR Laptop Manager feature is "live" from this file. Status stays in `.sir/CHECKPOINT.md` and `.sir/TASKS.md`.
- A competitor feature listed under "Copy" is a design reference, not a licence to reuse its code or assets.
- All "unverified" markings mean the figure could not be confirmed from an official source on the research date.

---

## 5. Sources (for verification)

| Product | Source URLs (accessed 2026-11-12) |
|---------|-----------------------------------|
| Microsoft PC Manager | https://pcmanager.microsoft.com/ |
| CCleaner | https://www.ccleaner.com/ccleaner/pricing |
| Glary Utilities | https://www.glarysoft.com/glary-utilities/pro/ |
| Razer Cortex | https://www.razer.com/cortex |
| MSI Center | https://www.msi.com/center |
| Dell Optimizer | https://www.dell.com/support/kbdoc/en-us/000178580 |
| BleachBit | https://www.bleachbit.org/ ; https://api.github.com/repos/bleachbit/bleachbit |
| Bulk Crap Uninstaller | https://www.bcuninstaller.com/ ; https://api.github.com/repos/Klocman/Bulk-Crap-Uninstaller |
| Windhawk | https://windhawk.net/ ; https://api.github.com/repos/ramensoftware/windhawk |
| Sysinternals Autoruns | https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns |
| PowerToys | https://github.com/microsoft/PowerToys |

---

## 6. Adoption Notes for Other Products

Per `SHARED_PLATFORM_KIT.md` rule 16: Every product runs this competitor research before plan acceptance. When SIR Laptop Manager hardens a reusable piece (e.g., the weighted health score algorithm, the quarantine engine, the game-mode snapshot ledger), it updates `SHARED_PLATFORM_KIT.md` and posts one line to `ops/bus/sir-hq.md` so HQ queues the adaptation for others.

**Adopted from SIR Laptop Manager** (to be added when features are verified):
- Quarantine-before-delete pattern with SHA-256 manifests
- Game-mode process snapshot + graceful restore
- Agent-config sync across 18 tools with dry-run parity check
- Local RAG with Arabic/English evals on private corpus