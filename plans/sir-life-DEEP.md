# DEEP PLAN & MASTER SPEC: SIR Life
**Project**: SIR Life (`D:/Projects/SIR Life`)  
**Mission**: Sovereign Personal Lifestyle OS, Habit Tracker, Cairo Prayer Sentinel & Reflection Journal  
**Privacy Boundary**: Strictly personal to Ahmed; completely distinct from AHome (zero couple data)  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Life is Ahmed Alaa's personal lifestyle operating system, mindfulness journal, habit tracker, and daily spiritual sentinel. Engineered to operate offline-first with zero cloud telemetry, it tracks personal development habits (hydration, workouts, reading, coding practice), calculates high-precision Islamic prayer times for Cairo with subtle non-intrusive chimes, facilitates concise morning intentions and evening reflections, and maintains long-term goal progression metrics with compassionate streak protection.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Life/legacy/`)
- Historical habit routines, Markdown daily logs, and standalone prayer time calculation scripts.

### 2.2 What is Valuable to Port
- **Egyptian General Authority of Survey Prayer Timing Math**: Astronomical solar position formulas computing Fajr, Dhuhr, Asr, Maghrib, and Isha with Cairo elevation corrections.
- **Compassionate Habit Streak Engine**: Streak counting algorithm supporting planned rest days and compassionate sick-day freezes without breaking momentum.
- **Micro-Journaling Reflection Flow**: 2-minute morning focus ("What 1 thing moves the needle today?") and evening gratitude prompts.

### 2.3 What Must Be Discarded
- Brittle third-party Notion API integrations that broke on network drops.
- Hardcoded calendar files that drifted across years.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Frontend**: Next.js 14 App Router, React 18, Tailwind CSS, Dynamic Island spring engine.
- **Data Persistence**: Offline-first encrypted IndexedDB on client + SQLite local database over loopback and Tailnet.
- **Notifications**: Web Notifications API and Telegram bot alerts via `@PersonalAI_1Bot`.
- **Astronomical Math**: Standalone local math library calculating Cairo solar prayer angles without external network calls.

### 3.2 Design Identity
- **Brand Aesthetic**: Tranquil Serenity & Sacred Horizon. Calming, reflective, tactile, and mindful.
- **Palette**:
  - Primary Tranquil Teal: `#0D9488` (Teal 600) / `#0F766E` (Teal 700)
  - Secondary Amethyst Twilight: `#8B5CF6` (Violet 500)
  - Dark Surface Base: Deep Twilight Obsidian (`#060F0E` / `#0C1817`)
  - Elevated Glass: Translucent Teal Glass (`rgba(12, 24, 23, 0.75)` with `backdrop-filter: blur(14px)`)
  - High-Contrast Text: `#F0FDFA`
  - **Zero Yellow Buttons**: Action buttons strictly use teal, violet, and slate tokens.
- **Typography**: Serene, elegant typography (`Cairo` for Arabic, `Inter` for English, clean serif accents for daily wisdom quotes).
- **Motion Personality**: Dynamic Island breathing spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), gentle pulse glows, active-only tab labels.
- **Emblem**: Vector SVG stylized lotus flower blossoming beneath an illuminated crescent horizon.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Daily wellness status and Pomodoro state to `SIR Laptop Manager` and `SIR Study`.
- **Consumes**: Morning briefing automation from `SIR AI`; owner authentication from `SIR Platform`.
- **Risks**: Habit tracker anxiety and guilt if streaks reset too harshly; prayer time calculation drift if astronomical formulas lack Cairo survey offsets.

---

## 5. The First 25 Prioritized Tasks

### LF-101 | Offline Cairo Astronomical Prayer Timing Engine
- **Files**: `src/lib/prayerMath.ts`, `src/lib/cairoSurveyMethod.ts`
- **Steps**: Implement Egyptian General Authority of Survey prayer calculation formula (Fajr 19.5°, Isha 17.5°); compute exact daily Cairo prayer schedule offline.
- **Acceptance**: Prayer times match official Cairo Egyptian awqaf timetable within ±30 seconds.

