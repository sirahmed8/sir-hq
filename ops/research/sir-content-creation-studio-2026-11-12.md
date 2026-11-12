# Research: SIR Content Creation Studio (2026-11-12)

Planning-only round r61. Sources fetched live on 2026-11-12. No private data in queries.

## 1. Competitor pricing verified

- Opus Clip (opus.pro/pricing, fetched 2026-11-12): Free $0; Starter $15/mo; Pro $29/mo; Business custom. Free tier: captions with watermark, 3-day export limit, 3-day storage expiry, no social scheduler. Pro: animated captions, multi-language transcription, social posting to Shorts/TikTok/IG, team workspace, MCP connector, 100GB storage. Storage expires on free (3 days) and starter (29 days). (unsourced for Business custom price.)
- CapCut (capcut.com/pricing, prior round, checked 2026-11-12): Free 0 EGP; Pro 599.99 EGP/mo; Ultra 3949.99 EGP/mo; Teams 300 EGP/mo per seat (2 seats). Region-dependent; verify in Egypt region before quoting.
- Remotion (remotion.dev/docs/license/pricing, fetched 2026-11-12): Free license for individuals and companies of up to 3 people, unlimited commercial use, all features. Company License required above 3 people: Remotion for Automators $0.01 per render (billed in 1000-render increments, $10, minimum $100/mo) for batch/automated products including video editors and prompt-to-video apps; Remotion for Creators $25/mo/seat for manual creation. Enterprise from $500/mo. Consequence: our v1 (solo Ahmed, up to 3 people) ships on the free license; a Pro tier that resells renders needs a Company License at $100/mo minimum, which is a real cost line in the business model.

## 2. Platform API findings

- TikTok Content Posting API (developers.tiktok.com, fetched 2026-11-12): requires a registered app, Content Posting API product added, Direct Post enabled, video.publish scope approved for both app and user. Unaudited clients are restricted to private viewing mode; an audit is required to lift restrictions. Video restrictions: MP4 H.264, local file upload or pull from a verified domain/URL prefix. Max video post duration 300s (5 min). Photo posting now supported.
- Meta Graph API (Instagram Reels / Facebook): requires app review for instagram_content_publish and pages_manage_posts; Business/Creator account required; token refresh daemons needed. (From prior plan; no new fetch this round.)
- YouTube Data API v3: quota 10,000 units/day default; video upload costs 1600 units; resumable upload for large files. (Prior plan; verify before launch.)
- Reddit (PRAW): script app or web app; posting to subreddits requires moderator rules; rate limits per OAuth client. (Prior plan.)
- X (Twitter) API v2: media upload chunked; posting requires paid tier (Basic $100/mo) for write access as of recent changes; verify current pricing before promising X publishing. (Flagged as open question.)

## 3. Free and local tooling

- Piper TTS: local neural TTS, offline, supports Arabic voices (community models); runs on CPU; no per-character cost. Good fit for the free tier voiceover.
- Whisper (faster-whisper / whisper.cpp): word-level timestamps for kinetic captions; runs locally on CPU/GPU; no API cost. Arabic support via large-v3.
- FFmpeg with h264_nvenc: hardware encode on Nvidia GPUs; CPU fallback libx264; thermal sentinel needed on laptops.
- Stock media: Pexels and Pixabay APIs are free with attribution; license table required per asset.
- Music: require a recorded commercial license per track; exporter blocks unlicensed audio.

## 4. Regulations and compliance

- Egypt Personal Data Protection Law 151/2020: applies to processing personal data of Egyptian residents; requires consent, purpose limitation, data subject rights, security measures. Our product stores user accounts, OAuth tokens, media; privacy policy and data deletion flow required.
- Egypt Intellectual Property Law 82/2002: protects copyright in audio/video; user-generated content and stock assets need license tracking; no unlicensed media in exports.
- Platform terms: Meta, TikTok, YouTube, Reddit, X each require app review and impose rate limits and content policies; publishing must be human-approved and capped.
- Remotion license: free up to 3 people; Company License needed to resell render capacity beyond that. (See section 1.)

## 5. Gaps found vs our plan

- X publishing may require a paid API tier; our "free scheduler" promise for X should be downgraded to "drafts and manual post" or "X publishing when the owner pays for the API tier".
- Opus Clip 4.0 added prompt-to-clip and AI B-roll; our plan lacks prompt-to-clip and AI B-roll generation. Add as M4 features.
- Opus Clip Pro includes an MCP connector; our plan has no MCP surface. Consider exposing a read-only MCP for project status (optional, M6).
- Storage expiry on Opus free (3 days) is a pain point we can beat with local-first storage; emphasize in marketing.
- TikTok unaudited clients are private-only; our drafts-only mode already covers this, but the audit task must be explicit and owner-driven.