# TickTick to portfolio map (Phase 3.2, 2026-10-29)
Read: 9 projects (Daily/Weekly/Monthly routine untouched, My life, Yearly goals, My 2026 Goals, My notes, 30-Day Projects Sprint, Inbox). Backup before any change: `D:\Projects\Backups\TickTick-2026-10-29\sprint-ideas-goals-backup.json` (outside git on purpose: several personal notes hold passwords and family details and are NOT copied anywhere; HQ never edits them).

## 30-Day Projects Sprint (24 open tasks, Oct 28 to Nov 26): already a security remediation plan that matches the scout findings
| Sprint day | Project | Matches inventory finding |
|---|---|---|
| Rotate secrets, Day 1 (overdue) | Laptop manager, Tele Gateway, GTA V, ModPack | Telegram token in 5 tracked files (Laptop manager); owner actions already listed |
| Day 2 shared kit (owner claim, nonce CSP, billing.ts) | platform | Phase 4 the shared kit: the same 5 flaws repeat in every project |
| Day 3 Hagoozat/merged-sites | Merged sites | webhook `dev_signature` fallback (critical) |
| Day 4 SIR Controller | SIR Controller | unsigned webhook returns success |
| Day 5 SIR CCS | Content Creation Studio | no token check, personal state tracked |
| Day 6 SIR AI | SIR AI | owner telemetry trusts client |
| Day 7 EGFootball5 | EGFootball5 | API routes 404 on static host |
| Day 8 SIR Optimizer | SIR Optimizer | self-grant OP mode, keys in bundle |
| Day 9-12 | 11Players, Education Hub, Negm, GTA V mods | owner checks, rules, fake data |
| Day 13-14 Restaurant; 16-23 Market/Library/Pharmacy | SIR Business | shared core: fix once (see consolidation) |
| Day 24-28 | Odysseus, AHome, agent suite, Laptop manager, download buttons | |
Decision: keep the sprint but re-order by blast radius and by what is live: (1) anything with a webhook or admin gate reachable from the internet (Merged sites, SIR Controller, SIR Optimizer, SIR AI), (2) shared kit before the per-project days so each project imports it instead of re-fixing, (3) the four SIR Business apps as one shared-core job.

## 30 program ideas (note "أفكار برامج ومشاريع") mapped to modules, not 30 new products
| Idea numbers | Becomes | Home |
|---|---|---|
| 1, 2, 3, 4, 5, 9, 10, 11, 13, 17, 18, 22 | **SIR Life**: prayer-aware daily routine, adhkar and Quran wird, habits, medication and water reminders, diet and calories, gym log, expenses, personal development, skill plans | one new product (Phase 6), local-first, Arabic first |
| 6, 7, 8 | web to app wrappers (Hagoozat Elite, Education Hub, player cards) | platform wrappers (Capacitor or Expo), Phase 10 |
| 24, 25, 27 | study help, language learning, teaching platform | modules of Obour Academic Hub (hints and practice, never graded work) |
| 12, 19, 20 | HR attendance, auto-reorder, B2B ordering | modules of the SIR Business shared core |
| 30 | position coach | module of Hagoozat Elite |
| 15, 16 | price and game-deal finder | concept (needs lawful data sources) |
| 23, 26, 28, 29 | cars, accessibility map, handyman requests, movie list | concept backlog |
| 14, 21 | citizens program, face rating | dropped: government scope; face scoring is a biometric privacy risk with little value |

## Other items
- My 2026 Goals / Yearly goals / 4-year plan: first income via payment gateways on Education Hub, EGFootball5, 11Players, restaurant and shop systems. Matches Phase 8 and the Coming Soon fallback rule (no gateway keys yet).
- "مشاريعي والأنظمة" note lists 12 projects incl. **x360ce App**, which has no folder in `D:\Projects`: not in the inventory; check whether it lives inside SIR Controller.
- Inbox: subscriptions to compare (Adobe, CapCut/Canva, ChatGPT Plus, YouTube Premium), doctor visits, line ownership, SSD upgrade deferred until income. Personal, not touched. Free tools cover the creative stack, so no subscription is bought (no budget).
- **Security note for Ahmed:** two personal notes (named "Accounts" and the university email note) store account passwords in plain text. Please move them to a password manager and change those passwords. Listed in OWNER_ACTIONS.
