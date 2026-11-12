# PLAN: SIR Controller (Wave 8, optional and last, GLOBAL product, not started)

Audited 2026-11-12. Replaces `SIR Controller (v1)` and `SIR Optimizer` (both in `legacy/`, kept until M6). The controller part is derived from the open-source x360ce project, so it is not Ahmed's own work; the optimizer part is his. Whether to sell any of it is decided at M0 by the licence audit.

## 1. Purpose (plain words) and Promise

SIR Controller is a game controller mapper and PC gaming optimizer for Windows gamers. It makes PlayStation, Switch, and wheel controllers work as Xbox controllers in any game, and it scans a Windows laptop explaining in plain words what slows it down. **One-sentence promise**: *Enable any gamer, anywhere, to use any controller with zero setup and zero anti-cheat risk, while their PC runs at peak performance—all with Arabic and English support, five states, and Apple-level motion.*

## 2. Names and IDs

| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Controller` |
| GitHub (private) | `sirahmed8/sir-controller` (legacy repos `sirahmed8/SIR-Controller`, `sirahmed8/sir-optimizer`) |
| Stack (planned) | Mapper: keep existing .NET core (Engine, tests) and decide the UI after a 2 hour spike: WinUI 3 or Tauri v2 in an ADR; Optimizer: .NET 8 or PowerShell engine with a Tauri UI; web portal: Next.js 15+ on Cloudflare Pages |
| Domain | The old plan used `sircontroller.app` and `siroptimizer.com`: neither resolved when last checked (2026-10-29 inventory); owner checks and buys a name; price "(unsourced, verify)" |
| Platforms | **Platform Matrix (GLOBAL):** Windows ✅ (first, both tools); Web portal ✅; macOS ⏭️ skipped (tools use Windows drivers); Linux ⏭️ skipped; Android ⏭️ skipped; iOS ⏭️ skipped; TV ⏭️ skipped; watchOS ⏭️ skipped; Car ⏭️ skipped. Browser extension: skipped. All platforms share the same Firebase project and auth. |
| Money | **Pricing & Free Tier:** Free controller mapping (core x360ce functionality). Pro in EGP for profile sync and the optimizer suite; older strings in the optimizer used 249 EGP/month and 1,999 EGP/year: test prices only, "(unsourced, verify)". EGP first, USD/SAR/AED toggle auto-detected from locale/IP with manual override. "Launching soon" + email capture until keys exist. Owner gets all Pro features free. Subscription grants owner all permissions in owner dashboard. |

## 3. Current state

Not started. `.sir/CHECKPOINT.md` is the HQ setup note; 9 commits, setup and plan only. PORTFOLIO.md: 2 of 20 tasks. Legacy facts (inventories 2026-10-29, nothing run): Controller is a WinForms app on .NET Framework 4.6.2 with about 410 vendored engine files and a commit claiming "298/298 MSTest pass" (unverified); about 20 binaries tracked in git; LGPL-3.0 text sits beside a proprietary EULA that names "SIR Systems LLC" (no evidence this company exists: remove the name unless the owner confirms a real registered entity); three identical generic agent files; download button pointed at a private repo; unsigned webhook and client-side owner gate with a hard-coded email (stopgaps merged separately). Optimizer: any user could flip an owner flag in the client, AI keys in the web bundle, open CORS chat route with no auth, simulated owner transactions, a nested `public_repo/.git`, tracked .exe and .zip files.

## 4. Rules (each needs a test or command)

1. **Licence audit first (M0):** list every vendored component with licence (`docs/THIRD_PARTY.csv`). LGPL-3.0 parts stay replaceable (dynamic link or source offered) and the EULA must not contradict the licence. Selling is allowed only if the audit says so; otherwise the controller stays free and open and only the optimizer is Pro. Legal reading is the lawyer step; "(unsourced, verify)".
2. **Driver-level changes are risky:** ship a read-only scan first. Any change to Windows settings is a dry run with an undo (restore point or saved registry export), tested on a VM.
3. **No binaries in git:** releases hold installers; a CI check fails on files over 5 MB.
4. **Server-side owner and Pro checks only** (verified ID token, allow-list) (use `owner-auth` from SHARED_PLATFORM_KIT). Test: client flag flip changes nothing.
5. **No AI key in any bundle:** chat route authenticated, rate-limited, CORS locked (use `ai-proxy` from SHARED_PLATFORM_KIT).
6. **Webhooks signed with timestamp inside the payload**; idempotent (use `signed-webhook` from SHARED_PLATFORM_KIT).
7. **No fake transactions or numbers in the owner dashboard:** empty states are honest.
8. **The "OP mode" idea** (owner bypass) exists only server-verified for the owner account.
9. **No performance claim without a reproducible benchmark script on named hardware:** no "boosts FPS by X percent".
10. **Owner-only analytics page:** separate route, server-verified owner token, shows all metrics (downloads, installs, scan runs, errors). No other user sees it.

## 5. Features list (on par with best in category + owner's ideas from TickTick and legacy)

**Mapper features:**
- One-click install of ViGEmBus virtual Xbox 360 controller
- Per-game profile editor with button remapping, analog stick deadzone calibration, trigger saturation
- Test pad for verifying mappings in real time
- Profile per-game switching based on active window detection
- Settings and Profile tabs with save/load

**Optimizer features:**
- Read-only scan of startup items, disk free space, power plan, and network latency
- Plain-language findings explaining what slows down gaming
- Fix with preview and undo (`.reg` delta backups before any system modification)
- Sub-millisecond Windows timer resolution (0.5ms) via `timeBeginPeriod(1)`
- Nagle algorithm disablement for TCP/online gaming
- Network adapter configuration (`TcpAckFrequency=1`, `TCPNoDelay=1`)
- Safe-mode anti-cheat guard: detects competitive game processes and restricts tweaks to certified safe OS timer resolution only
- Ultra-lightweight daemon: under 25MB RAM and 0.1% CPU when idling, `CREATE_NO_WINDOW = 0x08000000`
- Permanent free core tier: zero adware, zero bundled toolbars, zero telemetry tracking

**Owner ideas from TickTick and legacy:**
- Arabic RTL first UI with English; bidi-isolated mixed text inputs
- Five states on every screen: idle, loading skeleton, empty with one action, error with retry, populated
- Spring physics motion (transform and opacity only, 120Hz safe)
- High-contrast tactile UI with zero yellow buttons
- Device list with one-click install and profile preview
- Dashboard showing scan findings, fix history, and profile per-game
- "Why is my game stuttering?" support assistant grounded in known issues

## 6. Platform matrix (Web, Windows, macOS, Linux, Android, iOS, Wear OS, watchOS, TV, car)

| Platform | v1 inclusion | Notes |
|---|---|---|
| Windows | ✅ Both tools (mapper + optimizer) | Primary platform; .NET 8 / Tauri v2 desktop client |
| Web portal | ✅ Landing, Downloads, Pricing, Privacy/Terms/Refunds, Owner dashboard | Next.js 15+ on Cloudflare Pages; dual-hosted Firebase + Vercel |
| macOS | ⏭️ skipped | Tools use Windows drivers; no native port |
| Linux | ⏭️ skipped | No x360ce / ViGEm support |
| Android | ⏭️ skipped | Controller mapping via OTG; not v1 scope |
| iOS | ⏭️ skipped | Apple MFi restrictions; not v1 scope |
| Wear OS | ⏭️ skipped | Not applicable |
| watchOS | ⏭️ skipped | Not applicable |
| TV | ⏭️ skipped | Big-screen not v1 |
| Car | ⏭️ skipped | Not applicable |

## 7. Architecture on the shared kit (plans/SHARED_PLATFORM_KIT.md)

**Reuses SHARED_PLATFORM_KIT entirely**; only controller/optimizer features differ.

- **Accounts & Authentication (`owner-auth`):** Firebase Auth (Google sign-in), ID token verified on server with JWKS; owner/admin gate allow-list `OWNER_EMAILS`/`OWNER_UIDS`, email verified, fail closed; session cookie HttpOnly, Secure, SameSite=Strict; rate limits on sign-in and AI endpoints; 2FA offer for owner accounts.
- **Owner-Only Analytics Page (every GLOBAL product):** Route `/owner`, gate server-verified owner token (from `owner-auth`), fail closed. Content: real metrics only (downloads, installs, scan runs, errors, subscriptions). No other user sees it; middleware returns 403 for non-owner.
- **AI Gateway with Fallback Chain (`ai-proxy`):** Provider chain: 1. Gemini `flash-lite-latest` (free tier), 2. Gemini `flash` (free tier), 3. Any Gemini model, 4. OpenRouter free models, 5. Other free providers (Groq, etc.), 6. Local models (Ollama in `D:\Projects\AI_Models_Hub`). Per-project keys; routing flags `private=true` forces local models; fail closed if local unavailable; free users 5 per rolling 24h with badge; owners unmetered; kill switch `AI_ENABLED` env var per product; daily cost cap in `config/limits.json`; evals with Arabic + English sets.
- **Billing Readiness (`billing-fallback`):** Pricing page "Subscriptions launching soon" + email capture (lead stored in Firestore); currency EGP first, USD/SAR/AED toggle auto-detected from visitor locale/IP with manual override; payment gateway Paymob (Egypt), Fawry (Egypt), test mode in code; keys in env only; subscription state server-side only with grace period; webhook signed with timestamp inside payload, idempotent activation; subscription grants owner all permissions in owner dashboard.
- **Design Tokens (`design-tokens`):** Themes: light, dark, system, high contrast (WCAG 2.2 AA). Tokens for colors, spacing (4/8px grid), radii, shadows, typography, motion. CSS logical properties only (margin-inline-start, padding-inline-end, etc.), RTL-first. Bidi: per-character detection in inputs; mixed content uses `<bdi>` or `unicode-bidi: isolate`; never show "(RTL)"/"(LTR)". Touch targets: minimum 44px. Five states on every screen: idle, loading skeleton, empty with one action, error with retry, populated.
- **Motion (`motion`):** Spring physics only (transform and opacity, 120Hz safe). No layout-thrashing animations. Matching open/close for every sheet, panel, modal, drawer, overlay. Dynamic Island pattern: continuous morph, single instance, never covers composer or tab bar. Tab bar: active label centered in pill, swipe between tabs, sized to text, min 44px. Scroll into view: active tab scrolls into view on mount and tab change.
- **Signed Webhook (`signed-webhook`):** Signature: HMAC-SHA256 with timestamp inside the signed body. Verification: server-side only; rejects tampered, replayed, unsigned events. Idempotency: activation keys stored, duplicate events no-op.
- **Changelog (`changelog`):** Format: `CHANGELOG.md` per product, reverse chronological, grouped by version (stays 1.0.0). Categories: Added, Changed, Fixed, Security, Removed. Owner-visible: linked from Settings and Owner dashboard.
- **Help Center (`help-center`):** Grounded in `docs/help/*.md` only (no hallucinated answers). Support assistant: floating drawer, same component across products. Search: local index, no external service. Five states: idle, loading, empty (with "contact support" action), error (retry), populated.

## 8. Premium quality bar (Apple-level motion, Arabic and English, five states, accessibility)

- **Themes:** light, dark, system, high contrast (WCAG 2.2 AA)
- **Motion:** Spring physics only (transform and opacity, 120Hz safe). No layout-thrashing animations. Matching open/close for every sheet, panel, modal, drawer, overlay. Dynamic Island pattern. Tab bar with active label. Scroll into view.
- **Arabic and English:** RTL-first layout with logical CSS properties. Bidi-isolated mixed text in inputs (Arabic types from right, Latin from left); mixed content uses `<bdi>` or `unicode-bidi: isolate`; never shows "(RTL)"/"(LTR)" suffixes. All labels and error messages available in both Arabic and English.
- **Five states on every screen:** idle, loading skeleton, empty with one action, error with retry, populated. Empty states show a real action (not "no data"). Error states have a retry button and a neutral message.
- **Accessibility:** 44 px touch targets. Color contrast: WCAG 2.2 AA. High contrast mode support. No emoji headers. No gradient hero text. No pill-everything. Real icons (SVG). Glass or tonal surfaces per design tokens.
- **Proof:** Screenshots at 320, 390, 768, 1280 and 1920 px; LTR/RTL; light and dark; Lighthouse mobile 90+. WCAG contrast measured by browser audit probe. No horizontal overflow at any viewport.

## 9. First 10 tasks (ready to hand to free agents, title + one-paragraph brief each)

See `ops/briefs/sir-controller-tasks.md` for the full task listings. These tasks are scoped to under 2 hours and work in `D:\Projects\SIR Controller` (app code) and write reports/evidence only inside that project or `D:\Projects\_SIR\ops\`. Version stays 1.0.0. No placeholders, no invented data, every screen keeps five states, Arabic RTL and English, 44 px touch targets, bidi-isolated mixed text.

**Task 1 - Inventory vendored components:** Read legacy engine files and inventory `ops/inventory/SIR-Controller.md`; produce `.sir/reports/vendored-inventory.md` listing every component with licence column. Done when: every vendored folder has a row with licence; exits non-zero if any component missing licence.

**Task 2 - Write LICENSE_DECISION.md:** Write `docs/LICENSE_DECISION.md` citing what may be sold, what stays free, and which licence file paths support this. Done when: file cites each licence file path; `npm test` green.

**Task 3 - Remove binaries from new repo layout, add size check script:** Remove all binaries from the new repo layout; add `scripts/check-size.mjs` that fails on a 6 MB test file. Done when: size check script fails on 6 MB test; CI passes.

**Task 4 - UI spike ADR (WinUI 3 vs Tauri):** 2-hour spike measured against size and start time; write `docs/adr/001-ui.md` with decision. Done when: ADR has numbers present for both options.

**Task 5 - Optimizer read-only scan v0:** Write `apps/optimizer/engine/scan.ps1` or `.cs` that outputs startup items, disk free, power plan as JSON. Done when: JSON output passes schema validation; `npm test` green.

**Task 6 - Plain-words explanation for mapper findings:** Write unit tests for 10 findings (rules, no AI) in Arabic and English; implement explanation logic that never changes anything itself. Done when: unit tests pass for 10 findings both languages.

**Task 7 - Portal scaffold with owner check:** Create Next.js portal with landing, downloads, pricing, and `/owner` route that returns 403 on client flag flip. Done when: client flag flip test returns 403; owner route shows metrics with verified token.

**Task 8 - Signed webhook package with 10 negative tests:** Create signed webhook package; implement 10 negative tests (tampered, replayed, unsigned, wrong timestamp, etc.). Done when: tests green.

**Task 9 - Honest-claims lint for site and README:** Lint that fails on "boost", "100%" without a linked benchmark. Done when: lint fails on claim without benchmark; passes on claims with linked benchmark.

**Task 10 - Honest claims lint for README:** Same as task 9 but specifically for README.md. Done when: README passes lint with only benchmark-linked claims.

## 10. Risks and open questions (defaults)

- Third-party and AGPL/LGPL obligations: default is keep the mapper free and open if the audit is unclear.
- Console-brand trademarks (PlayStation, Xbox): default is nominative use only with a "not affiliated" notice.
- Driver and registry changes can brick a setup: default is read-only until undo is proven on a VM.
- Competitor claims (x360ce itself, DS4Windows, Steam Input, vendor tools): `plans/competitors/sir-controller.md` must carry links or "(unsourced, verify)".
- Domain and certificate cost: owner may delay buying `sircontroller.app` and code-signing certificate.

## 11. Only the owner can do

Decide to sell or not after the licence note; buy domain and certificate; create payment accounts; test with real controllers (he must plug them in); lawyer review.

## 12. Competitor matrix reference

See `ops/competitors/sir-controller.md` for the 10-competitor matrix with strengths, flaws, our edge, and ideas to steal (each with source link or "(unsourced, verify)").

## 13. Feature parity target

Match or exceed the best controller tool for: one-click install, per-game profiles, test pad, read-only optimizer with undo, plain-language explanations, Arabic RTL, signed installer, owner analytics, no fake claims.