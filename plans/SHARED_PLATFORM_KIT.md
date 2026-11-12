# SHARED PLATFORM KIT (what every GLOBAL product reuses)
Version: 1.0.0 (living document, updated when a reusable piece is hardened in any product).
One fix reaches all products. Each product builds these as internal `packages/*` first with the Platform names and interfaces, then swaps to `@sir/*` when Platform extracts them (Wave 7). PERSONAL products (SIR Jobs, SIR Study, SIR Laptop Manager, SIR Life Part A, SIR AI Tier 1) use design tokens, motion, i18n, legal-pack patterns only; no auth/billing/ai-proxy needed for single-owner loopback.

---

## 1. Accounts & Authentication (`owner-auth`)
- **Server-verified ID token**: Firebase Auth (Google sign-in), ID token verified on server with JWKS.
- **Owner/admin gate**: allow-list `OWNER_EMAILS`/`OWNER_UIDS`, email verified, fail closed.
- **Session cookie**: HttpOnly, Secure, SameSite=Strict; no localStorage tokens.
- **Rate limits**: on sign-in, AI, and mutating endpoints.
- **2FA offer**: for admin/owner accounts.
- **Test**: forged token → 403; client-side flag flip → no access.

## 2. Billing Readiness (`billing-fallback`)
- **Pricing page**: "Subscriptions launching soon" + email capture (lead stored in Firestore).
- **Currency**: EGP first, USD/SAR/AED toggle auto-detected from visitor locale/IP with manual override (never manual picker as only way).
- **Payment gateway**: Paymob (Egypt), Fawry (Egypt), test mode in code; keys in env only.
- **Subscription state**: server-side only; license cached with grace period (no mid-service lockout).
- **Webhook**: signed with timestamp inside payload, idempotent activation (see `signed-webhook`).
- **Owner permissions**: subscription grants owner all permissions in owner dashboard.
- **Test**: invalid email → error; lead doc created; forged webhook → rejected.

## 3. Owner-Only Analytics Page (every GLOBAL product)
- **Route**: `/owner` (or `/admin` for internal tools).
- **Gate**: server-verified owner token (from `owner-auth`), fail closed.
- **Content**: real metrics only (users, revenue, AI cost, errors, subscriptions, active shops/pitches, downloads, installs, etc.).
- **No other user sees it**: middleware returns 403 for non-owner.
- **Test**: forged token → 403; non-owner token → 403.

## 4. Notifications (`notifications`)
- **Telegram sender**: single shared sender at `_SIR/scripts/deliver/send-telegram.mjs` (token in user env var, never in git).
- **Report format**: title, ≤5 one-fact lines, numbers with meaning, Egyptian Arabic, ends with "المطلوب منك: لا شيء" or single tap.
- **Weekly report**: scheduled at round times (:00 or :30), simple Arabic, per-product metrics.
- **Emergency alerts**: outage, leaked key, cost over cap, auth failure spikes.
- **Bot link flow**: one bot per product, every user links their own account via OAuth (see `bot-link`).
- **Test**: send returns API ok; privacy filter redacts private paths.

## 5. Bot Link Flow (`bot-link`)
- **One bot per product** (not one bot per user).
- **User links account**: OAuth through the app (PKCE where supported), tokens stored server-side or encrypted, never in localStorage.
- **States**: not linked, linking, linked (with account name), syncing, failed with Retry button.
- **Commands**: approval taps for destructive actions, status queries, sync now, unlink.
- **Test**: wrong chat id ignored; unapproved destructive call refused.

## 6. AI Gateway with Fallback Chain (`ai-proxy`)
- **Provider chain** (from `OWNER_DEFAULTS.md` item 11 and `plans/AI_FALLBACK_CHAIN.md`):
  1. Gemini `flash-lite-latest` (free tier)
  2. Gemini `flash` (free tier)
  3. Any Gemini model
  4. OpenRouter free models
  5. Other free providers (Groq, etc.)
  6. Local models (Ollama in `D:\Projects\AI_Models_Hub`)
- **Per-project keys**: each product creates its own API keys on its own Firebase/GCP project and its own OpenRouter key.
- **Routing flags**: `private=true` forces local models; fail closed if local unavailable.
- **Quotas**: free users 5 per rolling 24h with badge; owners unmetered.
- **Kill switch**: `AI_ENABLED` env var per product.
- **Cost cap**: daily cap in `config/limits.json`.
- **Evals**: per-product eval sets (Arabic + English), runner exits non-zero below threshold.
- **Model selection**: newest suitable model from `ops/MODELS.json`.
- **Test**: `private=true` + local off → fail closed; quota badge shows correct count.

