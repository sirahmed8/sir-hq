# PORTFOLIO (skeleton, Phase 0, 2026-10-29)

Facts only. Tier, wave, score and platform matrix stay `?` until the Phase 3 scan; nothing here is judged yet. Sizes are on-disk GB including `node_modules`/build output. Every git repo below has branch `pre-sir-snapshot` and tag `pre-sir-2026-10-29` (local only) and its `main` HEAD is on GitHub (verified with `git ls-remote`).

## Git repos in D:\Projects
| Project | Branch | Commits | Last commit | Size GB | GitHub repo (sirahmed8/…) | Tier/Wave/Score |
|---|---|---|---|---|---|---|
| 11Players | main | 430 | 2026-10-26 | 1.46 | 11Players | ? |
| AHome (was AhmedAndHabiba, renamed 2026-10-29) | main | 28 | 2026-10-28 | 1.23 | ahmed-and-habiba-sanctuary | ? (private, rule: never exposed) |
| EGFootball5 | main | 177 | 2026-10-26 | 1.24 | EGFootball5 | ? |
| Laptop manager | main | 41 | 2026-10-28 | 2.26 | laptop-manager | ? (3 untracked paths, local snapshot only) |
| Merged sites | main | 21 | 2026-10-26 | 1.00 | merged-sites | ? (holds Hagoozat Elite launcher target) |
| Negm Furniture | main | 17 | 2026-10-26 | 0.93 | negm-furniture-eg | ? |
| Obour Academic Hub | main | 121 | 2026-10-26 | 1.50 | obour-academic-hub | ? |
| Odysseus app | main | 3180 | 2026-10-26 | 1.55 | odysseus | ? (Windows build in `dist\win-unpacked`) |
| SIR AI | main | 65 | 2026-10-26 | 0.94 | SIR-AI | ? |
| SIR Content Creation Studio | main | 458 | 2026-10-26 | 2.90 | sir-content-creation-studio | ? |
| SIR Controller | main | 9 | 2026-10-26 | 0.87 | SIR-Controller | ? |
| SIR Library | main | 16 | 2026-10-26 | 0.92 | sir-library | ? |
| SIR Market | **master** | 23 | 2026-10-26 | 4.71 | sir-market | ? |
| SIR ModPack | main | 9 | 2026-10-29 | 16.86 | SIR-ModPack (**public**, release v1.0.0) | ? (largest; payload files). History rewritten 2026-10-29 to drop launcher account files; all SHAs changed; `.git` 1.2 GB → 6.5 MB; original at `D:\Backups\SIR-2026-10-29\SIR-ModPack-original.bundle` |
| SIR Mods for GTA V | main | 10 | 2026-10-26 | 3.19 | sir-mods-for-gta-v | ? |
| SIR Optimizer | main | 29 | 2026-10-26 | 0.85 | sir-optimizer | ? |
| SIR Pharmacy | main | 15 | 2026-10-26 | 0.93 | sir-pharmacy | ? |
| SIR Restaurant | main | 36 | 2026-10-26 | 2.74 | restaurant-os | ? (repo name differs from folder) |
| antigravity-agent-suite | main | 10 | 2026-10-26 | 0.01 | antigravity-agent-suite | ? |
| sirahmed8 (GitHub profile repo) | main | 18 | 2026-10-26 | 0.00 | sirahmed8 | n/a profile |

## Not git repos
| Folder | Size GB | What it holds | Backup |
|---|---|---|---|
| Jobs | 0.00 | CV, job scrapers, auto-apply scripts, trackers (personal data) | `D:\Backups\SIR-2026-10-29\Jobs.zip` |
| Learning | 0.00 | 4 small practice files (A.cpp, A.dart, A.py, A.exe) | `Learning.zip` |
| Obour Institute Second Year 1st term | 0.18 | 7 course folders, Moodle/sync scripts, study prompts | `Obour Institute Second Year 1st term.zip` |
| AI_Models_Hub | 9.22 | Ollama model blobs (bge-m3, deepseek-r1 1.5b, nomic-embed-text, qwen2.5 1.5b, qwen2.5-coder 1.5b, qwen3 8b) | manifest only, re-pullable |
| old projects | 0.35 | `Desktop_SIR_Tele_Gateway`, `SIR Tele Gateway` | `old projects.zip` |

