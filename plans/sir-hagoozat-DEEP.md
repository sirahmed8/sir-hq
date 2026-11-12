# DEEP PLAN & MASTER SPEC: SIR Hagoozat
**Project**: SIR Hagoozat (`D:/Projects/SIR Hagoozat`)  
**Mission**: Sovereign Football Pitch Booking, 5v5 Matchmaker & Amateur Tournament Engine  
**Consolidation**: Unifies `Hagoozat Elite`, `11Players`, and `EGFootball5` into one unified platform  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Hagoozat is the definitive football community and facility management platform for amateur footballers and pitch owners across Egypt. By unifying three previously fragmented prototypes (`Hagoozat Elite`, `11Players`, and `EGFootball5`), SIR Hagoozat provides: (1) Instant, race-condition-free pitch reservations across Cairo and Giza, (2) A "Missing 11th Player" squad matchmaking hub, (3) Automated knockout/group-stage tournament bracket orchestration, and (4) An offline-resilient pitch owner cash register and slot management dashboard.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Hagoozat/legacy/`)
1. **`Hagoozat Elite`**: Pitch booking web app with hourly calendar slots, pitch amenities (turf quality, lighting, showers, balls), and booking records.
2. **`11Players`**: Player profile hub, skill ratings, position preferences (GK, DEF, MID, FWD), and public match lobbies for incomplete squads.
3. **`EGFootball5`**: Egyptian 5-a-side tournament tracker with points tables, goal differential math, and yellow/red card discipline ledgers.

### 2.2 What is Valuable to Port
- **Slot Reservation State Machine**: Slot lock with 5-minute checkout reservation hold to eliminate double-booking race conditions.
- **Player Position Matchmaker Algorithm**: Logic matching players searching for games with squads needing specific positions within geographic proximity.
- **Tournament Bracket Engine**: Single-elimination and round-robin scheduling algorithms with automatic tie-break math.
- **Owner Cash & Deposit Reconciliation**: Daily cash receipt logs, online deposit tracking, and refund policies.

### 2.3 What Must Be Discarded
- Unsigned payment callback bypasses (`dev_signature` bypass found in Wave 0 audit).
- Client-side owner authorization checks; all owner actions must validate server-side HMAC tokens.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Frontend**: Next.js 14 App Router, React 18, Tailwind CSS, Dynamic Island spring engine.
- **Backend / DB**: Edge serverless routes with PostgreSQL / Cloudflare D1 with strict row-level ACID transactions for slot reservations.
- **Real-Time Subsystem**: WebSockets / Server-Sent Events (SSE) for live slot availability and tournament scorecards.
- **Security**: Signed webhook verification, rate-limited SMS/WhatsApp OTP verification, and strict zero-trust owner roles.

### 3.2 Design Identity
- **Brand Aesthetic**: Night Match Stadium & Pitch Emerald. Athletic, vibrant, tactile, and competitive.
- **Palette**:
  - Primary Turf Emerald: `#10B981` (Emerald 500) / `#059669` (Emerald 600)
  - Secondary Floodlight Cyan: `#06B6D4` (Cyan 500)
  - Accent Goal Amber: `#F59E0B` (Amber 500)
  - Dark Surface Base: Deep Stadium Obsidian (`#080F0C` / `#0E1A15`)
  - Elevated Cards: Translucent Turf Glass (`rgba(14, 26, 21, 0.75)` with `backdrop-filter: blur(12px)`)
  - **Zero Yellow Buttons**: Action buttons strictly use semantic emerald and slate tokens.
- **Typography**: Dynamic athletic typography (`Inter`, `Cairo`, `Teko` for scoreboard numbers).
- **Motion**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), pitch map expansion, active-only tab labels.
- **Emblem**: Vector SVG geometric football pentagon merged with illuminated stadium floodlight beacon.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Tournament and recreation community hubs to `SIR Life`.
- **Consumes**: Owner authentication and signed webhook verification from `the shared kit`.
- **Risks**: Concurrent slot contention on prime Thursday/Friday evening slots; pitch owners manually overriding online bookings without syncing.

---

## 5. The First 25 Prioritized Tasks