## 7. Design Tokens (`design-tokens`)
- **Themes**: light, dark, system, high contrast (WCAG 2.2 AA).
- **Tokens for**: colors, spacing (4/8px grid), radii, shadows, typography, motion.
- **CSS**: logical properties only (margin-inline-start, padding-inline-end, etc.), RTL-first.
- **Bidi**: per-character detection in inputs (Arabic types from right, Latin from left); mixed content uses `<bdi>` or `unicode-bidi: isolate`; never show "(RTL)"/"(LTR)".
- **Touch targets**: minimum 44px.
- **Five states** on every screen: idle, loading skeleton, empty with one action, error with retry, populated.
- **Test**: screenshots at 320, 390, 768, 1280, 1920; LTR/RTL; light/dark/contrast; Lighthouse mobile 90+.

## 8. Motion (`motion`)
- **Spring physics** only (transform and opacity, 120Hz safe).
- **No layout-thrashing animations**.
- **Matching open/close** for every sheet, panel, modal, drawer, overlay.
- **Dynamic Island pattern**: continuous morph, single instance, never covers composer or tab bar.
- **Tab bar**: active label centered in pill, swipe between tabs, sized to text, min 44px.
- **Scroll into view**: active tab scrolls into view on mount and tab change.
- **Test**: reduced-motion path works; no jank at 120Hz.

## 9. Changelog (`changelog`)
- **Format**: `CHANGELOG.md` per product, reverse chronological, grouped by version (stays 1.0.0).
- **Categories**: Added, Changed, Fixed, Security, Removed.
- **Owner-visible**: linked from Settings and Owner dashboard.
- **Auto-generation**: from conventional commits (optional).

## 10. Help Center (`help-center`)
- **Grounded in**: `docs/help/*.md` only (no hallucinated answers).
- **Support assistant**: floating drawer, same component across products.
- **Search**: local index, no external service.
- **Five states**: idle, loading, empty (with "contact support" action), error (retry), populated.
- **Test**: assistant refuses ungrounded answers; eval set with 20 grounded + 10 ungrounded prompts.

## 11. Signed Webhook (`signed-webhook`)
- **Signature**: HMAC-SHA256 with timestamp inside the signed body.
- **Verification**: server-side only; rejects tampered, replayed, unsigned events.
- **Idempotency**: activation keys stored, duplicate events no-op.
- **Test**: 10 negative tests (tampered, replayed, unsigned, wrong timestamp, etc.).

## 12. Legal Pack (`legal-pack`)
- **Generated from**: `data-inventory.yml` (what data is collected, where it goes, retention).
- **Documents**: Privacy, Terms, Refunds (with auto-renewal text), Cookies, DPA, Sub-processors, AI-use note.
- **Marking**: "AI-drafted, to be reviewed by a qualified lawyer before paid launch".
- **Country rules**: Egypt PDPL 151/2020, GDPR, Saudi PDPL, etc. as tasks with "(unsourced, verify)" until sourced.
- **Lawyer review**: mandatory before any paid launch.
- **Test**: all pages exist at `/legal/*`; no fake claims (SOC 2, ISO, etc.).

## 13. Internationalization (`i18n`)
- **Languages**: Arabic (Egyptian dialect) first, English second.
- **RTL-first**: logical CSS, bidi isolation, per-character input detection.
- **Currency/region**: auto-detected from locale/IP, manual override available.
- **Date/time**: prayer-time aware where relevant; `Intl` for formatting.
- **Test**: every screen at 320/390/768/1280 in Arabic RTL and English LTR.

## 14. UI Styles & Hooks (`ui/styles/hooks`)
- **Shared components**: InputBox (chat, AI, voice, search), TabBar, BottomSheet, SidePanel, Modal, Card, Chip, Button, Select, Avatar, Toast, DynamicIsland.
- **Spring config**: shared stiffness/damping for open/close.
- **InputBox**: voice recorder grows out of input with spring; reply preview matches input surface.
- **TabBar**: swipe, centered active label, icon-only inactive, 44px minimum.
- **Card**: 8px grid spacing, no sticking, button labels wrap correctly.
- **Test**: click-target audit (min 44px, no covered hit areas); automated in CI.

## 15. Dual Hosting (every public web product)
- **Firebase Hosting**: primary, custom domain, clean Google sign-in screen.
- **Vercel**: import GitHub repo with Vercel CLI (installed and signed in), same build, same env vars.
- **Verification**: both addresses curl-checked (retry once on timeout); written in checkpoint.
- **DNS**: owner buys domain, points to both (or uses Cloudflare for load balancing).

