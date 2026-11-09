# DEEP PLAN & MASTER SPEC: SIR Portfolio
**Project**: SIR Portfolio (`D:/Projects/SIR Portfolio`)  
**Mission**: Sovereign Public Product Wall, Real-Time Engineering Showcase & Developer Portfolio  
**Truth Rule Invariant**: Every project is being rebuilt from zero; zero inflated or unverified claims  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Portfolio is Ahmed Alaa's authoritative public engineering showcase and sovereign portfolio wall. Built to represent Ahmed's actual craft as an ambitious second-year Computer Science student building advanced systems with AI, it adheres strictly to the **Truth Rule**: every project displays its real, honest verification state today (rebuilding from scratch, active prototypes, verified modules), completely eliminating fabricated claims or unverified metrics. It features interactive live demos, technical architecture deep-dives, live GitHub commit telemetry, and downloadable agency-grade CVs.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Portfolio/legacy/`)
- **`sirahmed8`**: Historical GitHub profile repository, static HTML portfolios, earlier Next.js landing pages, and outdated resume text claiming production deployments for legacy prototypes.

### 2.2 What is Valuable to Port
- **High-Contrast Project Showcase Grid**: Responsive visual cards showcasing project emblems, tags, and architectural summaries.
- **Bilingual Arabic/English Toggle**: Instant client-side locale switcher with verified Cairo/Inter typography.
- **Direct Contact Channel Bridges**: Verified links to Ahmed's GitHub (`@sirahmed8`), LinkedIn, and Telegram.

### 2.3 What Must Be Discarded
- Inflated claims claiming old legacy apps are "live commercial products".
- Dead links pointing to abandoned Vercel/Firebase deployments of old merged projects.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Frontend**: Next.js 14 App Router (Static Export / Edge runtime), Tailwind CSS, Dynamic Island spring engine.
- **Data Layer**: Static build-time compilation reading physical project states and git commits directly from `_SIR/ops/` and `_SIR/plans/`.
- **Hosting**: Cloudflare Pages / Vercel with automated GitHub Actions CI deployment.
- **Zero-Telemetry**: No invasive third-party tracking scripts; privacy-preserving aggregated visitor counters.

### 3.2 Design Identity
- **Brand Aesthetic**: Sovereign Luminary & High-Contrast Obsidian. Minimalist, authoritative, architectural, and tactile.
- **Palette**:
  - Primary Sovereign Platinum: `#F8FAFC` (Slate 50)
  - Secondary Electric Sapphire: `#2563EB` (Blue 600)
  - Accent Luminous Cyan: `#06B6D4` (Cyan 500)
  - Dark Surface Base: Deep Void Obsidian (`#06080D` / `#0B0F19`)
  - Elevated Cards: Translucent Slate Glass (`rgba(15, 23, 42, 0.75)` with `backdrop-filter: blur(14px)`)
  - **Zero Yellow Buttons**: Enforced sapphire, platinum, and slate tokens.
- **Typography**: Precision executive typography (`Inter`, `Cairo`, `JetBrains Mono` for tech tags and git hashes).
- **Motion Personality**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), smooth staggered project card entrance, active-only tab labels.
- **Emblem**: Vector SVG sovereign monogram "SA" intersected by a celestial compass star.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Public face, live project links, and authoritative portfolio showcase for all SIR products.
- **Consumes**: Live project statuses and git commit hashes from `SIR Control Room`; CV PDF generator from `SIR Jobs`.
- **Risks**: Stale project statuses displayed if portfolio build is not re-triggered upon product releases.

---

## 5. The First 25 Prioritized Tasks

### PF-101 | Single-Source Portfolio Data Pipeline from `_SIR`
- **Files**: `src/lib/portfolioData.ts`, `scripts/sync_portfolio_data.py`
- **Steps**: Compile project card data directly from `_SIR/ops/PORTFOLIO.md` and `_SIR/plans/*.md` ensuring 100% adherence to Truth Rule.
- **Acceptance**: Renders accurate status badges ("Rebuilt from zero", "Active Wave 2", "In Development") with zero fake claims.