## Desktop (C:\Users\a7med\Desktop)
25 folders, all `.lnk` launchers plus icons, no source: one per project above (SIR *, 11Players, EGFootball5, Hagoozat Elite, Laptop Manager, Negm Furniture, Obour Academic Hub, Odysseus, sirahmed8, Antigravity Agent Suite) and category folders (AI & Productivity, Development & Programming, Games & Launchers, Media & Social, NI Design Suite, System & Utilities). `NI Design Suite\Experiments` holds real files (the only non-shortcut content found); leave it alone.

## Outside the portfolio but on the disk
`D:\Games` is 199 GB (about 75% of D:). Personal; Phase 2.4 handles cleanup with quarantine, never deletion.

---
# Phase 3 strategy (2026-10-29): scores, tiers, waves, consolidation
Evidence: `ops/inventory/*.md` (scout reads, nothing built or run, so every score is a judgement from code reading), `ops/TICKTICK_MAP.md`. Priority = revenue x3 + closeness to shippable x2 + value to the platform x2 + Ahmed's priority x2 - effort (each 0-5; effort S=1, M=2, L=3, XL=4). Ahmed's priority comes from his TickTick goals: payment gateways on Obour Hub and the football sites, restaurant and shop systems.

| Product | Rev | Close | Platform | Ahmed | Effort | Score | Tier | Wave |
|---|---|---|---|---|---|---|---|---|
| Hagoozat Elite (Merged sites + 11Players + EGFootball5) | 4 | 3 | 4 | 5 | 3 | **33** | Flagship | 0 then 2 |
| SIR Business (Restaurant, Market, Pharmacy, Library on one core) | 5 | 2 | 5 | 4 | 4 | **33** | Flagship | 2-3 |
| Obour Academic Hub | 3 | 4 | 3 | 5 | 3 | **30** | Flagship, golden path | 1 |
| SIR Content Creation Studio (+ ByteVibeHQ media) | 3 | 3 | 4 | 4 | 2 | 29 | Core | 3 |
| SIR Controller (+ SIR Optimizer merged in) | 3 | 2 | 3 | 3 | 3 | 22 | Core | 0 then 3 |
| SIR AI | 2 | 2 | 4 | 3 | 3 | 21 | Core (its AI gateway feeds the platform) | 4 |
| Laptop manager (Personal OS, not sold) | 0 | 3 | 4 | 4 | 2 | 20 | Core, internal | 4 |
| Negm Furniture (client brand) | 2 | 4 | 1 | 3 | 2 | 20 | Maintenance, separate | 3 |
| SIR ModPack + SIR Mods for GTA V | 2 | 3 | 2 | 3 | 3 | 19 | Maintenance, kept as two repos (see ADR 10) | 0 for GTA V admin auth, then 4 |
| AHome (private, no subscription, local AI) | 0 | 3 | 2 | 5 | 2 | 18 | Core, private, never exposed | 4 |
| SIR Optimizer (as a stand-alone) | 3 | 2 | 2 | 2 | 3 | 18 | merged into SIR Controller | 3 |
| SIR Life (new, from the TickTick ideas) | 3 | 0 | 4 | 4 | 3 | 22 | Concept | 4+ |
| Odysseus app (fork, AGPL) | 1 | 1 | 1 | 2 | 3 | 8 | Maintenance, licence decision | 4 |

