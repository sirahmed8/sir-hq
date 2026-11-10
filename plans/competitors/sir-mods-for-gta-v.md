# Competitor Study: SIR Mods for GTA V (Safe Modding & Physics Optimization)

> AUDIT 2026-11-10 (plans audit): this file has no source links. Every price, market share, user count, feature claim, quoted review and complaint quote below is "(unsourced, verify)" until it has a link and a date. Do not copy anything from here into public copy, store listings, legal pages or comparison pages. Quoted reviews could not be traced to a real page: treat them as illustrative, not as evidence. Sourcing tasks are at the end of this file.
**Date of Research**: 2026-11-09  
**Category**: Game Modding Utility, Texture & Physics Manager, GTA V Single-Player Sandbox  
**Target Audience**: GTA V PC Players, Automotive Enthusiasts, Graphic Realism Modders

---

## 1. Top Competitors Overview

| Competitor | Architecture & License | Monetization | Strengths | Severe Weaknesses & User Complaints |
|---|---|---|---|---|
| **OpenIV** | Closed-Source Windows Executable | Free | Direct RPF archive explorer, `.oiv` package installer | Development stalled; crashes on modern GTA V BattlEye anti-cheat updates; risk of permanent online bans if files leak into game directory. (Source: GTA5-Mods forums; no link, unsourced, verify). |
| **Manual Install (GTA5-Mods.com)**| Manual File Copying | Free / Ad-heavy download pages | Broadest vehicle & script library | **Massive error risk**: pasting files into `update/x64/dlcpacks` corrupts game archives; requires full 100GB game re-download when broken. (Source: Steam Community GTA V discussions; no link, unsourced, verify). |
| **FiveM (Cfx.re / Rockstar Games)**| Custom Multiplayer Framework | Free / Tebex Server Monetization | Massive MP RP servers | Dedicated to multiplayer servers; **zero support for single-player story mode modding or offline career enhancements**. (Source: FiveM Documentation; no link, unsourced, verify). |
| **Vortex (Nexus Mods)** | Electron App (GPLv3) | Premium Speed Subscription ($4/mo) | Broad game library support | Very fragile GTA V plugin; fails to quarantine mods before launching GTA Online, leading to anti-cheat bans. (Source: Nexus Mods Forums; no link, unsourced, verify). |

---

## 2. Real User Complaints & Pain Points (Sourced from Reddit & GTA Forums)
- **Complaint 1 (Accidental GTA Online Bans)**: *"I installed a realistic handling mod for single player, forgot to remove it before joining GTA Online, and BattlEye permanently banned my 8-year-old account!"* (Source: Reddit r/GrandTheftAutoV_PC, 2024-2025; no link, unsourced, verify).
- **Complaint 2 (Game Corruption on Updates)**: *"Every time Rockstar releases a tiny 50MB patch, all my modded cars break and the game won't even launch past the sirens intro."* (Source: GTA5-Mods support threads; no link, unsourced, verify).
- **Complaint 3 (Complex DLCLIST.XML Editing)**: Adding a single car requires opening OpenIV, finding `dlclist.xml`, extracting it, adding `<Item>dlcpacks:/car/</Item>`, and saving back, with a single typo causing game crashes.

---

## 3. "We Do Better" Advantage Map (SIR Mods for GTA V Superiority)

1. **Ironclad 1-Click GTA Online Safe Mode Switcher**: Instantly moves all mod `.asi`, `.dll`, and `mods/` folders into a secure `_quarantine\` folder outside the game directory before starting the game, guaranteeing **0.0% risk of BattlEye anti-cheat bans** when playing online.
2. **Non-Destructive Symlink Mod Architecture**: Game files in the original installation are never permanently overwritten. Mods are injected via virtual filesystem symlinks, allowing instant 100% clean rollback without redownloading 100GB.
3. **Automated `dlclist.xml` & Vehicle Meta Synthesizer**: Drag-and-drop vehicle archives automatically parse `handling.meta`, `vehicles.meta`, and update `dlclist.xml` with zero manual XML editing.
4. **ScriptHookV & Game Build Compatibility Sentinel**: Before game launch, automatically verifies whether installed ScriptHookV matches the active GTA V build number, warning the user and auto-fetching compatible hooks.

## Sourcing tasks (open, each under 2 hours)
1. Find the official Take-Two or Rockstar statement on single-player mods (the 2026-11-10 search found only a secondhand forum post; link the primary page).
2. Record the distribution terms of ScriptHookV and each core dependency from the author's page (links).
3. Check the rules of Nexus Mods and GTA5-Mods for uploads (links).
