# PLAN: SIR Mods for GTA V (Wave 6, GLOBAL product, not started, HIGH LEGAL RISK)
Audited 2026-11-10. Replaces `SIR Mods for GTA V (v1)` (in `legacy/`, kept until M6). Single-player only. Free base, optional supporter tier in EGP. Because of third-party code and game-publisher rules this plan has a hard gate: nothing is sold or distributed publicly until M0 licence and policy checks are green. **GLOBAL**: anyone in the world, accounts, subscriptions, every platform and OS including phone, watch, car, TV. Owner-only analytics page, dual hosting (Firebase + Vercel), subscription grants owner all permissions.

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
Owner buys domain and code-signing certificate and creates payment accounts only after the M0 gate passes. Legal pack: privacy, terms/EULA (single-player, no warranty, user installs at own risk), DMCA/takedown form, third-party credits page, sub-processors; lawyer review mandatory before any paid launch.
**Dual hosting**: Firebase Hosting AND Vercel (import GitHub repo with Vercel CLI), same build, same env vars on both. Both addresses curl-checked (retry once on timeout).
Visibility: Arabic and English GTA V mod queries, install guides and YouTube tutorials, `llms.txt`, facts page.

## 10. Three-Milestone Roadmap (owner-visible checks)
| Milestone | Goal | Owner-Visible Exit Check |
|---|---|---|
| **M1: Gate & Core Slice** | `docs/THIRD_PARTY.csv` complete; official publisher policy read and summarized; secrets rotated list handed to OWNER_ACTIONS; installer installs and uninstalls on a temp folder with hash equality | 1. `docs/THIRD_PARTY.csv` → every binary has row with proof. 2. `docs/PUBLISHER_POLICY.md` has URL and read date. 3. Secrets rotation list in `docs/OWNER_STEPS.md` (names only). 4. Run installer on temp folder → install → uninstall → hashes equal to start. 5. Screenshot at 390/1280, LTR/RTL, light/dark. |
| **M2: Security, Legal, Billing, Owner Page** | Portal catalog and admin with real data; NPC server runs locally; forged cookie test, key grep, rate limit test, legal pages, owner-only analytics page live | 1. Forged cookie → 401/403 on all admin routes (test). 2. Grep finds no key in client bundle. 3. Rate limit test passes. 4. Open `/owner` → server-verified token required → shows installs, NPC sessions. 5. Legal pages exist at `/legal/*`. 6. Pricing page shows "Launching soon" + email capture. 7. Dual hosting verified: curl both Firebase and Vercel URLs. |
| **M3–M6: AI, Quality, Release** | NPC dialog eval recorded; clean-VM install test, screenshots, a11y, RTL; public release only if M0 gate stays green; legacy archived | 1. Run `npm run eval:npc` → 40 prompts pass safety/persona. 2. Clean VM install test passes. 3. Lighthouse mobile 90+ JSON saved. 4. Public release only if M0 gate green. 5. Legacy archived. |

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

*Every claim in competitor matrix must carry a source link or "(unsourced, verify)".*

## 15. Feature Parity Target (best-in-category)
Match or exceed the best GTA V mod site for: curated single-player pack, one-click reversible installer, AI NPC conversations, Arabic guide, no paywall on mod files, publisher policy compliance, signed installer, owner analytics, WCAG 2.2 AA.