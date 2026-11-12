# PLAN: SIR Mods for GTA V (Wave 6, GLOBAL product, not started, HIGH LEGAL RISK)
Audited 2026-11-12. Replaces `SIR Mods for GTA V (v1)` (in `legacy/`, kept until M6). Single-player only. Free base, optional supporter tier in EGP. Because of third-party code and game-publisher rules this plan has a hard gate: nothing is sold or distributed publicly until M0 licence and policy checks are green. **GLOBAL**: anyone in the world, accounts, subscriptions, every platform and OS including phone, watch, car, TV. Owner-only analytics page, dual hosting (Firebase + Vercel), subscription grants owner all permissions.

## 1. Purpose (plain words)
An installer and a website for a set of GTA V single-player mods, plus an AI-driven city-life mod (NPC conversations). A player installs the mods in a few clicks and can undo it. For global users: any GTA V single-player modder anywhere can use the same installer and AI NPC mod.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Mods for GTA V` |
| GitHub (private) | `sirahmed8/sir-mods-for-gta-v` |
| Stack (planned) | Windows installer (Electron or Tauri v2, decided in an ADR), manifest with SHA-256, web portal on Cloudflare Pages, a small server for the NPC AI (Node or Python, keys server-side only) |
| Domain | candidate `sirgtamods.com` (owner checks and buys; price "(unsourced, verify)"); `pages.dev` until then |
| Platforms | **Platform Matrix (GLOBAL):** Windows installer ✅ and web portal ✅. Linux/macOS: ⏭️ skipped (the game's mod tools are Windows). Mobile, TV, watch, Car: ⏭️ skipped. Browser extension: skipped. All platforms share the same Firebase project and auth. |
| Money | **Pricing & Free Tier:** Free base (all mods, installer, uninstall). Supporter tier in EGP is allowed only if M0 policy check says paid mod access is acceptable; default is donations and cosmetic supporter perks only until then. EGP first, USD/SAR/AED toggle auto-detected from locale/IP with manual override. "Launching soon" + email capture until keys exist. Owner gets all perks free. Subscription grants owner all permissions in owner dashboard. |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30); 9 commits. PORTFOLIO.md: 2 of 18 tasks, "admin auth hardening and secret regeneration pending".

Legacy facts (`ops/inventory/SIR-ModPack-and-GTA-V-mods.md`, 2026-10-29, nothing run): admin gate was forgeable (cookie set from client JavaScript; a stopgap was merged separately); `.env` files were tracked in three places; about 90 third-party DLLs (ScriptHookV by Alexander Blade, MinHook, dinput8 and about 87 script DLLs) were redistributed with no licence files; the README said 79 tests while the count was 28; EULA says not for GTA Online. Secrets in those `.env` files must be rotated (owner list).

## 4. Rules (each needs a test or command)
1. Hard gate: no third-party DLL or mod is redistributed unless `docs/THIRD_PARTY.csv` has name, author, licence text, source URL and "redistribution allowed: yes with proof". Items without proof are not bundled; the installer tells the player where to download them from the author. CI fails on a binary without a row.
2. Publisher policy: reportedly Take-Two tolerates single-player, non-commercial mods that respect its IP (secondhand forum report, 2026-11-10 search; verify against the official Take-Two/Rockstar policy page at M0). Default: single-player only, nothing for GTA Online, no paid gating of mod files, no Rockstar assets redistributed, "not affiliated" notice.
3. Server-side admin: verified ID token plus allow-list, fail closed (use `owner-auth` from SHARED_PLATFORM_KIT); no cookie built in the browser grants anything. Test: forged cookie returns 401/403 on every admin route.
4. Secrets never in git; NPC AI keys only on the server; CORS locked; rate limit per IP and per account (use `ai-proxy` from SHARED_PLATFORM_KIT). Test: no key string in the client bundle (grep).
5. Installer is reversible: it backs up the files it replaces, writes an install log, and "Uninstall" restores them. Test on a temp game folder: install then uninstall leaves hashes equal to the start.
6. The NPC AI never sends player identity or game files off the machine; conversation text goes through the server proxy with a profanity and safety filter; kill switch.
7. No unprovable claims in copy (test counts, "undetectable", performance numbers) without a script that reproduces them.
8. **Owner-only analytics page**: separate route, server-verified owner token, shows all metrics (installs, uninstalls, NPC sessions, errors). No other user sees it.

## 5. Shared pieces
Platform `owner-auth`, `ai-proxy` (NPC dialog provider chain, quotas), `billing-fallback`, `legal-pack`, `i18n`, `ui/styles/hooks`, Telegram sender. Installer/manifest/hash code is shared in shape with SIR ModPack; write a small `packages/installer-core` in whichever of the two starts first and reuse by copy until Platform extracts it. **Reuses SHARED_PLATFORM_KIT entirely; only GTA V-specific features differ.**

## 6. Screens and entities
Installer: Home (detect game folder), Mods list (with licence and source), Install/Update/Uninstall, Backups, Settings and Profile. Portal: Landing, Mods catalog, Guide, Supporters, Legal, Admin (real counts only), **Owner dashboard**. Entities: Mod, Manifest, Install, Backup, Supporter, Inquiry, NpcSession.
Five states, Arabic RTL first and English, themes, 320 px to 4K portal, WCAG 2.2 AA, own logo.

## 7. AI and support
NPC dialog assistant (flagship), support assistant grounded in the guide. Chain via `ai-proxy` (from SHARED_PLATFORM_KIT), per-session cost cap, kill switch, evals: 40 dialog prompts with safety and persona checks; latency measured and recorded. Free quota 5 per day for the support bot.

## 8. Operations (standard 26 from SHARED_PLATFORM_KIT)
Installer telemetry only with consent (install success/failure, game version), crash report option, weekly Telegram line, mod update watcher, status JSON, emergency alerts (admin auth failure spikes, key leak).

## 9. Launch, legal and visibility
Owner buys domain and code-signing certificate and creates payment accounts only after the M0 gate passes. Legal pack: privacy, terms/EULA (single-player, no warranty, user installs at own risk), DMCA/takedown form, third-party credits page, sub-processors; lawyer review mandatory before any paid launch. **Dual hosting**: Firebase Hosting AND Vercel (import GitHub repo with Vercel CLI), same build, same env vars on both. Both addresses curl-checked (retry once on timeout). Visibility: Arabic and English GTA V mod queries, install guides and YouTube tutorials, `llms.txt`, facts page.

## 10. Six-Milestone Roadmap (owner-visible checks)
| Milestone | Goal | Owner-Visible Exit Check |
|---|---|---|
| **M1: Gate & Core Slice** | `docs/THIRD_PARTY.csv` complete; official publisher policy read and summarized; secrets rotated list handed to OWNER_ACTIONS; installer installs and uninstalls on a temp folder with hash equality | 1. `docs/THIRD_PARTY.csv` → every binary has row with proof. 2. `docs/PUBLISHER_POLICY.md` has URL and read date. 3. Secrets rotation list in `docs/OWNER_STEPS.md` (names only). 4. Run installer on temp folder → install → uninstall → hashes equal to start. 5. Screenshot at 390/1280, LTR/RTL, light/dark. |
| **M2: Security, Legal, Billing, Owner Page** | Portal catalog and admin with real data; NPC server runs locally; forged cookie test, key grep, rate limit test, legal pages, owner-only analytics page live | 1. Forged cookie → 401/403 on all admin routes (test). 2. Grep finds no key in client bundle. 3. Rate limit test passes. 4. Open `/owner` → server-verified token required → shows installs, NPC sessions. 5. Legal pages exist at `/legal/*`. 6. Pricing page shows "Launching soon" + email capture. 7. Dual hosting verified: curl both Firebase and Vercel URLs. |
| **M3: AI, Quality, Screens** | NPC dialog eval recorded; clean-VM install test, screenshots, a11y, RTL; public release only if M0 gate stays green; legacy archived | 1. Run `npm run eval:npc` → 40 prompts pass safety/persona. 2. Clean VM install test passes. 3. Lighthouse mobile 90+ JSON saved. 4. Public release only if M0 gate green. 5. Legacy archived. |
| **M4: Owner Enhancements** | Owner dashboard shows full metrics, billing fallback live, subscription grants all permissions | 1. Owner dashboard loads with real metrics from emulator. 2. Billing fallback page shows currency auto-detected and email capture. 3. Subscription grants owner all permissions in dashboard. |
| **M5: Multi-Lingual & Accessibility** | Full Arabic RTL and English LWCAG 2.2 AA across all screens; five states on every view | 1. Every screen at 320/390/768/1280/1920 in Arabic RTL and English LTR. 2. WCAG 2.2 AA contrast verified by tool. 3. Five states (idle, loading, empty, error, populated) on every screen. |
| **M6: Public Release & Legacy Archive** | Public release candidate; legacy archived; CI green; domain live | 1. Public release candidate built and domain `sirgtamods.com` live. 2. Legacy `legacy/` archived with read-only marker. 3. CI green on all gates. 4. Domain serves both Firebase and Vercel. |

## 11. Next 10 tasks (each under 2 hours)
1. Inventory every binary in `legacy/` (name, size, SHA-256) into `docs/THIRD_PARTY.csv` with blank licence columns. Check: row count equals binary count.
2. Research each top-level dependency (ScriptHookV, MinHook, dinput8) for its distribution terms and fill the CSV with source URLs. Check: no cell empty or marked "unknown, do not bundle".
3. Read the official publisher mod policy and write `docs/PUBLISHER_POLICY.md` with URL and read date. Check: file exists with quoted headings.
4. CI check "no binary without CSV row" plus gitleaks. Files: `scripts/check-binaries.mjs`. Check: injected binary fails.
5. Scaffold portal with server-verified admin and `/api/health`. Check: forged cookie test returns 403.
6. Installer core: detect game folder, copy with backup, uninstall. Files: `packages/installer-core/`. Check: temp-folder test, hashes equal after uninstall.
7. Manifest generator with SHA-256 and a licence-column requirement. Check: missing licence fails.
8. NPC server skeleton with provider interface and per-session cost cap. Check: cap test stops after N tokens.
9. Portal catalog page with five states and honest claims lint. Check: screenshots at 390 px; lint rejects "undetectable".
10. Owner list file: rotate the keys that were in the tracked `.env` files (names only), `ADMIN_SECRET_KEY` at deploy. Check: list in `docs/OWNER_STEPS.md`, no key values.

## 12. Risks and open questions (defaults)
- Publisher policy and DMCA risk: default is no commercial gating, single-player only, instant takedown.
- Third-party DLL licences: default is do not bundle without proof.
- Anti-cheat/online ban risk for players who use mods online: default is a clear warning and block of installs while the game process runs.
- Competitor claims (Nexus Mods, GTA5-Mods): `plans/competitors/sir-mods-for-gta-v.md` must carry links or "(unsourced, verify)".

## 13. Only the owner can do
Rotate leaked keys; buy domain and certificate; accept payment gateway terms; contact mod authors for permission; lawyer review before paid launch.

## 14. Competitor Matrix (from plans/competitors/sir-mods-for-gta-v.md)
| Competitor | Strengths | Flaws | Our Edge | Ideas to Steal |
|---|---|---|---|---|
| Nexus Mods | Huge library, community | No curated pack, no installer, no AI NPC | Curated single-player pack, one-click installer, AI NPC mod | Mod management |
| GTA5-Mods.com | Large selection | Manual install, no quality gate | Curated, verified, one-click, Arabic guide | Variety |
| OpenIV | Full modding toolset, OpenIV .oiv support | No one-click installer, no AI, no portal | Integrated installer + AI NPC + web portal | .oiv package parsing |
| FiveM | Framework for multiplayer mods, resource hub | Not for single-player, different rules | Focused on single-player only, no GTA Online conflict | Resource management ideas |
| ModDB | Established mod database, community | No installer, no quality gate, mixed commercial/non-commercial | Curated single-player pack with verified mods | Mod discovery layout |
| Steam Workshop (GTA V) | Built-in, auto-updates, discoverable | Heavily curated, limited to workshop format, not single-player focused | Curated single-player outside workshop | Workshop discovery UI |
| GTA Forums Mod Section | Large community, long-standing | No quality gate, inconsistent formatting, no installer | Curated, verified, one-click experience | Forum integration |
| Reddit (r/GTAMods) | Community discussion, feedback | No curation, no installer, no quality control | Curated pack with quality gate | Thread aggregation |
| Personal Trainer (trainer mods) | Specific gameplay tweaks, trainer features | No installer, no curated pack, safety concerns | Safe-mode toggles, reversible installer | Individual tweak UI |

*Every claim in competitor matrix must carry a source link or "(unsourced, verify)".*

## 15. Feature Parity Target (best-in-category)
Match or exceed the best GTA V mod site for: curated single-player pack, one-click reversible installer, AI NPC conversations, Arabic guide, no paywall on mod files, publisher policy compliance, signed installer, owner analytics, WCAG 2.2 AA.

## 16. Feature Detail (best-in-category plus owner ideas from TickTick and legacy)
- **Curated single-player pack**: Hand-picked mods with licence proof, organised by category (graphics, handling, vehicles, gameplay)
- **One-click reversible installer**: Detects game folder, backs up original files, installs to `mods\` folder, uninstall restores originals
- **AI NPC conversations**: Server-driven NPC dialog assistant with safety filter, per-session cost cap, kill switch
- **Arabic guide**: Full Arabic RTL support for installation guides and configuration
- **No paywall on mod files**: All core mods free; optional curated audio/vehicle packs as one-time EGP fee
- **Publisher policy compliance**: Single-player only, "not affiliated" notice, no Rockstar assets redistributed
- **Signed installer**: Code-signing certificate for Windows installer (tauri/electron)
- **Owner analytics**: Installs, uninstalls, NPC sessions, errors, all server-verified behind owner token
- **WCAG 2.2 AA**: Full accessibility compliance across all screens
- **From TickTick/legacy ideas**: Dynamic Island-style spring animations, per-chapter progress tracking, offline mode for mod configuration, bilingual (AR/EN) toggle, game mode integration with SIR Laptop Manager
- **From legacy insights**: `.oiv` package parser, handling.meta tuner, vehicle sound switcher, texture memory allocator, clean uninstaller with orphan vacuum

## 17. Platform Matrix
| Platform | v1 Includes |
|---|---|
| **Windows (Desktop)** | Tauri/Electron installer, full mod management, handling editor, graphics presets, NPC AI server integration |
| **Web Portal** | Landing, mods catalog, guide, supporters, legal, admin (owner-only), responsive 320px to 4K, Arabic RTL and English LTR |
| **Linux** | ⏭️ skipped (game mod tools Windows-only) |
| **macOS** | ⏭️ skipped (game mod tools Windows-only) |
| **Android** | ⏭️ skipped (no touch-first mod installation model for GTA V) |
| **iOS** | ⏭️ skipped (same as Android) |
| **Wear OS** | ⏭️ skipped |
| **watchOS** | ⏭️ skipped |
| **TV** | ⏭️ skipped |
| **Car OS** | ⏭️ skipped |

## 18. Architecture on the Shared Kit
- **Accounts**: Firebase Auth (Google sign-in), server-verified ID token, owner allow-list `OWNER_UIDS`, fail-closed, HttpOnly Secure SameSite=Strict session cookie, no localStorage tokens, rate limits on sign-in, 2FA offer for admin accounts (from `plans/SHARED_PLATFORM_KIT.md` section 1).
- **Owner-Only Analytics Page**: Route `/owner`, gated by server-verified owner token from `owner-auth`, fail closed, shows real metrics only (installs, uninstalls, NPC sessions, errors, AI cost). No other user sees it; middleware returns 403 for non-owner (from `plans/SHARED_PLATFORM_KIT.md` section 3).
- **AI with the fallback chain**: `ai-proxy` (from `plans/SHARED_PLATFORM_KIT.md` section 6): provider chain Gemini `flash-lite-latest` → `flash` → any Gemini → OpenRouter free → other free → local models (Ollama in `D:\Projects\AI_Models_HUB`). Per-project keys on product's own Firebase/GCP project and own OpenRouter key. Per-session cost cap, kill switch `AI_ENABLED` env var, daily cost cap in `config/limits.json`. Free quota 5 per day for support bot.
- **Hosting**: Firebase Hosting (primary, custom domain `sirgtamods.com` once bought, else `pages.dev`) AND Vercel (import GitHub repo with Vercel CLI, same build, same env vars on both). Both addresses curl-checked (retry once on timeout) and written in checkpoint (from `plans/SHARED_PLATFORM_KIT.md` section 15).

## 19. Premium Quality Bar (Apple-level motion, Arabic and English, five states, accessibility)
- **Themes**: light, dark, system, high contrast (WCAG 2.2 AA) - design tokens only.
- **Motion**: Spring physics only (transform and opacity, 120Hz safe). No layout-thrashing animations. Matching open/close for every sheet, panel, modal, drawer, overlay. Dynamic Island pattern: continuous morph, single instance, never covers composer or tab bar. Tab bar: active label centered in pill, swipe between tabs, sized to text, min 44px. Scroll into view: active tab scrolls into view on mount and tab change.
- **Arabic and English**: Bidi first - per-character detection in inputs (Arabic types from right, Latin from left); mixed content uses `<bdi>` or `unicode-bidi: isolate`; never show "(RTL)"/"(LTR)" to users. RTL-first: logical CSS properties only (margin-inline-start, padding-inline-end, etc.). Auto-detect currency/region from visitor locale/IP with manual override on top.
- **Five states** on every screen: idle, loading skeleton, empty with one action, error with retry, populated.
- **Accessibility**: WCAG 2.2 AA contrast verified by tool. Minimum 44px touch targets. `escHtml()` for every interpolated text/attribute. `escapeJs()` only inside inline handler args. `safeHref()` allowing only http(s) for every external link.
- **Click-target audit**: every interactive element must have a real, unobstructed hit area (min 44px). No absolutely-positioned element may sit on top of a button without intentional `pointer-events`.
- **No literal "(RTL)"/"(LTR)" in copy**: language toggles show only "English" / "العربية". Auto-detect direction per character live.

## 20. Free Tier and Fair Pricing Outline (EGP and USD)
- **Free tier**: All core mods, installer, uninstall, NPC support bot (5 per day). No paywall on mod files.
- **Supporter tier (EGP)**: Optional cosmetic supporter perks only until M0 policy check passes. Default is donations only.
- **Curated audio/vehicle packs**: 49 EGP one-time pack fee (Paymob test checkout integrated with "Launching Soon" fallback).
- **Currency**: EGP first, USD/SAR/AED toggle auto-detected from visitor locale/IP with manual override (never manual picker as only way).
- **Pricing page**: "Launching soon" + email capture that writes a Lead document and rejects an invalid address.
- **Owner permissions**: Subscription grants owner all permissions in owner dashboard.
- **USD equivalent**: EGP 49 ≈ USD 3.00 at fixed rate (EGP 16.35 = USD 1), adjustable when payment gateway keys are live.

## 21. Milestones M0 to M6 with Acceptance Tests
| Milestone | Acceptance Tests |
|---|---|
| **M0: Licence & Policy Gate** | 1. `docs/THIRD_PARTY.csv` complete with proof row for every binary. 2. `docs/PUBLISHER_POLICY.md` has URL and read date. 3. Secrets rotation list in `docs/OWNER_STEPS.md` (names only). 4. Run installer on temp folder → install → uninstall → hashes equal to start. 5. Screenshot at 390/1280, LTR/RTL, light/dark. |
| **M1: Core Slice** | 1. Installer installs and uninstalls on temp folder with hash equality. 2. Portal landing page loads with mods catalog. 3. NPC AI server responds to health check. 4. Arabic RTL and English LTR toggle works. 5. WCAG 2.2 AA contrast on all pages. |
| **M2: Security + Legal + Billing** | 1. Forged cookie → 401/403 on all admin routes (test script). 2. Grep finds no key in client bundle (grep test). 3. Rate limit test passes (per IP and per account). 4. Open `/owner` → server-verified token required → shows installs, NPC sessions. 5. Legal pages exist at `/legal/*`. 6. Pricing page shows "Launching soon" + email capture. 7. Dual hosting verified: curl both Firebase and Vercel URLs. |
| **M3: AI + Quality + Screens** | 1. Run `npm run eval:npc` → 40 prompts pass safety/persona. 2. Clean VM install test passes. 3. Lighthouse mobile 90+ JSON saved. 4. Public release only if M0 gate green. 5. Legacy archived. |
| **M4: Owner Enhancements** | 1. Owner dashboard loads with real metrics from emulator. 2. Billing fallback page shows currency auto-detected and email capture. 3. Subscription grants owner all permissions in dashboard. 4. Owner list file has rotated keys, no key values committed. |
| **M5: Multi-Lingual + Accessibility** | 1. Every screen at 320/390/768/1280/1920 in Arabic RTL and English LTR. 2. WCAG 2.2 AA contrast verified by tool. 3. Five states (idle, loading, empty, error, populated) on every screen. 4. Bidi detection per character live in all inputs. 5. No "(RTL)"/"(LTR)" in copy. |
| **M6: Public Release & Legacy Archive** | 1. Public release candidate built and domain `sirgtamods.com` live. 2. Legacy `legacy/` archived with read-only marker. 3. CI green on all gates. 4. Domain serves both Firebase and Vercel. |

## 22. First 10 Tasks for Free Agents (queue ready)
1. **Inventory every binary in `legacy/`**: Scan the three legacy apps and write one honest matrix to `.sir/reports/parity.md`: every route, every API route and every component with no route, each with the source file that proves it, and a verdict of keep, port, drop or drop-with-reason, plus the target module of the new build (`booking`, `mods`, `installer`, `catalog`, `admin`, `ai`, `npc`, `profile`). Check: row count equals binary count. Report: what was found, the count of routes per app, the ten biggest files to split, and the list of features that must be dropped on purpose.

2. **Research top-level dependencies**: For each top-level dependency (ScriptHookV, MinHook, dinput8 and about 87 script DLLs), research its distribution terms and fill `docs/THIRD_PARTY.csv` with source URLs. Check: no cell empty or marked "unknown, do not bundle". Report: CSV row count, any unknown cells and their DLL names, and the list of DLLs cleared for bundling.

3. **Read the official publisher mod policy**: Read the official Take-Two/Rockstar policy page on single-player modding and write `docs/PUBLISHER_POLICY.md` with URL and read date. Check: file exists with quoted headings. Report: URL, read date, and key policy headings quoted.

4. **CI check "no binary without CSV row"**: Add the gitleaks check to the GitHub Actions workflow and verify that an injected binary fails the check. Files: `scripts/check-binaries.mjs`, `.github/workflows/verify.yml`. Check: injected binary fails both the CSV row check and gitleaks. Report: verify command output, CI run URL, and the gitleaks findings.

5. **Scaffold portal with server-verified admin**: Create the web portal scaffold in `apps/web` (Next.js 15+ App Router, React 19, TypeScript strict, Tailwind v4 with design tokens), `packages/core` (domain types and zod schemas for Mod, Manifest, Install, Backup, Supporter, Inquiry, NpcSession), `packages/data`, `packages/ui`, `packages/kit`, `apps/api`, `docs/`, `scripts/`, with layers depending inward only, files under 300 lines, absolute imports and no `any`. Add the `verify` script (typecheck, lint, tests, build, secret scan) and a GitHub Actions workflow that runs exactly that on `main`. Add a health route at `/api/health` returning real status values, never fake ones. Exit check: the verify command output is pasted into the report, the CI run URL is in it, and one screenshot of the shell exists in Arabic and in English at 390 px and 1280 px in `.sir/evidence/`. Report: the tree, the commands with their real output, and anything that could not be installed for free.

6. **Installer core**: Detect game folder, copy with backup, uninstall. Files: `packages/installer-core/`. Check: temp-folder test, hashes equal after uninstall. Report: the installer code path, the test output with before/after hashes, and the backup restore verification.

7. **Manifest generator with SHA-256**: Create a manifest generator with SHA-256 hash and a licence-column requirement. Check: missing licence fails. Report: the manifest generation code, the test that fails when licence is missing, and the hash format.

8. **NPC server skeleton**: Create NPC server skeleton with provider interface and per-session cost cap. Check: cap test stops after N tokens. Report: the server code, the cost cap test output, and the kill switch behaviour.

9. **Portal catalog page with five states**: Build the portal catalog page with five states (idle, loading skeleton, empty with one action, error with retry, populated) and honest claims lint. Check: screenshots at 390 px; lint rejects "undetectable". Report: the catalog page code, the five states implemented, the lint errors fixed, and the 390 px screenshots in Arabic and English.

10. **Owner list file**: Rotate the keys that were in the tracked `.env` files (names only), `ADMIN_SECRET_KEY` at deploy. Check: list in `docs/OWNER_STEPS.md`, no key values. Report: the rotated key names, the `docs/OWNER_STEPS.md` update, and confirmation that no key values are in git.

---

**Queue order and dependencies.** T1, T2 and T3 can run in parallel (T1 is read-only, T2 owns the repo scaffold, T3 owns the Firebase project and auth). T4 needs T2. T5 needs T2 and T4. T6 needs T2. T7 needs T2 and T6. T8 needs T2 and T5. T9 needs T2 and T8. T10 needs T3 and T2. Each task writes to its own area of the repository so two agents never fight over one file: T1 writes `.sir/reports/parity.md`, T2 writes the scaffold, `packages/ui` skeleton and the workflow, T3 writes `packages/kit/owner-auth` and `.firebaserc`, T4 writes `scripts/check-binaries.mjs` and the workflow, T5 writes `packages/installer-core/`, T6 writes `packages/ui`, T7 writes `apps/web/app/(player)/catalog`, T8 writes `packages/installer-core` and its tests, T9 writes `apps/web/app/(player)/catalog` five states, T10 writes `packages/kit/owner-auth` and `docs/OWNER_STEPS.md`. Each task writes to its own area of the repository so two agents never fight over one file.

**What is deliberately not in these ten:** the tournaments engine, the owner console with the cash register, the Windows installer, the AI features beyond the NPC support bot, the marketing work. They are M4, M5 and M6 in the plan and each one needs the ten above to be green first.
---

## 23. Refresh delta (2026-11-12, round r61, rule 20 rescan)

This section is the current truth where it differs from anything above. Research source: `ops/competitors/sir-mods-for-gta-v.md` section 5 (second pass, same date).

### 23.1 The two-edition reality (new, blocking for the installer)

- GTA V ships as Legacy (`GTA5.exe`, Gen8) and Enhanced (`GTA5_Enhanced.exe`, Gen9, builds 1.0.811.x/812.x, released 2025-03-25). ScriptHookV supports Enhanced since 2025-03-23, but most Legacy `.asi` scripts are broken on it (memory patterns changed; SHVDN issue #1558).
- Mods-folder loaders differ: Legacy = `OpenIV.asi`, Enhanced = `OpenRPF.asi`. RPF assets are not interchangeable between editions (Gen8 content crashes Gen9; CodeWalker converts).
- Decision (recommended): v1 detects the edition at install time (exe name + build number) and marks every catalogue mod with `editions: ["legacy"] | ["enhanced"] | ["both"]`. Mods without an Enhanced-safe loader are shown only to Legacy installs. Enhanced support ships in M3 at the earliest, after the Legacy path is proven; never install a Legacy-only asset onto Enhanced.

### 23.2 Monetisation correction (legal)

- Rockstar's official single-player mod support page was updated 2026-09-15 and links the Rockstar Games Mod Guidelines. Per secondary coverage, monetized mods are only allowed "via digital storefront providers approved by Rockstar Games" (reported as Cfx Marketplace). Selling mod files outside an approved storefront is now an explicit violation.
- Decision (recommended): every mod file stays free forever. Paid surface = services, not mods: NPC AI conversation packs (server-side quota), installer convenience features, supporter cosmetics. If paid mod packs are ever wanted, the only path is a Rockstar-approved storefront - owner decision, lawyer review first. This replaces the "49 EGP curated pack" line in section 20.

### 23.3 Competitive reality

- The drag-drop installer is no longer unique: ModDrop V (Legacy+Enhanced, 13 languages, profiles, load order, check-and-repair), Nexus ModMaster Fluent (`.oiv`/`.oivs`/`.nexus`, Legacy+Enhanced), ModsHub (FiveM sync), LSPDFRManager (open source, MIT), OIV Package Installer (CodeWalker core, `.oivs` wizard) all do it.
- Feature bar to match: profiles, mod load order and per-file conflict resolution, check-and-repair after game updates, `.ini/.xml/.json` config editing in-app, dlc.rpf registration in dlclist.xml, uninstall-all, game-version compatibility check before install.
- Surviving edges: AI NPC conversations (unique), licence-gated curated pack, Egyptian Arabic guide first, free forever, Rockstar-policy-safe by design, owner analytics page.

### 23.4 Data model (Firestore, product project `sir-mods-for-gta-v`)

Collections and key fields (full rules in `firestore.rules`, detail doc `docs/data-model.md`):

- `mods/{id}`: slug, name_ar, name_en, description_ar/en, category, editions[], loader (`openiv.asi`|`openrpf.asi`|`none`), files[] {path, sha256, size, target}, licence {name, author, sourceUrl, redistributionProof}, status (`draft|review|published|blocked`), owner_uid (curator), created_at, updated_at.
- `manifests/{gameVersion}/{edition}`: generated manifest per game build; entries reference mod ids + file hashes; signed with server key.
- `installs/{uid}`: game edition, game build, mod ids installed, install log entries, created_at. One doc per user, subcollection `installs/{uid}/events` for telemetry.
- `backups/{uid}/{id}`: snapshot metadata (which files, hashes), retention 30 days.
- `supporters/{uid}`: tier, perks, since, payment ref (names only, no card data).
- `inquiries/{id}`: contact form rows.
- `npcSessions/{id}`: uid, started_at, message count, tokens used, cost_usd, ended_at, kill_switch flag.
- `profiles/{uid}`: named install profiles (mod sets) for the multi-profile feature.
- `leads/{id}`: pricing-page email capture (email, locale, created_at).
- `auditLog/{id}`: owner/admin actions, server-written only.

### 23.5 API list (all server-side, keys never in client)

- `GET /api/health` - real status (db ping, ai provider chain status, manifest freshness).
- `GET /api/mods` - published mods filtered by detected edition; `GET /api/mods/:slug` - detail + licence block.
- `POST /api/manifest` - body {edition, gameBuild}; returns signed manifest for the installer. Rate limited.
- `POST /api/install-report` - installer posts install/uninstall result (consent-gated telemetry).
- `POST /api/npc/session` - start NPC dialog session; returns session id + provider chain order.
- `POST /api/npc/message` - {sessionId, text} -> streamed reply; enforces per-session token cap and daily quota.
- `POST /api/support/ask` - support bot, 5/day free quota, grounded in docs only.
- `POST /api/leads` - pricing email capture, validates address, writes `leads`.
- `GET /api/owner/metrics` - owner-only (server-verified token), real counts only.
- `GET /api/legal/*` - static legal pack pages.

### 23.6 AI features (via `ai-proxy`, all server-side)

1. NPC city-life dialog (flagship): persona-grounded conversations, safety + profanity filter, per-session token cap, daily cost cap, `AI_ENABLED` kill switch, 40-prompt eval suite.
2. Support assistant: grounded strictly in the guide/docs, 5 free questions/day, quota badge, upgrade prompt on exhaustion.
3. Mod-description writer (curator tool, owner-only): drafts AR/EN descriptions from licence notes; human approves before publish.
4. Crash-log triage: parses `ScriptHookV.log`/`asiloader.log`, names the failing script, suggests disable (runs locally, no AI needed for v1; AI summary optional later).

### 23.7 Security and privacy additions

- Edition/build fingerprint sent with install reports is minimal (edition + build number only); no file paths, no Steam id.
- Telemetry is opt-in per install; uninstall offers "remove my telemetry data" which deletes `installs/{uid}` and `npcSessions` for that uid.
- NPC dialog text is filtered server-side; nothing is stored beyond session metadata (message text kept 24h max for abuse review, then deleted - documented in privacy page).
- Manifest signing: server signs manifests with an Ed25519 key held in Secret Manager; installer verifies signature before applying; unsigned manifests are refused.

### 23.8 Launch and marketing additions

- Launch surfaces: GTA5-Mods.com tool page (if the policy gate passes - needs the tool to be a legit file tool, not a mod), Nexus Mods forum thread, r/GTAMods post, Egyptian Arabic YouTube tutorial (owner or hired), Discord server for support.
- SEO/GEO: `llms.txt`, `/facts` page, Arabic queries ("برنامج تثبيت مودات GTA V", "مود سيارات قراند 5"), English queries ("safe GTA V mod installer single player").
- 12-week calendar lives in the DEEP plan section 5.4; keep it, add the Enhanced-edition angle as a news hook ("works on Legacy AND Enhanced").
- Dual hosting from day one of the portal: Firebase Hosting + Vercel, both curl-checked.

### 23.9 Risks (each with the recommended answer)

- R1 Rockstar guideline change bans even free mod redistribution tooling: answer - the installer distributes zero Rockstar assets; mods are either licence-clean third-party files or links to authors; lawyer review before launch.
- R2 Enhanced edition fragments the audience and halves the usable mod list: answer - detect edition, ship Legacy first (bigger installed base today), add Enhanced-safe mods progressively.
- R3 A competitor ships the same AI NPC idea: answer - speed on the NPC eval suite and persona quality; the licence-gated pack and Arabic guide are not copyable quickly.
- R4 ScriptHookV/loader licence does not allow bundling: answer - CSV gate; bundle nothing without proof; installer can download-from-author mode.
- R5 Game updates break ScriptHookV offsets weekly: answer - version checker + update watcher + Telegram alert to owner; manifest per game build.
- R6 Paid surface accidentally looks like paid mods: answer - pricing page sells "supporter" and "AI conversation packs", never "mod files"; copy reviewed against the September 2026 guidelines.

### 23.10 Open questions (recommended answers)
- Q1 Can we sell AI conversation packs / supporter perks without touching the mod-files rule? Recommended: yes, they are services; still get lawyer sign-off.
- Q2 Do we support Enhanced at launch? Recommended: detect and warn; ship Legacy-only mods first.
- Q3 Domain: `sirgtamods.com` (section 2) vs `sirgtamods.app` (DEEP plan)? Recommended: owner picks one at purchase time; plan defaults to `.com`.
- Q4 Bundle ScriptHookV/dinput8 or require the player to install them? Recommended: require + verify + link to author (licence unproven until CSV task completes).
- Q5 GTA 6 released Nov 2026 - does it change anything for v1? Recommended: no for v1; revisit after launch if GTA V modding audience migrates.