### HZ-101 | Unified PostgreSQL Pitch & Reservation Schema
- **Files**: `src/db/schema.sql`, `src/db/migrations/001_hagoozat_unified.sql`
- **Steps**: Merge schemas from Hagoozat Elite, 11Players, and EGFootball5 into normalized DDL with foreign keys and slot time indices.
- **Acceptance**: Schema compiles cleanly with indexes on `pitch_id`, `date`, `start_time`, and `status`.

### HZ-102 | Atomic Slot Reservation State Machine with 5-Minute Hold
- **Files**: `src/lib/slotLock.ts`, `src/api/slots/reserve.ts`
- **Steps**: Implement database row-level locking (`SELECT ... FOR UPDATE` or conditional atomic write) placing a 5-minute hold during checkout.
- **Acceptance**: Concurrent reservation attempts on same slot result in one reservation and immediate 409 Conflict for second request.

### HZ-103 | Interactive Cairo/Giza Football Pitch Map & Filter
- **Files**: `src/components/map/PitchMap.tsx`, `src/components/map/PitchCard.tsx`
- **Steps**: Build responsive map/list view filtering pitches by neighborhood (Maadi, Tagamoa, Nasr City, Dokki), turf type, and price.
- **Acceptance**: Filtering neighborhood smoothly pans map and updates results cards with zero layout glitch.

### HZ-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Deploy unified tab bar (Pitches, Matchmaker, Tournaments, Dashboard) displaying labels only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### HZ-105 | "Missing Player" 5v5 Squad Matchmaking Hub
- **Files**: `src/components/matchmaker/MatchLobby.tsx`
- **Steps**: Matchmaking feed where squad captains post open slots (e.g. "Need 1 Goalkeeper tonight 9 PM at Maadi Olympic"); players join with 1 tap.
- **Acceptance**: Player can filter by position and join match; captain receives push alert with player rating.

### HZ-106 | WhatsApp Team Invite & Match Confirmation Link
- **Files**: `src/lib/whatsappInvite.ts`
- **Steps**: Generate formatted WhatsApp invite link detailing pitch address, Google Maps link, kickoff time, and individual share cost (EGP).
- **Acceptance**: Tapping "Invite Squad" opens WhatsApp with pre-filled message and RSVP deep link.

### HZ-107 | Automated Knockout & Group Stage Tournament Bracket Engine
- **Files**: `src/lib/tournamentBrackets.ts`, `src/components/tournament/BracketTree.tsx`
- **Steps**: Generate interactive SVG bracket trees for 8, 16, and 32 teams; compute winners, goal differentials, and automatic round advances.
- **Acceptance**: Entering match score automatically advances winner to next bracket node with spring animation.

### HZ-108 | Pitch Owner Daily Cash Register & Offline Booking Ledger
- **Files**: `src/components/owner/OwnerDashboard.tsx`, `src/lib/offlineLedger.ts`
- **Steps**: Dedicated offline-first tablet dashboard for pitch managers to log walk-in cash payments and block maintenance hours.
- **Acceptance**: Offline cash bookings sync seamlessly to central server when network restores.

### HZ-109 | Signed Webhook Security & Payment Gate
- **Files**: `src/api/webhooks/payment.ts`
- **Steps**: Implement strict HMAC-SHA256 signature verification on payment callbacks (Fawry/InstaPay/Paymob); eliminate all legacy bypasses.
- **Acceptance**: Rejects unsigned or tampered webhooks with 401; validates matching order amounts before slot confirmation.

### HZ-110 | Player Skill Rating & Fair Play Karma Engine
- **Files**: `src/lib/playerRating.ts`
- **Steps**: Post-match peer review system where teammates rate skill (1-5) and reliability/punctuality; calculates player Fair Play score.
- **Acceptance**: Displays player card with verified games played and reliability rating.

### HZ-111 | Hourly Dynamic Pricing & Off-Peak Discount Lab
- **Files**: `src/lib/dynamicPricing.ts`, `src/components/booking/SlotPicker.tsx`
- **Steps**: Allow pitch owners to set variable pricing (e.g., afternoon off-peak 300 EGP vs evening prime 600 EGP).
- **Acceptance**: Slot picker cards render distinct price badges with strikethrough discount pills for off-peak hours.

### HZ-112 | Bespoke Vector SVG Stadium Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design geometric football pentagon with illuminated floodlight beacon; render multi-size favicons and PWA icons.
- **Acceptance**: Crisp vector rendering across mobile PWA and desktop header.

