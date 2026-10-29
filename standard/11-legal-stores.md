# 11 — Legal, consent and store compliance

**Documents per product,** in every project locale, stored in `docs/legal/` and rendered in the web and apps. Arabic and English are the reviewed, governing versions; the other locales are translations and say so.

- Privacy Policy; Terms of Service; EULA (desktop and mobile); Refund & Cancellation policy (if anything is paid); Cookie Policy (web).
- A Data Deletion page (Google Play requires a web link); Acceptable Use; open-source licenses; an AI disclosure section.
- Each document is versioned and carries a changelog.

**Consent gate:**

- Shown on first run and again after material changes.
- Explicit, unticked checkboxes; links open the full documents.
- A consent record stored on the server: user, document versions, timestamp, locale, app version.
- Optional marketing consent kept separate. An age gate where the product needs one.

**Account and data rights:** in-app account deletion plus a web route, and data export.

**Google Play:** Data safety form, content rating, target audience, permission declarations (background location, exact alarms, foreground services), the health-apps declaration where relevant, and the closed-testing rule for personal accounts.

**Apple:**

- App Privacy labels and privacy manifest; account deletion; the login rule (4.8).
- In-app purchase for digital goods and subscriptions; physical goods and services may use other payment methods. Follow the current rules for each storefront.
- Minimum functionality (4.2): no thin web wrappers. Privacy (5.1). No medical claims without basis.

**Microsoft Store:** the listing in every project locale, the age rating questionnaire (IARC), a privacy policy URL, the current Store policies, and certification notes for the testers.

**Alternative Android stores** (Huawei AppGallery, Samsung Galaxy Store): their own content ratings, privacy forms and policies.

**User-generated content** (comments, posts, reviews, communities, the suggestions board): terms that forbid abuse, a way to report content and block users, moderation with response times, and removal of offenders. Both major app stores require this.

**Domain disclaimers:**

- SIR Health: not medical advice, plus emergency guidance.
- SIR Deen: sources cited for every text.
- SIR Deals: prices can change; affiliate disclosure.
- SIR Business: a data processing agreement for business customers.
- AI features: an AI disclosure.

**Identity:** brand and legal entity name, jurisdiction (Egypt), support contact, and version, in footers and About screens.

**Reality check:** these documents start from solid templates adapted to each product, but they are drafts. Ahmed should have a lawyer review them before charging money or handling sensitive data at scale. Don't promise that anything is "lawsuit-proof".
