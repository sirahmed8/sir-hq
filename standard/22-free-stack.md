# 22 — The zero-cost stack: free services, limits and resets

There is no budget, so every product runs on free tiers, preferring ones whose quotas reset daily or monthly. Free tiers change often. The facts below were checked in October 2026 on each provider's pricing page. Re-verify a limit before relying on it, keep the results in `D:\Projects\_SIR\knowledge\free-tiers.md`, and re-check them every month (a scheduled task).

## How to choose a provider

1. Generous limits that reset (daily or monthly) beat one-time credits, which expire.
2. No pausing on inactivity, no penalty that takes every site down, and terms that allow commercial use.
3. Fits the expected usage: estimate reads, writes, requests and storage per active user per day, multiply by the expected users, and keep a 3× margin.
4. Good SDKs for everything we ship (web, React Native, Electron) and a clean exit: every provider sits behind an adapter in `@sir/*` (module 02), so switching is a configuration change.
5. New providers appear all the time. When one offers a better free tier, compare it against these rules in an ADR and switch the golden-path product first.

## Default stack (verified October 2026)

| Need | Default | Free allowance (reset) | Notes |
|---|---|---|---|
| Sign-in | Firebase Authentication | 50,000 monthly active users (monthly) | Email, Google and Apple sign-in; passkeys where the provider supports them. SMS sign-in isn't free on this plan: don't use phone auth |
| App data (realtime, offline) | Cloud Firestore | 1 GiB stored; 50,000 reads, 20,000 writes, 20,000 deletes per day (daily); 10 GiB egress per month | The best offline sync for mobile. The daily read limit is usually the first one a product hits: design reads carefully |
| Relational data, reports, full-text search | Cloudflare D1 (SQLite) | 5 GB; 5 million rows read and 100,000 rows written per day (daily, 00:00 UTC) | SQL joins and FTS5 search for business products, catalogs and reports |
| Server code | Cloudflare Workers | 100,000 requests per day; 10 ms CPU per request (daily) | Firebase's free plan has no Cloud Functions. Workers verify Firebase ID tokens and call Firestore and FCM through their REST APIs |
| Live sessions, counters, rate limits | Cloudflare Durable Objects (SQLite-backed) | 100,000 requests per day; 5 GB stored (daily) | Rate limiting, live rooms, quota tracking for the AI gateway |
| Cache and config | Workers KV | 100,000 reads and 1,000 writes per day; 1 GB (daily, 00:00 UTC) | Read-heavy data only |
| Background jobs | Cloudflare Queues and Cron Triggers | 10,000 queue operations per day (daily) | Scheduled jobs, retries, fan-out |
| Files | Cloudflare R2 | About 10 GB stored, no egress fees, monthly operation allowances (verify) | Uploads through short-lived signed URLs issued by a Worker. Firebase Cloud Storage needs the paid plan |
| Image and video transforms | Cloudinary | 25 credits per month; one credit = 1,000 transformations, 1 GB stored or 1 GB delivered (monthly) | Keep originals in R2; Cloudinary transforms and caches |
| Web hosting | Cloudflare Workers static assets (or Pages) | Static requests free and unlimited | Firebase Hosting (10 GB stored, 360 MB transfer per day) is the backup. Vercel's free Hobby plan is non-commercial only. Netlify's free plan pauses every site on the account when one goes over its limit |
| Push notifications | Firebase Cloud Messaging | Free | iPhone push needs an APNs key from the paid Apple account; until then, in-app and email notifications on iOS |
| Feature flags and remote config | Firebase Remote Config | 100,000 fetches per day per project (daily) | Paid tiers begin above that from September 2026 |
| Abuse protection | Firebase App Check; Cloudflare Turnstile; Cloudflare's free WAF, bot and DDoS protection | Free (App Check quotas vary by attestation provider) | Module 04 |
| Crashes and errors | Firebase Crashlytics; Sentry (the Student Developer Pack adds 50,000 errors for a year) | Free | |
| Analytics, surveys, experiments | Firebase Analytics; PostHog's free tier (verify the current limits) | Free | PostHog surveys can run the NPS prompt (module 21) |
| Transactional email | A free sending tier, for example Resend or Brevo (verify daily and monthly limits); Cloudflare Email Routing for receiving | Daily or monthly | SPF, DKIM and DMARC on the sending domain |
| Maps | MapLibre with free OpenStreetMap-based tiles (for example OpenFreeMap; verify terms and attribution) | Free | Google Maps needs a billing account |
| AI | The provider chain in module 10 | Mostly daily | |
| Private access to the laptop (AHome's local AI) | Cloudflare Tunnel with Access, or Tailscale's free personal plan (verify user limits) | Free | Phones reach the local AI without opening ports |
| Domains | Free subdomains (`*.workers.dev`, `*.pages.dev`, `*.web.app`) until a domain is affordable, or a free first-year domain from the Student Developer Pack (Name.com, Namecheap `.me`, `.TECH`; verify) | | One domain per strong product, through the reinvestment ladder |

## Builds and CI, free

- **EAS free plan:** 15 Android and 15 iOS builds a month (low priority, 45-minute limit). iOS simulator builds need no Apple account.
- **Codemagic free plan:** 500 macOS M2 build minutes a month for personal accounts (one build at a time).
- **GitHub Actions:** the plan's included compute (more with GitHub Pro); public repos build free.
- Build Android, Windows and Linux locally whenever possible, and save cloud macOS time for Apple targets at milestones.

## Free with what Ahmed already has or can claim (verify each)

- His Google AI Pro accounts include large Google Drive storage: use it for off-site backups, media archives and build artifacts instead of the small local disks.
- **GitHub Student Developer Pack** (Ahmed verifies his student status once): GitHub Pro, Copilot for students, Codespaces, $100 of Azure credit plus free Azure services, Heroku credit for 24 months, $50 of MongoDB Atlas credit, student plans from Sentry, Datadog and New Relic, Clerk's Pro plan, Appwrite's Education plan for 6 months, and free first-year domains.
- Use one-time credits for experiments and burst work, never as the foundation of a product.

## Good alternatives (choose by ADR when a product fits them)

- **Supabase:** Postgres, auth, storage and edge functions in one, but only 2 free projects, 500 MB per database, and free projects pause after a week of inactivity. Good for prototypes, weak as the base for many products.
- **Appwrite:** a free plan that freezes a project (read-only) when it hits a limit, until the next cycle; the Education plan is free for 6 months.
- **Netlify, Render and similar hosts:** check pausing rules and commercial-use terms first.

## Watch the limits

- Every product's backend reports its usage against each free limit to the Command Center (`D:\Projects\_SIR\phases\07-launchpad.md`, 7.2), with the next reset time. Alerts go out at 70% and 90%.
- Design for the limits: cache aggressively, batch writes, paginate everything, and move read-heavy lists to D1 or KV.
- At a limit: degrade gracefully (cached data, queued writes, a clear message). Never crash, and never silently drop data.
- An attacker burning a free quota is a security incident (module 04).
- Never create extra accounts on the same provider to multiply free quotas: most terms forbid it, and it risks losing everything. Spread load across different providers instead.
