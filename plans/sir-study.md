# PLAN: SIR Study (Wave 2, PERSONAL private study helper)
Audited 2026-11-12 (r52 plan rewrite). Replaces the legitimate parts of the old Obour Institute scripts (materials download, convert, study portal, briefings). Private tool for one owner: never sold, never listed, `noindex`. Commercial items are marked "n/a" with the reason. Nothing graded is ever done for Ahmed; the tool explains, summarizes, quizzes him for practice and plans his week.

## 1. Who it is for and the one-sentence promise
For Ahmed (second-year student, Obour Higher Institutes, Management & Informatics) during and outside exam weeks. Promise: "Turn your own lecture files into readable guides, flashcards and practice questions, show what is due and when exams are, and remind you on your phone - and never do the graded work for you."

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Study` |
| GitHub (private) | `sirahmed8/sir-study` |
| Runtime | Python local engine (`scripts/`), `guides/*.html` PWA (one per subject plus `START_HERE.html`), `scripts/serve.py` on `127.0.0.1:3300`, scheduled task `SIR_Study_Sync` every 3 hours (paused in game mode) |
| Firebase / Vercel | n/a - local only, no public site. If it is ever published, it must be rebuilt on the shared kit with its own Firebase project and Vercel import (OWNER_DEFAULTS 2) |
| App ids | `app.sir.sir-study` (Android/iOS/Windows) reserved, not shipped (private tool) |
| Platforms | see section 4 |
| Money | none. Subscription, EGP/USD checkout, legal pack, marketing, SEO: n/a. Default: if ever offered to others, rebuild on the shared kit billing and legal pack, never inside this folder |

## 3. Current state (verified vs claimed)
Claimed in `.sir/CHECKPOINT.md` (2026-11-12): portal sync built and verified; exams verified against the portal table; integrity guard 105/105 (73 refused + 32 answered); 8 Playwright browser tests; M1 restart proof; shared assets extracted; touch targets; English shell; defect fixes through r22; 52 unit tests green; CI green at bb6feb7.
Built and verified by this audit's reading: `scripts/verify.ps1` all 11 checks green, 52 unit tests OK, gitleaks clean (per checkpoint). Not independently re-run here.
Open items (honestly open): M2 flashcards + spaced-repetition backend is still open; T-103 portal/Moodle watcher is still unchecked; T-107 Drive mirror is still unchecked; T-023 retirement of the old Obour scripts folder is still unchecked. Nothing is called working until re-verified today.

## 4. Platform matrix (v1 scope)
| Platform | v1 | Notes |
|---|---|---|
| Web (local) | yes | `guides/*.html` served by `scripts/serve.py` on loopback |
| PWA (laptop + phone over Tailscale) | yes | service worker `sw.js`, offline cache, installable |
| Windows | skipped | private tool; no installer shipped. If published, follows WINDOWS_APP_STANDARD |
| macOS / Linux | skipped | private tool |
| Android / iOS | skipped | phone uses the tailnet page; no store build |
| Wear OS / watchOS / TV / car | skipped | private tool |
| Browser extension | skipped | private tool |
Shared kit rule still applies to any future public build: own Firebase project and own repo named after the product.

## 5. Competitors / best in class
See `ops/competitors/sir-study.md` (10 competitors/channels with strengths, flaws and our edge). Headline: the real competition is the pile of Facebook/Telegram groups plus the official portal; the global leaders (Course Hero, Studocu, Quizlet, Chegg) price in USD and sell graded answers, which we refuse.

## 6. Features (on par with the best, plus Ahmed's own ideas from legacy and TickTick)
- Materials index of all course folders (734 files indexed) with counts and hashes.
- Per-subject study guides: lesson summaries, key terms, worked examples, flashcards, self-test quizzes with answers, formula/code sheets, exam map; regenerated on upload.
- Today screen: lectures, deadlines, what to study; live exam countdown.
- Deadline calendar from a read-only Moodle iCal feed; portal sync (`scripts/portal_sync.py`) lists every course item with date, downloads new lectures/attachments, dedups by sha256, files into `{Lectures,Assignments,Quizzes,Summaries,Practice}`, regenerates `guides/portal-deadlines.json`, sends Telegram "مادة جديدة" per new item.
- Flashcard mastery engine with mastery buttons and spaced repetition (SM-2 style) - backend still open (M2).
- Practice mode: mock quizzes in real exam format, explanations, weak-topic tracking, daily plan sized to 15/30/60 minutes.
- Assignment and quiz coaching: plain-words requirements, needed lecture sections, parallel worked example with different numbers, step hints, checklist; Ahmed writes the final answer.
- Interactive solver tools (OR Simplex/Graphical/Big-M, SAD DFD/PERT).
- Integrity guard: explainer refuses graded work in Arabic and English; eval stays at 100% refusals (105/105).
- Local AI explainer with source citations (file + page); fallback chain local model A -> local model B -> keyword search; kill switch `STUDY_AI=off`.
- Telegram reminders (dates and subject names only, no material text); exam briefing sender.
- Sanitised shared export of study pages (course content only) with personal-data scan.
- Backup/restore drill, destructive-action dry run + undo.
- English shell (i18n, RTL/LTR toggle), Arabic RTL first.
- Coverage proof per subject (`guides/COVERAGE.md`).
- (Owner ideas to port explicitly from legacy and TickTick: see `.sir/TASKS.md` and `materials/digest/`. TickTick notes "30-Day Projects Sprint" and project-ideas notes, column "Me", are to be re-checked before any rewrite per OWNER_DEFAULTS 18; the "habobty" column is never read.)

## 7. Architecture on the shared kit
- Accounts: two named accounts only (Ahmed + one), passkey or strong password + TOTP, HttpOnly/Secure/SameSite=Strict sessions, server-side check on every route, device allow-list. No public signup. Local bind to 127.0.0.1; phone access via Tailscale with auth.
- Owner-only analytics page: the local health/today dashboard is owner-only by transport identity (Tailscale + loopback); no other user can reach it. No public metrics.
- AI: local models only (private data never leaves the machine). Chain: local model A -> local model B -> keyword search over the index. No shared-kit `ai-proxy`/cloud keys; `ask.ps1` private mode. Kill switch `STUDY_AI=off`.
- Hosting: local only. No Firebase Hosting or Vercel for the private build. If published later, dual host (Firebase + Vercel) with the same build and env vars (OWNER_DEFAULTS 2) and both curl-checked.
- Shared pieces used: Telegram sender `scripts/deliver/send-telegram.mjs` (do not build another); design family tokens shared with Jobs and Laptop Manager; integrity eval pattern.

## 8. Premium quality bar (Apple-level)
- Arabic RTL first + English; light/dark/system/high-contrast; 320 px to 4K; zoom 80-200%; WCAG 2.2 AA; 44 px touch targets; spring motion with reduced-motion path; transform/opacity only.
- Five states on every screen: idle, loading skeleton, empty with one action, error with retry, populated.
- Bidi text per character (OWNER_DEFAULTS 15); native-app feel: disable default selection/context menu, own context menu (OWNER_DEFAULTS 14).
- Self-audit loops until two clean cycles; browser tests for layout invariants at 320/390/768/1280/1920 in both languages/themes.
- No invented numbers; no fake users; no emoji; no em-dashes in copy; version stays 1.0.0.

## 9. Free tier and fair pricing (EGP and USD)
n/a - private tool, not sold, not listed. No pricing, no checkout, no legal pack. Default: if ever offered to others, rebuild on the shared kit billing (EGP first, auto currency from locale/IP with manual override) and legal pack, never inside this folder.

## 10. Milestones M0-M6 with acceptance tests
| M | Goal | Exit check |
|---|---|---|
| M0 | Foundations + Desktop folder kit recreated | `scripts/verify.ps1` green; threat model + ADR exist; Desktop/SIR Projects/SIR Study folder with folder.ico, shortcuts (web links both hosts n/a, Start dev, Stop dev, Open folder), Versions.txt 1.0.0; gitleaks clean |
| M1 | Materials index and deadlines | index lists all course folders; Today shows deadlines from iCal feed (fixture test + one real read-only fetch) |
| M2 | Converters, flashcards + spaced repetition, weekly plan, reminders | PDF/DOCX to markdown test; flashcard schedule unit test; reminders fire in a dry run |
| M3 | Security | rules (no public bind, loopback/Tailnet guard, no wildcard CORS, no POST to submit/attempt) have tests; brute-force n/a (no login) |
| M4 | AI | refusal eval 100% and citation eval at or above stored score |
| M5 | Quality | screenshots at 320/390/768/1440, RTL and LTR; no horizontal scroll; two clean audit cycles |
| M6 | Retirement of legacy | old Obour scripts folder moved to `old projects` keeping course materials; recorded in checkpoint |

## 11. Skills to use (from ops/SKILLS_INDEX.md)
a11y-debugging, chrome-devtools, cookie-debugging, memory-leak-debugging, modern-web-guidance, mobile-ergonomics-polish, react-best-practices, owasp-vulnerability-shield, zero-trust-security-hardening, vibe-auth-hardening, database-reliability-transactions, managing-python-dependencies, verification, troubleshooting, direct-action-shield, karpathy-skills, production-engineering-standards.

## 12. Risks and open questions (defaults)
- Institute rules on automated access: official feed only, read-only, otherwise manual import.
- Study guides built by AI can contain errors: every claim shows source file + page; `verify_accuracy.py` stays in the verify chain.
- Exam-period urgency may tempt shortcuts: no feature may answer a live graded item; refusals are tested.
- Disk space: materials stay where they are, only an index is built.
- Tailscale/loopback identity is the auth boundary; if the tunnel is misconfigured, nothing is exposed (fail closed).

## 13. Only the owner can do
Sign in to the institute site to copy his own iCal link or create a read-only token; sign in to Tailscale on his phone; click Submit on any assignment himself; rotate secrets.

## 14. Market-grade note
Private study tool: no competitor study needed beyond inspiration (`ops/competitors/sir-study.md` exists; unsourced lines tagged). No country legal pack. Data in the folder is the owner's course material: do not publish it, do not put it in a public repo. AHome and Habiba data never leaves AHome.