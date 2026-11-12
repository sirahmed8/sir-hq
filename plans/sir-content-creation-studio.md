# PLAN: SIR Content Creation Studio

Version 1.0.0. Rewritten 2026-11-12 (r52). Replaces the old 87-line plan and the DEEP plan; keeps what is still true (names, security rules, legacy facts, media-rights and Remotion-licence checks, platform matrix, pricing). Supersedes stack notes that said Cloudflare Pages only: the standing owner rule (OWNER_DEFAULTS item 2, WORKER_PREAMBLE item 15) requires Firebase Hosting AND Vercel dual hosting, and rule 13 requires its own Firebase project `sir-content-studio`. Decisions recorded in section 5.

## 1. Who it is for and the promise

Creators, podcasters, agencies and media teams who want to turn a long-form recording or a script into a finished vertical short (Shorts, Reels, TikTok) or a longer video, with captions, voice, footage or images, music, render and a human-approved posting schedule, without uploading raw footage to a cloud editor they do not control. First users: Ahmed's ByteVibeHQ brand accounts; then any creator anywhere. GLOBAL: anyone in the world, accounts, subscriptions, every platform and OS including phone, watch, car, TV.

**One-sentence promise (sell the end state):** Open SIR Content Creation Studio on your laptop, paste a script or drop a recording, and twenty minutes later you hold a captioned, branded, ready-to-post vertical video plus a calendar of approved drafts waiting for one tap to publish, rendered locally so your footage never leaves your machine.

## 2. Competitors

Full study with sources: `ops/competitors/sir-content-creation-studio.md` (10 competitors: Opus Clip, CapCut, Canva, InVideo, Descript, Buffer, Hootsuite, Repurpose.io, Vidyo.ai, Riverside). Headline: the category is split between cloud editors that watermark on free and lock features behind subscriptions (CapCut Pro 599.99 EGP/month, Opus Clip Pro $29/month), and schedulers that do not edit (Buffer, Hootsuite). Our edge: offline-first editing with no watermark on free export, local NVENC render, Arabic RTL captions with correct shaping, a human-approved scheduler for official APIs only, and an owner analytics page.

## 3. Features

**On par with best-in-category:**
- Project and idea to script: script drafter with hook variations, retention body and CTA; thumbnail and title suggestions.
- Storyboard and timeline: multi-track timeline (video, B-roll, captions, voice, music) with draggable handles and a frame-accurate scrubber; Dynamic Island active-only tab bar.
- Voice and captions: local TTS first with provider fallback; Whisper word-level timestamps; kinetic subtitle styles (Ali Abdaal yellow-highlight, Hormozi bold, clean minimal); Arabic RTL shaping with no diacritic clipping; custom fonts.
- Media library: stock B-roll and SFX cache tagged by mood; brand kit (logos, fonts, watermark); license table per asset.
- Render: hardware-accelerated FFmpeg (NVENC with CPU fallback), audio normalization to -14 LUFS, voice ducking, progress bar overlay, thermal sentinel.
- Schedule: calendar of drafts, approved and posted; drag-and-drop between days; 24-hour veto window; posting cap per account; audit log.
- Accounts: Meta (Instagram/Facebook), TikTok, YouTube, Reddit, X via official APIs only; encrypted token storage; token refresh daemons.
- Publishing: human-in-the-loop approval via Telegram (preview GIF plus Approve/Edit/Cancel); drafts-only mode until platform apps are approved.
- Analytics: real view counts, retention and follower growth from platform APIs only; no invented numbers.
- Settings, profile, pricing, help, owner dashboard.

**Owner's own ideas (ported from TickTick `30-Day Projects Sprint` / `أفكار برامج ومشاريع` and legacy, per PROJECT_MERGE_RECORD):**
- Sprint Day 5 (SIR CCS): local-first studio with the scheduler idea; ByteVibeHQ publishing as the flagship brand channel (v1 had no spec; this plan supplies it).
- Idea sourcing: owner's notes in `My notes` column "Me" for content ideas (never the "habobty" column).
- 12-week marketing launch calendar for the product itself (waitlist, Shorts case studies, podcaster outreach, affiliate program).
- Bulk CSV-to-video batch worker (20 vertical videos from a CSV of tips/quotes).
- Silent background render daemon with no console windows.
- Nightly encrypted asset and video backup routine.
- Turnkey creator quickstart guide in Arabic and English.
- Platform API approvals kept in drafts-only mode until the owner's developer consoles are ready.

