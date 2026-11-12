# Competitor Study: SIR Obour Hub (student portal, notes vault, timetable, GPA, AI tutor)

> AUDIT 2026-11-12 (r52 plan rewrite): every row now carries a source link and a check date where one exists. Rows still marked "(unsourced, verify)" must not be copied into public copy, store listings or comparison pages until sourced. Student complaints quoted below are paraphrased from public forum threads unless a link is given; treat unlinked quotes as illustrative.

**Date of research**: 2026-11-12
**Category**: campus student portal / study-notes marketplace / timetable + GPA tools / AI study assistant
**Audience**: students of Obour Higher Institutes (Management & Informatics, Engineering & Technology) first, then other Egyptian institutes.

---

## 1. The 10 competitors and channels

| # | Competitor / channel | What it is | Strengths | Weaknesses / student frustrations | Our edge |
|---|---|---|---|---|---|
| 1 | **MyU student portal** (`student.oi.edu.eg`, "نظام ابن الهيثم - معاهد العبور") | Official institute services portal (grades, registration). Source: https://student.oi.edu.eg/ (checked 2026-11-12) | Official record of grades and registration; Arabic UI | Legacy desktop-era design; mobile-hostile; crashes under result-day load per repeated student complaints ("(unsourced, verify)" for crash frequency); zero notes, timetable or community features | A fast, mobile-first front door that stays useful on result day; links out to official portal only where needed; never stores grades as the source of truth |
| 2 | **Obour e-learning (Moodle)** (`elearning.oi.edu.eg`) | Official LMS for course materials and quizzes. Source: https://elearning.oi.edu.eg/ (checked 2026-11-12) | Official, per-course structure; Arabic/English UI | Fragmented per course; no cross-course notes vault; weak mobile UX; students still keep notes in Telegram | One organized vault across all courses plus practice quizzes that cite the uploaded notes |
| 3 | **OUST student portal** (`student.oust.edu.eg`, Obour University) | Sister university's portal: student handbook, LMS, services portal links. Source: https://oust.edu.eg/en/pages/students (checked 2026-11-12) | Shows what a modernized portal bundle looks like (handbook PDF, LMS, services) | University-level, different institute; same legacy patterns likely | We can later serve both institutes from one codebase; our timetable/GPA/notes layer sits on top of any official portal |
| 4 | **Unofficial Facebook & Telegram groups** (per institute, per year, per subject) | Where notes, exam dates and complaints actually live today | Free; huge reach; instant word of mouth | Chaos: spam, lost PDFs, scam book sales, no search, no structure, deleted history | Structured, searchable, permanent notes organized Year > Department > Subject > Doctor; takedown and moderation rules |
| 5 | **Course Hero** | Global study-document marketplace + tutors. Premier ~$38.99/mo US (source: https://silentstudent.com/vs/coursehero, checked 2026-10-20 data); Egypt regional price listed at E£709.99 (~$13.31) per region-pricing aggregator (source: https://apppricelens.com/app/course-hero-ai-homework-help-922208952, "(unsourced, verify)" for exact current checkout price) | 100M+ documents claim; tutor access; textbook solutions | Priced in USD tiers far above Egyptian student budgets; generic content, almost nothing for Egyptian institute curricula and named professors; document quality varies | Free-first vault of real Obour notes; EGP pricing; AI tutor grounded in the actual course material, not a generic corpus |
| 6 | **Studocu** | Student notes marketplace + AI quiz + lecture recorder. Premium $34.99/quarter or $79.99/year in its iOS app (source: https://silentstudent.com/vs/coursehero, checked 2026-10-20 data) | 50M+ notes claim; organized by university/course; strong mobile app | Subscription wall for most content; generic global library; not built for Obour timetable/GPA/attendance | Free browsing with fair limits; Obour-specific timetable, hall directory, GPA simulator that Studocu does not have at all |
| 7 | **Chegg Study** | Textbook solutions + expert Q&A. Chegg Study ~$15.99/mo in its iOS app (source: https://silentstudent.com/vs/coursehero, checked 2026-10-20 data) | Expert-verified answers; math solver | USD-priced; generic US curriculum; doing graded work for you is exactly what we refuse | Integrity-first tutor: hints and explanations only, never solves graded assignments or live quizzes |
| 8 | **Quizlet** | Flashcards and practice sets. (Pricing "(unsourced, verify)") | Great spaced-repetition UX; huge content library | No institute-specific timetable, halls, attendance or notes vault; content is user-generated with quality drift | Built-in practice quizzes generated from the course's own notes with citations; attendance and absence-threshold tracker Quizlet lacks |
| 9 | **Google Keep / Notion (student setups)** | Generic note-taking students improvise with | Free/cheap; flexible; familiar | No Obour structure, no timetable sync, no exam countdown, no shared class vault; every student rebuilds the same system alone | The ready-made version of what students already hack together: timetable, GPA planner, notes, planner in one place |
| 10 | **Campus used-book market (Facebook Marketplace groups, informal WhatsApp chains)** | Peer-to-peer resale of textbooks, drafting tools, calculators | Direct, free to list, trusted within the cohort | No structure, scams happen, no search, listings disappear, zero commission but zero safety | Optional peer marketplace with direct WhatsApp contact, listing moderation, and a low 30 EGP/semester business-listing tier (price from `.sir/MASTER_PLAN.md`, "(unsourced, verify)" as market rate) |

---

## 2. What the research actually says (sourced facts only)

- Official student services live at `student.oi.edu.eg` ("نظام ابن الهيثم - معاهد العبور") and course content at `elearning.oi.edu.eg`. Both checked live 2026-11-12. Neither offers notes search, GPA planning, attendance tracking or a student marketplace. (Sources above.)
- The global leaders (Course Hero, Studocu, Chegg) all price in USD-equivalent subscriptions; Egypt regional pricing still lands around $9-$14/month entry tiers per the aggregators above ("(unsourced, verify)" for exact current checkout numbers). An Obour student paying in EGP gets far more value from a free-first local product. (Inference, flagged.)
- The real competition is not a product; it is the pile of Facebook/Telegram groups plus the official portal. Winning means being the single place a student opens every morning. (Inference, flagged.)

## 3. "We do better" advantage map

1. **Resilient, mobile-first front door**: timetable, today's lectures with hall numbers, exam countdown and urgent notices in one screen that works on the institute's weak campus network (PWA, offline cache).
2. **Curated course vault**: Year > Department > Subject > Doctor organization, 1-click download of verified summaries and past papers hosted on our own storage (Firebase Storage), never paywalled behind a USD subscription.
3. **Integrity-first AI tutor**: grounded strictly in uploaded notes and institute docs; explains, quizzes and gives hint ladders; refuses graded work. This is a feature competitors cannot copy without breaking their own model (Chegg/Studocu sell answers; we sell understanding).
4. **Obour-specific tools nobody else has**: GPA simulator on the Egyptian credit-hour scale, absence tracker against the 25% deprivation rule, hall directory, used-book marketplace with direct WhatsApp contact.
5. **Arabic-first, Egyptian dialect**: the global apps are English-first; our RTL-first Arabic UI is the default, not a translation.

## Sourcing tasks (open, each under 2 hours)

1. Record the official reuse/terms position of `student.oi.edu.eg`, `elearning.oi.edu.eg` and `oi.edu.eg` (what may be linked, scraped or mirrored; links + dates).
2. Find 5 real student-run notes groups/sites used by Egyptian students with links; record exactly what each lacks.
3. Find an official enrolment figure for Obour institutes (institute site or ministry page) before any student count is quoted publicly.
4. Verify current Egypt checkout prices for Course Hero Premier, Studocu Premium and Chegg Study on their own pages (not aggregators) and replace the "(unsourced, verify)" tags.
5. Find the official regulation text for the 25% absence rule and grade-appeal procedure on an oi.edu.eg page; cite it before the app states it as fact.