## 16. Competitor Matrix & Feature Parity (per product)
- **Matrix file**: `plans/competitors/sir-<slug>.md` with columns: Competitor, Strengths, Flaws, Our Edge, Ideas to Steal.
- **Sourcing**: every claim carries a source link or "(unsourced, verify)".
- **Parity target**: match or exceed best-in-category for the product's domain.

## 17. Security Baseline (every product)
- **Firestore rules**: deny by default, per-tenant/per-user claims, emulator tests (cross-tenant read fails).
- **Secrets**: env only, gitleaks in CI, keys in `legacy/` rotated at launch.
- **CSP**: no unsafe-inline/eval; analytics load only after consent; Reject All as prominent as Accept.
- **User data**: deletion and export in one tap each.
- **Graded work**: never done by AI (eval: 100% refusal on assignment/quiz/exam prompts).
- **No fake data**: no mock users, reviews, numbers where users see them.

## 18. Operations Standard 26 (every product)
- Health check endpoint (`/api/health`).
- Error digest (daily/weekly).
- Nightly backup (Firestore → R2/Cloud Storage) with monthly restore test.
- Weekly dependency update with tests.
- Status page (static JSON).
- Support inbox triaged by assistant (grounded in `docs/help`).
- Weekly Telegram report (simple Arabic, product metrics).
- Emergency alerts (outage, leaked key, cost over cap, auth spikes).
- Owner contact only for emergencies and sign-in/payment steps.
- AI daily cost cap and ad spend cap in `config/limits.json`.

## 19. Launch Package Standard 24 (prepared for owner)
- Domain, Cloudflare project, Firebase project (brand-clean Google sign-in), payment accounts (test mode), Play Console later.
- Legal pack generated, marked for lawyer review.
- Code-signing certificate (for desktop apps).
- Dual hosting verified.
- Old site 301 redirects, keys rotated.
- Real content/partners onboarded before invite.

## 20. Visibility Standard 27 (every product)
- Arabic queries first, Egyptian dialect where relevant.
- One landing page per major feature/entity.
- `llms.txt`, facts page, JSON-LD (`WebApplication`, `FAQPage`, `BreadcrumbList`, domain-specific).
- Search Console and Bing steps for owner.
- Weekly AI-answer check script.
- YouTube tutorials (later).
- No fake reviews or user counts.

---

## Adoption Rules
1. When a product hardens a reusable piece, it updates this file and posts one line to `ops/bus/sir-hq.md` so HQ queues the adaptation for others.
2. Products in planning use this file as the spec; products building import from the first finisher's `packages/*`.
3. Platform (Wave 7) extracts the best version into `@sir/*` npm packages after at least two products have consumed them.
4. PERSONAL products adopt: design-tokens, motion, i18n, legal-pack, help-center, ui/styles/hooks, changelog, security-baseline, operations-standard, launch-package, visibility-standard.
5. GLOBAL products adopt: ALL of the above.

---

## Current Consumers (as of 2026-11-12)
| Product | Wave | Tier | Adopted From |
|---|---|---|---|
| SIR Obour Hub | 5 | GLOBAL | (planning) |
| SIR Hagoozat | 5 | GLOBAL | (planning) |
| SIR Business | 5 | GLOBAL | (planning) |
| SIR Content Creation Studio | 4 | GLOBAL | (planning) |
| SIR Controller | 8 | GLOBAL | (planning) |
| SIR ModPack | 6 | GLOBAL | (planning) |
| SIR Mods for GTA V | 6 | GLOBAL | (planning) |
| SIR Life Part B | 6 | GLOBAL | (planning) |
| SIR AI Tier 2 | 4 | GLOBAL | (planning) |
| SIR Jobs | 2 | PERSONAL | design-tokens, motion, i18n, legal-pack, help-center, ui/styles/hooks, security-baseline, operations-standard, launch-package, visibility-standard |
| SIR Study | 2 | PERSONAL | (same as Jobs) |
| SIR Laptop Manager | 2 | PERSONAL | design-tokens, motion, i18n, legal-pack, ui/styles/hooks (extract to Platform) |
| SIR Life Part A | 6 | PERSONAL | (same as Jobs) |
| SIR AI Tier 1 | 4 | PERSONAL | design-tokens, motion, i18n, legal-pack, ui/styles/hooks |
| AHome | 1 | PRIVATE | (separate, but lessons flow to LESSONS.md) |
| SIR Negm Furniture | 3 | CLIENT | plans only |

---

## Version History
- 1.0.0 (2026-11-12): Initial version from r44 portfolio plans upgrade.