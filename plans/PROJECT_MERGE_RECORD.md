# PROJECT MERGE RECORD (from TickTick "30-Day Projects Sprint" and "أفكار برامج ومشاريع")
Source: `ops/TICKTICK_MAP.md` (2026-10-29), `ops/PORTFOLIO.md` (2026-11-08), `ops/OWNER_REQUEST_LEDGER.md` (2026-11-11). Never opened the "Accounts" note or the "habobty" column.

---

## Original TickTick "30-Day Projects Sprint" (24 tasks, Oct 28 – Nov 26)
Each sprint day was a security remediation task for one legacy product.

| Sprint Day | Legacy Product | Merged Into (Current SIR Product) | Status |
|---|---|---|---|
| Rotate secrets, Day 1 | Laptop manager, Tele Gateway, GTA V, ModPack | SIR Laptop Manager, SIR AI, SIR Mods for GTA V, SIR ModPack | Keys rotated per project; legacy keys archived |
| Day 2 shared kit | Platform (concept) | Shared standards kit, `SHARED_PLATFORM_KIT.md` (SIR Platform cancelled 2026-11-12) | Standards every product follows; not a product |
| Day 3 Hagoozat/merged-sites | Merged sites (Hagoozat Elite) | SIR Hagoozat (Wave 5) | `legacy/` has 11Players, EGFootball5, Merged sites |
| Day 4 SIR Controller | SIR Controller | SIR Controller (Wave 8) | `legacy/` has SIR Optimizer absorbed |
| Day 5 SIR CCS | Content Creation Studio v1 | SIR Content Creation Studio (Wave 4) | `legacy/` preserved |
| Day 6 SIR AI | SIR AI v1, SIR Tele Gateway, AgentsRoom | SIR AI (Wave 4) | `legacy/` has all three; Tier 1 personal first |
| Day 7 EGFootball5 | EGFootball5 | SIR Hagoozat (Wave 5) | Absorbed into Hagoozat Elite |
| Day 8 SIR Optimizer | SIR Optimizer | SIR Controller (Wave 8) | Absorbed into Controller `legacy/` |
| Day 9-10 11Players | 11Players | SIR Hagoozat (Wave 5) | Absorbed |
| Day 9-10 Obour Hub | Obour Academic Hub | SIR Education Hub (Wave 5, renamed 2026-11-12) | `legacy/` preserved |
| Day 9-10 Negm | Negm Furniture | SIR Negm Furniture (Wave 3, plans only) | Client handoff pack prepared |
| Day 9-10 GTA V mods | SIR Mods for GTA V | SIR Mods for GTA V (Wave 6) | `legacy/` preserved, HIGH LEGAL RISK |
| Day 13-14 Restaurant | SIR Restaurant | SIR Business (Wave 5) | Mode of shared core |
| Day 16-23 Market/Library/Pharmacy | SIR Market, SIR Library, SIR Pharmacy | SIR Business (Wave 5) | Modes of shared core |
| Day 24-28 Odysseus | SIR Odysseus | Removed (not Ahmed's project) | Source in SIR AI/legacy read-only; folder in old projects |
| Day 24-28 AHome | AHome | AHome (Wave 1, private) | Separate from all SIR products |
| Day 24-28 agent suite | antigravity-agent-suite | SIR Laptop Manager (Wave 2) | 97 skills in `legacy/`; licence audit pending |
| Day 24-28 Laptop manager | Laptop manager | SIR Laptop Manager (Wave 2) | Merged with agent suite |
| Day 24-28 download buttons | Download UI pattern | Shared across all products | In Platform `ui/styles/hooks` |

---

## Original "أفكار برامج ومشاريع" Note (30 ideas) → Mapped Modules

| Idea Numbers | Original Concept | Became Module In | Current Home |
|---|---|---|---|
| 1,2,3,4,5,9,10,11,13,17,18,22 | Prayer routine, adhkar, habits, meds, water, diet, gym, expenses, personal dev, skills | SIR Life (Part B) | `SIR Life` Wave 6, Part B not started |
| 6,7,8 | Web-to-app wrappers (Hagoozat, Obour, player cards) | Standard for every product: wrappers for web, Android and iOS (Capacitor/Expo) | Shared standards kit, M6+ |
| 24,25,27 | Study help, language learning, teaching platform | Education Hub modules (hints, practice) | SIR Education Hub Wave 5 |
| 12,19,20 | HR attendance, auto-reorder, B2B ordering | SIR Business shared core | SIR Business Wave 5 |
| 30 | Position coach | Hagoozat module | SIR Hagoozat Wave 5 |
| 15,16 | Price and game-deal finder | Concept (needs lawful data) | Backlog, not planned |
| 23,26,28,29 | Cars, accessibility map, handyman, movies | Concept backlog | Backlog, not planned |
| 14,21 | Citizens program, face rating | **DROPPED** | Government scope / biometric privacy risk |

---

## Where Each Original Idea Lives Now

| Original Project / Idea | Current SIR Product | Wave | Folder | Status |
|---|---|---|---|---|
| Obour Academic Hub | SIR Education Hub (renamed from SIR Obour Hub) | 5 | `D:\Projects\SIR Education Hub` | Planning |
| Hagoozat Elite + 11Players + EGFootball5 | SIR Hagoozat | 5 | `D:\Projects\SIR Hagoozat` | Planning |
| SIR Restaurant / Market / Pharmacy / Library | SIR Business | 5 | `D:\Projects\SIR Business` | Planning |
| Content Creation Studio v1 | SIR Content Creation Studio | 4 | `D:\Projects\SIR Content Creation Studio` | Planning |
| SIR Controller + SIR Optimizer | SIR Controller | 8 | `D:\Projects\SIR Controller` | Planning |
| SIR AI v1 + Tele Gateway + AgentsRoom | SIR AI | 4 | `D:\Projects\SIR AI` | Planning (Tier 1 first) |
| Laptop manager + agent suite | SIR Laptop Manager | 2 | `D:\Projects\SIR Laptop Manager` | Building (tests failing) |
| SIR ModPack | SIR ModPack | 6 | `D:\Projects\SIR ModPack` | Planning |
| SIR Mods for GTA V | SIR Mods for GTA V | 6 | `D:\Projects\SIR Mods for GTA V` | Planning (legal gate) |
| SIR Life (prayer/habits) | SIR Life Part B | 6 | `D:\Projects\SIR Life` | Part A building, Part B planning |
| SIR Negm Furniture | SIR Negm Furniture | 3 | `D:\Projects\SIR Negm Furniture` | Building (handoff only) |
| AHome | AHome | 1 | `D:\Projects\AHome` | Building (private) |
| SIR Study | SIR Study | 2 | `D:\Projects\SIR Study` | Building |
| SIR Jobs | SIR Jobs | 2 | `D:\Projects\SIR Jobs` | Building |
| SIR Platform | cancelled 2026-11-12 (shared standards, not a product) | - | `D:\Projects\old projects\SIR Platform` | Cancelled |
| SIR Portfolio | SIR Portfolio | 7 | `D:\Projects\SIR Portfolio` | Planning |

---

## Still Unplanned (from TickTick and Owner Ledger)

1. **Price/Game Deal Finder** (ideas 15,16) — needs lawful data sources, no API found
2. **Cars / Accessibility Map / Handyman / Movies** (ideas 23,26,28,29) — concept backlog only
3. **Download Buttons pattern** — extracted to the shared standards kit, not yet built
4. **Platform Wrappers** (ideas 6,7,8) — Capacitor/Expo decision at M6 of each product (every product ships on all platforms)
5. **SIR Controller macOS/Linux builds** — explicitly skipped for v1
6. **SIR Business macOS/Linux Electron builds** — skipped for v1 (no customers asked)
7. **SIR Life Wear OS / watchOS** — listed for M6+, not in v1
8. **SIR AI Tier 2 (multi-user cloud)** — gated behind Tier 1 verification at M6
9. **SIR Negm Furniture build work** — explicitly plans only until friend takes over
10. **AHome couple data in SIR Life** — explicitly forbidden (zero data either direction)
11. **LinkedIn growth pack** — first post, job alerts, connections (OWNER_REQUEST_LEDGER uncaptured #3)
12. **ChatGPT/Codex renewal date tracking** — needs Haiku to read and write to ACCOUNT_LEDGER (uncaptured #2)
13. **Windsurf / other free CLI evaluation** — not yet installed (uncaptured #9)
14. **Ordered PDF reports** — no half-empty pages (uncaptured #8)
15. **Two-host rule enforcement** — every web product on Firebase + Vercel with curl check (uncaptured #4)
16. **Portfolio truth checklist** — titles, numbers, NVIDIA MCP cert, no GPA (uncaptured #5)
17. **Reassign GLM/ZCode tasks** — Study r20, AHome help need new owners (uncaptured #6)
18. **TickTick refresh with browser operator** — payload ready in `_local/ticktick_refresh.json` (bus note)
19. **Stop unknown audio on laptop** — find process/tab, add guard in Laptop Manager (uncaptured #1)
20. **WhatsApp per-group list** — cohort, archive, work, job groups for digest (uncaptured #9)

---

## Merge Decisions Summary

- **24 sprint tasks** → folded into **10 SIR products** (some products absorbed multiple tasks)
- **30 program ideas** → **9 became modules** in existing products, **4 dropped**, **4 concept backlog**, **3 became Platform wrappers**
- **No new products created** from the merge; all mapped to the 16 portfolio products
- **SIR Platform** was planned as an extraction target (Wave 7); cancelled 2026-11-12. Its standards live in `SHARED_PLATFORM_KIT.md`.
- **SIR Portfolio** created as showcase (Wave 7), not a merge source
- **AHome** kept entirely separate (private, no SIR prefix)
- **SIR Negm Furniture** kept as client project (plans only)

---

## Verification

All mappings verified against:
- `ops/TICKTICK_MAP.md` lines 5-30 (sprint and ideas mapping)
- `ops/PORTFOLIO.md` lines 8-25 (16 products table)
- `ops/OWNER_REQUEST_LEDGER.md` uncaptured items (lines 122-131)
- `plans/WAVE_STUDY.md` lines 7-16 (wave order)
- `AGENTS.md` lines 47-50 (portfolio map)

No private data from "Accounts" note or "habobty" column was read or used.