### HZ-113 | Live Match Scoreboard & Goal Scorers Ticker
- **Files**: `src/components/tournament/LiveScoreTicker.tsx`
- **Steps**: Real-time WebSocket ticker displaying live tournament matches, minute-by-minute scores, and goalscorer names.
- **Acceptance**: Score updates push to connected clients in under 200ms without page reload.

### HZ-114 | Pitch Facility Amenities & Photo Carousel
- **Files**: `src/components/pitch/AmenityPills.tsx`, `src/components/pitch/PhotoCarousel.tsx`
- **Steps**: Display verified amenity badges (FIFA-certified turf, LED floodlights, locker rooms, parking, cafeteria) with image lightbox.
- **Acceptance**: Touch-friendly carousel with smooth swipe physics and zero layout jumping.

### HZ-115 | Rain & Extreme Weather Reschedule Voucher Flow
- **Files**: `src/lib/weatherVoucher.ts`
- **Steps**: When rain or storm forces pitch closure, automatically convert cancelled bookings into 30-day rescheduling credit vouchers.
- **Acceptance**: Customer receives SMS voucher code and credits appear in app wallet.

### HZ-116 | Captain Team Roster & Jersey Color Conflict Checker
- **Files**: `src/components/match/JerseyColorChecker.tsx`
- **Steps**: Allow teams to register home/away kit colors; alert captains if competing teams select identical jersey colors.
- **Acceptance**: Displays visual warning ("Both teams in Red; Away team wear bibs").

### HZ-117 | Referee & Match Official Match Log Subsystem
- **Files**: `src/components/referee/MatchScorecardForm.tsx`
- **Steps**: Mobile-optimized referee card for logging goals, yellow/red cards, penalty shootouts, and match incidents.
- **Acceptance**: Submitting scorecard locks final match result and recalculates tournament standings.

### HZ-118 | Split-Bill Calculator for Squad Members
- **Files**: `src/components/booking/SplitBillModal.tsx`
- **Steps**: Dynamic Island modal dividing total pitch fee by squad count (e.g., 600 EGP / 10 players = 60 EGP/person) with InstaPay QR.
- **Acceptance**: Generates formatted InstaPay payment request text with individual share amount.

### HZ-119 | Multi-Screen Responsive Verification (320px to 4K)
- **Files**: `tests/responsive_hagoozat.test.mjs`
- **Steps**: Playwright tests verifying slot grid, player cards, and brackets across 320px, 390px, 768px, 1024px, 1440px viewports.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### HZ-120 | Pitch Owner Revenue & Utilization Analytics
- **Files**: `src/components/owner/UtilizationCharts.tsx`
- **Steps**: Render clean SVG charts showing peak hours, weekly revenue, cancellation rates, and customer retention.
- **Acceptance**: Visual analytics render cleanly without third-party heavy charting libraries.

### HZ-121 | Offline First PWA Service Worker Engine
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache upcoming match bookings, pitch maps, and player passes offline with background sync for match RSVPs.
- **Acceptance**: App launches instantly offline and displays confirmed bookings barcode.

### HZ-122 | Dark Stadium & Floodlight Daylight Theme Engine
- **Files**: `src/hooks/useStadiumTheme.ts`
- **Steps**: Flawless zero-flash theme engine; daylight mode provides maximum contrast for bright afternoon pitch-side usage.
- **Acceptance**: Theme switch triggers with zero white flash and updates all CSS variables.

### HZ-123 | Automated SMS & WhatsApp Match Reminder Routine
- **Files**: `scripts/send_match_reminders.py`
- **Steps**: Scheduled task scanning bookings 2 hours before kickoff; dispatches SMS and Telegram reminder with location pin.
- **Acceptance**: Cron/Task Scheduler sends reminders automatically with accurate Cairo timestamps.

### HZ-124 | Instant QR Code Pitch Entry Pass
- **Files**: `src/components/booking/EntryQrPass.tsx`
- **Steps**: Generate cryptographically signed offline QR pass for confirmed bookings; scanned by pitch manager tablet to confirm entry.
- **Acceptance**: Pitch owner app scans QR code and marks booking as "Arrived" in real time.

