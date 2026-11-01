# NEEDS AHMED (only what an agent truly cannot do; it never blocks any work)

Format: `- [ ]` open, `- [x]` done. The SIR Control Room dashboard and pane read this file, so keep it true: tick or remove an item the moment it is done.

## Open
- [ ] **AHome hosted site: sign in to Vercel once on this PC** (run `vercel login` in a terminal, open the link, allow access and enter your authenticator code; agents never enter 2FA codes). Then the AHome chat deploys the hardened web app and checks the live site (task T-039). If the Vercel project is connected to the GitHub repo, pushes to main may already deploy it; check the Vercel dashboard.
- [ ] **AHome: delete the Gemini API key that was in the web build** (Google AI Studio, API keys; the key named in the old `NEXT_PUBLIC_` setting, which shipped to browsers). The code no longer uses it. An agent can do this in Chrome when you say so (task T-025 follow-up).
- [ ] **AHome first sign-in (you and Habiba, 5 minutes each).** The PC's AHome core now needs a login. Each of you has a setup code file: `D:\Projects\AHome\local-vault\auth-setup-ahmed.txt` and `auth-setup-habiba.txt` (agents never read them). Open http://127.0.0.1:8090/login, choose "First time here", enter your code, pick a password, add the key to an authenticator app on your phone, save the 10 recovery codes, then delete the file. Why only you: the authenticator app lives on your phone.
- [ ] **AHome phones: install Tailscale on the PC and on both phones, sign in with your Google accounts** (free personal plan). It is the private tunnel from ADR-001 (task T-021 in AHome). Until then the phones keep using only the Firebase features they use today.
- [ ] **AHome Firebase console check (2 minutes):** Authentication, Sign-in method: Email/Password must be off; Google Cloud, Credentials: restrict the web API key to the site's referrers. Tell the AHome chat when done (task T-023).
- [ ] **Move the account passwords out of the two TickTick notes into a password manager and change them.** Why only you: agents cannot type or handle your passwords. Bitwarden is free.
- [ ] **Study portal (optional): sign in once to https://elearning.oi.edu.eg in Chrome** when you want the read-only digest of new uploads, deadlines and quiz dates in SIR Study. Quizzes and assignments are never done by agents.
- [ ] **Decide when you like: publisher name SIR, domains, store developer accounts, payment gateway keys (Paymob, Fawry, Stripe).** Free pages.dev addresses and the Launching Soon billing fallback cover it until then.

## Done (latest first)
- [x] 2026-10-30 Telegram bot tokens of the AHome AI bot and the SIR AI bot revoked in BotFather (HQ, your Telegram Web).
- [x] 2026-10-30 Wrangler signed in (Google one-click and Authorize in your Chrome).
- [x] 2026-10-30 Leaked GTA Gemini key and four stale Gemini keys deleted; six old OpenRouter keys deleted; Sourcery AI removed from GitHub; 30 old repos archived; five security fixes merged.
- [x] 2026-10-30 TickTick plans refreshed (wave tasks, goals text, one note); Habiba notes and personal lists untouched.
