# Report: r54-plan-sir-handyman (2026-11-12)

Round r54 (HQ, 2026-11-12), worker continuation. Output only under `D:/Projects/_SIR` (plans and ops folders). No project folder, no repo, no Firebase project, no code was created, as the brief requires. AHome was never opened.

## What was done

1. Read the required files: `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/OWNER_DEFAULTS.md`, `standard/23-premium-code-bar.md`, `plans/PRODUCT_DIRECTION_2026-11-12.md` (sections 5, 6 and 8), `plans/BACKLOG_IDEAS_DECISIONS.md`, `ops/TICKTICK_MAP.md`, `plans/SHARED_PLATFORM_KIT.md`, `ops/SKILLS_INDEX.md`, `ops/briefs/r52-product-premium-plan.md`, `plans/sir-hagoozat.md` sections 3.4 and 3.5, and the old `plans/sir-handyman.md` (r51 first draft, superseded).
2. Rescan done: the only existing notes are the r51 first draft, the TICKTICK_MAP row (idea 28), the BACKLOG_IDEAS_DECISIONS row (3.5), the Hagoozat decision 3.4 and the PRODUCT_DIRECTION sections 5/6/8. All facts from them are carried into the new plan or explicitly marked superseded.
3. Web research (2026-11-12, DuckDuckGo HTML and direct page fetches): the ten competitors are FilKhedma, Khidhma, Mahlola, Mu'een, YalaFix, Taskty, Fixawy, SAADK (Egypt), ServiceMarket (UAE) and Urban Company (India, UAE/KSA via noon). Global second ring: TaskRabbit, Thumbtack, Angi, Handy, Mr. Handyman, Airtasker, Noon home services, Seyanti, Handyman.com.eg, Homeserviceapp. The r51 note's "Taskday / Khidmeh / Handyman.com.eg" are stale: Taskday is now a to-do app (taskday.app), Khidmeh's live product is khidhma.com, and handyman.com.eg could not be fetched. Every claim not read on an opened page is tagged "(unsourced, verify)".
4. Wrote `ops/competitors/sir-handyman.md`: ten competitors with strengths, flaws and our edge, plus a second ring, a "what the Egyptian market actually looks like" section, five promises and ten open sourcing tasks each under one hour.
5. Rewrote `plans/sir-handyman.md` as a premium GLOBAL product plan: vision, who it is for and the promise ("Describe the job with photos, agree the price, and watch the worker come to you"), the ten-competitor summary table, section 3 features (parity list with sources, the owner's own ideas with sources incl. the Hagoozat booking-family absorption, explicitly out-of-scope list, lawful data), section 4 platform matrix (web, PWA, Windows, macOS, Linux, Android, iOS; Wear OS, watchOS, TV, car skipped with written reasons; widgets M5), section 5 architecture on the shared kit (shape, owner-auth, full data model `packages/core` with 15 entities, owner-only analytics page at `/owner`, AI with the fallback chain and an advisory-only table, data and money with the escrow transaction and the 20-parallel-accepts test, hosting Firebase + Vercel, security baseline), section 6 premium quality bar, section 7 free tier and fair EGP/USD pricing (Customer Free 0, Worker Free 12% per completed job test rate, Worker Pro 249 EGP/month or 2,490/year test rate, homeowners never pay, escrow and fee rules, USD at 48 EGP per 1 USD tagged "(unsourced, verify)"), section 8 milestones M0 to M6 with acceptance tests (M0 creates the project folder D:\Projects\SIR Handyman with .sir/, AGENTS.md, folder.ico in the project root, and the Desktop folder kit per OWNER_DEFAULTS item 19, plus the Firebase project sir-handyman and the private repo sirahmed8/sir-handyman; M0 is NOT executed in this round), section 9 first ten tasks pointer, section 10 skills from the library, section 11 risks and defaults, section 12 owner-only actions, section 13 sources.
6. Wrote `ops/briefs/sir-handyman-tasks.md`: the first ten build tasks, title plus one-paragraph brief each, from monorepo scaffold through the owner-only analytics page and the dispute queue.
7. Committed and pushed explicit paths only: commit `2c2b2ae` to `main` (`plans/sir-handyman.md`, `ops/competitors/sir-handyman.md`, `ops/briefs/sir-handyman-tasks.md`, `ops/bus/sir-hq.md`). One line added to `ops/bus/sir-hq.md` (newest first). The uncommitted files in the tree (dashboards, AUTOPILOT_QUEUE.json, plans/sir-hagoozat.md) belong to other workers and were not touched, not staged and not committed.

## Commands run (real output)

- `git status` / `git log --oneline -5` / `git diff --stat` at round start: 8 modified files (not mine), 40 untracked reports from other rounds; no handyman files existed.
- `webfetch` DuckDuckGo HTML searches and direct fetches: filkhedma.com, khidhma.com, mahlola.com/en, mueen-app.com, yalafix.com, servicemarket.com all opened 2026-11-12; play.google.com Taskty and App Store SAADK listings found via search snippets only ("(unsourced, verify)").
- `git add plans/sir-handyman.md ops/competitors/sir-handyman.md ops/briefs/sir-handyman-tasks.md ops/bus/sir-hq.md`
- `git commit -m "r54: SIR Handyman premium plan (small independent GLOBAL product)"` -> `[main 2c2b2ae]`
- `git push origin main` -> `bda2855..2c2b2ae  main -> main`

## What is still open (honest)

- No project folder, Firebase project, GitHub repo, Desktop kit or code exists. They are M0 of the plan and are NOT created in this round by design of the brief.
- All competitor numbers are their own claims, tagged "(unsourced, verify)" where the page was not opened. Ten under-one-hour sourcing tasks are listed in the competitor file section 4.
- The USD column uses 48 EGP per 1 USD, "(unsourced, verify)"; the fee rate (12%), Worker Pro price (249/m) and the 72h auto-release are proposals pending the owner and the lawyer and the official Paymob/Fawry fee schedules.
- The eKYC provider for Egypt is not chosen; `docs/EKYC.md` is an M0 deliverable.
- The old r51 note claimed "planning only, build starts when Ahmed decides the wave order"; the owner's 2026-11-12 decision (PRODUCT_DIRECTION section 8) turns this into its own project, so that line is superseded and marked as such in the plan.
- CI on main: GitHub Actions minutes quota was exhausted earlier on 2026-11-12; local verification (markdown read-through, 480-line plan renders) was used. See `ops/ci-quota-exhausted.flag` and WORKER_PREAMBLE rule 18. This round changed only markdown files, nothing in CI scope.

## What I recommend next

1. HQ approves the plan and queues M0 as its own round (create folder, .sir/, AGENTS.md, repo sirahmed8/sir-handyman, Firebase project sir-handyman on Spark, Desktop kit).
2. The owner or HQ picks the eKYC provider and the launch district (plan proposes one Cairo district, 5 real workers, 5 real completed jobs).
3. Run the competitor file section 4 sourcing tasks before any public copy or store listing is written.