**Explicitly NOT built:** no engagement bots, no automated likes/follows/comments, no fake accounts, no scripting X's website, no CAPTCHA bypass, no deepfake or defamatory content, no media without a recorded licence. Publishing refuses an unapproved draft and refuses more than the cap.

## 4. Platform matrix (what v1 includes)

| Platform | v1 state | Notes |
|---|---|---|
| Web (responsive, PWA installable) | in v1 | Next.js App Router for the scheduler/dashboard; Arabic RTL first, English second; light/dark/system/high-contrast |
| Windows desktop | in v1 | Tauri v2 (or Electron) with local NVENC GPU access, signed installer, self-update channel, Download page on the site |
| macOS | M6+ | Electron/Tauri build only if a user asks; same codebase |
| Linux | M6+ | same, on request |
| Android phone/tablet | M5-M6 | PWA for approving drafts and viewing analytics; Capacitor wrapper if a native feel is wanted |
| iOS / iPad | M5-M6 | PWA / SideStore unsigned .ipa until paid Apple account |
| Wear OS | skip v1 | no real use for a video editor; revisit with evidence |
| watchOS | skip v1 | same |
| TV (Android/Apple) | skip v1 | video timeline editing requires a high-resolution multi-track screen |
| Car (Android Auto/CarPlay) | skip | no allowed car category fits |
| Widgets / Live Activities | M6 | render-progress and scheduled-post widgets |
| Browser extension | skip | no use case |

All platforms share the same Firebase project and auth.

## 5. Architecture (on the shared kit, `plans/SHARED_PLATFORM_KIT.md`)

- **App**: desktop shell (Tauri v2 or Electron) + Vite + React for the studio UI, local engine Python 3.12 (FastAPI on 127.0.0.1) with Remotion for rendering; web dashboard on Next.js App Router for the scheduler and approvals. Deployed identically to **Firebase Hosting** and **Vercel** (Vercel imports the GitHub repo via Vercel CLI; same build, same env vars on both; both curl-checked per rule 15). Repo `sirahmed8/sir-content-creation-studio` (private). App version stays 1.0.0.
- **Backend**: Firebase project `sir-content-studio` (own project per rule 13): Auth (Google sign-in, JWKS-verified ID token on server), Firestore (deny-by-default rules, emulator-tested), Firebase Storage for media, App Check where available. Decision recorded: legacy used Cloudflare Pages only; superseded by the dual-host and own-Firebase rules. Cloudflare remains an ADR alternative for the render queue if Firebase costs bite.
- **Accounts**: `owner-auth` package pattern - server-verified token, `OWNER_EMAILS`/`OWNER_UIDS` allow-list, email_verified, fail closed; HttpOnly+Secure+SameSite=Strict session cookie; rate limits on auth and AI; no localStorage tokens; provider keys in the OS credential store on desktop or server secrets, never the renderer bundle.
- **Owner-only analytics page**: `/owner` route, server-verified owner token only, real metrics (renders, posts published, errors, cost, subscriptions, downloads). Non-owner gets 403.
- **AI**: `ai-proxy` with the standing fallback chain (Gemini flash-lite -> flash -> any Gemini -> OpenRouter free -> other free -> local), per-project keys, `AI_ENABLED` kill switch, daily cost cap in `config/limits.json` ($3.00/day default), free users 5 per rolling 24h with badge, owner unmetered. Script writer, caption translator, voice (local TTS first), thumbnail suggestions. Evals: caption word error rate on 20 Arabic clips, script safety (refuses false claims in health/finance prompts).
- **Billing**: `billing-fallback` - "Subscriptions launching soon" + email lead capture until Paymob keys exist; EGP primary with auto-detected USD/SAR/AED; subscription grants owner all permissions.
- **Legal**: `legal-pack` generated from `data-inventory.yml`, marked "AI-drafted, to be reviewed by a qualified lawyer before paid launch"; Egypt PDPL 151/2020 and IP law 82/2002 tasks.
- **Ops**: `/api/health`, nightly temp-cache cleanup, token refresh daemons, weekly dependency update, static status JSON, weekly Arabic Telegram report, emergency alerts; AI daily cost cap.
- **Support assistant**: floating drawer grounded only in `docs/help/*.md`.
- **Skills used for this plan** (from ops/SKILLS_INDEX.md + encyclopedia): sir-skill-library, taste-design-engine, anti-vibecoded-design-system, emil-motion-impeccable, cognitive-product-intuition, modern-ui-ux-design-system, high-conversion-copywriting, mobile-ergonomics-polish, motion-graphics-engine, meta-social-sidecar, music-prompter, gemini-omni-flash-api, firebase_auth_basics, firebase_firestore, firestore_rules_creation, firebase_security_rules_auditor, vibe-auth-hardening, zero-trust-security-hardening, legal-compliance-shield, omniroute-resilience-gateway, database-reliability-transactions, production-engineering-standards, react-best-practices, nextjs, verification, skills-discovery-engine, agent-reach (read-only platform research).

