# 16 — Search, AI-assistant visibility and store discovery

**The honest goal:** be the best answer in the category, in every locale, wherever people look: Google, Bing, AI assistants (Google AI Overviews and AI Mode, ChatGPT, Gemini, Copilot, Perplexity, Claude), the App Store and Google Play. Nobody can promise rank #1; Google itself says indexing and serving aren't guaranteed even when every requirement is met. So do everything in our control, and measure it.

**AHome is excluded:** `noindex`, robots disallow, no sitemap, no store listing, no directory submissions.

**Technical foundations**

- Every public page is server-rendered or static HTML, with its content available as text and internal links to related pages. Nothing important hides behind logins or client-only rendering.
- `robots.txt` allows crawling (check the CDN and hosting setup too). XML sitemaps per locale; canonical URLs; `hreflang` plus `x-default`; clean URLs per locale.
- Module 06 performance budgets; mobile-first; HTTPS; no intrusive interstitials.
- JSON-LD structured data that matches the visible text: `Organization`, `WebSite`, `SoftwareApplication` / `MobileApplication`, `Product` / `Offer` where relevant, `FAQPage`, `BreadcrumbList`, `LocalBusiness` for local services, `Article` for posts. Validated in CI.
- Verify Google Search Console and Bing Webmaster Tools; submit sitemaps; ping IndexNow (used by Bing and others) on publish. Bing's index matters beyond Bing.
- Google's official guidance: there are no extra requirements, special files or special markup for AI Overviews or AI Mode; SEO fundamentals apply. An `llms.txt` is optional and cheap; don't expect it to matter for Google.

**Content that deserves to rank**

- Per product and per locale, research what people actually search in Arabic, English, Chinese and Hindi (not translated English keywords), and map intents to pages:
  - landing page, feature pages, use-case pages, honest comparison pages ("X vs Y"), pricing, FAQ, help center, a blog with genuinely useful guides;
  - free tools where they fit (a calorie calculator for SIR Health, prayer times for SIR Deen, a price checker for SIR Deals). Tools earn links and AI citations.
- **E-E-A-T:** real author and company pages, sources cited, visible update dates, demonstrated expertise. This matters most for health, money and religion.
- **Extractable answers:** clear headings, a short direct answer near the top, tables, lists and definitions. That's the shape AI assistants quote.
- **Freshness:** update the top pages monthly; publish changelogs and release notes.
- **Never:** keyword stuffing, doorway pages, mass AI-generated pages without real value, unreviewed machine translation, hidden text, fake reviews. These break search spam policies and can sink the whole domain.

**Authority and AI recommendations**

AI assistants recommend brands that are described widely and consistently across the web. Build that honestly:

- **Consistent brand facts everywhere:** name, one-line description, category, founder, links, also in `Organization.sameAs`.
- **Presence where assistants read:** YouTube (the content engine; `D:\Projects\_SIR\phases\08-business.md`, 8.2); Reddit and forums through genuine participation, never astroturfing; GitHub (open-source parts and strong READMEs); Product Hunt and relevant directories; the app stores; local directories.
- **Earned links and mentions:** launch posts, guest articles, partnerships, local press, case studies with SIR Business customers.
- **Wikipedia / Wikidata** only once a product is genuinely notable, and never through self-promotional edits.
- **Monthly assistant check:** ask the main assistants the category questions in each locale ("best app for X in Egypt"), record whether and how the product appears, and fix the gaps. Track AI referral traffic in analytics.
- Never buy links, spam communities, or post fake reviews.

**App Store Optimization (ASO)**

- Per store and per locale:
  - a title and subtitle carrying the main keyword
  - the iOS keyword field (don't repeat words already in the title)
  - Google Play short and full descriptions with natural keywords
  - the right category
  - localized screenshots with captions (the first two do most of the selling), a preview video, and an icon that stands out in search results
- **Ratings:** ask through the native in-app review APIs at a moment of success, never after an error and never with incentives. Reply to reviews (AI drafts, human tone).
- **Experiments:** Google Play store listing experiments and App Store product page optimization to A/B test icons, screenshots and copy.
- **Linking:** Android App Links, iOS Universal Links, smart app banners on the website, web-to-app links.
- **Release notes** written as updates people care about.

**Local and social**

- Google Business Profile for local services (SIR Business pilots, Hagoozat Elite venues, Negm Furniture): categories, photos, hours, review replies. The same name, address and phone everywhere.
- Social profiles linked from the site.

**Measure and iterate**

- Track per locale:
  - Search Console and Bing performance
  - Core Web Vitals
  - rankings, with the available SEO tools and plugins
  - store analytics (impressions → page views → installs)
  - the monthly assistant check
- A weekly n8n automation summarizes the changes and files tasks (`D:\Projects\_SIR\phases\07-launchpad.md`, 7.4).
