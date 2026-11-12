# DEEP PLAN & MASTER SPEC: SIR Content Creation Studio
**Project**: SIR Content Creation Studio (`D:/Projects/SIR Content Creation Studio`)  
**Mission**: Autonomous Programmatic Video Production, Motion Graphics & Social Media Syndication Engine  
**Flagship Channel**: ByteVibeHQ (Instagram Reels, TikTok, YouTube Shorts, Reddit, Facebook, X)  
**Safety & Compliance Invariant**: Official APIs and schedulers first; never script X directly (Tier 3 policy)  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Content Creation Studio is an autonomous programmatic video generation studio and multi-platform social media syndication engine. Engineered to power Ahmed's ByteVibeHQ media properties, it automates script generation, high-fidelity neural voiceover synthesis, kinetic typography with word-level karaoke highlighting, programmatic FFmpeg visual layering, and multi-channel publication across short-form vertical video networks (TikTok, Reels, Shorts) and community hubs (Reddit, Facebook, X).

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Content Creation Studio/legacy/`)
- **`SIR Content Creation Studio (v1)`**: Python and Node.js command-line scripts running local FFmpeg commands, Whisper subtitle alignment, ElevenLabs/gTTS voiceover generation, and rudimentary social posting bots.

### 2.2 What is Valuable to Port
- **FFmpeg Programmatic Video Compositor**: Robust bash/PowerShell FFmpeg filtergraphs for 9:16 vertical video formatting, dynamic background blur, audio ducking (-14 LUFS), and animated progress bars.
- **Word-Level Subtitle Alignment Algorithm**: Timestamp extraction from Whisper model output for synchronized kinetic caption styling.
- **ByteVibeHQ Multi-Platform Scheduler Schema**: Data models tracking content calendar, scheduled publish times, post copy variants, hashtags, and engagement metrics.

### 2.3 What Must Be Discarded
- Brittle Selenium/Puppeteer scripts attempting to automate X/Twitter web interfaces (violates workspace security rule 21 and Tier 3 safety boundaries).
- Hardcoded expired social media session cookies and leaked webhook tokens.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Frontend**: Next.js 14 App Router, Web Audio API, Canvas video preview, Dynamic Island spring engine.
- **Rendering Subsystem**: Local Node.js + Python hardware-accelerated FFmpeg pipeline utilizing Nvidia NVENC (`h264_nvenc`) for high-speed rendering.
- **Voice & Audio Pipeline**: Offline neural speech synthesis via `AI_Models_Hub` (piper-tts / local Whisper) with background music ducking.
- **Syndication Bridge**: Official platform APIs (Meta Graph API for Instagram/Facebook, TikTok Content Posting API, YouTube Data API v3) with human-in-the-loop approval before publication.

### 3.2 Design Identity
- **Brand Aesthetic**: Neon Cyber Studio & Kinetic Crimson. Dynamic, cinematic, fluid, and high-impact.
- **Palette**:
  - Primary Kinetic Crimson: `#E11D48` (Rose 600) / `#BE123C` (Rose 700)
  - Secondary Neon Violet: `#8B5CF6` (Violet 500)
  - Dark Surface Base: Deep Studio Obsidian (`#0A060E` / `#130D1B`)
  - Elevated Glass: Translucent Studio Glass (`rgba(19, 13, 27, 0.75)` with `backdrop-filter: blur(16px)`)
  - High-Contrast Text: `#FFF1F2`
  - **Zero Yellow Buttons**: Action buttons strictly use crimson, violet, and slate tokens.
- **Typography**: Cinematic bold typography (`Inter`, `Cairo`, `Bebas Neue` for punchy video headlines).
- **Motion Personality**: Kinetic spring physics (`cubic-bezier(0.16, 1, 0.3, 1)`), tactile timeline scrubbers, active-only tab labels.
- **Bespoke Emblem**: Vector SVG cinematic camera aperture with pulsing central play prism.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Automated promotional video and release changelog clips to `SIR Portfolio` and `SIR Jobs`.
- **Consumes**: Speech synthesis from `SIR AI`; media storage and auth from `the shared kit`.
- **Risks**: Social media API rate limits and shadow-bans if posting frequency is too aggressive; NVENC GPU rendering contention during gaming.

---

## 5. The First 25 Prioritized Tasks

