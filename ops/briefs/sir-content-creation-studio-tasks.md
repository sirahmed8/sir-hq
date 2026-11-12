# Tasks for free agents: SIR Content Creation Studio

PLANNING ONLY (owner order 2026-11-12, rule 22): no build is authorized. Free agents may run tasks 1-3 only after owner authorization; until then these are queued plans. Each task under 2 hours unless noted. Ordered by dependency. Skills are names from `ops/SKILLS_INDEX.md`.

## First 10 (ready to hand to agents)

### T1 - Deep scan of legacy and feature list
Read `legacy/SIR Content Creation Studio (v1)` and the inventory `ops/inventory/SIR-Content-Creation-Studio.md`; produce `.sir/reports/deep-scan.md` listing every feature with keep/drop and a note on tracked personal state files (profile, uid, pro flag, studio.db, audio files). Do not edit legacy.
Done when: the file lists each feature with keep/drop and each personal-state file is named.
Skills: sir-skill-library, production-engineering-standards, verification.

### T2 - Secrets report and key rotation plan
Scan legacy for the ~40 provider key names in `.env` (ignored), the 18 `curl-auth-header` hits under `.agents`/`.claude`, and the two Firebase admin JSON keys mentioned in the inventory; write `.sir/reports/secrets-report.md` with key names only (never values), which are tracked vs ignored, and a rotation order.
Done when: report exists and names only key names, no values.
Skills: zero-trust-security-hardening, vibe-auth-hardening, firebase_security_rules_auditor.

### T3 - Pin Python 3.12 and create the engine skeleton
Add `.python-version` (3.12), `pyproject.toml`, and CI using Python 3.12; create the FastAPI engine skeleton with `/health` returning 200 and `/api/status` JSON.
Done when: `uv run pytest` green and health returns 200 locally.
Skills: production-engineering-standards, react-best-practices.

### T4 - Remotion minimal composition rendering a 5-second caption clip
Under `apps/render/`, create a Remotion composition that renders a 5-second 1080x1920 clip with a caption from JSON input.
Done when: an MP4 file exists and ffprobe prints duration 5s.
Skills: motion-graphics-engine, taste-design-engine.

### T5 - Arabic caption shaping test
Render a fixture Arabic sentence (RTL, with diacritics) in a frame and compare against a golden frame image.
Done when: the image diff test passes and the frame shows connected Arabic with no diacritic clipping.
Skills: a11y-debugging, react-best-practices.

### T6 - License table and exporter check
Create `docs/LICENSES.csv` and an exporter check that refuses an asset with no licence row.
Done when: a test fails when an asset has no licence row and passes when it does.
Skills: legal-compliance-shield, production-engineering-standards.

### T7 - Credential store wrapper for provider keys
Wrap the OS credential store (Windows Credential Manager) for provider keys; round-trip a key; ensure no key is in the repo (gitleaks).
Done when: round-trip test passes and gitleaks is clean.
Skills: vibe-auth-hardening, zero-trust-security-hardening.

### T8 - Draft model and approval flow
Implement the draft state machine (draft, approved, scheduled, posted) with tests; an unapproved publish is refused.
Done when: the unapproved-publish test passes and the state transitions are covered.
Skills: database-reliability-transactions, production-engineering-standards.

### T9 - Posting cap and audit log
Implement a per-account posting cap and an append-only audit log; tests for cap exceeded and append-only behaviour.
Done when: the cap test passes and audit lines are append-only (test verifies).
Skills: database-reliability-transactions, production-engineering-standards.

### T10 - Dry-run publisher against a mock platform server
Implement a dry-run publisher that sends the right payload to a mock platform server with no real network call.
Done when: the mock receives the expected payload and no real network request is made (test asserts).
Skills: production-engineering-standards, verification.

## Foundations and infrastructure (T11-T18)

### T11 - Firebase project sir-content-studio and Vercel import
Create Firebase project `sir-content-studio` (Auth Google, Firestore), dual hosting on Firebase Hosting and Vercel; OAuth app name "SIR Content Creation Studio"; logo and support email. Owner action for console sign-in.
Done when: both Firebase and Vercel URLs curl 200; sign-in brand check screenshot saved in `.sir/evidence/`.
Skills: firebase_basics, firebase_auth_basics, firebase_firestore, nextjs.

### T12 - Login brand check in a real browser
Sign in with Google in a real browser; the screen must not show a Firebase project id; save screenshot.
Done when: screenshot exists in `.sir/evidence/` and shows the product name, not the project id.
Skills: verification, a11y-debugging.

### T13 - CI pipeline green
Typecheck, lint, test, build, gitleaks on every push; first green run (or local verify pasted while CI quota flag exists).
Done when: `gh run list` green or local verify output pasted in checkpoint.
Skills: production-engineering-standards, verification.

