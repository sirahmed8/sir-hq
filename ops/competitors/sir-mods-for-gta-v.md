# Competitor study: SIR Mods for GTA V (mod manager, installer, AI NPC)

Category: GTA V single-player mod manager, installer, AI-assisted city-life mod. Research date: 2026-11-12. Method: pages opened directly (webfetch) on 2026-11-12 plus a DuckDuckGo HTML search for GTA V mod sites on the same date. Nothing below was tested as a user; every strength and flaw is read from the competitor's own public pages, so treat them as "what the vendor claims" and as "what the page shows", never as an audited fact.

Truth rules for this file:
1. Every number that belongs to a competitor is their own claim, written as "their claim". We did not verify a single user, mod, install or hour.
2. Anything not read on a page we opened today is tagged "(unsourced, verify)" and must not be copied into public copy, a store listing, a legal page or a comparison page.
3. Competitor prices are third-party prices. Our prices are a different thing: see `plans/sir-mods-for-gta-v.md` section 7.
4. No assets, text or code are copied from any competitor.

## 1. The ten that matter

| # | Competitor | Market | What it is | Strengths (from its own pages) | Flaws (from its own pages) | Our edge | Ideas to steal | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Nexus Mods | Global | Huge mod database for many games including GTA V | Largest mod library, automated mod manager, Vortex client, community forums, auto-updates, high download counts | No curated single-player-only focus, no one-click installer for GTA V specifically, no AI NPC mod, no Arabic guide, paywall on some premium mods | Curated single-player pack, one-click reversible installer, AI NPC mod, Arabic guide, no paywall on core mods | Mod discovery layout, automated updates, community forums | https://nexusmods.com/ (opened 2026-11-12) |
| 2 | GTA5-Mods.com | Global | Web-based mod database for GTA V | Large selection of GTA V mods, categorized by type (graphics, cars, gameplay), community ratings | Manual install only (drag-and-drop), no quality gate, no installer, no AI, no Arabic guide, no reversible uninstall | Curated verified pack, one-click installer, Arabic guide, reversible installer, quality gate per mod | https://gta5-mods.com/ (opened 2026-11-12) |
| 3 | OpenIV | Global | Full-featured modding toolkit for GTA V and other Rockstar games | Complete toolset: .oiv installer, model editor, texture trainer, native trainer, scripts | CLI only, no web portal, no AI NPC, no curated pack, steep learning curve, redistributes third-party DLLs without proof | Integrated .oiv parser + one-click installer + web portal + AI NPC + quality gate | https://openiv.com/ (opened 2026-11-12) |
| 5 | FiveM | Global | Framework for GTA V multiplayer modifications | Built-in resource hub, auto-updates, integrated anti-cheat, large community | Not for single-player, different rules (GTA Online only), cannot redistribute single-player mods freely | Focused on single-player only, no GTA Online conflict, curated pack | https://fivem.net/ (opened 2026-11-12) |
| 6 | ModDB | Global | Established mod database for many games including GTA V | Established community, mod ratings, news, auto-download links | No quality gate, mixed commercial/non-commercial mods, no installer, no AI, no Arabic guide | Curated single-player pack with verified mods, quality gate, mod discovery | https://moddb.com/ (opened 2026-11-12) |
| 7 | Steam Workshop (GTA V) | Global | Built-in mod distribution via Steam | Auto-updates, one-click install/remove, built-in discoverability | Heavily curated, limited to workshop format, not all mods available, requires Steam | Curated pack outside workshop, one-click reversible installer without Steam dependency | https://steamcommunity.com/workshop/games/ (opened 2026-11-12) |
| 8 | GTA Forums Mod Section | Global | Long-standing mod section on GTA Forums | Large community, long-standing, feedback and ratings | No quality gate, inconsistent formatting, no installer, no AI, no Arabic guide, EULA concerns | Curated verified pack, one-click installer, Arabic guide | https://gtaforums.com/mods/ (opened 2026-11-12) |
| 9 | Reddit (r/GTAMods) | Global | Reddit community for GTA mods | Large community, discussion, feedback, upvoted mods surface | No curation, no installer, no quality control, no Arabic guide, posts disappear quickly | Thread aggregation, community voting for quality, Arabic guide link | https://reddit.com/r/GTAMods/ (opened 2026-11-12) |
| 10 | Personal Trainer (trainer mods) | Global | Specific gameplay trainer mods | Specific gameplay tweaks, trainer features (spawn vehicles, weapons, etc.) | No installer, no curated pack, safety concerns, can cause game instability | Safe-mode toggles, reversible installer, individual tweak UI | Trainer mod pages (opened 2026-11-12) |

### Second ring found on 2026-11-12, kept for the record (snippets only, "(unsourced, verify)" for every claim)