### LF-102 | Dynamic Island Next-Prayer Countdown & Adhan Alert
- **Files**: `src/components/prayer/PrayerIsland.tsx`
- **Steps**: Render mini Dynamic Island pill showing immediate next prayer name, time, and remaining countdown; play soft acoustic chime on Adhan.
- **Acceptance**: Header displays live countdown (e.g. "Asr in 42m"); chimes softly at exact minute.

### LF-103 | Compassionate Habit Tracker & Streak Protection Engine
- **Files**: `src/lib/habitEngine.ts`, `src/components/habits/HabitCard.tsx`
- **Steps**: Track daily habits (Coding, Reading, Hydration, Workout); implement compassionate "Rest Day" freeze preserving streak counters.
- **Acceptance**: Marking habit complete fills radial progress ring with spring bounce animation.

### LF-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Unified navigation bar (Today, Habits, Reflection, Prayer, Milestones) displaying text label only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### LF-105 | 2-Minute Morning Focus & Evening Gratitude Journal
- **Files**: `src/components/journal/ReflectionCard.tsx`
- **Steps**: Streamlined journaling interface: 3 morning intention bullets and 3 evening gratitude highlights with instant save.
- **Acceptance**: Entries save instantly to encrypted local IndexedDB with daily timeline scroll.

### LF-106 | Hydration Water Intake Tracker with Acoustic Drop Chime
- **Files**: `src/components/habits/HydrationTracker.tsx`
- **Steps**: Visual water glass animation; 1-tap `+250ml` button fills glass with fluid spring physics and soft water droplet audio chime.
- **Acceptance**: Tracks daily intake towards 3,000ml goal with visual wave fill animation.

### LF-107 | Cairo Daily Fasting (Suhoor & Iftar) Countdown Hero
- **Files**: `src/components/prayer/FastingCountdown.tsx`
- **Steps**: During Ramadan or voluntary fasting days (Mondays/Thursdays), display visual hero banner tracking remaining hours until Iftar.
- **Acceptance**: Shows exact sunset timestamp and remaining minutes with serene dusk gradient.

### LF-108 | Bespoke Vector SVG Lotus & Horizon Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design blooming lotus flower beneath crescent horizon; render multi-size favicons and PWA icons.
- **Acceptance**: Crisp vector rendering across mobile PWA and desktop header.

### LF-109 | Daily Islamic Duaa & Dhikr Counter (Tasbeeh Lab)
- **Files**: `src/components/prayer/TasbeehCounter.tsx`
- **Steps**: Haptic-enabled digital Tasbeeh counter (33x SubhanAllah, Alhamdulillah, AllahuAkbar) with full-screen tap target.
- **Acceptance**: Tapping phone screen vibrates subtly and increments count with smooth circular progress indicator.

### LF-110 | Spaced Work & Deep Focus Pomodoro Timer
- **Files**: `src/components/focus/PomodoroTimer.tsx`
- **Steps**: Dynamic Island 50/10 deep focus timer with white noise / rain soundscapes; integrates with `SIR Study` sessions.
- **Acceptance**: Timer runs silently in background and chimes softly on cycle completion.

### LF-111 | Weekly Habit Mastery & Consistency Radar Heatmap
- **Files**: `src/components/analytics/HabitHeatmap.tsx`
- **Steps**: GitHub-style green contribution heatmap showing habit completion consistency over the past 52 weeks.
- **Acceptance**: Visual grid renders 365 days of habit data with tooltip completion percentages.

### LF-112 | Sleep Schedule & Circadian Rhythm Optimizer
- **Files**: `src/components/wellness/SleepTracker.tsx`
- **Steps**: Track sleep/wake times; calculate completed 90-minute REM sleep cycles; recommend optimal bedtime for chosen wakeup hour.
- **Acceptance**: Selecting "Wake at 06:00 AM" highlights bedtimes (10:30 PM, 12:00 AM) aligned to 90m sleep cycles.

