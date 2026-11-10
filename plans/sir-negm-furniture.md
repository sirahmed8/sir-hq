# PLAN: SIR Negm Furniture (friend's project)
**PLANS ONLY, NO BUILD WORK, CHAT, CI OR DEPLOY UNTIL THE OWNER SAYS SO** (AGENTS.md, 2026-11-09). This file may be improved; the code folder must not change. Nothing here was run by the audit.
Client brand: the public name stays Negm Furniture. Ahmed builds it as a favour for a friend; no accounts are created in Ahmed's name for the client, and the client owns the final cloud projects at handover. Commercial items for Ahmed (his subscription, his marketing, his SEO plan) do not apply; the client's own online presence does, so those items are written as a handoff pack for the client.

## 1. Purpose (plain words)
A bilingual (Arabic and English) website for a furniture showroom. Visitors browse the catalog, see the two showrooms, plan a room in 2D and 3D with real products, and send a quote request on WhatsApp.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Negm Furniture` |
| GitHub (private) | `sirahmed8/sir-negm-furniture` (delivery channel to the friend) |
| Layout | `apps/web` (Next.js), `packages/planner-engine` (pure geometry), `reference-source`, `docs`, `HANDOFF.md`, `FRIEND_AGENT_PROMPT.md` |
| Domain | the client buys and owns it; candidate chosen by the client |
| Platforms | Web (Cloudflare Pages, static plus Workers API) and PWA install. Android, iOS, Windows, macOS, TV, watch: skipped, a showroom site |
| Money | client service, no subscription. Ahmed's fee, if any, is a separate agreement outside the code |

## 3. Current state (read from files, not re-run)
Claimed in `.sir/CHECKPOINT.md` (2026-11-08): M0, M1, M4, M5 shipped: pure geometry engine with 11 tests, 2D blueprint canvas with grid and rotation snapping, 3D view, catalog drawer wired to `PRODUCTS` data, bill of materials and WhatsApp quote modal with EGP prices, planner route, desktop and mobile screenshots, "175/175 tests green, typecheck clean, gitleaks clean". PORTFOLIO.md: 12 commits, 8 of 16 tasks. All of this is **built, unverified**.
Rule conflict to note: the plans-only rule is dated 2026-11-09, after this build work (2026-11-08). The folder is therefore frozen as it is. The CI workflow was added and then reverted in git history; CI state is unknown.
Open items seen: lead capture form with server validation and rate limit (T-011) and App Check, security rules and production headers (T-030) are next in the checkpoint but not done.
Facts to confirm with the client before launch: product list, prices and photos (who owns the images), showroom addresses and opening hours, WhatsApp number, whether a decor AI assistant is wanted. Ratings and follower counts from the old site were fabricated and must not return.

## 4. Security and conduct rules (for the build later)
1. Admin only through a server-verified token with an allow-list; no client-only admin; no fake login user.
2. No fabricated social proof: no ratings, review counts or follower counts unless they come from a real source the client controls, shown with the source.
3. Lead form: server validation (zod), rate limit, honeypot, spam check, stored in the client's own project; the client's contact numbers are not hard-coded in public JS beyond the WhatsApp click link they asked for.
4. Image licences confirmed in writing with the client; no stock images with unclear licences.
5. CSP without `unsafe-eval`, security headers, gitleaks.
6. The client's Firebase/Cloudflare projects are created by the client (or with the client's sign-in) at handover, never inside Ahmed's accounts.

## 5. Shared pieces
Use Platform `ui/styles/hooks`, `i18n`, `legal-pack`, `owner-auth` (client admin) and Telegram sender only when the owner says build work starts. The planner engine stays in this repo (nobody else needs it).

## 6. Screens and entities
Home, Catalog, Product, Showrooms, Room planner (2D, 3D, quote), Inquiry form, Admin catalog, Legal. Entities: Product, Category, Showroom, Inquiry, AdminUser, PlannerLayout.
Five states, Arabic RTL first and English, 320 px to 4K, WCAG 2.2 AA, client logo.

## 7. AI
Optional decor assistant with an offline rule engine as fallback, server route with quota, grounded only in the client's catalog; evals in Arabic and English; kill switch. Default: do not build until the client asks for it.

## 8. Operations (client handoff pack)
A one-page runbook for the client: how to edit products, how to read inquiries, where the backups are, who to call. Uptime check and monthly link check run by the owner's tools only if the owner agrees. Weekly Telegram line to Ahmed only (not to the client).

## 9. Visibility and legal (client handoff, advice only)
Local SEO for a showroom: Google Business Profile for each showroom (client sign-in), consistent name/address/phone, Arabic and English landing pages per product category, `Product` and `LocalBusiness` JSON-LD from real data, sitemap, `llms.txt`, facts page. Legal: privacy page covering the inquiry form and WhatsApp click, cookie notice only if analytics is added. All "AI-drafted, to be reviewed by a qualified lawyer".

## 10. Milestones with exit checks (apply only after the owner lifts the freeze)
| M | Goal | Exit check |
|---|---|---|
| M0 | Re-verify the frozen state | `scripts/verify.ps1` output saved; claimed 175 tests counted |
| M1 | Lead capture and headers | form test with rate limit; `curl -I` header list |
| M2 | Catalog from real data | client-approved product file; no fabricated numbers (grep test) |
| M3 | Security | rules and token tests; gitleaks clean |
| M4 | Planner polish | keyboard use, touch use, 320 px layout, screenshot set |
| M5 | Quality | Lighthouse mobile 90+ saved JSON; RTL/LTR screenshots |
| M6 | Handover | client owns domain, Cloudflare and Firebase; `HANDOFF.md` steps followed once by the client |

## 11. Next 10 tasks (frozen until the owner says; each under 2 hours when unfrozen)
1. Run `scripts/verify.ps1` and save the output. Files: `.sir/evidence/verify.md`. Check: counts match or the difference is written down.
2. Grep test that fails on "4.95", "38 reviews", "285" and similar fabricated proof. Files: `scripts/check-no-fake-proof.mjs`. Check: passes on the repo, fails on an injected line.
3. Lead capture form with zod validation and honeypot (T-011). Files: `apps/web/src/app/api/lead/`. Check: tests for valid, invalid and flood.
4. Rate limit helper tests. Check: sixth request in a minute returns 429.
5. Security headers file and CSP. Check: header list via `curl -I` on preview.
6. Product data review sheet for the client (CSV of products, prices, image sources). Files: `docs/client-review.csv`. Check: every row has an image source field.
7. Planner keyboard controls (move, rotate, delete) with tests. Check: engine tests plus a keyboard e2e.
8. Planner touch handling at 390 px (pinch, drag). Check: screenshot and no horizontal scroll.
9. Client handoff checklist in plain Arabic with exact clicks (domain, Cloudflare, Firebase, Google Business Profile). Files: `HANDOFF.md`. Check: another person can follow it (owner to ask the friend).
10. Visibility foundation: sitemap, JSON-LD generator from real data, `llms.txt`. Check: validator output saved.

## 12. Risks and open questions (defaults)
- The freeze: default is no code change until the owner lifts it; only this plan is edited.
- Image and product rights: default is use only client-supplied images with written permission.
- Quote prices in the planner may become wrong: default is every quote says "estimate, confirmed by the showroom".
- WhatsApp deep link behavior differs by device: default is test on one Android and one iPhone before handover.
- Market claims: `plans/competitors/sir-negm-furniture.md` must show links or "(unsourced, verify)".

## 13. Only the owner (and the client) can do
Lift the freeze; talk to the friend about scope; the client signs in to create Cloudflare, Firebase, Google Business Profile and domain accounts and pays for them; the client confirms prices, photos and legal wording.
