# PLAN REFRESH LOG: SIR Life

Rule 20 rescan, round r61, 2026-11-12. Planning only - no code, nothing written inside `D:/Projects/SIR Life`, no repos created (owner order: free tools must NOT start building these projects).

## What was re-read

- `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `ops/bus/team.md` (last 40 lines)
- `plans/PRODUCT_DIRECTION_2026-11-12.md` (SIR Life is in the final product list, line 22)
- `plans/sir-life.md` and `plans/sir-life-DEEP.md` (full)
- `ops/briefs/sir-life-tasks.md` (found half-finished by the previous worker: tasks expanded but plan, competitor file, this log and the report untouched, and T38-T42 contained copy-paste errors from other products - escrow jobs, lawyer review, 301 redirects)
- `ops/competitors/sir-life.md` (r52 version, 10 competitors + second ring)
- `D:/Projects/SIR Life` read-only state as recorded in `plans/sir-life.md` truth rule (65/65 tests green on 2026-11-12, uncommitted `.sir` doc reversions belong to task T1)
- `ops/TICKTICK_MAP.md` row 23 (SIR Life owns TickTick ideas 1-5, 9-11, 13, 17, 18, 22)
- `ops/SKILLS_INDEX.md` for per-task skill names

## Research added (second pass, 2026-11-12 evening)

Written into `ops/competitors/sir-life.md` section 5 and summarized in `plans/sir-life.md` section 15:

1. Muslim Pro now bundles Qalbox streaming into Premium, ships an "AiDeen" religious Q&A bot, gamified prayer quests/streaks, and made the whole Quran free. Competing on Islamic feature count is lost; calm + privacy + life-module breadth is the surviving edge.
2. "Plan your day around the salah" is now a marketed position: Sahibukum Regimen places habits/tasks inside prayer windows (with a Privacy PIN that encrypts on-device before sync); Barakah Planner sells niyyah tasks, family lists and medication lists around prayer times. Our Today screen must out-execute, not merely exist.
3. Verified/official prayer times are expected (Sahibukum badges MUIS/Kemenag/JAKIM official timetables). Plan now prefers the Egyptian General Authority published times and badges the source/method on every prayer surface (R9).
4. New second-ring competitors recorded: Salah Home, Just Pray (prayer-time app blocking, AI coach), Deeny, Salah Focus, Islamic Tracker, Pillars.
5. Positioning decision recorded: lead with "your whole day, organised"; prayer is one pillar; audience includes non-Muslims (Q6).

## Plan changes (`plans/sir-life.md`)

- Header updated: r61 refresh noted, tasks file now 42 tasks.
- Section 15 added: category delta from the second research pass.
- Section 16 added: full Part B screen inventory (19 web routes + mobile/desktop notes) with milestone mapping.
- Section 17 added: API and integration surface (auth session, health, sync, leads, billing webhook, AI proxy, owner metrics, accessible POIs, AlAdhan as validation-only, Egypt GA timetable, OSM geocoding, Firebase, Vercel, Part B Telegram bot).
- Section 18 added: launch and marketing plan (20-50 user beta with written consent, Arabic-first SEO, comparison pages only after re-verification, pricing validation interviews, weekly owner report).
- Section 19 added: risks R8-R12 and open questions Q6-Q7, each with a recommended answer.

## Tasks file changes (`ops/briefs/sir-life-tasks.md`)

- Kept T1-T10 order identical to the r52 queue; expanded the list to 42 tasks across M0-M6.
- Repaired copy-paste errors from other products: T29 notification payload no longer mentions visit codes/ETA; T38-T42 rewritten for SIR Life (domain + dual hosting go-live, store-readiness drafts, backup/restore drills, consent-based beta onboarding, legal + paid-launch gate). Escrow jobs, lawyer contract review and 301 redirects removed - they never belonged to this product.
- Every task now carries an explicit **Acceptance test** and a **Skills** line naming skills from `ops/SKILLS_INDEX.md`.
- Milestone headings corrected to match plan M0-M6; fixed the "fourty-two" typo and the stale "first ten" title.

## Date

2026-11-12. Continuation note: an earlier worker this round expanded the tasks file only; this pass completed the research, plan sections, log and repairs, then committed and reported.
