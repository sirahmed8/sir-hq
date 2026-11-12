# PLAN: SIR Portfolio (Wave 7 in WAVE_STUDY, not started)
Audited 2026-11-10. Public site: it is the one SIR project that must be found in search and in AI answers (standard 27, section 4). Commercial items that do not apply (subscription, checkout, owner analytics beyond basics) are n/a below.

## 1. Purpose (plain words)
Ahmed's personal website. One page that says who he is, what he builds, and shows every public SIR product with its real status ("In build", "Beta", "Live"), with links and real screenshots. No hype, no personal data, nothing invented.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Portfolio` |
| GitHub | `sirahmed8/sir-portfolio` (private source; the site is public) |
| Cloudflare Pages project | `sir-portfolio` (`sir-portfolio.pages.dev` until the owner buys a domain). No Firebase: the site has no login |
| Domain | candidate names to check availability and buy by owner: `ahmedalaa.dev` or `sirahmed8.com` (check; price "(unsourced, verify)") |
| Platforms | Web static (Cloudflare Pages) plus one tiny Worker for the contact form; PWA not needed; Windows/Android/iOS/macOS/TV/watch: skipped, a website |
| Money | none; no subscription. Free |

## 3. Current state
Not started. `.sir/CHECKPOINT.md` is still the HQ setup note dated 2026-10-30 ("nothing is built yet"); git log holds only setup and plan commits (9). `legacy/sirahmed8` holds the old GitHub profile README, which this plan says has hype and unprovable claims. No site code exists. The first open task in the project's own list is T-003, the deep scan.

## 4. Rules (each needs a test or command)
1. No personal data on the site: build-time scan for phone, email, address and study patterns fails the build. Contact only through the form.
2. AHome is never listed. Private tools (Study, Jobs, Laptop Manager, Control Room) are unlisted by default. SIR Negm Furniture is the friend's project: listed only after the owner records the friend's OK in `OWNER_ACTIONS.md`.
3. Status badges are generated from `content/products.json`, which is generated from `ops/PORTFOLIO.md` plus each product's `.sir/status.json`. A status above "In build" needs a dated evidence file or a live URL that returns 200 (checked in CI).
4. No fake numbers, testimonials, logos or counts. Test: a lint for banned patterns ("10,000", "trusted by", "8+ applications").
5. Contact Worker: rate limit, honeypot, validation (zod), no email exposed; Turnstile only if spam appears.
6. Cookie banner only if analytics is added; if added it blocks the tracker until consent and has an equal-prominence Reject button. Default: use Cloudflare Web Analytics without cookies, so no banner.
7. CSP without `unsafe-eval`, security headers file verified by `curl -I`.

## 5. Shared pieces (from the shared kit)
`@sir/styles` and `@sir/ui` for tokens, motion and RTL; `@sir/i18n` for ar/en; `@sir/legal-pack` for privacy and cookie pages. Until they exist, use local copies in `packages/` behind the same names. Telegram weekly visibility report via the shared sender. The assistant (if built) uses `@sir/ai-proxy`.

## 6. Pages and entities
Home (one sentence plus the product wall), Products (cards with status), Product detail, Work and writing (real case studies only), Social links, Contact, Privacy, Cookies if needed, Facts page (`/facts`, for AI readers), 404. Entities: Product, SocialLink, Post (markdown), CaseStudy (needs real result and proof).
Five states where data loads, Arabic RTL and English first (Chinese and Hindi later, lowest priority), light/dark/system/contrast, 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI
Optional "ask about Ahmed's work" box answering only from `content/*.json`, refusing personal-data questions, daily quota per visitor, provider fallback through `ai-proxy`, kill switch. Eval: 30 questions (10 personal-data traps) with 100 percent refusal. Default: build it last (M4); the static site is the product.

## 8. Visibility plan (standard 27, owner steps listed)
- Month 0: server-rendered/static HTML, `sitemap.xml`, `robots.txt` allowing legitimate AI crawlers, `llms.txt`, hreflang ar/en, canonical tags, JSON-LD `Person`, `Organization`, `SoftwareApplication` per product (only for products that exist), `BreadcrumbList`. Facts page with dated facts and links.
- Months 1 to 3: one page per public product, a "how I build with AI agents" write-up with real results, GitHub README that links here, honest profile bios on GitHub and LinkedIn that match the site exactly.
- Weekly: script that asks a fixed list of questions about "Ahmed Alaa SIR" in Arabic and English to search and AI tools and logs how the site is described (`scripts/visibility-check.mjs`); wrong descriptions become fix tasks.
- Owner steps: add the site in Google Search Console and Bing Webmaster (sign-in), verify DNS TXT record.
- Honest limit: nobody can promise rank 1; name searches are the realistic first win.

