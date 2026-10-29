# 21 — Product essentials: notifications, owner dashboard, support, subscriptions, benchmark

**Notifications (every product)**

- **Channels:**
  - push (FCM, with APNs on Apple devices), web push, and desktop notifications (Electron)
  - email for important account events (a transactional email provider, on a domain with SPF, DKIM and DMARC)
  - an in-app notification center
  - watch and car surfaces through the phone
- Per-category preferences, quiet hours, localized text, deep links into the right screen, and permission asked at a meaningful moment.
- Sent server-side through one notifications service (server code plus FCM topics and segments), with rate limits and an audit log. Every notification must be useful to the person receiving it.

**Owner dashboard (every product; private to Ahmed)**

- **Access:** a secured admin console (`/admin` on the web, also in the desktop app). Requires the Firebase Auth custom claim `role: owner`, 2FA and App Check; every admin action goes to an audit log.
- **What it shows:**
  - growth: signups, daily and monthly active users, retention cohorts, funnels
  - revenue: MRR, subscriptions, trials, churn, refunds
  - usage: features, screens, locales, platforms, app versions
  - quality: crash-free rate, errors, performance, AI cost and latency
  - support: tickets and response times, top questions, suggestion votes, bug reports, NPS, reviews
  - store, SEO and notification-campaign stats
- **Tools:** broadcast and segmented notifications, announcements, feature flags and remote config, content management, moderation, and support actions on a user's account (with the user's consent where needed).
- **Privacy guardrails** (law and user trust):
  - Aggregates by default; personal details masked unless a support case needs them.
  - Never browse users' private content: health logs, religious-practice data, messages, photos.
  - All access is logged, and the privacy policy says what the owner can see.
- **AHome:** the owners are Ahmed and Habiba, and neither has an admin view into the other's private content.
- The portfolio Command Center pulls the headline numbers from every product's dashboard.

**Support, help and suggestions (every product)**

Big apps make help easy to find and feedback easy to give. Every product has:

- **Help center** in the app and on the web: searchable articles in every locale, written from the real features (never generic filler), with screenshots, updated at each release, and linked from the screens they explain.
- **FAQ:** the real questions users ask (from tickets, reviews and search queries), reviewed monthly.
- **Contact and support:** an in-app form and a support email (SPF, DKIM, DMARC), sending device, version and locale details automatically, plus logs or screenshots when the user agrees; an honest response-time target.
- **AI support assistant** (on the module 10 gateway), grounded only in the product's help center and the user's own account context. It says when it doesn't know, hands off to a human ticket, and never invents policies or promises.
- **Suggestions board:** users post ideas, vote, and see the status (planned, in progress, shipped); shipped items link to the changelog.
- **Bug reports** from inside the app, plus automatic crash reports (with consent).
- **What's new and roadmap:** the real changelog in the app, and a public roadmap for public products.
- **Tips and tutorials:** first-run onboarding, contextual tips, short how-to videos from the media engine.
- **Status page** for products with a backend (free, for example Upptime, or a free tier whose terms allow commercial use).
- **Community** where it helps (a moderated Telegram or Discord group).
- **Feedback loops:** a short satisfaction or NPS prompt at value moments (rarely, never on first launch), and store-review prompts through the native APIs.
- **Accessibility statement** and a way to report accessibility problems.
- Everything feeds the owner dashboard: tickets and response times, top questions, suggestion votes, bug trends, NPS.
- **AHome:** a private help page, tips and a feedback box between the two of them; no public pages.

**Subscriptions (win-win)**

- **AHome has no subscriptions, ads or paywalls.** It's private and free for its two users; skip this section there.
- **Free tier:** genuinely useful on its own.
- **Premium:** depth, convenience and power: advanced AI, higher limits, cloud sync across devices, extra platform features (watch, TV), customization, export tools, priority support.
- **Never paywall safety or essentials:** medication reminders, prayer times, core accessibility, data export and account deletion stay free.
- **Fair pricing:** local prices in EGP and regional pricing through the stores; monthly and yearly (yearly cheaper); a free trial; family or team plans where they fit; per-business tiers for SIR Business.
- **Upgrade prompts** appear at value moments (when someone reaches a premium feature after getting real value), never as nags. No dark patterns: cancelling is as easy as subscribing, purchases can be restored, renewal terms are clear.
- **Implementation:** in-app purchases through RevenueCat on iOS and Android once the paid store accounts exist (store rules for digital goods); until then, and for web users, checkout on the web; web payments through a local gateway that supports subscriptions (Paymob or similar; verify recurring billing support), and for international cards a merchant of record that pays out to Egypt (Stripe doesn't accept Egypt-based businesses; verify); entitlements checked on the server; subscription metrics in the owner dashboard.
- **Measure** conversion, paid retention, refund rate and user feedback. If users feel cheated, the model is wrong; change it.

**Benchmark: match the best, then beat them (every product)**

Ahmed wants every product to have what the big apps and sites have, and more. Before a product's wave and before every major release, its PM:

1. Finds the 3–5 leading apps and sites in the category, global and Arabic-market, through store charts and search (not memory).
2. Studies them from public sources: store listings, feature pages, changelogs, help centers, and their 1–3 star reviews (what users hate is our opportunity).
3. Writes `docs/BENCHMARK.md`: a feature matrix (feature × competitor × us), each gap marked as table stakes, differentiator or nice-to-have, plus the complaints we can solve.
4. Turns the gaps into BOARD tasks (table stakes first, then the differentiators that fit the strategy) and records the decisions in `docs/PRODUCT.md`.
5. Builds every feature its own way: never copy their code, text, design or brand (module 11).

Features the big apps usually have and teams forget: universal search (and a command palette on desktop), cross-device sync, offline mode, undo and drafts, import and export, sharing and deep links, smart reminders, streaks and goals where they genuinely help, personalization, widgets, passkeys and social sign-in, account recovery, a privacy dashboard, session and device management, family or team sharing, referral rewards, a help center, in-app what's new, a status page, and accessibility settings.
