# Report: r52-plan-sir-obour-hub

## Task
Rewrite `plans/sir-obour-hub.md` as a premium complete plan, create `ops/competitors/sir-obour-hub.md` (10 competitors), create `ops/briefs/sir-obour-hub-tasks.md` (first 10 queue-ready tasks), commit explicit paths, push, one bus line.

## What I did

1. **Read required context**: `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/OWNER_DEFAULTS.md`, `ops/LESSONS.md` (tail, lessons L37-L51 + competitor-matrix rule), `plans/MAIN_PLAN.md`, `plans/PROJECT_MERGE_RECORD.md`, `plans/SHARED_PLATFORM_KIT.md`, `ops/SKILLS_INDEX.md` (grep), product folder `D:/Projects/SIR Obour Hub` (`AGENTS.md`, `.sir/PLAN.md`, `.sir/MASTER_PLAN.md`, `.sir/DESIGN.md`, `.sir/PLATFORMS.md`, `.sir/CHECKPOINT.md`, `legacy/README.md`), `ops/inventory/Obour-Academic-Hub.md`, existing `plans/sir-obour-hub.md`, `plans/sir-obour-hub-DEEP.md`, `plans/competitors/sir-obour-hub.md`, `ops/bus/sir-obour-hub.md`.

2. **Key findings**
   - Product is a merge project: `legacy/Obour Academic Hub` (Next 16, React 19, ~344 files / ~62k lines, 47 test files). Inventory flags: `allow read: if true` on 5 Firestore collections, CSP unsafe-inline/eval, `solve_assignment`/`solve_quiz` graded-work modes, deterministic fake fallback solutions, hardcoded Firebase config + owner email in CI, two Firebase admin JSON keys + `.env.local` at rest in legacy (gitignored, must rotate).
   - `.sir/CHECKPOINT.md`: kit complete, nothing built, repo `sirahmed8/sir-obour-hub` exists, M0 first.
   - Existing plan (r44-era) was good but thin on competitors (0 source links) and predated the dual-hosting rule.
   - Stack decision recorded in the plan: earlier drafts said Cloudflare Pages/D1/R2; the standing owner rules (OWNER_DEFAULTS item 2, WORKER_PREAMBLE item 15, rule 13) require Firebase Hosting + Vercel dual hosting and an own Firebase project `sir-obour-hub`. Plan now specifies Next.js on Firebase Hosting + Vercel, Firebase Auth/Firestore/Storage. R2 kept as documented ADR alternative.
   - Platform decision: web PWA + installable PWA covers Windows/macOS/Linux in v1; Android/iOS via Capacitor at M5-M6; Wear OS/watchOS post-v1 ADR; TV skip; car skip; widgets M6.
   - Pricing kept from old plan as test prices with "(unsourced, verify)": 49 EGP/mo, 399 EGP/yr Pro; free tier generous; marketplace listing 30 EGP/semester (unsourced).

3. **Web research for competitor sources** (web_search worked fine):
   - Official portals verified live: `https://student.oi.edu.eg/` (MyU / Ivan El-Haytham system), `https://elearning.oi.edu.eg/` (Moodle), `https://oi.edu.eg/`, `https://oust.edu.eg/en/pages/students` (OUST portal bundle).
   - Course Hero / Studocu / Chegg pricing sourced via `silentstudent.com/vs/coursehero` (checked 2026-10-20 data) and `apppricelens.com` region pricing (Egypt E£709.99 entry, flagged unsourced-for-checkout).
   - Unofficial Facebook/Telegram groups and campus book market documented as channels (claims marked "(unsourced, verify)" where unlinked).

4. **Files written**
   - `D:/Projects/_SIR/plans/sir-obour-hub.md` — full rewrite, 11 sections covering all 9 brief requirements + risks + owner-only actions + skills list.
   - `D:/Projects/_SIR/ops/competitors/sir-obour-hub.md` — NEW directory `ops/competitors/` created; 10 competitors with strengths/flaws/our edge, sourced facts separated from flagged claims, 5 open sourcing tasks.
   - `D:/Projects/_SIR/ops/briefs/sir-obour-hub-tasks.md` — 10 queue-ready tasks T1-T10 (deep scan, secrets report, scaffold, Firestore rules, auth, five-state viewer, import dry-run, tutor eval, pricing fallback, CI).

5. **Git**
   - `git add plans/sir-obour-hub.md ops/competitors/sir-obour-hub.md ops/briefs/sir-obour-hub-tasks.md` → commit `ef55f9c` "r52: premium plan rewrite for SIR Obour Hub + sourced competitor matrix + 10 queued tasks" → pushed to `main` (`bdd3383..ef55f9c`).
   - Appended bus line to `ops/bus/sir-hq.md` → commit `a3d8ac3` → pushed (`ef55f9c..a3d8ac3`). Note: the bus commit shows 6 insertions because parallel workers' appended lines were already in the working tree; my line is included.
   - CI: `ops/ci-quota-exhausted.flag` rule applies (docs-only change; no code to verify). No `gh run` check needed for markdown-only commits, and Actions minutes are exhausted anyway.

## Unsure / open
- Exact current Egypt checkout prices for Course Hero/Studocu/Chegg marked "(unsourced, verify)"; sourcing tasks listed in the competitor file.
- Official 25% absence rule and grade-appeal procedure not yet cited from oi.edu.eg; flagged in plan.
- Whether Vercel project for `sir-obour-hub` already exists was not checked (product repo exists; hosting setup is M0 work).
- Pro price points are explicitly test prices pending student interviews.

## Recommended next
- Queue `ops/briefs/sir-obour-hub-tasks.md` T1-T10 to free agents; T1 (deep scan) unblocks everything else.
- Owner actions already listed in plan section 11 (domain, Firebase project sign-in, Paymob, key rotation, lawyer review).