### CS-101 | Hardware-Accelerated FFmpeg 9:16 Render Engine
- **Files**: `src/render/ffmpeg_pipeline.py`, `src/render/nvenc_check.py`
- **Steps**: Build Python FFmpeg pipeline utilizing Nvidia NVENC (`-c:v h264_nvenc`) with auto-fallback to CPU libx264; render 1080x1920 at 60fps.
- **Acceptance**: Renders 60-second 1080p vertical video in under 15 seconds using GPU acceleration.

### CS-102 | Kinetic Typography Subtitle Generator with Word-Level Highlighting
- **Files**: `src/render/subtitle_generator.py`, `src/render/ass_styler.py`
- **Steps**: Generate Advanced SubStation Alpha (`.ass`) subtitle files with custom font (`Bebas Neue`), yellow/cyan active word highlight, and bounce animation.
- **Acceptance**: Produces stylish subtitle tracks where spoken word pops with spring scale on screen.

### CS-103 | Background Audio Normalization & Voice Ducking Engine
- **Files**: `src/render/audio_mixer.py`
- **Steps**: Mix background lo-fi music track with speech voiceover; apply `sidechaincompress` filter ducking music by 12dB during vocal presence.
- **Acceptance**: Voiceover is crisp and dominant (-14 LUFS) while music swells smoothly during pauses.

### CS-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Deploy unified tab bar (Studio, Timeline, Scripts, Media, Calendar) displaying text label only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### CS-105 | Interactive In-Browser HTML5 Canvas Timeline Scrubber
- **Files**: `src/components/timeline/VideoTimeline.tsx`, `src/components/timeline/TrackItem.tsx`
- **Steps**: Multi-track visual timeline (Video, B-Roll, Subtitles, Voice, Music) with draggable start/end handles and frame-accurate scrubber.
- **Acceptance**: Dragging playhead updates preview canvas frame with zero audio desync.

### CS-106 | ByteVibeHQ High-Conversion Script Generator
- **Files**: `src/generators/script_generator.py`, `src/prompts/viral_hooks.json`
- **Steps**: Script drafter structuring 60-second shorts: (1) 3s psychological hook, (2) 15s problem setup, (3) 30s demonstration, (4) 12s call to action.
- **Acceptance**: Generates structured 3-part script with estimated reading duration in words/second.

### CS-107 | Meta Graph API (Instagram Reels & Facebook) Publisher
- **Files**: `src/publishers/meta_publisher.py`
- **Steps**: Official Meta Graph API integration: upload video container, query status, and publish Reels with caption, cover, and hashtags.
- **Acceptance**: Successfully publishes video container to test page and returns permanent permalink URL.

### CS-108 | TikTok Content Posting API Direct Integration
- **Files**: `src/publishers/tiktok_publisher.py`
- **Steps**: Implement TikTok direct post API with OAuth token refresh and creator privacy settings.
- **Acceptance**: Dispatches video upload and returns TikTok post verification ID.

### CS-109 | YouTube Shorts Direct API Uploader & Metadata Optimizer
- **Files**: `src/publishers/youtube_publisher.py`
- **Steps**: Upload short-form video via YouTube Data API v3; inject `#Shorts` tag, category ID, and SEO tags.
- **Acceptance**: Uploads video in unlisted or public state with verified monetization flags.

### CS-110 | Reddit Video & Community Publisher Engine
- **Files**: `src/publishers/reddit_publisher.py`
- **Steps**: Authenticated PRAW Reddit client publishing video posts to targeted subreddits with tailored flair and discussion comment.
- **Acceptance**: Posts video to designated subreddit and returns submission URL.

### CS-111 | X (Twitter) Official Media V2 API Uploader
- **Files**: `src/publishers/x_publisher.py`
- **Steps**: Chunked media upload via official Twitter API v2 (`media/upload`); attach video to tweet with thread formatting; zero web scraping.
- **Acceptance**: Uploads chunked MP4 and posts tweet with verified media ID.

### CS-112 | Bespoke Vector SVG Studio Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design vector camera aperture with central play prism; generate multi-size favicons and PWA icons.
- **Acceptance**: Crisp vector rendering across mobile PWA and desktop studio header.

