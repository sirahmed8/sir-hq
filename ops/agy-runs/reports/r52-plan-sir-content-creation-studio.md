# Report: r52-plan-sir-content-creation-studio

## Task
Rewrite `plans/sir-content-creation-studio.md` as a premium complete plan, create `ops/competitors/sir-content-creation-studio.md` (10 competitors), create `ops/briefs/sir-content-creation-studio-tasks.md` (first 10 queue-ready tasks), commit explicit paths, push, one bus line.

## What I did

1. **Read required context**: `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/OWNER_DEFAULTS.md`, `ops/LESSONS.md`, `plans/MAIN_PLAN.md`, `plans/PROJECT_MERGE_RECORD.md`, `plans/SHARED_PLATFORM_KIT.md`, `ops/SKILLS_INDEX.md`, product folder `D:/Projects/SIR Content Creation Studio` (`AGENTS.md`, `.sir/PLAN.md`, `.sir/MASTER_PLAN.md`, `.sir/DESIGN.md`, `.sir/PLATFORMS.md`, `.sir/CHECKPOINT.md`, `legacy/README.md`), `ops/inventory/SIR-Content-Creation-Studio.md`, existing `plans/sir-content-creation-studio.md`, `plans/sir-content-creation-studio-DEEP.md`, `ops/bus/sir-hq.md`. Checked legacy folder (README + v1 folder present). Did not open AHome.

2. **Key findings**
   - Product is a merge project: `legacy/SIR Content Creation Studio (v1)` (Electron + FastAPI on 127.0.0.1:5000 + Remotion; 120 test files; Python 3.10/3.11/3.13 mismatch; personal state tracked in git; no server-side token check; unsigned installer; CI failing; no social publishing code despite the ByteVibeHQ idea).
   - `.sir/CHECKPOINT.md`: kit complete (2026-10-30), nothing built, repo `sirahmed8/sir-content-creation-studio` exists.
   - Existing plan (r44-era) was 87 lines plus a 235-line DEEP plan; thin on sourced competitors (only CapCut and Canva rows, "to be sourced").
   - Stack decision recorded in the plan: earlier drafts said Cloudflare Pages only; standing owner rules (OWNER_DEFAULTS item 2, WORKER_PREAMBLE item 15, rule 13) require Firebase Hosting + Vercel dual hosting and an own Firebase project `sir-content-studio`. Plan now specifies desktop shell (Tauri v2 or Electron) + Vite + React, local engine Python 3.12 FastAPI, Remotion, web dashboard on Next.js, Firebase Hosting + Vercel. Cloudflare remains an ADR alternative for the render queue.
   - Platform decision: Windows desktop in v1; macOS/Linux at M6+ on request; Android/iOS PWA at M5-M6; Wear OS/watchOS/TV/car skipped with reasons; widgets at M6.
   - Pricing kept and anchored to sourced competitor prices: Pro 290 EGP/month or 2,900 EGP/year (test price, "(unsourced, verify)" until 10 creator interviews); free tier with no watermark on free export; CapCut Pro 599.99 EGP/month and Ultra 3949.99 EGP/month (capcut.com/pricing, checked 2026-11-12); Opus Clip Pro $29/month, Starter $15/month (opus.pro/pricing, checked 2026-11-12).

3. **Web research for competitor sources** (web_search cancelled in this environment; used webfetch on official pricing pages):
   - Opus Clip pricing page fetched (opus.pro/pricing): Free $0, Starter $15/mo, Pro $29/mo, Business custom; feature gates read from the page.
   - CapCut pricing page fetched (capcut.com/pricing): Free 0 EGP, Pro 599.99 EGP/month, Ultra 3949.99 EGP/month, Teams 300 EGP/month per seat.
   - Remaining competitors (Canva, InVideo, Descript, Buffer, Hootsuite, Repurpose.io, Vidyo.ai, Riverside) documented with strengths/flaws/our edge and pricing marked "(unsourced, verify)" with sourcing tasks listed.

4. **Files written**
   - `D:/Projects/_SIR/plans/sir-content-creation-studio.md` - full rewrite, 11 sections covering all 9 brief requirements plus risks and owner-only actions.
   - `D:/Projects/_SIR/ops/competitors/sir-content-creation-studio.md` - NEW; 10 competitors with strengths/flaws/our edge, sourced facts separated from flagged claims, 6 open sourcing tasks.
   - `D:/Projects/_SIR/ops/briefs/sir-content-creation-studio-tasks.md` - 10 queue-ready tasks T1-T10 (deep scan, secrets report, Python pin + engine skeleton, Remotion caption clip, Arabic caption shaping test, license table + exporter check, credential store, draft approval flow, posting cap + audit log, dry-run publisher).

5. **Git**
   - `git add plans/sir-content-creation-studio.md ops/competitors/sir-content-creation-studio.md ops/briefs/sir-content-creation-studio-tasks.md` -> commit `b4583f9` "r52: premium plan rewrite for SIR Content Creation Studio + sourced competitor matrix + 10 queued tasks" -> pushed to `main` (`f555d83..b4583f9`).
   - Appended bus line to `ops/bus/sir-hq.md` -> commit `0feffe5` -> pushed (`b4583f9..0feffe5`).
   - CI: `ops/ci-quota-exhausted.flag` applies (markdown-only change, no code to verify; Actions minutes exhausted). No `gh run` check needed for markdown-only commits; local verification not applicable beyond file existence and content review.

## Unsure / open
- Exact current Egypt checkout prices for Canva/Descript/Buffer/Hootsuite/Repurpose.io/Vidyo.ai/Riverside/InVideo marked "(unsourced, verify)"; sourcing tasks listed in the competitor file.
- Remotion commercial licence terms not yet checked; flagged as owner action at M0.
- Whether Vercel project for `sir-content-creation-studio` already exists was not checked (product repo exists; hosting setup is M0 work).
- Pro price points are explicitly test prices pending creator interviews.

## Recommended next
- Queue `ops/briefs/sir-content-creation-studio-tasks.md` T1-T10 to free agents; T1 (deep scan) unblocks everything else; T2 (secrets report) and T3 (Python pin) can run in parallel.
- Owner actions already listed in plan section 11 (domain, Firebase project sign-in, Paymob, key rotation, lawyer review, platform developer consoles, Apple Developer account).