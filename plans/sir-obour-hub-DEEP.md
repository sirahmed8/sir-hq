# DEEP PLAN & MASTER SPEC: SIR Obour Hub
**Project**: SIR Obour Hub (`D:/Projects/SIR Obour Hub`)  
**Mission**: Sovereign Academic Portal, Timetable Hub, GPA Simulator & Campus Community for Obour Higher Institutes  
**Academic Integrity Invariant**: Strict learning and schedule support only. Zero quiz solving or automated grading bots.  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Obour Hub is a high-craft, student-centric academic companion and campus portal engineered for the student body of Obour Higher Institutes (Computer Science, Engineering, Business Administration). It provides seamless, instant access to lecture timetables, hall allocations, attendance trackers, semester GPA forecasting tools, professor announcement streams, and verified curriculum materials, completely eliminating the confusion of fragmented social media channels and outdated PDF schedules.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Obour Hub/legacy/`)
- **`Obour Academic Hub`**: Next.js & Python backend prototype containing earlier institute schedule views, grading calculators, and campus news feeds.
- **Quarantine Note**: Historical Moodle quiz auto-solvers (`ba_quiz_live_solver.py`, `academic_submission_engine.py`) were permanently quarantined inside `_quarantine/` per workspace rule 14 (never take graded work for the owner).

### 2.2 What is Valuable to Port
- **Academic Timetable Data Models**: Normalized schedule structure (department, year, section, day, time, lecture hall, professor).
- **Egyptian Higher Education GPA Algorithm**: Exact credit-hour grading formulas (4.0 scale with Letter grades A+, A, B+, B, C+, C, D+, D, F and percentage thresholds).
- **Lecture Hall Map Directory**: Campus building map and hall directory (Halls 533, 401, etc.) with accessibility paths.

### 2.3 What Must Be Discarded
- Automated grading scripts or submission automation.
- Hardcoded scraper credentials and brittle scraping routines.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Frontend**: Next.js 14 App Router, React 18, Tailwind CSS, Dynamic Island spring navigation.
- **Backend**: Serverless API routes (Edge runtime) + Cloudflare D1 / Turso SQLite database for timetable data.
- **Offline / PWA**: Stale-while-revalidate Service Worker caching entire semester schedules locally.
- **Auth**: Optional student profile sign-in (email/passkey) via `SIR Platform` owner auth, with full guest read-only access for schedules.

### 3.2 Design Identity
- **Brand Aesthetic**: Academic Prestige & Campus Beacon. Modern, accessible, vibrant, and orderly.
- **Palette**:
  - Primary Campus Emerald: `#059669` (Emerald 600) / `#047857` (Emerald 700)
  - Secondary Gold Accent: `#D97706` (Amber 600)
  - Dark Surface Base: Deep Forest Obsidian (`#06110D` / `#0C1E17`)
  - Elevated Cards: Translucent Emerald Slate (`rgba(12, 30, 23, 0.75)` with `backdrop-filter: blur(12px)`)
  - High-Contrast Text: `#F0FDF4`
  - **Zero Yellow Buttons**: Strictly enforced.
- **Typography**: Clean bilingual typography (`Cairo` for Arabic, `Inter` for English).
- **Motion Personality**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), active-tab labels only, zero outline glitches.
- **Bespoke Emblem**: Vector SVG academic gate with towering beacon and open scroll book.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Direct campus context, exam date synchronizers, and hall directories to `SIR Study`.
- **Consumes**: Curated study guides and cram sheets from `SIR Study`; authentication and UI tokens from `SIR Platform`.
- **Risks**: Unannounced institute timetable revisions; student privacy protection; exam stress friction.

---

## 5. The First 25 Prioritized Tasks

### OH-101 | Academic Timetable D1 Database Schema & Seed Data
- **Files**: `src/db/schema.sql`, `src/db/seeds/curriculum_2026.sql`
- **Steps**: Build SQLite/D1 schema for departments, study years, sections, courses, professors, and halls; seed with CS Year 2 schedule.
- **Acceptance**: Queries return complete weekly timetable for any selected student section in under 5ms.