### T14 - Desktop folder kit
Recreate the Desktop folder kit from scratch: `folder.ico`, SIR Projects shortcuts, `Versions.txt` 1.0.0.
Done when: Desktop folder exists with real shortcuts and folder.ico.
Skills: modern-app-engineering.

### T15 - Deny-by-default Firestore rules with emulator tests
Author Firestore rules deny by default with per-user claims; emulator tests for cross-tenant read failure.
Done when: emulator tests green; forged-token read returns 403.
Skills: firestore_rules_creation, firebase_security_rules_auditor, zero-trust-security-hardening.

### T16 - Owner-auth package (JWKS verified token)
Server-verified Firebase ID token via JWKS, OWNER_EMAILS/OWNER_UIDS allow-list, email_verified, fail closed; HttpOnly+Secure+SameSite=Strict session cookie; rate limits on auth.
Done when: forged token returns 403 in CI; session cookie flags verified.
Skills: vibe-auth-hardening, auth, zero-trust-security-hardening.

### T17 - Billing fallback "Subscriptions launching soon"
Billing fallback with email lead capture; EGP primary with auto-detected USD/SAR/AED; subscription grants owner all permissions.
Done when: pricing page shows the fallback and lead capture creates one Firestore doc.
Skills: legal-compliance-shield, production-engineering-standards.

### T18 - Legal pages and cookie banner
Legal pack generated from data-inventory.yml; cookie banner with equal Reject; account and data deletion flow; Egypt PDPL 151/2020 and IP law 82/2002 tasks.
Done when: legal pages present and marked "AI-drafted, to be reviewed by a qualified lawyer".
Skills: legal-compliance-shield.

## Engine and render (T19-T26)

### T19 - FFmpeg 9:16 pipeline with NVENC and CPU fallback
Hardware-accelerated FFmpeg 9:16 vertical pipeline using h264_nvenc with auto-fallback to libx264; audio normalization to -14 LUFS; voice ducking.
Done when: renders a 60s 1080x1920 video in under 15s on GPU; CPU fallback works.
Skills: motion-graphics-engine, production-engineering-standards.

### T20 - Whisper word-level timestamps for captions
faster-whisper/whisper.cpp with word-level timestamps; Arabic via large-v3; golden frame test for RTL diacritics.
Done when: caption WER recorded on 20 Arabic clips; golden frame diff passes.
Skills: motion-graphics-engine, verification.

### T21 - Kinetic subtitle styles
Subtitle style presets: Ali Abdaal yellow-highlight, Hormozi bold, clean minimal; custom fonts; Arabic RTL shaping with no diacritic clipping.
Done when: preview shows all three styles; Arabic frame golden diff passes.
Skills: motion-graphics-engine, taste-design-engine.

### T22 - Local TTS with provider fallback
Local TTS first (Piper) with provider fallback via ai-proxy; voice selection; preview.
Done when: round-trip TTS produces audio; fallback triggers on local failure (test).
Skills: gemini-api-dev, omniroute-resilience-gateway.

### T23 - Audio normalization and voice ducking
EBU R128 (-14 LUFS) normalization; sidechaincompress ducking music 12dB during speech.
Done when: output measures -14 LUFS; music ducks during voice (audio test).
Skills: motion-graphics-engine.

### T24 - Progress bar and hook timer overlay
Programmatic FFmpeg filter drawing kinetic progress bar and "Wait for it..." pulse pill during first 3 seconds.
Done when: rendered video includes synchronized progress indicator.
Skills: motion-graphics-engine, emil-motion-impeccable.

### T25 - Thermal sentinel
Check Nvidia GPU temperature before batch renders; pause export above 82C.
Done when: sentinel pauses render in test when temperature threshold exceeded (mock).
Skills: production-engineering-standards.

### T26 - Batch CSV-to-video worker
Generate 20 vertical videos from a CSV of tips/quotes; silent background daemon with CREATE_NO_WINDOW.
Done when: 20 MP4s produced; no console window flashes.
Skills: production-engineering-standards, motion-graphics-engine.

## Scheduler and publishing (T27-T34)

### T27 - Draft state machine and approval flow
Draft state machine (draft, approved, scheduled, posted); unapproved publish refused; tests.
Done when: unapproved-publish test passes; transitions covered.
Skills: database-reliability-transactions.

### T28 - Posting cap and append-only audit log
Per-account posting cap; append-only audit log; tests for cap exceeded and append-only behaviour.
Done when: cap test passes; audit lines append-only verified.
Skills: database-reliability-transactions.

### T29 - Dry-run publisher against mock platform
Dry-run publisher sending correct payload to mock server; no real network call.
Done when: mock receives expected payload; test asserts no network request.
Skills: production-engineering-standards, verification.

### T30 - Meta Graph API publisher (IG Reels, Facebook)
Official Meta Graph API: upload container, query status, publish Reels with caption, cover, hashtags; token refresh daemon.
Done when: publishes to test page and returns permalink; token refresh test passes.
Skills: production-engineering-standards, zero-trust-security-hardening.