### CS-113 | Stock B-Roll Video Ingestion & Smart Tagging Library
- **Files**: `src/media/stock_manager.py`, `src/components/media/MediaLibrary.tsx`
- **Steps**: Download, organize, and tag royalty-free B-roll clips (Pexels / Pixabay / Local stock) indexed by semantic mood (Coding, Gaming, Coffee, Urban).
- **Acceptance**: Search query "typing" returns matching tagged B-roll clips with 1-click timeline insert.

### CS-114 | Dynamic Animated Progress Bar & Hook Timer Overlay
- **Files**: `src/render/overlay_elements.py`
- **Steps**: Programmatic FFmpeg filter drawing kinetic progress bar along bottom edge and "Wait for it..." pulse pill during first 3 seconds.
- **Acceptance**: Rendered video includes smooth horizontal progress indicator synchronized to duration.

### CS-115 | Multi-Variant A/B Test Headline & Thumbnail Generator
- **Files**: `src/generators/thumbnail_generator.py`
- **Steps**: Generate 3 distinct high-contrast thumbnail variants with bold text overlays and face cutouts via Pillow / SVG.
- **Acceptance**: Produces 3 export-ready 1080x1920 JPG thumbnails with distinct title hooks.

### CS-116 | Content Calendar Drag-and-Drop Scheduling Matrix
- **Files**: `src/components/calendar/ContentCalendar.tsx`
- **Steps**: Interactive monthly calendar showing scheduled posts across platforms with color-coded network icons.
- **Acceptance**: Dragging post card between calendar days updates scheduled publication timestamp.

### CS-117 | Safe Human-in-the-Loop 1-Tap Mobile Review Flow
- **Files**: `src/components/review/MobileReviewModal.tsx`, `scripts/notify_review.py`
- **Steps**: Before any post is published, dispatch Telegram review message with video preview and "Approve / Edit / Cancel" buttons to Ahmed's iPhone.
- **Acceptance**: Post remains in "Awaiting Approval" state until Ahmed taps Approve on his phone.

### CS-118 | Split-Screen Reaction / Duet Video Compositor
- **Files**: `src/render/duet_compositor.py`
- **Steps**: Composite two video feeds (original video top 50%, creator reaction bottom 50%) with synchronized audio and border styling.
- **Acceptance**: Outputs clean 9:16 vertical split video with centered framing.

### CS-119 | Multi-Screen Responsive Studio Verification (320px to 4K)
- **Files**: `tests/responsive_studio.test.mjs`
- **Steps**: Playwright tests verifying studio timeline, media drawers, and calendar across 320px mobile to 4K desktop.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### CS-120 | Analytics & Engagement Velocity Harvester
- **Files**: `src/analytics/engagement_tracker.py`
- **Steps**: Hourly cron harvesting views, likes, shares, and comments across published posts; compute 24-hour velocity score.
- **Acceptance**: Dashboard displays real view counts and retention curves without invented numbers.

### CS-121 | Offline First Local Asset Caching PWA
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache video editor interface, stock audio chimes, and scripts offline for zero-latency local drafting.
- **Acceptance**: Studio launches instantly offline and allows editing local project timelines.

### CS-122 | Dark Studio & High-Key Daylight Theme Engine
- **Files**: `src/hooks/useStudioTheme.ts`
- **Steps**: Zero-flash theme switcher; daylight mode optimized for color-accurate video grading and subtitle proofreading.
- **Acceptance**: Switching theme updates CSS variables instantly with zero white flash.

### CS-123 | Automated Copyright & Content ID Audio Safety Scanner
- **Files**: `src/render/copyright_guard.py`
- **Steps**: Verify all background audio against known public domain / creative commons whitelist to prevent DMCA strikes.
- **Acceptance**: Blocks render if audio track is not tagged with verified commercial license.

### CS-124 | GPU NVENC Stress Test & Hardware Thermal Sentinel
- **Files**: `src/render/hardware_sentinel.py`
- **Steps**: Check Nvidia GPU temperatures before batch renders; pause export if GPU core temperature exceeds 82°C.
- **Acceptance**: Protects laptop hardware by throttling video encoding during high-heat conditions.

### CS-125 | End-to-End Automated Studio Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_studio_integrity.py`
- **Steps**: Validate FFmpeg filtergraph syntax, video codecs, social publisher schemas, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.