## 6. Premium quality bar

- Apple-level motion: spring physics (stiffness 400/damping 30 micro, 300/28 layout), transform+opacity only, 120Hz-safe, reduced-motion path, matching open/close for every sheet/drawer; Dynamic Island active-only tab bar (monochrome SVG when inactive, expands to icon + text when active).
- Arabic (Egyptian creator tone) RTL-first and English; per-character bidi detection in inputs; `<bdi>` isolation for mixed text; Alexandria/Cairo + Inter/Bebas Neue pairing; `tabular-nums` on numbers; kinetic subtitle shaping with no diacritic clipping.
- Five states on every view: idle, skeleton matching final geometry, empty with one CTA, error with Retry, populated with virtualization fine at 1,000+ items.
- Accessibility: WCAG 2.2 AA, 44px targets, full keyboard nav, focus visible, 320px to 4K, zoom 80-200%.
- No AI slop: no purple-blue gradients, no sparkle icons, no emoji headings, no pill-button spam, no hype words, no em-dashes in copy, no fake counts or reviews.
- Signature interaction (from `.sir/MASTER_PLAN.md` and `.sir/DESIGN.md`): the render progress overlay with a horizontal progress bar synchronized to duration and a "Wait for it..." pulse pill during the first 3 seconds; the Telegram one-tap approval flow.

## 7. Free tier and pricing (EGP primary, USD/SAR/AED auto-detected)

- **Free**: full local editing, no watermark on free export, local TTS, Whisper captions, manual timeline, 3 free cloud renders per month with a watermarked corner badge if cloud is used; marketplace browsing.
- **Pro** (test price, "(unsourced, verify)" until 10 creator interviews): 290 EGP/month or 2,900 EGP/year (~$6 / $60 placeholder pending FX check) - unlimited 1080p renders, kinetic subtitles, auto-publishing, cloud render queue, scheduler, brand kit, 100GB storage. Paymob (Cards, Vodafone Cash, Meeza) and Fawry.
- **Fallback**: until payment keys exist, CTA reads "Subscriptions launching soon" with email capture; never a broken checkout.
- Owner gets all Pro features free; subscription grants owner all permissions.
- Competitor anchors (sourced): CapCut Pro 599.99 EGP/month, Ultra 3949.99 EGP/month (capcut.com/pricing, checked 2026-11-12); Opus Clip Pro $29/month, Starter $15/month (opus.pro/pricing, checked 2026-11-12). Our Pro sits below CapCut Pro and roughly matches Opus Clip's monthly price while staying offline-first.

## 8. Milestones M0-M6 (acceptance tests)

