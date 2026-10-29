# 04 — Security and privacy (defense in depth)

Ahmed's requirement: every product must stand up to hackers and every kind of attack. Nothing is unhackable, so the standard is defense in depth: make attacks hard and expensive, limit what any single failure can expose, detect problems fast, and recover quickly. Read this module before touching auth, data, APIs, uploads, payments, AI features or releases.

**Baseline and threat model**

- OWASP ASVS (latest version) Level 2 for anything with accounts or personal data; Level 3 for payments, health data and the owner dashboard. OWASP MASVS for mobile. The OWASP Top 10 and the OWASP Top 10 for LLM applications (latest editions) as review checklists.
- Each product keeps a threat model in `docs/ARCHITECTURE.md`: assets, entry points, trust boundaries, STRIDE threats, and abuse cases (how someone would cheat, scrape, spam, steal, or run up costs). Update it whenever a feature adds an entry point.
- Least privilege everywhere: user roles, service accounts, API keys, CI tokens, agents.

**Identity, sessions and access**

- Authentication through Firebase Auth (or the chosen provider): verified email, email-enumeration protection on, strong passwords checked against known breaches (Have I Been Pwned's free k-anonymity API), passkeys or social sign-in where available.
- Multi-factor authentication required for owner, admin and staff roles and offered to every user. If the provider's MFA isn't on the free tier, add a TOTP step verified on the server.
- Brute force and credential stuffing: per-account and per-IP rate limits, growing delays, temporary lockout with an email to the user, and a free human check (Cloudflare Turnstile) on sign-up, repeated failed sign-ins, password reset and other abuse-prone forms.
- Sessions: short-lived tokens; refresh tokens revoked on password change and on "sign out of all devices"; a device list in settings; re-authentication before sensitive actions (email change, deletion, payouts, role changes).
- Authorization on every read and write, in security rules and on the server: deny by default; ownership checks, so no user can reach another user's records by changing an ID (IDOR); role checks for business apps (owner, manager, staff, customer); tenant isolation in multi-business products (every record carries its tenant, and rules and queries enforce it); and tests that try to break each rule with a second test account and a second tenant.

**Input, output and data handling**

- Every external input (request bodies, params, headers, forms, webhooks, deep links, IPC, files, AI output) passes a strict Zod schema (`.strict()`) with size limits before business logic.
- Output is encoded for its context; user HTML is sanitized (DOMPurify) or not allowed; no `eval` or code built from data; parameterized queries only; regexes checked for catastrophic backtracking.
- Uploads: allowlisted types checked by content, not by extension; size limits; images re-encoded and stripped of metadata; files stored outside the web root and served through short-lived signed URLs; nothing uploaded is ever executed.
- Outbound requests (SSRF): only to allowlisted hosts; block private, loopback and cloud-metadata addresses. No open redirects.
- Webhooks: verify signatures and timestamps, reject replays, process idempotently.

**Web and API hardening**

- Headers: strict CSP with nonces (plus Trusted Types where supported), HSTS with preload, `X-Content-Type-Options: nosniff`, `frame-ancestors 'none'`, Referrer-Policy, Permissions-Policy, and cross-origin isolation headers where they fit.
- Cookies: Secure, HttpOnly, SameSite; CSRF protection for cookie-authenticated mutations; CORS limited to known origins, never a wildcard with credentials.
- Third-party scripts: as few as possible, self-hosted or pinned with Subresource Integrity.
- Edge protection: public sites and APIs sit behind Cloudflare's free plan (DDoS mitigation, managed WAF rules, bot protection, rate-limiting rules; check what the free plan currently includes). Request size limits and timeouts everywhere.
- Abuse limits: per-user, per-IP and per-route rate limits; quotas on expensive endpoints, above all AI; App Check enforced for Firestore, server endpoints and the AI gateway (Play Integrity, App Attest, reCAPTCHA on the web; check the free quotas). With no budget, abuse is also a cost attack: someone who burns a free quota takes the product offline.
- `/.well-known/security.txt` (RFC 9116) with a contact and an expiry date, and a short disclosure policy in `SECURITY.md`.

**Firebase specifics**

- Security rules are code: deny by default, validated fields and types, size limits, unit-tested in the emulator in CI.
- API keys restricted (HTTP referrers, Android package and SHA-256, iOS bundle ID) and limited to the APIs they need. Unused sign-in providers off; authorized domains reviewed. The Admin SDK and service-account keys only on the server, in the secret store, rotated on a schedule.
- Separate dev and prod projects; production data never in dev.

**Secrets**

- Never in git, client bundles, logs or screenshots. `NEXT_PUBLIC_` and `EXPO_PUBLIC_` are for non-secrets only. Firebase client config is public by design; App Check, rules and key restrictions protect it.
- Secrets live in the platform's secret store (Cloudflare Workers secrets, GitHub Actions secrets, EAS environment variables). Validate required env vars at startup and fail fast.
- gitleaks in pre-commit and CI. A leaked key is rotated immediately (no need to ask), then removed from git history on a backup branch.

**AI features**

- Treat everything a model reads (user text, web pages, documents, tool results) as untrusted: it may carry prompt-injection instructions.
- The model never sees secrets. Tools are allowlisted per feature. Actions with real impact (payments, deletions, messages, role changes) need a server-side policy check or the user's confirmation, never the model's word alone.
- Model output is validated against a schema before use and never executed. Every AI endpoint has rate limits, cost caps and abuse logging. Personal data is redacted before it reaches an outside provider unless the feature needs it, and then it's disclosed.

**Mobile (MASVS)**

- Tokens and secrets in the Keychain or Keystore (expo-secure-store), never in AsyncStorage or plain files.
- App Check with Play Integrity and App Attest. Root and jailbreak signals are risk signals, not hard blocks for honest users.
- Release builds: R8/ProGuard on Android, debugging off, no secrets in the binary, exported Android components kept to the minimum, sensitive data excluded from backups, verified App Links and Universal Links, deep-link parameters validated.
- Sensitive screens hidden from screenshots and the app switcher where the platform allows (FLAG_SECURE on Android); an optional biometric app lock.
- A minimum-supported-version check through Remote Config, so a vulnerable version can be forced to update.

**Desktop (Electron)**

- Module 09's checklist: `contextIsolation`, `sandbox`, no `nodeIntegration`, a strict CSP, validated IPC senders and payloads, `shell.openExternal` limited to allowlisted URLs.
- Electron Fuses: turn off `RunAsNode` and the Node options and inspect-argument fuses; turn on cookie encryption, embedded ASAR integrity validation and only-load-app-from-ASAR (check the current fuse names).
- Local secrets encrypted with `safeStorage`. Auto-updates only over HTTPS from the official release source, with SHA-256 checksums published for every download until code signing is affordable.

**Supply chain**

- Official packages only; lockfiles committed; versions pinned through the workspace catalog. pnpm doesn't run dependency install scripts by default: allow them one package at a time. Delay brand-new package versions with pnpm's minimum release age setting (check the current name), because compromised releases are usually caught within days.
- Renovate or Dependabot for updates, reviewed like any other change.
- GitHub: 2FA, fine-grained tokens with expiry dates, signed commits, Actions pinned to commit SHAs, least-privilege `permissions:` in every workflow.

**The security pipeline (a required CI job, all free tools)**

- Secrets: gitleaks. Static analysis: Semgrep Community Edition (CodeQL is free only on public repos). Dependencies: OSV-Scanner and `pnpm audit`. Rules: emulator tests.
- DAST: an OWASP ZAP baseline scan against each preview deployment. Mobile: MobSF static scans of release builds. Electron: Electronegativity.
- High and critical findings block the merge. A risk accepted on purpose gets an ADR with an expiry date.
- Before every release, the `security-auditor` agent attacks the staging build: the OWASP checklists, IDOR attempts with a second account, rate-limit and abuse tests, and a review of every new entry point. Findings are fixed before the release.

**Detection, monitoring and recovery**

- Crash and error tracking (Crashlytics, Sentry's free tier) and uptime monitoring (a free monitor whose terms allow commercial use).
- An append-only audit log for admin actions, role changes, payments, data exports and deletions; no client can edit or delete it.
- Alerts pushed to Ahmed's phone for spikes in failed sign-ins, 4xx and 5xx errors, App Check rejections, unusual usage or cost, and any admin action from a new device.
- Kill switches through Remote Config to turn a feature off fast.
- Backups: encrypted, scheduled, stored away from the main system, and restored for real every quarter (resilience against ransomware and mistakes).

**Owner accounts (the biggest target)**

- Ahmed's GitHub, Google, Firebase, Cloudflare, Expo, Apple, Microsoft, social and email accounts: unique passwords in a password manager (Bitwarden's free plan works), 2FA with passkeys or an authenticator app rather than SMS where possible, recovery codes stored offline, and a monthly review of connected apps and active sessions.

**Privacy by design and the law**

- Collect the minimum; state the purpose of each field; set retention periods; encrypt in transit and at rest; give users export, correction and deletion.
- Sensitive categories (health, religious practice, biometrics such as face images, precise location, children's data) need explicit consent, extra minimization, and no use for advertising.
- Follow Egypt's Personal Data Protection Law (Law 151/2020; verify the status of its executive regulations and breach-notification rules) with GDPR-grade defaults for users abroad.
- AI and privacy: don't send personal data to AI providers unless the feature needs it, and disclose it when it does.

**Incidents**

- `SECURITY.md` with a reporting contact, plus an internal runbook: contain, rotate, assess, notify users and authorities where the law requires, fix, write a blameless post-mortem, and add a test so it can't happen again.
