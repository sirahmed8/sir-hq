# Competitor Study: SIR Study (private study helper, flashcards, practice, portal sync)

> AUDIT 2026-11-12 (r52 plan rewrite): rows carry a source link and check date where one exists. Rows still marked "(unsourced, verify)" must not be copied into public copy until sourced. Student complaints are paraphrased from public forum threads unless a link is given.

**Date of research**: 2026-11-12
**Category**: personal study organizer / flashcards / practice / portal sync
**Audience**: one student (Ahmed), Obour Higher Institutes, Management & Informatics, year 2 term 1. Private tool, never sold.

---

## 1. The 10 competitors and channels

| # | Competitor / channel | What it is | Strengths | Weaknesses / frustrations | Our edge |
|---|---|---|---|---|---|
| 1 | **Anki** (ankiweb.net) | Open-source spaced-repetition flashcard app with huge add-on ecosystem. Source: https://apps.ankiweb.net/ (checked 2026-11-12) | Best-in-class SM-2 scheduling; offline; free desktop; sync across devices | Steep learning curve; card authoring is manual; no portal sync, no deadlines, no Arabic-first UX out of the box; community add-ons vary in quality | Our flashcards are generated from his own lectures with citations; scheduling is one feature inside a whole study flow, not the whole product |
| 2 | **Quizlet** | Flashcards and practice sets with spaced repetition. Pricing "(unsourced, verify)" | Great spaced-repetition UX; huge content library; mobile-first | No institute-specific timetable, halls, attendance or notes vault; content is user-generated with quality drift; USD subscription wall for premium | Practice quizzes generated from the course's own notes with citations; attendance/absence tracking Quizlet lacks |
| 3 | **NotebookLM** (Google) | AI notebook that summarizes sources and generates audio overviews and quizzes. Source: https://notebooklm.google.com/ (checked 2026-11-12) | Excellent source-grounded summaries; audio overview; free tier; strong citations | Cloud only, sends material to Google (not allowed for our private notes under our privacy rule); no deadline tracking, no portal sync, no offline | Local models only; material never leaves the machine; deadlines and portal sync built in |
| 4 | **Course Hero** | Global study-document marketplace + tutors. Premier ~$38.99/mo US (source: https://silentstudent.com/vs/coursehero, checked 2026-10-20 data); Egypt regional price listed at E£709.99 (~$13.31) per region-pricing aggregator (source: https://apppricelens.com/app/course-hero-ai-homework-help-922208952, "(unsourced, verify)" for exact current checkout) | 100M+ documents claim; tutor access; textbook solutions | USD-priced far above Egyptian student budgets; generic content, almost nothing for Egyptian institute curricula and named professors; quality varies | Free-first vault of real Obour notes; EGP mental model; AI tutor grounded in the actual course material, not a generic corpus |
| 5 | **Studocu** | Student notes marketplace + AI quiz + lecture recorder. Premium $34.99/quarter or $79.99/year in its iOS app (source: https://silentstudent.com/vs/coursehero, checked 2026-10-20 data) | 50M+ notes claim; organized by university/course; strong mobile app | Subscription wall for most content; generic global library; not built for Obour timetable/GPA/attendance | Free browsing with fair limits; Obour-specific timetable, hall directory and absence tracker Studocu does not have |
| 6 | **Chegg Study** | Textbook solutions + expert Q&A. Chegg Study ~$15.99/mo in its iOS app (source: https://silentstudent.com/vs/coursehero, checked 2026-10-20 data) | Expert-verified answers; math solver | USD-priced; generic US curriculum; doing graded work for you is exactly what we refuse | Integrity-first tutor: hints and explanations only, never solves graded assignments or live quizzes |
| 7 | **Notion / Google Keep (student setups)** | Generic note-taking students improvise with | Free/cheap; flexible; familiar | No Obour structure, no timetable sync, no exam countdown, no shared class vault; every student rebuilds the same system alone | Ready-made version of what students hack together: timetable, GPA planner, notes, planner in one place |
| 8 | **Obsidian** | Local-first linked-notes app with graph view and plugin ecosystem | Plain Markdown files on disk; graph of linked notes; huge plugin ecosystem; users trust plain files; sync optional | Not an agent; sync paid (~USD 4-5/mo, unverified); no institute timetable or portal sync | Linked-notes memory view and plain-file export; our summaries cite source file and page |
| 9 | **Khan Academy / Brilliant** | Structured courses with practice and mastery tracking. Source: https://www.khanacademy.org/ (checked 2026-11-12) | Excellent pedagogy; free; strong practice loops | Generic US curriculum; nothing for Obour's specific subjects, professors or exam format | Practice in the real midterm format of his own subjects, built from his own lectures |
| 10 | **Official institute portal + Facebook/Telegram groups** | `student.oi.edu.eg` ("نظام ابن الهيثم - معاهد العبور") and `elearning.oi.edu.eg` Moodle; per-subject Facebook/Telegram groups where notes and dates actually live. Sources checked 2026-11-12 | Official record of grades and registration; official course materials; groups have huge reach and instant word of mouth | Legacy desktop-era design; mobile-hostile; crashes under result-day load; fragmented per course; groups are chaos (spam, lost PDFs, scam book sales, no search, deleted history) | A fast, mobile-first front door that stays useful on result day; structured, searchable, permanent notes organized Year > Department > Subject > Doctor; links out to the official portal only where needed; never stores grades as the source of truth |

---

## 2. What the research actually says (sourced facts only)

- Official student services live at `student.oi.edu.eg` ("نظام ابن الهيثم - معاهد العبور") and course content at `elearning.oi.edu.eg`. Both checked live 2026-11-12. Neither offers notes search, GPA planning, attendance tracking or a student marketplace.
- The global leaders (Course Hero, Studocu, Chegg) all price in USD-equivalent subscriptions; Egypt regional pricing still lands around $9-$14/month entry tiers per the aggregators above ("(unsourced, verify)" for exact current checkout numbers). An Obour student paying in EGP gets far more value from a free-first local product. (Inference, flagged.)
- The real competition is not a product; it is the pile of Facebook/Telegram groups plus the official portal. Winning means being the single place a student opens every morning. (Inference, flagged.)
- Anki's scheduling is the gold standard for spaced repetition; our edge is not better scheduling but generating the cards from his own lectures with citations and tying them to deadlines.

## 3. "We do better" advantage map

1. **Resilient, mobile-first front door**: timetable, today's lectures with hall numbers, exam countdown and urgent notices in one screen that works on the institute's weak campus network (PWA, offline cache).
2. **Curated course vault**: Year > Department > Subject > Doctor organization, 1-click download of verified summaries and past papers hosted on our own storage, never paywalled behind a USD subscription.
3. **Integrity-first AI tutor**: grounded strictly in uploaded notes and institute docs; explains, quizzes and gives hint ladders; refuses graded work. This is a feature competitors cannot copy without breaking their own model (Chegg/Studocu sell answers; we sell understanding).
4. **Obour-specific tools nobody else has**: GPA simulator on the Egyptian credit-hour scale, absence tracker against the 25% deprivation rule, hall directory, used-book marketplace with direct WhatsApp contact (shared with SIR Education Hub).
5. **Arabic-first, Egyptian dialect**: the global apps are English-first; our RTL-first Arabic UI is the default, not a translation.
6. **Privacy**: material never leaves the machine; local models only; no cloud notebook that trains on his notes.

## 4. Facts that must not be claimed

- Any competitor price marked "(unsourced, verify)" must not appear in copy.
- Star counts and document counts are snapshots, not claims about SIR Study.
- No SIR Study feature is "live" from this file - status stays in `.sir/CHECKPOINT.md` and `.sir/TASKS.md`.
- No repos cloned; referenced through docs only.
- Refresh matrix every quarter and whenever a competitor changes owner.