## 9. Operations
Cloudflare Pages deploy on push to main, preview checks, uptime check every 5 minutes with a Telegram alert, monthly link checker, quarterly refresh of the product wall. No support desk; the contact form goes to the owner's mailbox.

## 10. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Deep scan and setup | `.sir/reports/deep-scan.md`; CI green URL; Cloudflare project exists (owner login if needed) |
| M1 | Minimal honest site | Home plus Products wall live on `*.pages.dev`; Lighthouse mobile 95+ (saved JSON); PII scan passes |
| M2 | Detail pages, contact, Arabic/English | contact Worker test passes (rate limit, honeypot); screenshots at 390 and 1280 in LTR and RTL |
| M3 | Visibility foundation | sitemap, robots, `llms.txt`, JSON-LD validated by a schema validator run; facts page |
| M4 | Assistant (optional) | eval 100 percent refusal on personal-data traps |
| M5 | Quality | a11y audit, 4 themes, Lighthouse budgets, e2e for the 3 journeys |
| M6 | Domain and profile | domain connected (owner buys), GitHub profile README replaced and links here, sitemap submitted |

## 11. Next 10 tasks (each under 2 hours)
1. (P-1) Deep scan of `legacy/sirahmed8` and the plan; write `.sir/reports/deep-scan.md` listing claims to drop; create `content/identity.json` with the one canonical founder name (English and Arabic spelling, taken from the verified CV in SIR Jobs `docs/`; the files currently show both "Ahmed Alaa" and "Ahmed Oraby"). Check: file lists each hype claim with a verdict; identity file exists and no page hard-codes a name.
2. Scaffold Astro (or plain Vite static) with tokens and a health script. Files: `apps/web/`. Check: `npm run build` exits 0; dist has HTML for `/` without JavaScript.
3. `scripts/build-products.mjs`: read `ops/PORTFOLIO.md` and `.sir/status.json`, write `content/products.json`, drop private projects. Check: output contains no AHome, Study, Jobs, Laptop Manager.
4. Home page and Products wall with status badges and five states. Check: screenshots at 390 and 1280.
5. PII scan in the build. Files: `scripts/pii-scan.mjs`. Check: failing fixture proves it catches a phone number.
6. Banned-claims lint. Check: fixture with "trusted by 10,000" fails.
7. Security headers file and CSP; test with `curl -I` against preview. Check: header list saved in evidence.
8. Contact Worker with rate limit and honeypot plus tests. Files: `workers/contact/`. Check: tests green; 6th request in a minute returns 429.
9. `sitemap.xml`, `robots.txt`, `llms.txt`, `/facts`, JSON-LD generation. Check: validator output saved; `llms.txt` lists only true facts.
10. Weekly visibility check script (dry run, writes `reports/visibility-YYYY-MM-DD.md`). Check: file produced with the question list.

## 12. Risks and open questions (defaults)
- Showing unfinished products: default is every card says "In build" until proof.
- Ordering: WAVE_STUDY puts this last, but search visibility needs months, so default is ship M1 early (small cost) and fill the wall as products finish. Reported to the manager as a conflict.
- Name and domain availability: default is `.pages.dev` until the owner buys.
- Founder name spelling differs across project files ("Ahmed Alaa" vs "Ahmed Oraby"): default is use the exact name on the verified CV, stored once in `content/identity.json`; never publish an unverified spelling in JSON-LD.
- The old profile README text may still be indexed: default is replace it at M6 and request recrawl.

## 13. Only the owner can do
Buy the domain; sign in to Cloudflare, Google Search Console, Bing Webmaster, GitHub and LinkedIn; confirm which social accounts are public; approve listing the friend's project.

## 14. Market-grade note
Competitor study `plans/competitors/sir-portfolio.md` (portfolio builders and developer sites); price or ranking claims there need links, else "(unsourced, verify)". Privacy law: with no cookies and no stored visitor data, a short privacy page is enough (Egypt PDPL 151/2020 and GDPR basics, reviewed by a lawyer before any analytics or newsletter).