### T31 - TikTok Content Posting API publisher
Direct post API with OAuth token refresh; creator info query; unaudited clients private-only.
Done when: dispatches upload and returns publish_id; status fetch works.
Skills: production-engineering-standards.

### T32 - YouTube Shorts uploader
YouTube Data API v3 resumable upload with chapters and localized tags; quota handling.
Done when: uploads short and sets visibility; quota test passes.
Skills: production-engineering-standards.

### T33 - Reddit publisher
Authenticated PRAW client publishing video posts to targeted subreddits with flair; rate limits.
Done when: posts to subreddit and returns submission URL.
Skills: production-engineering-standards.

### T34 - Telegram human-in-the-loop approval
Send 5s preview GIF with Approve/Edit/Cancel buttons; post stays awaiting approval until tap.
Done when: approval triggers publish; cancel leaves draft.
Skills: meta-social-sidecar, verification.

## Media library and brand (T35-T38)

### T35 - Stock B-roll and SFX cache with mood tags
Download, organize and tag royalty-free B-roll (Pexels/Pixabay) and SFX by mood; 1-click insert.
Done when: search returns tagged clips; insert snaps to subtitle markers.
Skills: production-engineering-standards.

### T36 - License table and exporter check
`docs/LICENSES.csv` and exporter refusing an asset with no licence row; copyright guard blocks unlicensed audio.
Done when: test fails on missing licence; passes on present; audio guard blocks.
Skills: legal-compliance-shield.

### T37 - Brand kit manager
Logos, fonts, watermark opacity; corner watermark burn-in without pixelation.
Done when: watermark burns into corner; brand kit persists.
Skills: taste-design-engine.

### T38 - Calendar drag-and-drop scheduling
Interactive monthly calendar with color-coded network icons; drag updates scheduled timestamp; 24-hour veto window.
Done when: drag updates timestamp; veto window test passes.
Skills: emil-motion-impeccable, react-best-practices.

## AI (T39-T42)

### T39 - Script drafter with hook variations
Generate 3 hook variations, retention body, CTA from a topic; estimated reading duration.
Done when: outputs structured 60s script with visual cue prompts.
Skills: gemini-api-dev, cognitive-product-intuition.

### T40 - Thumbnail and title generator
Generate 3 high-contrast thumbnail variants with bold text overlays; title suggestions.
Done when: produces 3 export-ready 1080x1920 JPGs with distinct hooks.
Skills: imagegen, high-conversion-copywriting.

### T41 - Prompt-to-clip and AI B-roll
Prompt-to-clip (Opus 4.0 style) and AI B-roll generation via image/video models; rate-limited.
Done when: prompt yields a clip plan; B-roll asset generated and licensed.
Skills: gemini-omni-flash-api, gemini-api-dev.

### T42 - Support assistant grounded in docs
Floating drawer grounded only in docs/help/*.md; refuses ungrounded answers on 10 prompts.
Done when: 10-prompt eval passes with zero hallucinated export limits.
Skills: ai-sdk, react-best-practices.

## Quality, release and ops (T43-T48)

### T43 - Five states and 4 locales on every screen
Idle, skeleton, empty, error, populated; 4 locales (Arabic, English, Simplified Chinese, Hindi) complete with no missing keys; 4 themes.
Done when: no missing keys; Lighthouse mobile 90+ JSON saved.
Skills: mobile-ergonomics-polish, react-best-practices.

### T44 - Accessibility and responsive audit
WCAG 2.2 AA; 44px targets; full keyboard nav; 320px to 4K; zoom 80-200%; Playwright responsive tests.
Done when: zero horizontal overflow across viewports; a11y audit green.
Skills: a11y-debugging, mobile-ergonomics-polish.

### T45 - E2E smoke test
Playwright E2E: script -> subtitles -> audio -> render -> preview; full suite green.
Done when: 100% green with 0 errors.
Skills: verification.

### T46 - Owner analytics page
/owner route with server-verified owner token; real metrics (renders, posts, errors, cost, subscriptions, downloads); 403 for non-owner.
Done when: open /owner requires token; shows real metrics; non-owner gets 403.
Skills: zero-trust-security-hardening, production-engineering-standards.

### T47 - Nightly cache cleanup and token refresh daemons
Nightly temp-cache cleanup; token refresh daemons; weekly dependency update; static status JSON; weekly Arabic Telegram report.
Done when: cleanup runs and logs; daemon refreshes a token in test.
Skills: production-engineering-standards.

### T48 - M6 release and retirement
Rebuilt signed installer (owner certificate), update channel, platform API approvals, retire v1 folder, move legacy/ to old projects; Remotion licence decision recorded.
Done when: installer smoke test on clean VM passes; legacy moved and recorded; checkpoint records both live URLs.
Skills: modern-app-engineering, verification.

## Task count: 48. First 10 (T1-T10) ready to hand to agents once owner authorizes build.