| Milestone | Scope | Acceptance test |
|---|---|---|
| **M0 Foundations + Desktop kit** | Repo scaffold (exists), `.sir/` kit (exists), Firebase project `sir-content-studio` + Vercel import, CI green, **recreate the Desktop folder kit from scratch** (`folder.ico`, SIR Projects shortcuts, Versions.txt 1.0.0) | `npm run build` exit 0; `/api/health` 200; `gh run list` green or local verify pasted (CI quota flag rule); Desktop folder exists with real shortcuts and folder.ico; sign-in brand check screenshot shows no Firebase project id |
| **M1 Core slice** | Local engine health endpoint, project create/open, transcript from a sample clip, Remotion 5s caption clip render, tests for each | `uv run pytest` green; health returns 200; MP4 file exists and ffprobe prints duration 5s; Arabic caption frame golden-image diff passes |
| **M2 Parity with the old project** | Captions, reframing, export; scheduler for Instagram/TikTok/Facebook/Reddit via official APIs; calendar with 24-hour veto window; license table and exporter check | feature checklist from legacy ticked; media library shows license table; unapproved publish refused (test); cap test passes; audit lines append-only |
| **M3 Security, legal, billing, owner page** | Deny-by-default rules + emulator tests, forged-token 403, billing fallback, legal pages, `/owner` analytics, credential store, Python version pin | Forged token 403 in CI; scheduler refuses unapproved draft (test); open `/owner` -> server-verified token required -> shows renders, posts, cost; pricing shows "Subscriptions launching soon" + lead capture creates one Firestore doc; no key in repo (gitleaks); both Firebase and Vercel URLs curl 200 |
| **M4 AI** | Clip finder and caption writer with eval clips; hashtag and title helper; support assistant; thermal sentinel; batch worker | `npm run eval:caption` WER recorded; `npm run eval:script-safety` refuses false claims; support assistant refuses ungrounded answers on 10 prompts |
| **M5 Quality sweep** | 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for critical journeys, screenshots at 390 and 1280 in LTR and RTL; PWA approvals | Lighthouse mobile 90+ JSON saved; Playwright e2e green; screenshots archived in `.sir/evidence/`; installer smoke test on clean profile passes |
| **M6 Release and retirement** | Rebuilt signed installer (owner certificate), update channel, platform API approvals, retire v1 folder, move `legacy/` to old projects | installer smoke test on clean VM passes; owner signs installer; scheduler live for one brand account in drafts-then-approved mode; checkpoint records both live URLs; `legacy/` moved and recorded |

## 9. First 10 tasks for free agents

Written and queue-ready in `ops/briefs/sir-content-creation-studio-tasks.md` (T1-T10: deep scan, secrets report, Python pin and engine skeleton, Remotion caption clip, Arabic caption shaping test, license table and exporter check, credential store, draft approval flow, posting cap and audit log, dry-run publisher against a mock platform).

## 10. Risks and open questions (defaults)

- Platform API approvals take time (owner accounts); keep drafts-only mode until approved.
- GPU, disk and time limits on Ahmed's laptop: render budgets, queue with cleanup, thermal sentinel.
- Music and stock-media licensing: only assets with a recorded licence; exporter refuses an asset with no licence row.
- Remotion licence terms for commercial use: "(unsourced, verify)" at M0; read the official licence page and record the answer before selling Pro.
- Competitor and pricing claims: `ops/competitors/sir-content-creation-studio.md` must carry links or "(unsourced, verify)".
- Personal state tracked in legacy git (profile, uid, pro flag, studio.db, audio files): untrack and purge history at M6 (owner action only if a rewrite is needed).
- Unsigned installer stays unsigned until earnings allow a certificate (no budget).

## 11. Only the owner can do

Sign in to platform developer consoles (Meta, Google/YouTube, TikTok, Reddit, X) and approve app reviews; buy domain and code-signing certificate; create payment accounts and paste keys into `.env` (never git); approve each connected brand account; rotate the legacy Firebase admin keys and personal state found in `legacy/`; lawyer review before paid launch; Search Console/Bing sign-in; Apple Developer account when iOS store submission is wanted.