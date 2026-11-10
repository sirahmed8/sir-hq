# SIR VISIBILITY PLAN: SEO, AI ANSWERS, STORES (rewritten 2026-11-10 by the plans audit)
Standard: 27. Scope: public products and SIR Portfolio. Private and internal projects are unlisted and noindex (section 7). Nothing here is live today: no public site exists yet, so every item is a task with a gate (the product's plan reaches M1 with a public URL).
Honest limit: nobody can promise rank 1 against large companies. The realistic wins are niche Arabic and Egyptian queries, long-tail intent, brand-name searches, speed, real content and real authority. White-hat only: no fake reviews, no link schemes, no cloaking, no spam, no fake engagement.

## 1. Entity and name consistency (do first, it costs nothing)
- The founder's name appears as "Ahmed Alaa" (package.json author, plans) and "Ahmed Oraby" (CV file names, earlier visibility text). Default decision: Portfolio task P-1 stores one canonical string and its Arabic spelling in `content/identity.json`, taken from the owner's verified CV; every page, JSON-LD block, GitHub bio and `llms.txt` reads from it. Until then do not publish either spelling in structured data.
- Product names are fixed as the plan titles ("SIR Hagoozat"). One facts page per product, one canonical domain, the same description sentence everywhere.

## 2. Keyword and intent map (starting points to check in a keyword tool; volumes are unknown, so none are claimed)
| Product | Arabic intents | Egyptian wording to test | English intents |
|---|---|---|---|
| SIR Hagoozat | حجز ملعب خماسي، حجز ملاعب كرة قدم، تأجير ملعب | احجز ملعب كورة، ملاعب قريبة مني | book a five-a-side pitch in Cairo, football pitch rental Egypt |
| SIR Business | برنامج كاشير للسوبر ماركت، برنامج مبيعات ومخازن، برنامج كاشير مطعم | كاشير للمحلات بالجنيه | POS software for small shops Egypt (e-invoicing terms only after it is built) |
| SIR Obour Hub | ملخصات معهد العبور، حاسبة المعدل التراكمي، جدول محاضرات | شيتات العبور | Obour institute notes, GPA calculator |
| SIR Content Creation Studio | برنامج مونتاج فيديو بالذكاء الاصطناعي، جدولة منشورات | عمل ريلز بسرعة | AI short video maker with Arabic captions |
| SIR AI (Tier 2) | مساعد ذكاء اصطناعي محلي على الكمبيوتر | شات بوت يشتغل من غير نت | local AI assistant for Windows |
| SIR Controller | تشغيل يد بلايستيشن على الكمبيوتر، محاكي يد إكس بوكس | يد بلايستيشن على الكمبيوتر | use a PlayStation controller on PC |
| SIR ModPack | مودات ماينكرافت بالعربي | مود باك ماينكرافت | Arabic Minecraft modpack installer |
| SIR Life Part B | تطبيق مواعيد الصلاة والعادات | | prayer times and habit tracker app |
| SIR Portfolio | the founder's name (section 1) and "SIR" product names | | same |
SIR Mods for GTA V: no visibility work until its licence gate passes. SIR Negm Furniture: advice only in the client handoff (local SEO for a showroom, Google Business Profile, product pages with real data).

## 3. Technical SEO checklist (every public site; each item is a test or a command)
- Static or server-rendered HTML for all public pages; check with `curl` that the main text is in the HTML without JavaScript.
- Core Web Vitals budgets: Lighthouse mobile performance 90 or more on home and one product page, results saved as JSON in the repo.
- `sitemap.xml`, `robots.txt` (allow legitimate search and AI crawlers; the owner may change this), canonical tags, `hreflang` for `ar-EG`, `ar` and `en`, clean URLs, 404 page, redirect map.
- Structured data validated with a schema validator run in CI: `Organization`, `SoftwareApplication` or `MobileApplication` (price offers only with the real price), `FAQPage`, `HowTo`, `BreadcrumbList`, `Person` on the Portfolio. `Review`/`AggregateRating` only with real reviews from a real platform. Author name from `content/identity.json` (not hard-coded).
- Security headers and no mixed content; image alt text; internal links; one H1 per page.
- Search Console and Bing Webmaster verification by the owner (DNS TXT record); Google Business Profile only for real local businesses (client showrooms).

## 4. AI answer engines (GEO)
- `/llms.txt` per public site: the product in one honest sentence, what is built today, platforms, price (only the real current one), privacy summary, links to facts and docs. Template, with no superlatives and nothing not yet true:
```text
# SIR Hagoozat
> Pitch booking and split payment for five-a-side football in Egypt. Status: in build.

## What it does today
- (list only verified features, each with the date it was verified)

## Price
- Free for players. Paid plans: not yet launched.

## Links
- Facts: https://<domain>/facts
```
- `/facts` page: first sentence "[Product] is a [category] for [audience] that [benefit]"; table of what it does and does not do; platforms; pricing; privacy; changelog link; founder link; dated and sourced numbers only. A comparison table against named competitors only when `plans/competitors/<slug>.md` has linked sources for each cell.
- Authority: GitHub README and docs, honest posts in communities in the brand's name following each site's rules, YouTube tutorials with transcripts, directories we truly qualify for, press kit (`MARKETING_PLAN_ALL.md` section 5). No bought mentions.
- Wrong descriptions found by the weekly check become fix tasks: update the facts page, publish a clearer source, request a correction where a form exists.

## 5. Weekly visibility check
`scripts/check_ai_visibility.py` is NOT built. The earlier file text contained a stub that printed "Completed audit" without checking anything; that is removed. Spec for the real script (task V-1):
- Input: `config/visibility-queries.json` with 5 to 10 queries per public product in Arabic and English (examples: "أفضل تطبيق حجز ملاعب في مصر", "Ahmed ... SIR products" using the canonical name).
- Method: use official search APIs or the assistants' official APIs where a free or owner-funded key exists; otherwise a manual checklist the owner or a computer-use agent fills in; never scrape against a site's terms and never bypass a CAPTCHA.
- Output: `ops/visibility-weekly.json` with date, query, engine, whether the product was named, the exact description text, and the source URLs cited.
- Report: weekly Telegram line in simple Arabic: mentions found, wrong descriptions, next fix.
Acceptance: running it twice on a fixture file with two fake engine replies produces the expected JSON (unit test).

## 6. App stores and video
ASO per store listing prepared for the owner: title, subtitle, keywords, screenshots with captions in Arabic and English, privacy labels that match the real data use, fair rating prompts, review replies. YouTube: one channel per brand, install and how-to videos with chapters and transcripts, titles tested on click-through. Store accounts and publishing are owner steps.

## 7. Private and internal projects (noindex)
AHome, SIR Study, SIR Jobs, SIR Laptop Manager, SIR Control Room, SIR Platform docs: no listing, `robots.txt` `Disallow: /`, `meta name="robots" content="noindex, nofollow"` wherever any page is reachable, no sitemap, no `llms.txt`. SIR Life Part A is private; only Part B (public app) is listed. SIR Negm Furniture visibility belongs to the client.

## 8. Cadence
Month 0: foundation (identity file, facts pages, sitemap, `llms.txt`, schema, Search Console and Bing). Months 1 to 3: one pillar page and one comparison or alternatives page per product (only with sourced competitor facts), weekly check, first honest mentions. After that: monthly content, quarterly competitor refresh, continuous mention building. The manager reports ranks, AI-answer presence and traffic weekly on Telegram.