### HZ-125 | End-to-End Automated Hagoozat Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_hagoozat_integrity.py`
- **Steps**: Run linter, typecheck, slot race condition simulations, webhook cryptographic checks, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.


---

## 5. Mandatory Standards 24 to 27 Architecture

### 5.1 Launch Package (Standard 24)
- **Identity & Domain**: Fresh dedicated repository (`sirahmed8/sir-hagoozat`), clean Supabase project (`sir-hagoozat-prod`), target domain `hagoozat.com` or `hagoozat.eg` (~$12.00 / ~550 EGP/yr).
- **Supported Platforms & Build Commands**:
  - Web & PWA: `npm run build` (Next.js 15 static + SSR).
  - Mobile (Android / iOS): `npx cap sync && npx cap build` (Capacitor native wrapper).
  - Watch (Wear OS): Glance tile showing upcoming match countdown (`cd wear && ./gradlew assembleRelease`).
  - Car: Skipped for v1 (match navigation route backlog).
- **Security Tasks**:
  - HMAC-SHA256 signature check and 5-minute replay window on all Paymob webhooks.
  - Rate limiting: max 10 booking requests/minute per IP; SMS OTP limited to 3 per hour.
  - Server-side session validation; HttpOnly secure cookies; zero PII in client logs.
- **Fair EGP Subscription Model**:
  - Free for individual players to browse, book, and split payments.
  - Venue Owner Tier: 450 EGP / month or 4,500 EGP / year.
  - Payment Gateway: Paymob (Cards, Mobile Wallets: Vodafone Cash, Orange Money, Etisalat Cash, WE Pay, Meeza) and Fawry.
  - Fallback Mode: When live payment keys are missing, displays "Online Booking Launching Soon - Reserve via WhatsApp" with email capture.
- **Owner Activation Checklist (Plain Arabic & English for Ahmed)**:
  1. Buy domain `hagoozat.com` on Namecheap (~$12.00 / 550 EGP) and point DNS CNAME to Vercel.
  2. Paste Paymob keys into `D:\Projects\SIR Hagoozat\.env`.
  3. Verify: Book test 5 EGP slot via Vodafone Cash, verify booking status changes to Confirmed and WhatsApp ticket arrives.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `_SIR/plans/competitors/sir-hagoozat.md` with cited sources comparing against Playtomic, Malaeb, and Grinta.
- **Regional Regulatory & Tax Compliance**: Complies with Egyptian Data Protection Law 151/2020 and ETA e-receipt v1.0 standard.
- **Privacy-First Analytics**: Opt-in anonymized telemetry tracking venue search volume and booking conversion rates; zero phone numbers or private messages captured.
- **Legal Pack with Lawyer Disclaimer**: Pre-drafted Terms of Reservation, Pitch Cancellation Policy, and Privacy Policy, marked: *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian attorney before commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "كابتن حجوزات" - embedded support assistant grounded in pitch ground rules, cancellation policies, and pitch directions.
- **Operations Runbook**: Nightly database backups, automatic slot lock cleanup daemon, error log digests, and health check route (`/api/health`).
- **12-Week Marketing Launch Calendar**: Pre-launch waitlist (Weeks -2 to 0), Cairo university blitz (Weeks 1 to 4), local sports academy partnerships (Weeks 5 to 8), regional padel tournament sponsorship (Weeks 9 to 12).
- **Escalation & Guard Rails**: Maximum daily external AI spend capped at $3.00/day. Chairman notified via Telegram bot ONLY for double-booking disputes or payment gateway disruptions.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"حجز ملاعب كرة قدم القاهرة", "تطبيق حجز ملاعب بادل", "تأجير ملاعب خماسي"*
  - Egyptian Slang: *"احجز ملعب كورة في دقيقة", "ملاعب كورة قريبة مني", "حجز بادل التجمع"*
  - English: *"football pitch booking Cairo", "padel court rental Egypt", "5v5 soccer turf reservation"*
- **Generative Engine Optimization (GEO)**: Publishes validated `llms.txt` and `/facts` page with structured venue pricing, platform availability, and direct entity definitions.
- **Technical SEO & Structured Data**: Pre-rendered Next.js metadata, valid `SportsApplication` JSON-LD schema, and automated weekly AI visibility testing script (`scripts/check_ai_visibility.py`).
