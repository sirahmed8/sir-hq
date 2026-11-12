# Competitor Study: SIR Education Hub (multi-tenant education platform)

> AUDIT 2026-11-12 (r53a plan rewrite): matrix rewritten to the 10 competitors named by the owner in `plans/PRODUCT_DIRECTION_2026-11-12.md` section 2. Every row carries a source link and a check date where one exists. Rows still marked "(unsourced, verify)" must not be copied into public copy, store listings or comparison pages until sourced.

**Date of research**: 2026-11-12
**Category**: multi-tenant education platform (LMS + campus portal + notes + AI tutor + attendance + grades + certificates)
**Audience**: any educational organization worldwide; first Hub is Obour Institute (EG).

---

## 1. The 10 competitors

| # | Competitor | What it is | Strengths | Weaknesses / frustrations | Our edge |
|---|---|---|---|---|---|
| 1 | **Google Classroom** | Free LMS bundled with Google Workspace for Education. Source: https://classroom.google.com (checked 2026-11-12) | Free for schools; tight Google Docs/Drive integration; simple assignment flow; huge adoption; works on mobile | Shallow: no real gradebook weights, no attendance, no timetable/halls, no notes vault, no certificates, no multi-tenant Hub branding, limited analytics; depends on Google Workspace | Multi-tenant Hub with branding, attendance, GPA, certificates, notes vault, and our own AI tutor; works without forcing Google Workspace; fair EGP pricing for Pro |
| 2 | **Moodle** | Open-source LMS, self-hosted or MoodleCloud. Source: https://moodle.org (checked 2026-11-12) | Free/open source; plugins for almost anything; strong quiz engine; gradebook; SCORM; huge community | Dated UX; heavy admin burden; hosting and upgrades are on you; mobile app is a wrapper; no built-in multi-tenant SaaS; Arabic UX is an afterthought | Hosted SaaS with premium UX, Arabic-first RTL, mobile-first, multi-tenant Hubs, AI tutor, no admin burden, fair pricing |
| 3 | **Canvas (Instructure)** | Cloud LMS dominant in higher ed. Source: https://www.instructure.com/canvas (checked 2026-11-12) | Modern UX; strong gradebook and analytics; mobile apps; SpeedGrader; large ecosystem | Priced for institutions (enterprise contracts); overkill for small institutes/teachers; Arabic support limited; no student-facing notes marketplace or AI tutor built in | Affordable per-Hub/per-seat tiers in EGP and USD; Arabic-first; built-in notes vault + AI tutor; fits a single teacher group up to a university |
| 4 | **Schoology (PowerSchool)** | K-12 LMS. Source: https://www.powerschool.com/schoology (checked 2026-11-12) | K-12 focus; parent portal; gradebook; attendance; SIS integration | Enterprise sales motion; weak outside North America; dated mobile; no Arabic-first UX; no AI tutor | Global, Arabic-first, mobile-first, AI tutor, marketplace, fair pricing, self-serve onboarding |
| 5 | **Microsoft Teams for Education** | Collaboration + assignments inside Teams/Office 365. Source: https://www.microsoft.com/education (checked 2026-11-12) | Free with Office 365 Education; strong video/meetings; assignments; OneNote Class Notebook | Heavy; requires Microsoft accounts; weak gradebook/analytics vs Canvas; no notes vault or GPA tools; Arabic UX is a translation | Lighter, purpose-built for education, own AI tutor, notes vault, GPA, attendance, certificates, multi-tenant branding |
| 6 | **Classera** | MENA-focused LMS/e-learning platform. Source: https://www.classera.com (checked 2026-11-12) | Arabic-first; MENA market focus; gamification; parent portal; mobile apps | Enterprise sales; pricing opaque; UX inconsistent; limited public docs/API; AI features bolted on | Self-serve onboarding, transparent pricing, premium UX, own AI tutor with integrity rules, open data export |
| 7 | **Teachable** | Course-selling platform for creators. Source: https://teachable.com (checked 2026-11-12) | Great course creation UX; payments built in; certificates; coaching; marketing tools | Built for selling courses, not running an institute; no attendance/timetable/grades/GPA; USD pricing; no multi-tenant Hub model for orgs | Institute-first model: timetable, attendance, grades, certificates, multi-role, Arabic-first, EGP pricing |
| 8 | **Udemy for Business** | Curated course library for companies. Source: https://business.udemy.com (checked 2026-11-12) | Large course catalog; analytics; SSO; mobile | Library model, not a platform you run your own courses on; no attendance/grades/timetable; USD pricing; no Arabic-first | You run your own Hub with your own courses, notes, quizzes, certificates; Arabic-first; fair pricing |
| 9 | **Edmodo successors** (Edmodo shut down 2022; successors include Google Classroom, Schoology, and regional clones) | Social-learning style LMS successors. Source: https://en.wikipedia.org/wiki/Edmodo (checked 2026-11-12) | Familiar feed-style classroom; parent/teacher/student roles; free tiers | Edmodo itself shut down (data loss lesson); successors vary in quality; many are abandoned; Arabic support uneven | Stable, owned data with export/deletion, multi-tenant, modern UX, AI tutor, clear pricing |
| 10 | **Local Egyptian platforms** (e.g., Obour's own MyU portal `student.oi.edu.eg`, Moodle `elearning.oi.edu.eg`, OUST portal) | Official institute portals and LMS instances. Sources: https://student.oi.edu.eg, https://elearning.oi.edu.eg, https://oust.edu.eg (checked 2026-11-12) | Official record of grades/registration; Arabic UI; per-course structure | Legacy desktop-era design; mobile-hostile; crash under result-day load (frequency "(unsourced, verify)"); zero notes search, timetable, community, AI; fragmented per course | Fast, mobile-first front door that stays useful on result day; structured notes vault; timetable, GPA, attendance; links out to official portal only where needed; never stores grades as the source of truth |

---

## 2. What the research says (sourced facts only)

- Official Obour student services live at `student.oi.edu.eg` ("نظام ابن الهيثم - معاهد العبور") and course content at `elearning.oi.edu.eg`. Both checked live 2026-11-12. Neither offers notes search, GPA planning, attendance tracking or a student marketplace.
- Google Classroom and Microsoft Teams for Education are free with their respective workspaces, which sets a high bar for "free"; our edge is the features they lack (notes vault, GPA, attendance, certificates, AI tutor, multi-tenant branding) and Arabic-first UX.
- Moodle and Canvas dominate higher ed but are heavy to run (Moodle) or enterprise-priced (Canvas); a self-serve, fairly priced Hub fits the gap below them.
- Classera is the closest regional competitor (Arabic-first, MENA) but is enterprise-sales and opaque pricing; self-serve + transparent pricing is our opening.
- Edmodo shut down in 2022, a reminder that data ownership and export matter; we commit to one-tap export and deletion.

## 3. "We do better" advantage map

1. **Multi-tenant Hub model**: any organization creates its own Hub with branding, roles, courses, billing; people join the Hubs they belong to. Competitors are either single-school (Classroom, Teams) or enterprise (Canvas, Moodle-hosted, Classera).
2. **Arabic-first, Egyptian-dialect UX**: RTL-first, logical CSS, bidi isolation, Cairo/IBM Plex Sans Arabic. Global LMSs treat Arabic as a translation.
3. **Integrity-first AI tutor**: grounded in the Hub's own notes; explains, quizzes, hints; refuses graded work. Competitors either have no tutor or sell answers.
4. **Obour-specific and institute-specific tools nobody else has**: GPA simulator on the Egyptian credit-hour scale, absence tracker against the institute's rule, hall directory, used-book marketplace with direct WhatsApp contact, .ics export.
5. **Fair EGP pricing**: free tier for students, free trial for Hubs, affordable per-Hub/per-seat subscriptions; no USD-only tiers.
6. **Resilient, mobile-first front door**: timetable, today's lectures with hall numbers, exam countdown, urgent notices in one screen that works on weak campus networks (PWA, offline cache, edge-cached public pages).
7. **Data ownership**: one-tap export and deletion, no lock-in, clear legal pack, audit log.

## 4. Ideas to steal (tagged)

- Google Classroom: assignment flow simplicity, class code to join, mobile app polish. (cite)
- Moodle: quiz engine (question banks, randomization, feedback), gradebook weights, SCORM import. (cite)
- Canvas: SpeedGrader UX, analytics dashboard, mobile app quality, calendar view. (cite)
- Schoology: parent portal, attendance module, SIS integration patterns. (cite)
- Microsoft Teams: video meetings integration, OneNote Class Notebook concept. (cite)
- Classera: gamification (badges, points), parent portal, Arabic UX patterns. (cite)
- Teachable: course creation UX, certificate generation, payment/checkout flow. (cite)
- Udemy for Business: analytics for managers, curated library concept. (cite)
- Edmodo successors: feed-style classroom, role-based views. (cite)
- Local Egyptian platforms: link out rather than replace; never store grades as source of truth. (original)

## Sourcing tasks (open, each under 2 hours)

1. Verify current pricing pages for Canvas, Schoology, Classera, Teachable, Udemy for Business and record with dates (all currently "(unsourced, verify)" for exact tiers).
2. Record the official reuse/terms position of `student.oi.edu.eg`, `elearning.oi.edu.eg` and `oi.edu.eg` (what may be linked, scraped or mirrored; links + dates).
3. Find 5 real student-run notes groups/sites used by Egyptian students with links; record exactly what each lacks.
4. Find an official enrolment figure for Obour institutes (institute site or ministry page) before any student count is quoted publicly.
5. Find the official regulation text for the 25% absence rule and grade-appeal procedure on an oi.edu.eg page; cite it before the app states it as fact.
6. Confirm Edmodo shutdown date and data-export outcome from a reliable source.
