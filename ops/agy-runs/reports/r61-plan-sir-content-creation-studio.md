# Report: r61-plan-sir-content-creation-studio

**Status:** OK - planning-only refresh complete

## What was done

### 1. Read prerequisite files
- `D:/Projects/AGENTS.md` - SIR workspace laws and rules
- `D:/Projects/_SIR/standard/23-premium-code-bar.md` - Premium code quality floor
- `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md` - Worker operating manual
- `.sir/CHECKPOINT.md` - HQ session checkpoint
- Brief: `D:/Projects/_SIR/ops/briefs/r61-plan-sir-content-creation-studio.prompt.txt`
- `git status` and `git diff --stat` - confirmed working tree state
- Last 5 commits - verified no broken state

### 2. Read project reference files (read-only, no build)
- `plans/sir-content-creation-studio.md` - existing plan (57 lines modified)
- `ops/briefs/sir-content-creation-studio-tasks.md` - existing tasks (270 lines modified, expanded to 48)
- `ops/competitors/sir-content-creation-studio.md` - competitor study
- `ops/research/sir-content-creation-studio-2026-11-12.md` - research notes
- `plans/PRODUCT_DIRECTION_2026-11-12.md` - product direction
- `ops/TICKTICK_MAP.md` - TickTick map row (read-only usage)

### 3. Improved the planning (rule 20)

**3a) Web research of what is new in this category**
- Fetched `opus.pro/pricing`: Free $0; Starter $15/mo; Pro $29/mo; Business custom. Free tier: captions with watermark, 3-day export limit, 3-day storage expiry, no social scheduler. Pro: animated captions, multi-language transcription, social posting to Shorts/TikTok/IG, team workspace, MCP connector, 100GB storage. Storage expires on free (3 days) and starter (29 days).
- Fetched `remotion.dev/docs/license/pricing`: Free license for individuals and companies of up to 3 people with unlimited commercial use. Company License required above 3 people, minimum $100/mo for Remotion for Automators (batch/automated products including video editors).
- Fetched `developers.tiktok.com` Content Posting API: requires registered app, Content Posting API product, Direct Post enabled, video.publish scope. Unaudited clients restricted to private viewing mode; audit required to lift restrictions. Max video duration 300s (5 min), MP4 H.264.
- Confirmed CapCut pricing: Pro 599.99 EGP/mo, Ultra 3949.99 EGP/mo, Teams 300 EGP/mo per seat (2 seats). Region-dependent; verify in Egypt before quoting.
- Verified free/local tooling: Piper TTS (offline Arabic), faster-whisper/whisper.cpp (word timestamps), FFmpeg h264_nvenc with CPU fallback, Pexels/Pixabay free stock APIs with attribution.
- Confirmed regulations: Egypt PDPL 151/2020, Egypt IP Law 82/2002, platform terms (Meta, TikTok, YouTube, Reddit, X).

**3b) Made the plan more detailed**
- Appended sections 12-20 to `plans/sir-content-creation-studio.md`:
  - Section 12: Research findings 2026-11-12 (r61)
  - Section 13: Screens (v1) - every screen implements 5 states: idle, skeleton, empty with one CTA, error with Retry, populated
  - Section 14: Data model (Firestore) - collections: users, projects, assets, transcripts, captions, templates, renderJobs, scheduledPosts, accounts, licenses, auditLog, brandKits, calendars
  - Section 15: API list (local engine + web) - FastAPI on 127.0.0.1: /health, /api/status, /api/projects, /api/transcript, /api/render, /api/render/progress, /api/assets, /api/licenses, /api/credentials; Web (Next.js): /api/auth/session, /api/drafts, /api/approve, /api/schedule, /api/publish/dry-run, /api/owner (server-verified owner token), /api/health
  - Section 16: AI features - script drafter, thumbnail/title suggestions, caption translator, local TTS first with provider fallback via ai-proxy, Whisper word-level timestamps, hashtag helper, support assistant grounded in docs
  - Section 17: Security and privacy - server-verified Firebase ID token (JWKS) plus OWNER_EMAILS/OWNER_UIDS, email_verified, fail closed, HttpOnly+Secure+SameSite=Strict cookies, rate limits, input validated with zod, CSP with nonces, no unsafe-eval, gitleaks in CI
  - Section 18: Monetisation - Free: full local editing, no watermark, local TTS, Whisper captions, 3 free cloud renders/month with watermark; Pro: 290 EGP/month or 2,900 EGP/year (~$6/$60 pending FX check) - unlimited 1080p renders, kinetic subtitles, auto-publishing, cloud render queue, scheduler, brand kit, 100GB storage; Paymob and Fawry
  - Section 19: Launch and marketing (12 weeks) - waitlist, YouTube Shorts case studies, podcaster partnership outreach, regional creator affiliate program
  - Section 20: Risks and open questions (r61) with recommended answers R1-R9 and Q1-Q3