---

## 5. Mandatory Standards 24 to 27 Architecture

### 5.1 Launch Package (Standard 24)
- **Identity & Domain**: Fresh dedicated repository (`sirahmed8/sir-content-creation-studio`), clean backend, target domain `sircreator.studio` or `sircontent.io` (~$20.00 / ~950 EGP/yr).
- **Supported Platforms & Build Commands**:
  - Web & PWA: `npm run build` (Next.js 15 static + SSR).
  - Desktop (Windows / macOS): `npm run tauri build` (Tauri v2 with local NVENC GPU access).
  - Mobile: PWA for approving drafts and viewing analytics (`npx cap sync && npx cap build`).
- **Security Tasks**:
  - Encrypted storage of social media OAuth2 refresh tokens using AES-256.
  - Strict compliance with Meta Graph API and YouTube Data API v3 terms; zero unauthorized scraping of X.
  - Rate limiting on rendering endpoints: max 5 concurrent renders per subscriber.
- **Fair EGP Subscription Model**:
  - Free Tier: 3 free video exports / month with watermarked corner badge.
  - Creator Pro Plan: 290 EGP / month or 2,900 EGP / year.
  - Payment Gateway: Paymob (Cards, Mobile Wallets: Vodafone Cash, Meeza) and Fawry.
  - Fallback Mode: When live payment keys are missing, displays "Subscriptions Launching Soon - Join Waitlist" with email capture.
- **Owner Activation Checklist (Plain Arabic & English for Ahmed)**:
  1. Buy domain `sircreator.studio` on Namecheap (~$20.00 / 950 EGP) and point DNS to Vercel.
  2. Create Meta Developer App (Instagram Graph API) and Google Cloud Project (YouTube Data API v3).
  3. Paste Client IDs and Secrets into `D:\Projects\SIR Content Creation Studio\.env`.
  4. Verify: Import a 30s test video, generate kinetic subtitles, export MP4, verify render completes in < 15s.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `_SIR/plans/competitors/sir-content-creation-studio.md` with cited sources comparing against Opus Clip, CapCut Pro, Buffer, and InVideo.
- **Regional Regulatory & Copyright Compliance**:
  - Full compliance with Egyptian Data Protection Law 151/2020 and Egyptian Intellectual Property Rights Law 82/2002.
  - Fair use guidelines for automated quote videos; copyright-free commercial audio licensing.
- **Privacy-First Analytics**: Opt-in anonymized telemetry measuring rendering latency and format popularity; zero creator script content or private raw footage uploaded to third parties.
- **Legal Pack with Lawyer Disclaimer**: Pre-drafted Terms of Service, Acceptable Use Policy, and Privacy Policy, marked: *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian attorney before commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "مساعد المونتاج وصانع المحتوى" - embedded support assistant grounded in social media video dimensions, subtitle formatting, and export presets.
- **Operations Runbook**: Nightly temporary video cache cleanup, automated token refresh daemons, error log digests, and health check route (`/api/status`).
- **12-Week Marketing Launch Calendar**: Creator waitlist (Weeks -2 to 0), YouTube Shorts case study series (Weeks 1 to 4), podcaster partnership outreach (Weeks 5 to 8), regional creator affiliate program (Weeks 9 to 12).
- **Escalation & Guard Rails**: Maximum daily external AI spend capped at $3.00/day. Chairman notified via Telegram bot ONLY for social API token revocations or video render server errors.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"برنامج مونتاج ذكاء اصطناعي", "عمل فيديوهات ريلز بالذكاء الاصطناعي", "توليد ترجمة متحركة للفيديو"*
  - Egyptian Slang: *"مونتاج ريلز وشورتس أوتوماتيك", "برنامج ترجمة فيديو عربي تلقائي", "أتمتة السوشيال ميديا"*
  - English: *"AI video repurposing tool", "auto subtitle generator Arabic", "short form video automation"*
- **Generative Engine Optimization (GEO)**: Publishes validated `llms.txt` and `/facts` page with structured pricing, export format specs, and entity linking to ByteVibeHQ.
- **Technical SEO & Structured Data**: Pre-rendered Next.js metadata, valid `SoftwareApplication` JSON-LD schema, and automated weekly AI visibility testing script (`scripts/check_ai_visibility.py`).