### PF-102 | Interactive Live Project Terminal & Showcase Cards
- **Files**: `src/components/projects/ProjectCard.tsx`, `src/components/projects/ProjectGrid.tsx`
- **Steps**: Render responsive project cards with bespoke vector logos, tech stack badges, architectural summaries, and deep links.
- **Acceptance**: Hovering card triggers subtle spring elevation (`translateY(-4px)`) with glowing border highlight.

### PF-103 | Dynamic Island Active-Only Navigation Bar
- **Files**: `src/components/nav/HeaderIsland.tsx`, `src/app/globals.css`
- **Steps**: Deploy Dynamic Island header (Overview, Projects, Architecture, Writing, Contact) showing labels only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label with zero outline glitch.

### PF-104 | Downloadable Agency-Grade A4 CV Bridge (`SIR Jobs`)
- **Files**: `src/components/hero/ResumeDownloadButton.tsx`
- **Steps**: Link directly to `SIR Jobs` verified A4 CV PDF (`/downloads/Ahmed_Alaa_CV.pdf`) generated via headless Chromium CDP.
- **Acceptance**: Clicking "Download CV" initiates immediate download of verified PDF with accurate student profile.

### PF-105 | Interactive Real-Time GitHub Commit Activity Stream
- **Files**: `src/components/github/CommitTicker.tsx`
- **Steps**: Display live feed of recent verified commits across public SIR repositories with commit messages, relative timestamps, and hashes.
- **Acceptance**: Displays live commit list with clean conventional commit badges (`feat`, `docs`, `fix`).

### PF-106 | Architectural Deep-Dive Case Study Modals
- **Files**: `src/components/case-studies/CaseStudyModal.tsx`
- **Steps**: Dynamic Island spring modal showcasing engineering case studies (e.g. AHome E2EE Vault, Laptop Manager Safe Quarantine).
- **Acceptance**: Clicking "Case Study" opens smooth modal with architecture diagrams and test coverage metrics.

### PF-107 | Bilingual Arabic / English Parity Switcher
- **Files**: `src/lib/i18n.ts`, `src/components/nav/LanguageToggle.tsx`
- **Steps**: Instant 1-tap language switch between English LTR and Arabic RTL with Cairo font rendering and zero text shifts.
- **Acceptance**: Seamlessly mirrors entire layout and updates all textual headings without page reload.

### PF-108 | Bespoke Vector SVG Sovereign Portfolio Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design geometric monogram "SA" with celestial apex star; render multi-size favicons and social OpenGraph cards.
- **Acceptance**: Vector SVG renders crisply across high-DPI mobile screens and browser favicons.