### OH-102 | Interactive Semester Schedule Calendar & Hall Navigator
- **Files**: `src/components/schedule/WeeklyScheduleView.tsx`
- **Steps**: Render responsive timetable grid with day/week views; highlight current active lecture based on Cairo local time.
- **Acceptance**: Active ongoing lecture card pulses subtly in emerald with time remaining indicator.

### OH-103 | Egyptian Higher Education GPA Simulator & Target Calculator
- **Files**: `src/components/gpa/GpaCalculator.tsx`, `src/lib/gpaMath.ts`
- **Steps**: Build interactive GPA calculator: input past credits and target cumulative GPA; calculate minimum grades needed in current courses.
- **Acceptance**: Dynamically computes required letter grades (e.g. "Needs 3 As and 1 B+ to reach 3.4 GPA").

### OH-104 | Lecture Hall & Campus Building Interactive Locator
- **Files**: `src/components/campus/HallDirectory.tsx`
- **Steps**: Searchable campus directory with hall numbers (e.g., Hall 533), building floors, lab locations, and walking directions.
- **Acceptance**: Typing "533" displays Floor 5, Main Academic Building with floorplan schematic.

### OH-105 | Official Professor Office Hours & Academic Contact Directory
- **Files**: `src/components/faculty/FacultyDirectory.tsx`
- **Steps**: Verified faculty listing with department titles, official office hours, and academic email addresses.
- **Acceptance**: Allows filtering faculty by department with 1-tap copy of academic email.

### OH-106 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Implement Dynamic Island tab bar where only active tab reveals label, while inactive tabs collapse to monochrome SVG icons.
- **Acceptance**: Inactive tabs show icons; active tab expands text label cleanly on 390px mobile and desktop.

### OH-107 | Lecture Cancellation & Urgent Notice Real-Time Banner
- **Files**: `src/components/notices/UrgentNoticeBanner.tsx`
- **Steps**: Dynamic Island announcement banner displaying verified administration notices and weather cancellations.
- **Acceptance**: High-priority notices render with amber/emerald pill and animated dismissal.

### OH-108 | Offline First PWA Schedule Caching Service Worker
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache complete semester timetable, hall maps, and GPA tool for 100% offline access during campus cellular dead-zones.
- **Acceptance**: App functions completely offline in Airplane mode without network errors.

### OH-109 | Absence & Attendance Threshold Warning Tracker
- **Files**: `src/components/attendance/AttendanceTracker.tsx`
- **Steps**: Allow students to log course absences; calculate remaining allowed absences before deprivation penalty (25% threshold).
- **Acceptance**: Course card warns in red when absences reach 3 out of 4 allowed lectures.

### OH-110 | Cross-Project Bridge to SIR Study Guides
- **Files**: `src/components/courses/StudyGuideLink.tsx`
- **Steps**: For every enrolled course, embed direct deep-link into `SIR Study` interactive cram sheets and exam simulators.
- **Acceptance**: Tapping "SAD Study Pack" navigates directly to `http://127.0.0.1:3300/sad.html`.

### OH-111 | Academic Exam Timetable Countdown Hero
- **Files**: `src/components/exams/ExamCountdownHero.tsx`
- **Steps**: Visual hero banner displaying upcoming final/midterm exam dates, times, hall assignments, and second-by-second countdown.
- **Acceptance**: Highlights immediate upcoming exam with hall number and remaining study days.

### OH-112 | Bespoke Vector SVG Campus Emblem & Logo Suite
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Author vector SVG academic gate with beacon star; generate multi-size favicons and PWA icons.
- **Acceptance**: Crisp vector rendering across mobile home screens and desktop navigation.

### OH-113 | Student Course Review & Difficulty Rating Benchmark
- **Files**: `src/components/courses/CourseReviewCard.tsx`
- **Steps**: Aggregated anonymous course difficulty metrics (effort hours, math intensity, lab workload) based on student surveys.
- **Acceptance**: Displays visual difficulty breakdown with verified student advice snippets.

