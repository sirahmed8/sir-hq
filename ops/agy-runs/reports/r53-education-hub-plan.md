# Report: r53a - SIR Education Hub big plan

## Summary

Merged the old SIR Obour Hub plan with the owner's 2026-11-12 direction into one bigger plan for SIR Education Hub, plus the 10-competitor matrix and the first 10 queued tasks.

## Files changed

- `D:/Projects/_SIR/plans/sir-education-hub.md` (rewritten, 349 lines): merged plan with sections: what changed vs r52, promise, competitors, names/IDs, multi-tenant model (Hub, members/roles, groups/classes/courses, schedules/materials/assignments/quizzes, practice/mock exams, chats/announcements, attendance, grades visibility, certificates, parent/guardian view, billing, settings/branding), Obour Institute as first Hub with full feature mapping, language-learning and study-help modules, AI tutor on fallback chain with privacy and no graded-work solving, onboarding wizard (linear stepper, future steps locked), owner-only analytics page, free tier + pricing, platform matrix, safety for minors + data protection (GDPR, Egyptian PDPL, moderation, reporting, export/deletion), architecture on Firebase + Vercel, premium quality bar, milestones M0-M6 with acceptance tests, first 10 tasks, risks, owner actions, skills/standards.
- `D:/Projects/_SIR/ops/competitors/sir-education-hub.md` (rewritten, 66 lines): 10 named competitors (Google Classroom, Moodle, Canvas, Schoology, Microsoft Teams for Education, Classera, Teachable, Udemy for Business, Edmodo successors, local Egyptian platforms) with strengths, flaws, our edge, ideas to steal, sourcing tasks.
- `D:/Projects/_SIR/ops/briefs/sir-education-hub-tasks.md` (rewritten, 33 lines): 10 queue-ready tasks with done-when checks.
- `D:/Projects/_SIR/plans/SHARED_PLATFORM_KIT.md`: consumer table row renamed from "SIR Obour Hub" to "SIR Education Hub".
- `D:/Projects/_SIR/ops/bus/sir-hq.md`: one appended entry.

## Commands run

- `wc -l` on the three new files: 349 + 66 + 33 = 448 lines.
- `git status` and `git log -5` at start: clean main, up to date with origin.
- `grep "SIR Obour Hub"` across _SIR to assess rename scope; only the consumer table row was changed (historical reports/logs left as history).

## What is still open

- Owner-only actions remain (domain, Firebase OAuth consent screen, Paymob/Fawry keys, legacy key rotation, lawyer review, Apple Developer account, final Hub prices after 5 interviews) - listed in plan section 19.
- Competitor pricing rows are "(unsourced, verify)" pending sourcing tasks.
- No code built in this round (planning only). CI quota flag means "CI green" is replaced by local verify; no build exists yet for this product.

## What I recommend next

- Queue the 10 tasks in `ops/briefs/sir-education-hub-tasks.md` for free agents (T1 deep scan first, then T3 scaffold, T4 rules, T5 auth).
- Sourcing tasks in the competitor file before any public comparison copy.
- A merge pass over the other r52 plans (Hagoozat, Business, etc.) against `plans/PRODUCT_DIRECTION_2026-11-12.md`, as the HQ checkpoint already notes.
