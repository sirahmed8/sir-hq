# PORTFOLIO (updated 2026-11-08)

True, verified facts only across all 16 SIR portfolio projects in `D:\Projects`.
Work model: **Claude Sonnet 5.5 (Claude desktop)** is manager and reviewer; **Antigravity chats (Gemini 3.8 Flash High)** are autonomous workers. AgentsRoom is retired (crashed React #185 on 2026-11-08; archived to `SIR AI/legacy/agentsroom/`). AHome appears as counts and status only; private data never leaves local systems. No pull requests: all changes commit and push straight to `main`.

## 16 Products in D:\Projects

| Product | Folder | Branch | Commits | Last commit | Since 11-02 | Wave | Status | Tasks | Scope & Current Reality |
|---|---|---|---|---|---|---|---|---|---|
| **AHome** | `AHome` | `main` | 303 | 2026-11-08 | +98 | Wave 1 | Building | 52/79 | Private (counts only). Security & two-way sync engine for Google Tasks/TickTick/ICS, telegram contact spoof hardening, drop unsafe-eval from CSP, dual deploy live (Vercel + Firebase). |
| **SIR Study** | `SIR Study` | `main` | 58 | 2026-11-08 | +49 | Wave 2 | Building | 16/33 | Cycle 4 complete: SAD 25-question exam simulation, live countdown ticker (09/11 11:30 Cairo), keyboard Anki ergonomics, universal A4 print engine, commit aa5c5f8 pushed to main. |
| **SIR Jobs** | `SIR Jobs` | `main` | 44 | 2026-11-08 | +35 | Wave 2 | Building | 21/21 | Standing orders & Cycle 3 complete: theme window resolution with headless CDP test, sw v2 Network-First, CSP strictly default-src 'self', 86 tests pass, 5 staged remote opportunities delivered to Telegram (message_id=382), commit 2545e7d pushed to main. |
| **SIR Laptop Manager** | `SIR Laptop Manager` | `main` | 29 | 2026-11-08 | +19 | Wave 2 | Building | 12/27 | Cycle 2 complete: ops-ui daemon persistence in dev-start, process drilldowns, shortcuts cheatsheet, dry-run rollback preview, ops UI server on 127.0.0.1:8765, 38 pytest pass, strict mypy 0 errors, commit 350ab80 pushed to main. |
| **SIR Negm Furniture** | `SIR Negm Furniture` | `main` | 12 | 2026-11-08 | +2 | Wave 3 | Building | 8/16 | M0, M1, M4, M5 shipped: pure geometric engine (`packages/planner-engine`), 2D blueprint studio with 5cm grid snapping, 3D Three.js hardware view, catalog drawer, WhatsApp BOM quote engine (+20 100 286 1668). 175 tests pass. Commit 1501e91 pushed to main. |
| **SIR AI** | `SIR AI` | `main` | 10 | 2026-11-08 | +1 | Wave 4 | In Planning | 3/44 | Ahmed's Jarvis: Sovereign Workstation Command & Multi-Tenant SaaS. M0 deep scan & 100x plan upgrade complete (.sir/reports/deep-scan.md, 5-layer Clean Architecture, 44 tasks across M0-M6, latency benchmarks, production topology). Commit 8ee4314 pushed to main. |
| **SIR Content Creation Studio** | `SIR Content Creation Studio` | `main` | 9 | 2026-11-01 | +0 | Wave 4 | Ready | 2/19 | Core media studio, ByteVibeHQ publishing module, video rendering templates. |
| **SIR Business** | `SIR Business` | `main` | 10 | 2026-11-01 | +0 | Wave 5 | Ready | 2/22 | Flagship monorepo core unifying 4 vertical modes: Restaurant, Market, Pharmacy, and Library (all preserved in `legacy/`). |
| **SIR Hagoozat** | `SIR Hagoozat` | `main` | 10 | 2026-11-01 | +0 | Wave 5 | Ready | 2/24 | Flagship Hagoozat Elite booking core absorbing Merged sites, 11Players, and EGFootball5 (all preserved in `legacy/`). |
| **SIR Obour Hub** | `SIR Obour Hub` | `main` | 10 | 2026-11-01 | +0 | Wave 5 | Ready | 2/28 | Flagship golden path product absorbing legacy Obour Academic Hub. Key rotation at launch. |
| **SIR ModPack** | `SIR ModPack` | `main` | 9 | 2026-11-01 | +0 | Wave 6 | Ready | 2/18 | Public release v1.0.0, mod package distribution. Maintenance. |
| **SIR Mods for GTA V** | `SIR Mods for GTA V` | `main` | 9 | 2026-11-01 | +0 | Wave 6 | Ready | 2/18 | GTA V mod portal; admin auth security hardening and secret regeneration pending. Maintenance. |
| **SIR Life** | `SIR Life` | `main` | 15 | 2026-11-08 | +6 | Wave 6 | Building | 7/24 | Personal OS life layer: calendar store sync, Telegram reminders, daily brief feeds, `sanitizeOutbound` privacy chokepoint with 65/65 tests green. |
| **SIR Platform** | `SIR Platform` | `main` | 9 | 2026-11-01 | +0 | Wave 7 | Ready | 2/29 | Shared platform kit (auth, billing Coming Soon fallback, legal pack) extracted from finished products. |
| **SIR Portfolio** | `SIR Portfolio` | `main` | 9 | 2026-11-01 | +0 | Wave 7 | Ready | 2/19 | Ahmed's public showcase site built from verified shippable products. |
| **SIR Controller** | `SIR Controller` | `main` | 9 | 2026-11-01 | +0 | Wave 8 | Ready | 2/20 | Hardware and PC optimization core (legacy SIR Optimizer absorbed into `legacy/`). |

## Consolidated Legacy Locations (Read-Only until M6 Cutover)
Every merged product preserves its original source code in `legacy/` inside its new SIR project folder. Never delete `legacy/` before Milestone 6.
- `SIR Hagoozat/legacy/`: `11Players`, `EGFootball5`, `Merged sites` (Hagoozat Elite launcher)
- `SIR Business/legacy/`: `SIR Restaurant`, `SIR Market`, `SIR Pharmacy`, `SIR Library`
- `SIR Laptop Manager/legacy/`: `Laptop manager`, `antigravity-agent-suite` (97 skills)
- `SIR Controller/legacy/`: `SIR Optimizer`
- `SIR Obour Hub/legacy/`: `Obour Academic Hub`
- `SIR AI/legacy/`: `agentsroom` (archived 2026-11-08), `SIR Tele Gateway`, `SIR Odysseus (removed 2026-11-01)`

## Non-Product Directories in D:\Projects
- `_SIR`: Workspace laws, standard, phases, plans, operations log, briefs, and tooling. (47 commits since 2026-11-02).
- `AI_Models_Hub`: Centralized Ollama model store (user env `OLLAMA_MODELS` points here). Duplicate `D:\AI_Models_Hub` purged on 2026-11-01.
- `Backups`: Local private snapshots, agent history backups, startup entries.
- `Android`: Local Android SDK, tools, and JDK.
- `old projects`: Deprecated archives (`SIR Odysseus`, `Learning`).
- `_quarantine`: Staging area for suspect or unverified files; gitignored.

## Waves Strategy
- **Wave 1:** AHome first (home sanctuary, local-only private AI, Pass 67).
- **Wave 2:** Automations & Urgent Foundations (SIR Study midterm exam cram packs, SIR Jobs verified gig income, SIR Laptop Manager deep scan & Windhawk inventory).
- **Wave 3:** Friend's handoff pack (SIR Negm Furniture client pack & Room Planner).
- **Wave 4:** AI and content (SIR AI gateway & clean-room learnings, SIR Content Creation Studio media pipeline).
- **Wave 5:** Earn the most (SIR Business monorepo core, SIR Hagoozat booking engine, SIR Obour Hub academic portal).
- **Wave 6:** Other paying products & personal OS (SIR ModPack, SIR Mods for GTA V, SIR Life daily feed aggregator).
- **Wave 7:** Extract and polish (SIR Platform shared kit, SIR Portfolio public showcase).
- **Wave 8:** Optional, last (SIR Controller hardware/system optimization).