### PF-109 | Interactive Tech Stack Matrix with Verification Badges
- **Files**: `src/components/skills/TechStackMatrix.tsx`
- **Steps**: Group skills by tier (Languages: TypeScript, Python, C#; Frameworks: Next.js, FastAPI, Tauri; Systems: Win32, Tailscale, Linux).
- **Acceptance**: Each tech badge links to real projects in the portfolio utilizing that specific technology.

### PF-110 | Dynamic Dark Void & Crystalline Daylight Theme Engine
- **Files**: `src/hooks/usePortfolioTheme.ts`
- **Steps**: Zero-flash theme switcher; daylight mode uses crisp high-contrast slate with 10:1+ contrast ratio for accessibility.
- **Acceptance**: Switching theme updates CSS variables instantly with zero white flash.

### PF-111 | Direct Encrypted Contact & Telegram Dispatch Form
- **Files**: `src/components/contact/ContactForm.tsx`, `src/api/contact.ts`
- **Steps**: Contact form sending messages directly to Ahmed's iPhone via `@PersonalAI_1Bot` with rate limiting and Turnstile captcha.
- **Acceptance**: Submitting form delivers instant notification to Telegram and displays smooth confirmation check.

### PF-112 | Interactive Audio Chime on Interaction & Theme Switch
- **Files**: `src/lib/audioFeedback.ts`
- **Steps**: Optional subtle Web Audio API acoustic tick on button hover and spring theme toggle (toggleable in footer).
- **Acceptance**: Plays soft, pleasant acoustic tick without external MP3 assets.

### PF-113 | OpenGraph & Twitter Card Dynamic Image Generator
- **Files**: `src/app/api/og/route.tsx`
- **Steps**: Next.js `@vercel/og` Edge route dynamically generating high-resolution 1200x630 social preview cards for each project.
- **Acceptance**: Sharing portfolio link on Telegram/X renders custom card with project title and vector emblem.

### PF-114 | Multi-Screen Responsive Verification (320px to 4K)
- **Files**: `tests/responsive_portfolio.test.mjs`
- **Steps**: Playwright tests verifying project grids, modals, and navigation across 320px mobile to 4K desktop viewports.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### PF-115 | Keyboard Shortcut Navigation Accelerator
- **Files**: `src/components/shortcuts/KeyboardNavigator.tsx`
- **Steps**: Global keyboard shortcuts (`j`/`k` for next/prev project card, `/` to filter, `l` toggle language, `t` toggle theme).
- **Acceptance**: Keyboard users can navigate entire product wall with visual focus rings.

### PF-116 | Client Testimonial & Peer Recommendation Wall
- **Files**: `src/components/testimonials/TestimonialWall.tsx`
- **Steps**: Curated section displaying verified client and professor testimonials with verified identity tags.
- **Acceptance**: Clean cards with quote typography and verified company/institution badges.

### PF-117 | Video Project Showcase Player with In-Browser Previews
- **Files**: `src/components/projects/VideoDemoModal.tsx`
- **Steps**: Lightweight WebM/MP4 preview modal streaming short-form product walk-throughs produced by Content Creation Studio.
- **Acceptance**: Tapping "Watch Demo" opens video modal with smooth auto-play and mute controls.

### PF-118 | Offline First PWA Service Worker Engine
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache entire portfolio shell, project descriptions, and CV offline for offline viewing on mobile devices.
- **Acceptance**: Disconnecting network allows full portfolio browsing without broken asset errors.

### PF-119 | SEO & Structured Data (Person & SoftwareApplication Schema)
- **Files**: `src/lib/jsonLd.ts`
- **Steps**: Inject rich Schema.org JSON-LD structured data for `Person` (Ahmed Alaa) and `SoftwareApplication` for each product.
- **Acceptance**: Passes Google Rich Results validation with 0 warnings.

### PF-120 | Live Platform Health & System Status Ticker
- **Files**: `src/components/status/PortfolioHealthBadge.tsx`
- **Steps**: Header pill displaying aggregate portfolio status (e.g. "16 Projects Active · 5 Deployed Today · All Systems Operational").
- **Acceptance**: Pill renders pulsing green indicator with direct link to architecture section.

### PF-121 | Project Filter Pills by Domain & Platform
- **Files**: `src/components/projects/FilterBar.tsx`
- **Steps**: Filter projects by domain (AI, Engineering, Gaming, Academic, Commerce) and platform (Web, Desktop, Mobile, Hardware).
- **Acceptance**: Tapping filter pill animates card list with smooth spring stagger transition.

### PF-122 | High-Performance Static Export & Lighthouse 100/100 Benchmark
- **Files**: `next.config.mjs`, `tests/lighthouse_audit.mjs`
- **Steps**: Configure `output: 'export'` for Cloudflare Pages; optimize images, fonts, and critical CSS for 100/100 Lighthouse score.
- **Acceptance**: Lighthouse audit confirms 100 Performance, 100 Accessibility, 100 Best Practices, 100 SEO.

### PF-123 | Interactive Code Snippet Sandbox with Copy Badge
- **Files**: `src/components/code/CodeSnippetCard.tsx`
- **Steps**: Syntax-highlighted code viewer displaying real, elegant snippets from built projects with 1-tap copy button and check animation.
- **Acceptance**: Tapping copy updates icon to green checkmark and copies snippet to clipboard.

### PF-124 | Automated GitHub Actions Production Deployment Workflow
- **Files**: `.github/workflows/deploy_portfolio.yml`
- **Steps**: GitHub Actions workflow running tests, building static export, and deploying to Cloudflare Pages on every push to main.
- **Acceptance**: Push to main automatically deploys new build in under 45 seconds.

### PF-125 | End-to-End Automated Portfolio Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_portfolio_integrity.py`
- **Steps**: Validate data synchronization, Truth Rule compliance, zero broken links, zero emojis, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 2 seconds with 100% green gates.