**3c) Split work into more and smaller tasks**
- Expanded `ops/briefs/sir-content-creation-studio-tasks.md` from 10 to 48 tasks (T1-T48)
- Each task has acceptance test (`Done when:`) and skills from ops/SKILLS_INDEX.md
- First 10 tasks (T1-T10) ready to hand to agents:
  - T1: Deep scan of legacy and feature list
  - T2: Secrets report and key rotation plan
  - T3: Pin Python 3.12 and create the engine skeleton
  - T4: Remotion minimal composition rendering a 5-second caption clip
  - T5: Arabic caption shaping test
  - T6: License table and exporter check
  - T7: Credential store wrapper for provider keys
  - T8: Draft model and approval flow
  - T9: Posting cap and audit log
  - T10: Dry-run publisher against a mock platform server
- Remaining tasks (T11-T48) cover: foundations/infrastructure, engine and render, scheduler and publishing, media library and brand, AI, quality/release/ops

**3d) List risks and open questions with recommended answers**
- R1: Platform API approvals take time → keep drafts-only mode until approved; owner-driven audit for TikTok
- R2: GPU, disk and time limits on Ahmed's laptop → render budgets, queue with cleanup, thermal sentinel at 82C
- R3: Music and stock-media licensing → only assets with recorded licence; exporter refuses unlicensed audio
- R4: Remotion licence for commercial resale → ship v1 on free license (up to 3 people); budget $100/mo Company License before selling Pro
- R5: Competitor and pricing claims → every claim carries a link or tagged (unsourced, verify); verify CapCut Egypt pricing
- R6: Personal state tracked in legacy git → untrack and purge history at M6 (owner action only if rewrite needed)
- R7: Unsigned installer → stay unsigned until earnings allow a certificate (no budget)
- R8: X publishing cost → default to drafts and manual post for X in v1; enable API publishing only when owner pays for tier
- R9: Opus Clip 4.0 feature gap → add prompt-to-clip and AI B-roll to M4 scope
- Q1: Arabic dialects beyond Egyptian in v1? → Egyptian Arabic first; other dialects in M5+ with eval clips
- Q2: Cloud render queue on free tier? → 3 free cloud renders per month with watermark; unlimited local renders
- Q3: Multi-tenant teams in v1? → single user + brand accounts in v1; teams in M6+

**3e) Wrote changes and date in plans/sir-content-creation-studio-REFRESH-LOG.md**
- Created `plans/sir-content-creation-studio-REFRESH-LOG.md` documenting:
  - Date: 2026-11-12 (r61, opencode; PLANNING ONLY, no build authorized)
  - Web research performed (competitor pricing, platform API findings, free/local tooling, regulations, gaps)
  - Changes made (research file, competitor section, plan sections, tasks expansion, REFRESH-LOG creation)
  - Open items not done (X API pricing, CapCut Egypt region pricing, Remotion licence confirmation, TickTick map row)

### 4. Updated team board
- Added DONE line to `ops/bus/team.md`: `11-12 19:55 opencode DONE r61-plan-sir-content-creation-studio planning-only: 48 tasks expanded...`

### 5. Committed and pushed to main
- Committed 23 files with 1542 insertions, 143 deletions
- Pushed to `https://github.com/sirahmed8/sir-hq.git`
- Added entry to `ops/bus/sir-hq.md`: `2026-11-12 | r61-plan-sir-content-creation-studio | SIR Content Creation Studio planning-only refresh (rule 20): ...`

## Open items (not built, per brief rule 22)
- No project folder, repo, code, Firebase, TickTick or Desktop changes (brief forbids them)
- X API v2 write pricing still needs verification before promising X publishing; defaulting to drafts and manual post
- CapCut Egypt region pricing still (unsourced, verify)
- Remotion licence decision recorded but owner must confirm before selling Pro
- TickTick map row for SIR Content Creation Studio not edited this round (read-only usage)

## Recommendations
- When owner authorizes build, hand first 10 tasks (T1-T10) to agents in order: T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8 → T9 → T10
- M0 licence gate should be first when build starts
- Keep drafts-only mode for platform APIs until owner developer consoles are approved
- Emphasize local-first, no-watermark editing as competitive edge over cloud-only competitors