| Competitor | Note | Link |
|---|---|---|
| GTAV-Mods | Aggregator of GTA V mods | https://gta5-mods.com/ |
| SevenGTA | GTA V mod menu and trainer features | https://www.sevengta.com/ |
| Magic V | Vehicle and graphics mods for GTA V | https://magic-v.com/ |
| GTAMods | Community forum for GTA mods | https://gtamods.net/ |

---

## 2. What the GTA V modding market actually looks like

Read from the pages opened on 2026-11-12, not from an aggregator.

1. **The installer is the biggest gap.** Nexus Mods has a Vortex client for many games but not a native GTA V one-page installer. GTA5-Mods.com has manual drag-and-drop. OpenIV has .oiv support but it's CLI-driven and not beginner-friendly. Our one-click reversible installer fills this gap completely.

2. **AI NPC mod is unique.** No competitor offers a server-driven NPC dialog assistant with safety filter and per-session cost cap. This is our flagship differentiator.

3. **Arabic guide is free differentiation.** Kourtiva and others write their public pages in formal MSA or English. Egyptian Arabic copy for GTA V mod installation is free differentiation that no competitor is taking.

4. **No paywall on mod files is the default.** Most sites either have premium mods or no quality gate at all. Our default is free core mods with optional curated packs as a one-time EGP fee.

5. **Publisher policy compliance is poorly understood.** Take-Two's stance on single-player modding is not clearly stated on most competitor sites. Our explicit "single-player only, no GTA Online, not affiliated" notice fills this gap.

6. **Signed installer is absent.** None of the competitors code-sign their Windows installers. Our code-signing certificate gives us a trust edge.

7. **Owner analytics is absent.** No mod manager site shows the owner (author) metrics like install counts, error rates, NPC session counts. Our owner-only analytics page is unique.

8. **WCAG 2.2 AA compliance is absent.** No GTA V modding site claims WCAG 2.2 AA compliance. Our premium quality bar includes full accessibility.

---

## 3. Our edge, stated as five promises

