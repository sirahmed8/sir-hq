# SIR MARKETING AND GROWTH PLAN (rewritten 2026-11-10 by the plans audit)
Standards: 26 (autonomous operations) and 27 (visibility). Scope: public products only. AHome, SIR Study, SIR Jobs, SIR Laptop Manager, SIR Control Room and the shared kit get no marketing (private or internal). SIR Negm Furniture is the friend's brand: Ahmed gives the client advice in the handoff pack but runs no campaigns for it.
Truth rules for all copy: no number, user count, review, logo or "verified" badge unless it is real and linked. No claim about a feature that is not built and verified (the lines below say "planned" until then). No em-dashes, no hype words, no emoji. Banned words: seamless, robust, empower, elevate, harness, unleash, delve, game-changing, cutting-edge.
Gate: a product's marketing starts only when its plan has passed M5 (quality sweep) and a reviewer verified the main journey on the same day. Before that, only a waitlist page with an honest "in build" status and the visibility foundation (sitemap, `llms.txt`, facts page) may exist.

## 1. Positioning (all items are drafts; every claim marked "planned" is not yet true)
| Product | Arabic line (draft) | English line (draft) | First audience | Status of the claim |
|---|---|---|---|---|
| SIR Hagoozat | احجز ملعب خماسي واقسم السعر بين اللاعبين | Book a five-a-side pitch and split the price | amateur football players and pitch owners in one area of Cairo or Giza | booking and split bill planned |
| SIR Business | كاشير ومخزون للمحل بالجنيه، يشتغل بدون إنترنت | Cash register and stock for small shops, works offline | owners of small supermarkets and restaurants | offline POS planned; e-invoicing planned later, do not mention until built |
| SIR Education Hub | ملخصات ومواعيد ومعدل تراكمي لطلاب معاهد العبور | Notes, timetable and GPA planner for Obour students | Ahmed's classmates first | planned |
| SIR Content Creation Studio | اعمل فيديو قصير من فكرة في دقائق | Make a short video from an idea | small creators and brands, Arabic first | planned |
| SIR AI (Tier 2 only) | مساعد يشتغل على جهازك ويحافظ على خصوصيتك | An assistant that runs on your PC and keeps your data local | privacy-minded power users | planned, Tier 1 is private |
| SIR Controller | شغّل يد التحكم في أي لعبة على الكمبيوتر | Make any controller work in any PC game | PC gamers | mapper derived from x360ce; no FPS claim |
| SIR ModPack | حزمة مودات ماينكرافت بنقرة واحدة بالعربي | One-click Minecraft modpack with an Arabic guide | Arabic-speaking Minecraft players | planned, subject to Mojang rules |
| SIR Mods for GTA V | gated by licence check, no marketing until M0 passes | | | gate |
| SIR Life (Part B) | خطط يومك مع مواعيد الصلاة والعادات | Plan your day with prayer times and habits | students | planned |
Audience sizes: none stated here. Any market-size number must come from a linked source in `plans/competitors/<slug>.md`, otherwise "(unsourced, verify)". The earlier "15,000+ students" line is removed (unsourced).

## 2. Launch calendar template (L = the day a product passes its launch gate)
This is a template; each product gets its own dated copy in its `docs/launch-calendar.md` after the gate.
- L minus 14 to L: waitlist with email capture (consent text, 1-click unsubscribe, physical address in the footer from the owner's real details), facts page, `sitemap.xml`, `robots.txt`, `llms.txt`, three real screenshots, one 45 second screen recording of the real product (made with SIR Content Creation Studio when it exists, otherwise a screen recorder).
- L: announce to the waitlist and personal network first. Public launch posts on developer or maker sites only where the rules allow self-promotion; read each site's rules the same day "(unsourced, verify)". Post as the brand, not as Ahmed in replies.
- L+1 to L+7: answer every message within 24 hours (assistant drafts, a human approves anything sensitive), fix the top three reported problems, publish a changelog.
- L+2 to L+4 weeks: onboarding emails, one honest case study per product only after a real user agrees in writing, referral loop test (idea: one free month of Pro for each 3 active referrals; test with a spend cap of zero).
- L+5 to L+8 weeks: pillar guides in Arabic (examples of queries to target, to be checked in a keyword tool: "برنامج كاشير للسوبر ماركت", "حجز ملعب خماسي") and comparison pages only against competitors whose existence and features are linked in `plans/competitors/`.
- L+9 to L+12 weeks: direct outreach to real businesses: pitch owners for Hagoozat and shop owners for Business; goal numbers are set after the first interviews, not before.

## 3. Social distribution
- Only official platform APIs and official schedulers; every post is a draft approved by a human or by the owner's Telegram tap until the owner changes that rule. Posting caps per account per day are set in the product's config.
- Platforms: Facebook and Instagram pages (Meta Graph API), YouTube (Data API), LinkedIn (company page). X (Twitter): not scripted at all; a manual post by the owner only (AGENTS.md rule).
- Brand voice: posts and replies carry the product name. Agents never pose as Ahmed in conversations. No engagement bots, no bought followers or reviews, no mass DMs, no scraping of private data.
- Ads: none until the owner writes a spend cap in `config/limits.json`; first tests use a cap of 0 to 200 EGP a week "(owner decides)".

## 4. Lifecycle email (templates, per product, only after consent)
1. Welcome (instant): 3-step start checklist and a link to the assistant.
2. Activation (day 2 without the first action): one short video of the first task.
3. Feature note (day 7): one real feature, no invented savings ("saves 5 hours" is removed unless measured).
4. Win-back (day 21 inactive): what changed since the last visit.
Rules: sender authenticated with SPF, DKIM, DMARC; unsubscribe link and physical address in every marketing email; transactional emails (receipts, security) are separate; unsubscribe takes effect at once; subject lines in Arabic by default for Arabic users, English otherwise.

## 5. Press kit and public facts (per public product)
`/press` page with logo SVGs, icon 1024 px, screenshots, one-page fact sheet (what it is, who it is for, platforms, price, privacy summary, launch date, contact), and the facts page. The contact address uses the product's own domain once bought; until then no email is published and the contact form is used. Metrics appear only when real and dated.

## 6. Measurement
Weekly report on Telegram in simple Arabic: visits (cookie-free analytics), sign-ups, activation rate, paid conversions, support tickets, top search queries, AI-answer presence from the visibility check. Decisions use at least 4 weeks of data; A/B tests only with consent and enough traffic.

## 7. Owner steps
Provide the physical address and legal entity details for email footers and legal pages; sign in to platform developer consoles; approve the first posts; set the ad spend cap; buy domains (see `LAUNCH_CHECKLIST_ALL.md`).
