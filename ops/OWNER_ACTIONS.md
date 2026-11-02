# NEEDS AHMED (only what an agent truly cannot do; it never blocks any work)

Format: `- [ ]` open, `- [x]` done. The SIR Control Room dashboard and pane read this file, so keep it true: tick or remove an item the moment it is done.

## Open (needs you now)

## Optional (when you like; shown on the dashboard in grey)
- [ ] Antigravity chat history (4.3 GB) is not moved yet: close Antigravity and free about 6 GB on D: (the 6.9 GB duplicate models folder is in the Recycle Bin: emptying it is enough), then run `python D:\Projects\_SIR\scriptsgent-reset.py agy-history` (it refuses while Antigravity runs or space is short; it moves, never deletes).
- [ ] **AHome: empty the Recycle Bin on D: when you like.** It holds the 6.9 GB duplicate models folder that the AHome chat moved there (this frees the space; nothing else needed).
- [ ] **AHome: tell the AHome chat what looks wrong on your phone** (the new dock, island, calendar and AI chat on the hosted site). Screenshots help.
- [ ] **Accounts when a product is ready (already chosen, 10 minutes each, HQ walks you through):** Microsoft Store individual account (free, storedeveloper.microsoft.com), Paymob and Fawry merchant accounts (ID, tax card, bank IBAN). Domains, Google Play and Apple wait for income. Nothing else to decide.

## Done (latest first)
- [x] 2026-11-01 AHome first sign-in done by Ahmed (his words); the AHome chat updates this list after it finishes its tasks.
- [x] 2026-11-01 Study portal: Ahmed signed in to Chrome; HQ took a read-only digest (materials/digest/2026-11-01.md in SIR Study); quizzes and assignments stay Ahmed's.
- [x] 2026-11-01 AHome chat did for Ahmed: vault recovery key saved as a private note in TickTick (inbox) and the local copy wiped; owner alerts target set (AHMED_CHAT_ID matches the pairing); Tailscale dropped (not needed: his phone uses the hosted site and the bot).
- [x] 2026-11-01 AHome Firebase check done by the AHome chat in your Chrome: only Google sign-in is on (Email/Password already off); the web API key is now limited to the hosted site, the Firebase domains and localhost (a foreign referrer gets 403, the site gets through); the Gemini key that shipped in the old web build is deleted (restorable 30 days).
- [x] 2026-11-01 Vercel CLI signed in on this PC (Ahmed, with 2FA); the AHome chat can deploy the hosted site.
- [x] 2026-10-30 Telegram bot tokens of the AHome AI bot and the SIR AI bot revoked in BotFather (HQ, your Telegram Web).
- [x] 2026-10-30 Wrangler signed in (Google one-click and Authorize in your Chrome).
- [x] 2026-10-30 Leaked GTA Gemini key and four stale Gemini keys deleted; six old OpenRouter keys deleted; Sourcery AI removed from GitHub; 30 old repos archived; five security fixes merged.
- [x] 2026-10-30 TickTick plans refreshed (wave tasks, goals text, one note); Habiba notes and personal lists untouched.
- [ ] 2026-11-02 AHome (owner only, never blocking): iOS App Store/TestFlight needs an Apple Developer account (paid); the PWA is the iPhone path now. Windows code signing, Apple notarization and a Play Store listing also need accounts; the unsigned desktop bundles come from the GitHub workflow `desktop-bundles`.
- [ ] 2026-11-02 AHome: after deploy, Settings > Devices > Add a device, make a code for Habiba, and install the APK from the same screen (the file goes online with `node scripts/publish-apk.mjs` before `vercel deploy`).