### OH-114 | Personal Academic Task & Assignment Reminder Board
- **Files**: `src/components/tasks/AssignmentBoard.tsx`
- **Steps**: Lightweight Kanban board for course assignments, lab deliverables, and project milestones with deadline tags.
- **Acceptance**: Allows adding tasks with deadline date and priority tags with local persistence.

### OH-115 | Academic Transcript PDF Parser & Auto-Populate Lab
- **Files**: `src/lib/transcriptParser.ts`
- **Steps**: Parse exported student portal grade transcripts locally in browser (PDF/HTML); auto-populate completed courses and GPA.
- **Acceptance**: Uploading portal transcript populates course history with 100% grade accuracy.

### OH-116 | Dark & Daylight Architectural Glass Theme Engine
- **Files**: `src/hooks/useCampusTheme.ts`
- **Steps**: Zero-flash theme switcher syncing with system dark mode; daylight mode uses crisp high-contrast emerald/slate.
- **Acceptance**: Daylight mode provides 7:1+ contrast ratio for direct sunlight campus usage.

### OH-117 | Student Section & Cohort Custom Filter
- **Files**: `src/components/schedule/SectionSelector.tsx`
- **Steps**: Filter schedule instantly by department (CS, Eng, Business), Year (1-4), and Section (A, B, C, D).
- **Acceptance**: Switching section immediately updates calendar view without page reload.

### OH-118 | Telegram Daily Schedule Alert Bot Bridge
- **Files**: `scripts/telegram_schedule_bot.py`
- **Steps**: Connect to `@PersonalAI_1Bot` to send daily morning schedule alert to students with their specific day's lecture sequence.
- **Acceptance**: Morning notification delivers list of today's halls and times at 07:30 AM Cairo time.

### OH-119 | Campus Library Book Availability & Catalog Checker
- **Files**: `src/components/library/BookCatalog.tsx`
- **Steps**: Searchable catalog of textbooks available in Obour Institute physical library with shelf codes.
- **Acceptance**: Query returns book title, author, edition, and exact shelf reference.

### OH-120 | End-of-Semester Grade Appeal & Review Runbook Guide
- **Files**: `src/components/guidance/GradeAppealGuide.tsx`
- **Steps**: Step-by-step procedural guide explaining formal institute grade re-check regulations, fees, deadlines, and forms.
- **Acceptance**: Interactive step checklist with downloadable official appeal form template.

### OH-121 | Peer Study Group Meeting Room Coordination Board
- **Files**: `src/components/groups/StudyGroupCoordinator.tsx`
- **Steps**: Lightweight board allowing classmates to propose public study sessions in cafeteria or designated library zones.
- **Acceptance**: Posts show subject, location, and start time with 1-tap "I'm attending" counter.

### OH-122 | Multi-Screen Responsive Layout Verification (320px to 4K)
- **Files**: `tests/responsive_audit.test.mjs`
- **Steps**: Automated Playwright test verifying zero horizontal overflow and zero button clipping across 6 viewports.
- **Acceptance**: All viewports pass with zero horizontal scrollbar.

### OH-123 | Privacy-Preserving Zero-Telemetry Local Storage Mode
- **Files**: `src/lib/privacyGuard.ts`
- **Steps**: Store all GPA calculations, personal course notes, and absence logs strictly on device via IndexedDB; zero analytics tracking.
- **Acceptance**: Network tab confirms zero telemetry pings emitted during student app usage.

### OH-124 | Export Semester Timetable to Apple/Google Calendar (.ics)
- **Files**: `src/lib/icsExporter.ts`
- **Steps**: Generate standard RFC 5545 `.ics` file containing all recurring lectures for selected section with hall locations and alarm reminders.
- **Acceptance**: Clicking "Add to Calendar" imports complete recurring schedule into phone calendar.

### OH-125 | End-to-End Automated Campus Hub Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_obour_hub.py`
- **Steps**: Run linter, strict TypeScript typecheck, GPA math test suites, and schedule rendering tests.
- **Acceptance**: `verify.ps1` runs in under 2 seconds with 100% green gates.
