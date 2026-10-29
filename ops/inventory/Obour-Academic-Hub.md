# Inventory: Obour Academic Hub (2026-10-29, scout, read-only, nothing built or run)

**What:** study platform for Obour Higher Institutes CS students (Arabic/English). Pages: /main /subject /exams /quiz /qa /todo /jarvis /market /alumni /plus /pricing /admin. Owner: Ahmed. No `.sir/` folder.
**Stack:** Next 16.1.1 App Router, React 19.2.3, TS 5.9.3, Tailwind 4.1.18, Firebase 12.7 + firebase-admin 13.7, zod 4.4, vitest 4.0.16, Node 22. 344 TS/TSX files, about 62k lines.
**Repo:** clean at 16722054 (2026-10-29). CI `.github/workflows/ci.yml`: lint, prettier, vitest, build, deploy to Firebase Hosting (deploy step treats 403 as success). `daily-backup.yml` exports Firestore (90-day artifacts).
**Live (not fetched):** obourinstitutes1.web.app, obour-academic-hub.vercel.app. **Platforms:** web + PWA only.
**Data/auth:** Firestore (60 allow lines), Storage rules, Upstash Redis rate limits, Cloudinary, Vercel Blob. Firebase Google popup; session cookie `__session` httpOnly, sameSite lax. 2FA not checked.
**AI:** OpenRouter, DeepSeek, Gemini via `src/lib/aiService.ts`; `/api/ai/*`, `/api/chat`; jarvis-study limited 25/60 per uid.
**Legal:** /privacy /terms /refunds /cookies and /legal/*. No sub-processor list, DPA or AI-training clause. Cookie banner has a decline button; Vercel Analytics loads before consent (layout.tsx:182-183).
**Tests:** 47 test files (not run). Desktop: "Obour Academic Hub.lnk".

## Scores (0-5)
| Area | Score | Evidence |
|---|---|---|
| Architecture | 3 | layered dirs; 24+ files over 530 lines (largest 2,104) |
| Code quality | 2 | 16 `any`, lint not run |
| Security | 2 | rate limits and httpOnly cookie good; `allow read: if true` on banners, exams, questions, projects, hagazSessions; CSP unsafe-inline/eval |
| UX/design | 3 | loading.tsx on 20+ pages per docs, not screenshot-verified |
| Performance | 2 | unmeasured; forced webpack build |
| Completeness | 3 | 60+ pages; payments not live (manual request/redeem plus waitlist) |
| Store readiness | 1 | |

## Red flags
1. **Graded work.** `D:\Projects\Obour Institute Second Year 1st term` (182 MB) holds Moodle automation: scripts such as `generate_and_submit_all_assignments.py`, `submit_all_new_assignments.py`, `*_quiz_live_solver.py`, `*_sentinel.py` log in with stored credentials, auto-solve quizzes and submit assignments; `MASTER_AUTOMATION_PROMPT.md` runs it nightly. Filenames `test_cf_waf.py`, `test_encoding_bypass.py`, `isolate_blocked_param.py` suggest bypass testing (unverified).
2. The Hub also does graded work: jarvis-study modes `solve_assignment` and `solve_quiz` (route.ts:11-15), "professor-ready submission" prompt (route.ts:129).
3. Fake output: deterministic `CURRICULUM_FALLBACKS` returned as solutions when AI fails (route.ts:150-173).
4. `ci.yml:12-24` hardcodes Firebase config, VAPID key and the owner email (PII in git).
5. Secret files at rest in the project root (two Firebase admin JSON keys, `new-service-account.json`, `.env.local`), gitignored and untracked. `.env.local` has an unused `NEXT_PUBLIC_GOOGLE_GENERATIVE_AI_API_KEY`.

## Upgrade size: L. Top 5 fixes
1. Agents stop touching the Moodle submit/solve scripts; decision logged (see HQ decision below).
2. Remove `solve_assignment`, `solve_quiz` and the fallback solutions; replace with hints, explanations and practice questions.
3. Tighten Firestore read rules on the five collections and test in the emulator.
4. Session cookie sameSite Strict; drop unsafe-inline/unsafe-eval from CSP.
5. Sub-processors, DPA and AI-training clause in /privacy; analytics only after consent; CI deploy fails on 403.

## HQ decision (2026-10-29)
Rule: help Ahmed learn, never take graded work for him (Tier 3). Agents will not run, repair, extend or schedule the Moodle automation, and will remove the solve modes from the Hub in its upgrade wave. His own files are not deleted or moved by an agent; the advice goes on OWNER_ACTIONS (stored Moodle credentials should be changed regardless, and academic-integrity rules at the institute apply to him, not to us).