## Waves (2 projects at a time; Wave 0 is an emergency, everything else follows the sprint order)
- **Wave 0, internet-facing exploit paths (Oct 29-Nov 4):** Merged sites webhook (`dev_signature` accepts any payment), SIR Mods for GTA V forgeable admin cookie, SIR Controller unsigned webhook, SIR Optimizer self-grant OP mode and client-bundled keys, SIR AI client-trusted owner telemetry; secret rotations (owner actions). These need no platform work, only server-side checks.
- **Wave 1:** SIR Platform shared kit (owner claim from verified token, nonce CSP, billing with Coming Soon fallback, legal pack with truthful claims) built with **Obour Academic Hub as the golden-path product** (closest to shippable: CI, 47 tests, live, session cookie already httpOnly). Solve-modes removed.
- **Wave 2:** Hagoozat Elite parity (routes, AI layer, slot lock, deposits) and SIR Business core with **Restaurant first** (most complete, has CI).
- **Wave 3:** Market, Pharmacy, Library as vertical modes of the core; Content Creation Studio; SIR Controller absorbing Optimizer; Negm Furniture cleanup.
- **Wave 4:** SIR AI, Laptop manager + agent suite, AHome, ModPack/GTA hub, Odysseus licence, SIR Life.

## Consolidation decisions (ADR-style, reversible through the Ideas Inbox)
1. **Merged sites is Hagoozat Elite and absorbs 11Players and EGFootball5**, but the merge is not complete (29 pages vs 55 and 36). Originals stay where they are until a parity checklist passes; then they move to `old projects\` with pointer READMEs. EGFootball5 and 11Players keep their live URLs until redirects exist.
2. **SIR Business = one monorepo core with four vertical modes** (Restaurant, Market, Pharmacy, Library). The four apps are copies of one shell with the same defects (no data layer, fake auth, AI and payment, false compliance text), so fixing each separately is four times the work. Separate store names and installers per mode stay possible. Pharmacy's clinical claims (DDI rules, canned stock answers) are removed or sourced before any release: patient-safety risk.
3. **SIR Optimizer merges into SIR Controller** (same job, PC optimization; Controller has the larger desktop base and pricing). Laptop manager stays a personal tool, not a product; shared hardware code is extracted once.
4. **antigravity-agent-suite merges into Laptop manager's agent-config** (its 97 skills are synced nowhere); licence audit first; the global installer is retired.
5. **SIR Content Creation Studio keeps the "SIR Media" idea inside it** and gains ByteVibeHQ publishing as a module (Phase 8.2).
6. **Negm Furniture stays separate**: client brand, own domain; share tooling only. Its fake ratings, followers and login are removed first.
7. **TickTick ideas become modules**, not 30 projects (see `ops/TICKTICK_MAP.md`); only SIR Life is a new product.
8. **Odysseus**: a fork of odysseus-dev/odysseus under AGPL-3.0. Decision: stay AGPL and say so (no proprietary EULA, fake testimonials removed) or stop distributing it; no sales until settled.
10. **SIR ModPack and SIR Mods for GTA V stay separate repos for now**: the GTA V portal's admin gate is forgeable (cookie set in client JS, admin routes unchecked), the licences and game-EULA risks differ, and third-party DLLs (ScriptHookV and about 87 more) are redistributed without licence files. Fix auth and the redistribution question first.
9. **Never merge published apps** (app IDs are permanent): none are on a store yet, so the merges above carry no store migration.

## Cross-project findings that shape the platform (Phase 4)
Every project except Odysseus repeats: client-side owner or admin gates; webhooks without signature checks; AI keys or calls in the client bundle; fake login, payment or AI screens (some with invented stock or reviews); SOC 2 / ISO claims in privacy text that cannot be backed up; tracked binaries and personal files; identical generic AGENTS/CLAUDE/GEMINI copies instead of project context. The SIR Platform kit therefore ships: verified-claim owner checks, signed-webhook helper, server-side AI proxy with quota, Coming Soon billing fallback, a truthful legal pack, and a per-project `.sir/` file set.
