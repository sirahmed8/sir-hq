# SIR LAUNCH CHECKLIST (owner steps only; rewritten 2026-11-10 by the plans audit)
Target reader: Ahmed (second-year student, not an expert). Standard: `standard/24-launch-package.md`.
How to read this file: the software is built and tested by the agents in test mode with "Subscriptions launching soon" fallbacks. This file lists only what a person must do: buy, sign in, pay, paste keys, sign. Every step says how to check it worked and what switches on. Agents never do these steps and never block on them (`ops/OWNER_ACTIONS.md` is the live list).
Truth rule: no product is "ready to launch" today. Each section starts only after that project's plan reaches its gate (M3 security, legal and billing green, and a reviewer verified it end to end that day). Dates are not promised; the old "Week 1, Week 2" targets are removed because the products are not built.
Prices and fees below are not sourced: every price is "(unsourced, verify)" at the registrar or provider page on the day of purchase.

## 0. One-time accounts (do once, reused by many products)
1. Cloudflare account (free plan): hosts all public sites on Cloudflare Pages and Workers. Check: dashboard opens; `sir-portfolio.pages.dev` style URLs work.
2. GitHub: already used. Check: private repos exist per `plans/repos.json`.
3. Google account for Firebase (Auth with Google, Firestore): one Firebase project per product, created by the agent after you sign in. Check: the Google sign-in screen shows the product name, not a project id.
4. Telegram bot token: already set as user environment variables `SIR_TELEGRAM_BOT_TOKEN` and `SIR_TELEGRAM_CHAT_ID`. Check: `node scripts/deliver/send-telegram.mjs "test"` prints `sent`.
5. Payment accounts (only when the first paid product is ready): Paymob (Egypt) and Fawry. Business registration documents may be needed: "(unsourced, verify)" on their sign-up pages. Until then every product shows "Subscriptions launching soon".
6. Lawyer review: every legal page is AI-drafted and is marked so. One lawyer review per market before the first paid launch.
7. Domain registrar: Cloudflare Registrar or Namecheap (compare the price on the day). `.eg` names need an Egyptian registrar and extra documents "(unsourced, verify)".

## 1. Per-product steps, in the order the plans reach their gate
For each product: (a) buy the domain, (b) add it to Cloudflare Pages (the agent prints the exact DNS records), (c) create the accounts listed, (d) paste keys into the product's `.env` (names listed), (e) run the check, (f) the agent flips the switch.

### SIR Business and SIR Hagoozat and SIR Education Hub (wave 5)
| Item | Candidate names | Keys to paste (names only) | Check |
|---|---|---|---|
| SIR Business | `sirbusiness.app` | `PAYMOB_API_KEY`, `PAYMOB_HMAC_SECRET`, `FAWRY_MERCHANT_CODE`, `FAWRY_SECURITY_KEY`, `SIGNING_CERT_PATH` (desktop installer certificate) | pricing page checkout opens in test mode; installer runs on a clean Windows VM |
| SIR Hagoozat | `hagoozat.com` or `hagoozat.app` | `PAYMOB_API_KEY`, `PAYMOB_INTEGRATION_ID_CARD`, `PAYMOB_INTEGRATION_ID_WALLET`, `PAYMOB_HMAC_SECRET` | a 5 EGP test booking moves to Confirmed; 20 parallel booking requests give 1 booking |
| SIR Education Hub | `obourhub.com` or `obour-hub.app` | `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET_NAME`, plus rotation of the old Firebase admin keys | sign in with a Google student account; a note downloads; old keys return 401 |
Also: tax authority e-invoicing onboarding for Business (certificates, possibly a USB token): "(unsourced, verify)" with an accountant; classmates' written consent for any shared notes; pitch-owner agreement for Hagoozat; at least 3 real pitches before any ad.

### SIR Content Creation Studio and SIR AI Tier 2 and SIR Controller (waves 4 and 8)
- Content Studio: domain; Meta developer app and YouTube Data API project (official APIs only; app review queues take time, so drafts-only mode first); keys `META_CLIENT_ID`, `META_CLIENT_SECRET`, `YOUTUBE_CLIENT_ID`, `YOUTUBE_CLIENT_SECRET`; code-signing certificate. Check: connect one test account, schedule a draft, approve it, see it publish once.
- SIR AI: Tier 1 needs no purchase. Tier 2 only: domain, provider keys (`OPENROUTER_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`), payment accounts. Check: `private=true` request never reaches a cloud provider.
- SIR Controller: decide to sell or not after the licence note (`docs/LICENSE_DECISION.md` in the project); then domain and code-signing certificate. A signed installer helps with the Windows SmartScreen warning but does not remove it immediately "(unsourced, verify)". Check: clean VM install and uninstall.

### SIR ModPack and SIR Mods for GTA V and SIR Life Part B (wave 6)
- ModPack: domain; code-signing certificate; no payment account until the Mojang rules note (`docs/MOJANG_RULES.md`) says supporter perks are fine. Check: the launcher refuses a corrupted download.
- GTA V mods: HARD GATE, nothing public until `docs/THIRD_PARTY.csv` shows redistribution proof for every binary and the publisher policy note exists. Owner also rotates the keys that were in the old tracked `.env` files and sets `ADMIN_SECRET_KEY` (server-side) at deploy. Check: forged admin cookie returns 403.
- Life Part B: domain, Google Play developer account and Apple developer account when the app is ready (fees "(unsourced, verify)"). Part A (private organiser) needs only the Google sign-in for Calendar and Gmail read scopes.

### SIR Portfolio (can go early)
- Buy a personal domain (candidates `ahmedalaa.dev`, `sirahmed8.com`); add the site to Google Search Console (DNS TXT record) and Bing Webmaster; submit `sitemap.xml`; confirm which social accounts are public; replace the GitHub profile README with the short honest one. Check: Search Console shows the sitemap as read.

### SIR Negm Furniture (friend's project; plans only until you say)
The client creates and owns the domain, Cloudflare, Firebase and Google Business Profile accounts and pays for them; Ahmed only walks him through `HANDOFF.md`. The planned contact method is a WhatsApp click link; the WhatsApp Business API and a Paymob deposit gateway are not planned (earlier text proposed them; removed until the client asks). Check: the friend can follow `HANDOFF.md` alone.

### the shared kit
No purchase. Internal packages; docs site stays `noindex`.

## 2. Private products (no purchases, unlisted, noindex)
AHome (local only; keys rotated at M6), SIR Study, SIR Jobs, SIR Laptop Manager, SIR Control Room. Their only owner steps: Tailscale sign-in on the phone, Telegram, Google read-only tokens, UAC prompts when installing scheduled tasks.

## 3. Budget estimate
Not a promise and not sourced. The only certain upfront cost is domains; at the time of writing no prices are sourced, so the previous totals ("about 75 USD", "about 3,600 EGP") are removed. Fill this table on the day of purchase from the registrar page.
| Item | Price on the day | Source link and date |
|---|---|---|
| Domains for the products you decide to launch | (unsourced, verify) | |
| Code-signing certificate | (unsourced, verify) | |
| Cloudflare / Firebase paid plans | start on free plans; upgrade only when a budget alert fires | |
| Payment gateways | per-transaction fees, check each provider | |
Budget alerts: set a monthly cap in each cloud console before enabling any paid plan; the owner sets the number.