### LF-113 | Long-Term Sovereign Life Goals & Milestone Compass
- **Files**: `src/components/goals/GoalCompass.tsx`
- **Steps**: Hierarchy for quarterly and annual goals with progressive milestone check-ins and visual progress bars.
- **Acceptance**: Goal card links individual daily habits to broader milestone objectives.

### LF-114 | Digital Detox Screen Time & Eye Rest (20-20-20 Rule)
- **Files**: `src/components/wellness/EyeRestTimer.tsx`
- **Steps**: Background eye-rest reminder triggering every 20 minutes of continuous screen work to look 20 feet away for 20 seconds.
- **Acceptance**: Non-intrusive Dynamic Island pill expands softly reminding user to rest eyes.

### LF-115 | Telegram Daily Intention & Reflection Dispatcher
- **Files**: `scripts/telegram_life_bot.py`
- **Steps**: Scheduled morning prompt sent via `@PersonalAI_1Bot` asking for today's 1 priority, and evening prompt at 21:00 for reflection.
- **Acceptance**: Replying to Telegram message records reflection text directly into local journal.

### LF-116 | Multi-Screen Responsive Verification (320px to 4K)
- **Files**: `tests/responsive_life.test.mjs`
- **Steps**: Playwright tests verifying habit cards, prayer countdowns, and journal modals across 5 viewports.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### LF-117 | Full-Text Encrypted Journal Search Engine
- **Files**: `src/lib/journalSearch.ts`
- **Steps**: Client-side encrypted search index over historical reflections; search by keyword, mood, or tag in under 30ms.
- **Acceptance**: Typing "focus" instantly highlights past reflections mentioning the term.

### LF-118 | Offline First PWA Service Worker Engine
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache entire lifestyle suite offline; allow logging habits and reading journal entries with zero internet connectivity.
- **Acceptance**: App functions completely offline in Airplane mode without network errors.

### LF-119 | Tranquil Twilight & High-Key Daylight Theme Engine
- **Files**: `src/hooks/useLifeTheme.ts`
- **Steps**: Zero-flash theme switcher; daylight mode optimized for outdoor morning reading with high contrast.
- **Acceptance**: Theme switch triggers with zero white flash and updates all CSS variables.

### LF-120 | Mood & Energy Level Correlator Analytics
- **Files**: `src/components/analytics/MoodCorrelator.tsx`
- **Steps**: Correlate logged daily energy levels (1-5) against sleep hours and completed workout habits.
- **Acceptance**: Renders insight cards (e.g. "Energy is 35% higher on days with 3L water and 7.5h sleep").

### LF-121 | Monthly Personal Life Operating Review PDF Generator
- **Files**: `scripts/generate_monthly_life_pdf.py`
- **Steps**: Automated script compiling monthly habit consistency, completed goals, and highlighted reflections into a beautiful 2-page PDF.
- **Acceptance**: Generates printable PDF review archive on the 1st of every month.

### LF-122 | Voice Memo Audio Reflection Note Ingestion
- **Files**: `src/components/journal/AudioJournal.tsx`
- **Steps**: Record 60-second audio reflections directly into journal; transcribes via local Whisper model from `AI_Models_Hub`.
- **Acceptance**: Recorded voice reflection saves audio blob and displays local transcript.

### LF-123 | Qibla Compass Direction Finder Lab
- **Files**: `src/components/prayer/QiblaCompass.tsx`
- **Steps**: Device orientation sensor compass pointing directly towards Makkah coordinates (`21.4225° N, 39.8262° E`) relative to Cairo.
- **Acceptance**: Rotating phone smoothly rotates needle pointing towards Kaaba bearing.

### LF-124 | Silent Windows Logon Scheduled Task Installer
- **Files**: `scripts/install-autostart.ps1`, `scripts/dev-start.vbs`
- **Steps**: Register `SIR_Life_Server` scheduled task running windowless via `pythonw.exe` on user login.
- **Acceptance**: Companion service launches headlessly on boot with zero console windows.

### LF-125 | End-to-End Automated Life Suite Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_life_integrity.py`
- **Steps**: Validate prayer calculation accuracy, habit streak math, encryption invariants, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 2 seconds with 100% green gates.


