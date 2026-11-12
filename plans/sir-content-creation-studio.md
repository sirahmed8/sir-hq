# PLAN: SIR Content Creation Studio (Wave 4, GLOBAL product, not started)
Audited 2026-11-10. Replaces `SIR Content Creation Studio (v1)` (in `legacy/`, kept until M6). Free local editing, paid cloud queue and scheduler in EGP. It also runs the owner's brand-channel publishing, so it doubles as the engine for standard 26 marketing of the other products. **GLOBAL**: anyone in the world, accounts, subscriptions, every platform and OS including phone, watch, car, TV. Owner-only analytics page, dual hosting (Firebase + Vercel), subscription grants owner all permissions.

## 1. Purpose (plain words)
A desktop program that turns an idea into a short vertical video (Shorts, Reels, TikTok) or a longer video: script, voice, captions, footage or images, music, render. It can schedule posts to a brand's accounts through the platforms' official APIs, always with a human-approved draft first. For global users: any creator anywhere can produce and schedule content with the same tools.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Content Creation Studio` |
| GitHub (private) | `sirahmed8/sir-content-creation-studio` |
| Stack (planned) | Electron + Vite + React shell, local engine Python 3.12 (FastAPI on 127.0.0.1) with Remotion for rendering, one Python version pinned everywhere (legacy had 3.10, 3.11 and 3.13 mixed); web dashboard on Cloudflare Pages for the scheduler |
| Domain | candidate `sirstudio.app` (owner checks and buys; price "(unsourced, verify)"); `pages.dev` until then |
| Platforms | **Platform Matrix (GLOBAL):** Windows desktop ✅ (first); Web dashboard ✅; macOS Electron build ⏭️ M6+ (only if a user asks); Linux Electron build ⏭️ M6+; Android ⏭️ skipped; iOS ⏭️ skipped; TV ⏭️ skipped; watchOS ⏭️ skipped; Car ⏭️ skipped. Browser extension: skipped. All platforms share the same Firebase project and auth. |
| Money | **Pricing & Free Tier:** Free local editing with a watermark-free export. Pro in EGP for the cloud render queue and the scheduler (price to test, "(unsourced, verify)"); "subscriptions launching soon" + email capture until keys exist. EGP first, USD/SAR/AED toggle auto-detected from locale/IP with manual override. Owner gets all Pro features free. Subscription grants owner all permissions in owner dashboard. |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30); 9 commits, all setup/plan. PORTFOLIO.md: 2 of 19 tasks.
Legacy facts (`ops/inventory/SIR-Content-Creation-Studio.md`, 2026-10-29, tests not run): 120 test files; personal state tracked in git (profile, uid, pro flag, `studio.db`, audio files); no server-side token check (owner by env in 6 files); unsigned installer older than the last source commit; CI failing; Python version mismatch; no social publishing code exists (the "ByteVibeHQ publishing" idea has no spec). Treat all legacy claims as unverified.

## 4. Security and conduct rules
1. Personal state files are not tracked; history purge for the legacy repo happens at M6 (owner action only if a rewrite is needed).
2. Pro and owner checks are server-side (verified ID token, allow-list) (use `owner-auth` from SHARED_PLATFORM_KIT). Test: forged local `.studio_pro.json` unlocks nothing.
3. Provider keys live in the OS credential store (desktop) or server secrets, never in the renderer bundle or git.
4. Publishing: official APIs only, human-approved draft, a posting rate cap per account, an audit log. No engagement bots, no automated likes, follows or comments, no fake accounts, no scripting X's website, no CAPTCHA bypass. Tests: scheduler refuses to publish an unapproved draft; refuses more than the cap.
5. Brand voice accounts post as the brand; they never pose as Ahmed in live conversations.
6. Media rights: every music, font, stock clip and model used has a licence entry in `docs/LICENSES.csv`; the exporter refuses an asset with no licence. AI-generated media labeled where a platform requires it.
7. Remotion licence terms for commercial use: "(unsourced, verify)" at M0; default is read the official licence page and record the answer before selling Pro.
8. Local-only mode works offline with local models; nothing is uploaded without a visible switch.
9. **Owner-only analytics page**: separate route, server-verified owner token, shows all metrics (renders, posts published, errors, cost). No other user sees it.

## 5. Shared pieces
Platform `owner-auth`, `ai-proxy` (script/voice providers with fallback), `billing-fallback`, `legal-pack`, `i18n`, `ui/styles/hooks`, Telegram sender (approval taps for posts). The scheduler and approval flow here is also the engine other plans call for their own marketing calendars; do not build another scheduler in other products. Laptop Manager's game mode must be able to pause renders (small endpoint). **Reuses SHARED_PLATFORM_KIT entirely; only rendering/scheduling features differ.**

## 6. Screens and entities
Home (projects), Idea to script, Storyboard/timeline, Voice and captions, Media library, Render queue, Schedule (calendar of drafts, approved, posted), Accounts, Analytics (real numbers from APIs only), Pricing, Settings and Profile, Help, **Owner dashboard**. Entities: Project, Scene, Asset, License, RenderJob, Draft, ScheduledPost, Account, AuditEntry, Subscription.
Five states, Arabic RTL (captions with correct Arabic shaping) and English, themes, 320 px to 4K for the dashboard, WCAG 2.2 AA, own logo.

## 7. AI
Script writer, caption translator, voice (local TTS first, provider fallback), thumbnail suggestions. Chain via `ai-proxy` (from SHARED_PLATFORM_KIT), cost cap per day, kill switch; evals: caption accuracy on 20 Arabic clips (word error rate recorded), script safety (no false claims in sample health or finance prompts: refuses). Support assistant grounded in docs; free users 5 per day; owner unmetered.

## 8. Operations (standard 26 from SHARED_PLATFORM_KIT)
Render failure alerts, disk-space guard (render budget and cleanup), weekly Telegram report (renders, posts published, errors, cost), update channel with signed installer (owner certificate), status JSON for the dashboard.

## 9. Launch, legal and visibility
Owner buys domain, code-signing certificate, payment accounts, platform developer app approvals (YouTube, Meta, TikTok review queues take time; keep drafts-only mode until approved). Legal pack: privacy, terms, refunds, DPA, sub-processors, AI-output disclosure, DMCA process.
**Dual hosting**: Firebase Hosting AND Vercel (import GitHub repo with Vercel CLI), same build, same env vars on both. Both addresses curl-checked (retry once on timeout).
Visibility: Arabic queries ("برنامج عمل فيديوهات ريلز"), tutorial videos made with the product itself, comparison pages once sourced, `llms.txt`, facts page.

## 10. Three-Milestone Roadmap (owner-visible checks)
| Milestone | Goal | Owner-Visible Exit Check |
|---|---|---|
| **M1–M2: Core Slice** | Script to 15 second rendered MP4 with captions on the laptop; render time recorded; parity: feature checklist from legacy ticked; media library with license table | 1. Run desktop app → write script → render 15s MP4 with captions → file exists, ffprobe prints 15s. 2. Media library shows license table for each asset. 3. Screenshot at 390/1280, LTR/RTL, light/dark. |
| **M3: Security, Legal, Billing, Owner Page** | Token tests, unapproved-publish test, billing fallback test, legal pages, owner-only analytics page live | 1. Forged token test returns 403 (CI). 2. Scheduler refuses unapproved draft (test). 3. Open `/owner` → server-verified token required → shows renders, posts, cost. 4. Pricing page shows "Subscriptions launching soon" + email capture. 5. Legal pages exist at `/legal/*`. 6. Dual hosting verified: curl both Firebase and Vercel URLs. |
| **M4–M6: AI, Quality, Release** | Caption word error rate and script safety evals recorded; quality screenshots; offline test; a11y; installer smoke test on clean profile; signed installer (owner); scheduler live for one brand account in drafts-then-approved mode | 1. Run `npm run eval:caption` → WER recorded. 2. Run `npm run eval:script-safety` → refuses false claims. 3. Lighthouse mobile 90+ JSON saved. 4. Installer smoke test on clean VM passes. 5. Owner signs installer. 6. Scheduler live for one brand account in drafts-then-approved mode. |

## 11. Next 10 tasks (each under 2 hours)
1. Deep scan of legacy: feature list and tracked personal files (names only) into `.sir/reports/deep-scan.md`. Check: file lists each feature with keep/drop.
2. Pin Python 3.12 (`.python-version`, `pyproject.toml`, CI) and create the engine skeleton with `/health`. Check: `uv run pytest` green; health returns 200.
3. CI workflow with gitleaks. Check: green Actions URL.
4. Remotion minimal composition rendering a 5 second caption clip from JSON. Files: `apps/render/`. Check: MP4 file exists, ffprobe prints duration 5 s.
5. Arabic caption shaping test with a fixture sentence (RTL, diacritics) in the rendered frame. Check: image diff against a golden frame.
6. License table `docs/LICENSES.csv` and the exporter check. Check: test fails when an asset has no licence row.
7. Credential store wrapper (Windows Credential Manager) for provider keys. Check: key round-trips; no key in repo (gitleaks).
8. Draft model and approval flow (draft, approved, scheduled, posted) with tests. Check: unapproved publish is refused.
9. Posting cap and audit log tests. Check: the cap test passes; audit lines are append-only.
10. Dry-run publisher against a mock platform server. Check: mock receives the right payload; no real network call.

## 12. Risks and open questions (defaults)
- Platform API approvals and policy changes: default is drafts-only mode first; check each platform's current rules when connecting ("(unsourced, verify)").
- GPU, disk and time limits on the laptop: default is a render budget and a queue with cleanup.
- Music and stock-media licensing: default is only assets with a recorded licence.
- Competitor and pricing claims: `plans/competitors/sir-content-creation-studio.md` must carry links or "(unsourced, verify)".

## 13. Only the owner can do
Sign in to platform developer consoles and approve app reviews; buy domain and certificate; create payment accounts and paste keys; approve each connected brand account; lawyer review before paid launch.

## 14. Competitor Matrix (from plans/competitors/sir-content-creation-studio.md)
| Competitor | Strengths | Flaws | Our Edge | Ideas to Steal |
|---|---|---|---|---|
| CapCut | Free, templates, auto-captions | Watermark on free, cloud-only, no scheduler | Offline-first, no watermark, local models, scheduler | Template library |
| Canva | Design + video, brand kit | Not video-first, subscription for Pro | Video-first, local render, Arabic RTL | Brand kit |
| (to be sourced) | | | | |

*Every claim in competitor matrix must carry a source link or "(unsourced, verify)".*

## 15. Feature Parity Target (best-in-category)
Match or exceed the best creator tool for: offline-first editing, local AI models, no watermark free export, multi-platform scheduler with approval flow, Arabic RTL captions, Remotion render quality, own logo, owner analytics.