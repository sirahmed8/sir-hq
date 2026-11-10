# PLAN: SIR Content Creation Studio (Wave 4, public product, not started)
Audited 2026-11-10. Replaces `SIR Content Creation Studio (v1)` (in `legacy/`, kept until M6). Free local editing, paid cloud queue and scheduler in EGP. It also runs the owner's brand-channel publishing, so it doubles as the engine for standard 26 marketing of the other products.

## 1. Purpose (plain words)
A desktop program that turns an idea into a short vertical video (Shorts, Reels, TikTok) or a longer video: script, voice, captions, footage or images, music, render. It can schedule posts to a brand's accounts through the platforms' official APIs, always with a human-approved draft first.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Content Creation Studio` |
| GitHub (private) | `sirahmed8/sir-content-creation-studio` |
| Stack (planned) | Electron + Vite + React shell, local engine Python 3.12 (FastAPI on 127.0.0.1) with Remotion for rendering, one Python version pinned everywhere (legacy had 3.10, 3.11 and 3.13 mixed); web dashboard on Cloudflare Pages for the scheduler |
| Domain | candidate `sirstudio.app` (owner checks and buys; price "(unsourced, verify)"); `pages.dev` until then |
| Platforms | Windows desktop (first), web dashboard; macOS and Linux Electron builds: later, only if a user asks; Android/iOS: skipped; browser extension: skipped |
| Money | Free local editing with a watermark-free export; Pro in EGP for the cloud render queue and the scheduler (price to test, "(unsourced, verify)"); "subscriptions launching soon" + email capture until keys |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is the HQ setup note (2026-10-30); 9 commits, all setup/plan. PORTFOLIO.md: 2 of 19 tasks.
Legacy facts (`ops/inventory/SIR-Content-Creation-Studio.md`, 2026-10-29, tests not run): 120 test files; personal state tracked in git (profile, uid, pro flag, `studio.db`, audio files); no server-side token check (owner by env in 6 files); unsigned installer older than the last source commit; CI failing; Python version mismatch; no social publishing code exists (the "ByteVibeHQ publishing" idea has no spec). Treat all legacy claims as unverified.

## 4. Security and conduct rules
1. Personal state files are not tracked; history purge for the legacy repo happens at M6 (owner action only if a rewrite is needed).
2. Pro and owner checks are server-side (verified ID token, allow-list). Test: forged local `.studio_pro.json` unlocks nothing.
3. Provider keys live in the OS credential store (desktop) or server secrets, never in the renderer bundle or git.
4. Publishing: official APIs only, human-approved draft, a posting rate cap per account, an audit log. No engagement bots, no automated likes, follows or comments, no fake accounts, no scripting X's website, no CAPTCHA bypass. Tests: scheduler refuses to publish an unapproved draft; refuses more than the cap.
5. Brand voice accounts post as the brand; they never pose as Ahmed in live conversations.
6. Media rights: every music, font, stock clip and model used has a licence entry in `docs/LICENSES.csv`; the exporter refuses an asset with no licence. AI-generated media labeled where a platform requires it.
7. Remotion licence terms for commercial use: "(unsourced, verify)" at M0; default is read the official licence page and record the answer before selling Pro.
8. Local-only mode works offline with local models; nothing is uploaded without a visible switch.

## 5. Shared pieces
Platform `owner-auth`, `ai-proxy` (script/voice providers with fallback), `billing-fallback`, `legal-pack`, `i18n`, `ui`, Telegram sender (approval taps for posts). The scheduler and approval flow here is also the engine other plans call for their own marketing calendars; do not build another scheduler in other products. Laptop Manager's game mode must be able to pause renders (small endpoint).

## 6. Screens and entities
Home (projects), Idea to script, Storyboard/timeline, Voice and captions, Media library, Render queue, Schedule (calendar of drafts, approved, posted), Accounts, Analytics (real numbers from APIs only), Pricing, Settings and Profile, Help. Entities: Project, Scene, Asset, License, RenderJob, Draft, ScheduledPost, Account, AuditEntry, Subscription.
Five states, Arabic RTL (captions with correct Arabic shaping) and English, themes, 320 px to 4K for the dashboard, WCAG 2.2 AA, own logo.

## 7. AI
Script writer, caption translator, voice (local TTS first, provider fallback), thumbnail suggestions. Chain via `ai-proxy`, cost cap per day, kill switch; evals: caption accuracy on 20 Arabic clips (word error rate recorded), script safety (no false claims in sample health or finance prompts: refuses). Support assistant grounded in docs; free users 5 per day; owner unmetered.

## 8. Operations
Render failure alerts, disk-space guard (render budget and cleanup), weekly Telegram report (renders, posts published, errors, cost), update channel with signed installer (owner certificate), status JSON for the dashboard.

## 9. Launch, legal and visibility
Owner buys domain, code-signing certificate, payment accounts, platform developer app approvals (YouTube, Meta, TikTok review queues take time; keep drafts-only mode until approved). Legal pack: privacy, terms, refunds, DPA, sub-processors, AI-output disclosure, DMCA process. Visibility: Arabic queries ("برنامج عمل فيديوهات ريلز"), tutorial videos made with the product itself, comparison pages once sourced, `llms.txt`, facts page.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Deep scan, setup, CI | scan report; one Python version pinned; green Actions URL; Remotion licence answer recorded |
| M1 | Core slice | script to 15 second rendered MP4 with captions on the laptop; render time recorded |
| M2 | Parity | feature checklist from legacy ticked; media library with license table |
| M3 | Security, legal, billing | token tests, unapproved-publish test, billing fallback test |
| M4 | AI | caption word error rate and script safety evals recorded |
| M5 | Quality | screenshots, offline test, a11y, installer smoke test on a clean profile |
| M6 | Release | signed installer (owner), scheduler live for one brand account in drafts-then-approved mode |

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