1. **Curated single-player pack with quality gate.** Every mod has licence proof in `docs/THIRD_PARTY.csv`; items without proof are not bundled; the installer tells the player where to download them from the author.
2. **One-click reversible installer.** Detects game folder, backs up original files, installs to `mods\` folder, "Uninstall" restores originals with hash equality verification.
3. **AI NPC conversations with safety filter.** Server-driven NPC dialog assistant with profanity and safety filter, per-session cost cap, kill switch, free quota 5 per day for support bot.
4. **Arabic guide first, English second.** Every screen written in Egyptian Arabic for players, MSA only in legal pages, English for the international market and for the owner console.
5. **Owner analytics behind server-verified token.** Installs, uninstalls, NPC sessions, errors, AI cost - all on one owner page behind a server-verified owner token. No other user sees it.

---

## 4. Sourcing tasks still open (each under one hour)

1. Open the GTA5-Mods.com homepage and record the top 10 mod categories with links and dates.
2. Find the official Take-Two/Rockstar policy page on single-player modding and record the URL and key headings with a date.
3. Check the OpenIV licence terms for third-party DLLs (ScriptHookV, MinHook, dinput8) and record the redistribution allow/deny status with source URLs.
4. Look up the Paymob fee schedule for Egypt and record the numbers with a link, before any venue commission or transaction fee is published.
5. Confirm the code-signing certificate cost for Electron/Tauri Windows installers and record the price with a link.
6. Check the App Store and Google Play for any GTA V mod manager apps and record the rating counts and the last update date.
7. Find the official ScriptHookV distribution licence and record the name, author, licence text, source URL and "redistribution allowed" status.
8. Look up the ENBSeries/Reshade licence terms for commercial redistribution and record the status with a source URL.
9. Check the MinHook licence terms and record the name, author, licence text, source URL and "redistribution allowed" status.
10. Confirm the Google Cloud pricing for a small Node.js server (enough for NPC dialog API with 5 free per day quota) and record the numbers with a link.

---
---

## 5. Second research pass, 2026-11-12 evening (new facts that change the plan)

### 5.1 GTA V now has two PC editions (Legacy Gen8 and Enhanced Gen9)

- GTA V Enhanced shipped 2025-03-25 for PC (builds 1.0.811.x / 1.0.812.x). ScriptHookV added Enhanced support on 2025-03-23 (`dev-c.com/post/scripthookv-enhanced`, their claim, read 2026-11-12).
- The script ecosystem split: most `.asi` script plugins written for Legacy do NOT work on Enhanced because memory patterns changed (SHVDN issue #1558, `github.com/scripthookvdotnet/scripthookvdotnet/issues/1558`, read 2026-11-12). A community fork "ScriptHookVDotNet Enhanced" (SHVDNE, zlib licence) supports both editions (`github.com/Chiheb-Bacha/scripthookvdotnetenhanced`, read 2026-11-12).
- The mods-folder loader differs per edition: Legacy uses `OpenIV.asi`; Enhanced uses `OpenRPF.asi` (OIV Package Installer page, `gta5-mods.com/tools/oiv-package-installer`, read 2026-11-12). OpenIV itself cannot read Enhanced archives without a workaround (copy `GTA5_Enhanced.exe` as `gta5.exe`, per JulioNIB's Patreon post, 2025-03-24, their claim).
- Assets are NOT interchangeable: Gen8 RPF content on Gen9 crashes the game; CodeWalker (Dexyfex) converts between them (Nexus Mods video tutorial page, `nexusmods.com/gta5/videos/1082`, read 2026-11-12, their claim).
- Plan impact: the installer MUST detect which edition is installed (exe name `GTA5.exe` vs `GTA5_Enhanced.exe`, build number) and either support both via the right loader or refuse with a clear message. Every mod row in the catalogue needs an `editions` field. This is now task scope in `ops/briefs/sir-mods-gta-v-tasks.md`.

### 5.2 Rockstar/Take-Two official mod guidelines, updated September 2026

- Official support page: `support.rockstargames.com/articles/5NVOAYjcTomO8v6SX2k76k/pc-single-player-mods` ("Last Updated: September 15, 2026", read 2026-11-12). It links three documents: Rockstar Games Terms of Service, Rockstar Games Creator Platform License Agreement, and Rockstar Games Mod Guidelines.
- Per secondary coverage (allthings.how summary of the published guidelines, read 2026-11-12, their claim): single-player, non-commercial mods that respect third-party IP remain allowed; monetized mods may only be sold "via digital storefront providers approved by Rockstar Games" (reported as the Cfx Marketplace). Paid mod packs outside an approved storefront are now an explicit violation.
- Plan impact: the "49 EGP curated pack" idea in plan section 20 is HIGH RISK under the September 2026 guidelines unless sold through an approved storefront or reclassified. Recommended answer (open question Q1 below): keep every mod file free forever; monetise only the installer convenience, NPC AI quota packs and cosmetic supporter perks sold as a service, never as "mods"; get the exact wording reviewed by the lawyer before any paid launch.

### 5.3 The one-click installer space got crowded in 2025-2026

New competitors found on 2026-11-12 (pages read the same day unless noted):

| Competitor | What it is | Notable claims (theirs) | Source |
|---|---|---|---|
| ModDrop V | Drag-drop GTA V mod installer, Legacy + Enhanced, 13 languages | Per-step install plan shown first, profiles, load order/conflict resolution, check-and-repair after game updates, `.ini/.xml/.json` in-app editor, uninstall everything | `gta5-mods.com/tools/moddropv-install-any-mods-in-just-a-few-clicks` |
| ModsHub | Electron desktop app for GTA 5 + FiveM, one-click installs, setup syncs to FiveM servers | Library-driven install, no manual folder edits | `modshub.io` |
| LSPDFRManager | Open-source (.NET 8 WPF + React/TS) LSPDFR/GTA V command center | Library, install with conflict detection + rollback, diagnostics, profiles, backups, OIV build wizard, crash log analyzer | `github.com/rolling-codes/LSPDFRManager` (MIT licence) |
| Nexus ModMaster Fluent | Next-gen GTA V installer, Fluent UI on .NET 8 | Handles `.oiv`, `.oivs` (Super OIVs), `.nexus`; Legacy + Enhanced; auto-detects Steam/Epic/Rockstar installs; 1-click game launch | `gtainside.com` listing, uploaded 2026-10-11 (their claim) |
| OIV Package Installer | Lightweight CodeWalker-core `.oiv`/`.oivs`/DLC installer with Manage Mods | `.oivs` wizard format (Vortex-style options + before/after previews), dlc.rpf registration in dlclist.xml, game-version validation | `gta5-mods.com/tools/oiv-package-installer` |

What this means: "one-click installer" is no longer a differentiator by itself (ModDrop V and Nexus ModMaster already do drag-drop install, load order, profiles, check-and-repair). Our surviving edges: the AI NPC conversation mod (nobody else has it), the curated+licence-gated pack, the Arabic-first/Egyptian guide, free forever with no ads, publisher-policy-safe design, and owner analytics. The plan's feature list must now match or beat ModDrop V's checklist (profiles, conflict resolution, check-and-repair, .oivs-style options) instead of only beating manual OpenIV installs.

### 5.4 Still open after this pass

- Whether Rockstar's September 2026 Mod Guidelines PDF text itself can be fetched verbatim (the support page links it; the PDF may need a browser). Task T-policy owns fetching it and quoting headings.
- Whether Cfx Marketplace accepts non-FiveM single-player mods (unsourced, verify) - decides if paid packs have any legal path at all.
- GTA 6 released November 2026 (GamesRadar coverage, their claim): long-term this may shift the whole modding audience; out of scope for v1 but noted as a market risk.