---

## 5. Mandatory Standards 24 to 27 Architecture

### 5.1 Launch Package (Standard 24)
- **Identity & Domain**: Fresh dedicated repository (`sirahmed8/sir-life`), clean architecture, target domain `sirlife.app` (~$12.00 / ~550 EGP/yr).
- **Supported Platforms & Build Commands**:
  - Web & PWA: `npm run build` (Next.js 15 App Router static + SSR).
  - Mobile (Android / iOS): `npx cap sync && npx cap build` (Capacitor PWA shell).
  - Watch (Wear OS / watchOS): Glance tile showing next prayer countdown and daily habit progress ring.
- **Security & Privacy Tasks**:
  - Zero Ads, Zero Location Data Tracking: Calculation runs completely offline using mathematical coordinates for Cairo/Giza.
  - Client-side AES-256 encryption for personal journal entries.
  - Complete data ownership: 1-click JSON data export and irreversible database wipe.
- **Fair EGP Commercial Model**:
  - 100% Free Core Tier: Full offline habit tracking, prayer times, fasting hero, and journal sheets.
  - Pro Cloud Sync Tier: 99 EGP / year.
  - Payment Gateway: Paymob (Cards, Mobile Wallets, Meeza) and Stripe.
  - Fallback Mode: When live payment keys are missing, displays "Sync Features Launching Soon - 100% Free During Beta".
- **Owner Activation Checklist (Plain Arabic & English for Ahmed)**:
  1. Buy domain `sirlife.app` on Namecheap (~$12.00 / 550 EGP) and point DNS to Vercel.
  2. Paste Paymob keys into `D:\Projects\SIR Life\.env`.
  3. Verify: Open web app, tick a habit, verify prayer time displays within 60s of Egyptian Survey Authority schedule.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `_SIR/plans/competitors/sir-life.md` with cited sources comparing against Streaks, Fabulous, Habitica, and Muslim Pro.
- **Regional Regulatory Compliance**:
  - Full compliance with Egyptian Data Protection Law 151/2020.
  - Medical Limitation Disclaimer: Habits and eye rest guides do not constitute certified medical treatment.
- **Privacy-First Analytics**: Opt-in anonymized telemetry measuring app launch frequency and error rates; zero journal text or habit names captured.
- **Legal Pack with Lawyer Disclaimer**: Pre-drafted Terms of Service, Wellness Disclaimer, and Privacy Policy, marked: *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian attorney before commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "مساعد التوازن والعادات" - embedded support assistant grounded in habit formation science, sleep hygiene, and prayer time calculations.
- **Operations Runbook**: Nightly database snapshots, automated calendar leap year calculations, error log digests, and health check route (`/api/health`).
- **12-Week Marketing Launch Calendar**: Product Hunt teaser (Weeks -2 to 0), Ramadan spiritual preparation launch blitz (Weeks 1 to 4), productivity blogger outreach (Weeks 5 to 8), New Year habit challenge (Weeks 9 to 12).
- **Escalation & Guard Rails**: Maximum daily external AI spend capped at $2.00/day. Chairman notified via Telegram bot ONLY for sync database outages.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"تطبيق متابعة العادات اليومية", "برنامج مواقيت الصلاة بدون إعلانات", "مفكرة يومية وتدوين شخصي"*
  - Egyptian Slang: *"برنامج تنظيم الوقت والعادات بالعامية", "مواقيت الصلاة القاهرة بدون إعلانات رخمة"*
  - English: *"holistic habit tracker app", "ad-free prayer times Cairo", "daily evening reflection journal"*
- **Generative Engine Optimization (GEO)**: Publishes validated `llms.txt` and `/facts` page with structured habit science methodologies, prayer calculation formulas, and entity definitions.
- **Technical SEO & Structured Data**: Pre-rendered Next.js metadata, valid `HealthAndFitnessApplication` JSON-LD schema, and automated weekly AI visibility testing script (`scripts/check_ai_visibility.py`).
