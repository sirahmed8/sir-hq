# Report: r52 premium plan for SIR Hagoozat

Task: `r52-plan-sir-hagoozat`. Worker: opencode (MiniMax M3.1 Flash). Date: 2026-11-12. Repo: `D:/Projects/_SIR` (private `sirahmed8/sir-hq`), branch `main`.

Result: **ok.** The plan, the competitor matrix and the ten agent briefs are written and are on `main` on GitHub (verified by blob SHA through the GitHub API, not only by the local ref). Nothing was built in the product folder: this was a planning round.

---

## 1. What was read before writing (the brief's list, all read)

| File | Why |
|---|---|
| `D:/Projects/AGENTS.md` | laws (read twice: before and after the owner direction change) |
| `D:/Projects/_SIR/standard/23-premium-code-bar.md` | the quality floor |
| `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md` (in the global preamble) | worker rules |
| `D:/Projects/_SIR/standard/OWNER_DEFAULTS.md` | standing defaults, including item 19 (Desktop folder kit) and item 18 (port the owner's own ideas with a citation) |
| `D:/Projects/_SIR/ops/LESSONS.md` | 51 cross-project lessons plus the competitor-research rule at the end |
| `D:/Projects/_SIR/plans/MAIN_PLAN.md` | wave order and the GLOBAL product rules |
| `D:/Projects/_SIR/plans/PROJECT_MERGE_RECORD.md` | where the TickTick ideas ended up |
| `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md` | the 20-section kit the architecture is built on |
| `D:/Projects/_SIR/plans/AI_FALLBACK_CHAIN.md` | the AI chain |
| `D:/Projects/_SIR/plans/GEMINI_QUALITY_CHARTER.md` | the premium bar in nine points |
| `D:/Projects/_SIR/plans/WINDOWS_APP_STANDARD.md` | the desktop app standard |
| `D:/Projects/_SIR/plans/WAVE_STUDY.md` | Hagoozat is Wave 5 |
| `D:/Projects/_SIR/ops/SKILLS_INDEX.md` (393 lines) plus `ops/encyclopedia/` | to pick the skills and to confirm each digest file exists |
| `D:/Projects/_SIR/plans/PRODUCT_DIRECTION_2026-11-12.md` | the owner direction that landed mid-round (SIR Platform cancelled, Hagoozat takes the booking family) |
| `D:/Projects/SIR Hagoozat/.sir/*` | CHECKPOINT, ARCHITECTURE, DESIGN, PLATFORMS, QUALITY, BENCHMARK of the product |
| `D:/Projects/SIR Hagoozat/legacy/` (3,014 files) | the three old apps: `11Players`, `EGFootball5`, `Hagoozat Elite` (route lists read, sources read) |
| `D:/Projects/_SIR/ops/inventory/11Players.md`, `EGFootball5.md`, `Merged-sites.md` | the legacy facts and the red flags |
| `D:/Projects/_SIR/ops/TICKTICK_MAP.md`, `ops/OWNER_REQUEST_LEDGER.md`, `ops/PORTFOLIO.md` | the owner's own ideas |
| `D:/Projects/_SIR/plans/sir-cars.md`, `sir-handyman.md`, `sir-deals.md`, `sir-movies.md`, `accessibility-map-module-note.md` | the r51 per-idea decisions, so my booking-family table does not contradict them |

`D:/Projects/AHome` was never opened.

---

## 2. Research done today, with real sources

The built-in web search tool asked for permission and returned `Web search cancelled`, so I used direct page fetches and the DuckDuckGo HTML endpoint instead, as the worker preamble allows.

**Pages opened on 2026-11-12 (content read, not guessed):**

| Page | What it gave |
|---|---|
| `https://hareefa.com/` | "Book Football Courts & Manage Venues in Egypt", real-time availability, instant confirmation, one-tap rebooking of the weekly match, a "Join As a Court Owner" form, a venue phone app ("LISTEN YOUR COURT"), iOS and Android |
| `https://www.yallahagz-eg.com/` | live availability, instant confirmation, football, padel and padbol, the solo "Kickoff" mode, deposit online and the rest at the venue, cancel inside 10 minutes, tournaments, venue chat, player passport and badges, their claims of 50K+ players and 250+ venues, free on iOS and Android |
| `https://kourtiva.com/ar/football` | the strongest rival found: split payment per player at join time, open matches showing the missing places, QR entry per booking with a scan timestamp, staff roles, knockout and league tournaments, per-period pricing, eight languages, developer API docs, llms.txt, cookie preferences, account deletion, demo-driven B2B motion |
| `https://playtomic.com/pricing` | four manager tiers (Standard, Professional, Champion, Master) with their feature lists, their claim of 6,700+ clubs, POS, wallet, API, support response times; the public prices were not readable on the page |
| `https://www.matchi.se/` | their claims of 1,708 active venues and 18,710 bookable courts, seven racket sports, level-based player matching, fourteen languages |
| `https://spond.com/` | their claim of over 12 million people, the team and club feature set (availability requests, collecting payments, fundraising, guardians, club website) |
| `https://pitchbooking.com/product` | facility listing with online booking and payment, operator-first positioning |
| `https://riadiapp.com/` | title only (client-rendered shell): "Egypt's sports booking platform", football, padel, ping pong, billiards, PlayStation centres, esports |
| DuckDuckGo HTML, Egyptian query | six more real rivals with their own snippets: Matchiva (matchiva.online), Riadi (riadiapp.com), Kickoff (kickoffapps.com), Matcho (matcho.app), Mal3b (mala3b.co), Mal3bk (mal3bk.com), Courty (courty.io/football), Hagz Kora (hagzkora.app) |

Every claim in the matrix carries a link and a date, or the tag `(unsourced, verify)`. Numbers that belong to a competitor are written as their claim. Nothing was tested as a user.

**Market findings that shaped the plan (the honest part):** the Egyptian player app is expected to be free (Yalla Hagz says free on iOS and Android), the money is on the venue side, the deposit pattern is established, the squad and payment problem is already solved by Kourtiva, Arabic is badly served (Kourtiva is formal MSA, the two consumer apps write English), and no Egyptian competitor claims offline. So the plan does not try to out-feature Yalla Hagz or Kourtiva; it wins on Egyptian Arabic, the split bill, the open match, offline and the owner numbers.

**Facts verified in the product repo, not assumed:**
```
$ gh repo view sirahmed8/sir-hagoozat --json name,visibility,defaultBranchRef,isPrivate,updatedAt
{"defaultBranchRef":{"name":"main"},"isPrivate":true,"name":"sir-hagoozat","updatedAt":"2026-11-09T18:28:22Z","visibility":"PRIVATE"}
```
The product folder has no `.firebaserc`, so the product's own Firebase project does not exist yet. `firebase` was not on the PATH in this round (`timeout: failed to run command 'firebase': No such file or directory`), so the project id is still unverified and is written as unverified in the plan. The Desktop kit for Hagoozat exists today (`folder.ico`, `Versions.txt` at 1.0.0, the shortcuts) but it was built for the legacy app, so M0 rebuilds it, as OWNER_DEFAULTS item 19 says.

---

## 3. Files written

| Path | Lines | What it is |
|---|---|---|
| `D:/Projects/_SIR/plans/sir-hagoozat.md` | 490 | the premium plan, rewritten from the r44 text, with the nine required sections: promise, competitors, features, platform matrix, shared-kit architecture, quality bar, EGP and USD pricing, M0 to M6 with acceptance tests, the first ten tasks, plus the skills list, the risks and the owner-only actions |
| `D:/Projects/_SIR/ops/competitors/sir-hagoozat.md` | 92 | the ten competitors with sources and dates, a second ring of six, the seven market findings, our five promises, and five sourcing tasks still open |
| `D:/Projects/_SIR/ops/briefs/sir-hagoozat-tasks.md` | 55 | the first ten queue-ready tasks (title plus one-paragraph brief each, the shared preamble, the done-when for all ten, the queue order, the dependencies and the file-ownership split so two agents never fight over one file) |
| `D:/Projects/_SIR/ops/bus/sir-hq.md` | one line | the bus note |

Sections the brief asked for and where they live: 1 in section 1 (who it is for, two one-sentence promises and the end state we sell), 2 in section 2 with the matrix in `ops/competitors/sir-hagoozat.md`, 3 in sections 3.1 to 3.4 (parity list, the owner's own legacy and TickTick ideas with the source of each one, the booking-family decision, out of scope), 4 in section 4 (web, Windows, macOS, Linux, Android, iOS, Wear OS, watchOS, TV, car, plus widgets), 5 in section 5 (shape, `owner-auth`, the owner-only analytics page, the AI table with the fallback chain, data and money, hosting on Firebase plus Vercel, security baseline), 6 in section 6 (Apple-level motion, Arabic and English, five states, accessibility, evidence), 7 in section 7 (five plans in EGP and USD with six fairness rules), 8 in section 8 (M0 to M6, every exit check is a command or a click), 9 in section 9 pointing at the briefs file. Section 10 lists the 28 skills picked from the library, each with the digest path I confirmed on disk.

---

## 4. Decisions I took, and why

1. **The ten competitors are mostly Egyptian, not global.** The brief says best-in-class apps; a European benchmark would hide the real market. Six Egyptian rivals plus four global ones (Playtomic, MATCHi, Spond, Pitchbooking) plus a second ring of six Egyptian names found today.
2. **Pricing is an outline with test prices, never published prices.** The player Pro 59 EGP and the venue 450 EGP are the owner's own numbers from the legacy pricing copy and the previous Hagoozat plan, so they are kept and labelled as test prices. The USD column uses 48 EGP per 1 USD and is tagged `(unsourced, verify)`. The rule that a venue pays one thing only (plan instead of commission) is written into the product, not just the plan.
3. **Playtomic is a depth benchmark, not a price benchmark.** Its prices were not readable on the page, so no number was invented.
4. **The plan replaces the old plan, it does not sit next to it.** The r44 text was overwritten; what was still true (names, the repo, the entity list, the legacy facts, the security rules, the shared-kit reuse, the dual hosting) was carried into the new structure. The old `plans/competitors/sir-hagoozat.md` is left untouched and is marked in the new file as superseded, so no one quotes the unsourced r44 table as current.
5. **The architecture follows the kit, not the legacy stack.** The legacy apps were Next 14 plus Cloudflare D1 plus Supabase in one note and Firebase in another; the plan fixes Next.js 15+ App Router, Firestore, Firebase Hosting plus Vercel, and it names the legacy defect that static export killed the API routes (`/api/ai/chat`, `/api/ai/tts`, `/api/admin/role` returned 404 in production).
6. **The M0 exit check recreates the Desktop folder kit**, because the current one belongs to the legacy build.
7. **The AI never decides a team.** The balancer is a pure function with a property test; AI only writes the sentence. That is stated in the architecture table, in the quality bar and in task T9.
8. **Booking-family decision (owner direction section 4 and 5), done in this round.** Twelve ideas are modules of SIR Hagoozat, each with a one-line reason (referee and professional player booking, position coach booking, padel and padbol courts, indoor and futsal slots, 7 and 11-a-side fields, equipment rental, photographer or recorder, venue add-ons, tournament organisation, multi-day bookings). Five ideas stay outside, matching the r51 decisions (Handyman, Cars, Deals, Movies are own products; the accessibility map is a module of SIR Life Part B). The rule for any new idea: one line here before any code.

---

## 5. The two rule changes that landed mid-round, and how I handled them

- **`D:/Projects/AGENTS.md` changed while I was working** (the harness told me): SIR Platform is cancelled as a project, SIR Obour Hub is now SIR Education Hub, the shared kit is a standards kit and not a product, and every product ships on web, Windows, macOS, Linux, Android and iOS. I read the new direction file `plans/PRODUCT_DIRECTION_2026-11-12.md` and updated my plan: section 5 now says the kit is the standard with no extraction target, section 4 marks the six platforms as required, and section 3.4 answers the booking-family question the direction file asked. Another agent had already inserted a "Vision" block and an empty "Previous plan (merge in the next round)" heading into my file; I kept the Vision text, replaced the empty heading with a proper note, and did the merge the heading was asking for (the old plan is gone, superseded, with the git history keeping it).
- **A concurrent agent swept my staged files into their commit.** I staged my four paths, and another agent's `git commit` picked them up, so my first three files landed under the message "r52: bus note for SIR AI plan completion". The content was correct but the message was not mine, so I committed the final version separately with the message "docs(r52): SIR Hagoozat plan merges owner booking-family decision and 2026-11-12 product direction". The local branch had also diverged from origin (4 local commits, 2 remote, plus more arriving every minute), and `git pull --rebase` would have conflicted on `ops/encyclopedia/deep/*` files that two other agents rewrote differently, so I pushed my final content from a temporary worktree instead of rebasing the shared branch. The worktree was removed afterwards (`git worktree list` shows only the three pre-existing worktrees).

**Confirmed on the remote, not just locally:**
```
$ gh api repos/sirahmed8/sir-hq/contents/plans/sir-hagoozat.md?ref=main --jq .sha
6526f5dcbcb668adeb19c32ef82188b9bd20fbe1     (local git hash-object: identical)
$ gh api repos/sirahmed8/sir-hq/contents/ops/competitors/sir-hagoozat.md?ref=main --jq .sha
60f12d384f9b8075f7597833b8882ce6660640fb     (local: identical)
$ gh api repos/sirahmed8/sir-hq/contents/ops/briefs/sir-hagoozat-tasks.md?ref=main --jq .sha
4eb56d82d0d06e54bd3184926da8ffbbba917403     (local: identical)
$ gh api repos/sirahmed8/sir-hq/commits/e3cf4f2 --jq '.sha[0:7] + " | " + .commit.message'
e3cf4f2 | docs(r52): SIR Hagoozat plan merges owner booking-family decision and 2026-11-12 product direction
```

---

## 6. Verification run today

```
$ python -m pytest tests -q
..............................................................           [100%]
62 passed in 21.52s
```
```
$ gh run list --limit 3
completed	success	chore: add deep digests for skills encyclopedia (396 files across all…	verify	main	push	43252998997	14s	2026-11-12T15:55:18Z
completed	success	chore: add deep digests for skills encyclopedia (396 files across all…	test	main	push	43252998875	11s	2026-11-12T15:55:18Z
completed	success	control room fix1-fix1: final report with the commit list and CI evid…	test	main	push	43252927075	8s	2026-11-12T15:54:55Z

$ gh run view 43252998997 --json conclusion,jobs
{"conclusion":"success","jobs":[{"conclusion":"success","name":"secrets","steps":5},{"conclusion":"success","name":"python-verify","steps":8}]}
```
The head commit that contains my files ran CI with real steps (the `python-verify` job has 8 steps, all successful, and the `secrets` job 5). The `ops/ci-quota-exhausted.flag` file still exists from 17:42, but the runs are green with steps, so the flag appears stale today.

---

## 7. What is unsure, and what I recommend next

**Unsure or unverified:**
1. The product's Firebase project does not exist and its id is unknown. Task T3 creates it; it must be named `sir-hagoozat` and must not reuse another product's project.
2. Every competitor number is the competitor's own claim. No competitor was used as a user, and no price of theirs was readable, so none is quoted.
3. The EGP to USD rate (48) is a placeholder with an explicit `(unsourced, verify)` tag; the pricing page must compute it live.
4. The Paymob and Fawry fee schedules are still unread, so the venue transaction fee is not published anywhere.
5. `plans/competitors/sir-hagoozat.md` (the r44 file) is now stale next to `ops/competitors/sir-hagoozat.md`. The new file says so in its header, but the old one still exists with unsourced claims in it.
6. The path convention changed in this round: the shared kit still says the matrix lives in `plans/competitors/<slug>.md`, while this round's brief says `ops/competitors/<slug>.md`. Sibling rounds (SIR AI, SIR Business, SIR Obour Hub, SIR Content Creation Studio) followed the new path, so the kit file needs one line updated to avoid two files per product.
7. `plans/MAIN_PLAN.md`, `plans/WAVE_STUDY.md` and `plans/SHARED_PLATFORM_KIT.md` still mention SIR Platform as a product and SIR Obour Hub as a product. That is outside my allowed paths for this round, so I left them alone.

**Recommended next:**
1. Queue `ops/briefs/sir-hagoozat-tasks.md` as ten rounds. T1 to T4 can run side by side, because each one owns a different area of the repository; the brief names the area for each.
2. Before any marketing, the five sourcing tasks at the end of the competitor file, especially the Paymob and Fawry fee schedules, because the venue price is the one number a real owner will check first.
3. HQ: one line in `plans/SHARED_PLATFORM_KIT.md` section 16 pointing the matrix at `ops/competitors/<slug>.md`, and one line removing SIR Platform from the consumers table, plus the old `plans/competitors/sir-hagoozat.md` marked as superseded or deleted as a duplicate of the new file.
4. The owner decides the wave: the plan assumes Hagoozat stays in Wave 5, but with the booking family attached, the market case is stronger than the r44 note assumed and it could move earlier.
5. The product folder's checkpoint is stale (written 2026-10-30, "nothing is built yet", next step T-003). The first worker in the product folder should rewrite it with the r52 plan as the source of truth, the ten tasks and the exact next command.
