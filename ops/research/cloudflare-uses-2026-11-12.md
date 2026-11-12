# What the Cloudflare account gives the products (2026-11-12, owner gave a full-access token; stored only in `_local/api-keys.env`)
Account id is the same one used for Workers AI. Free-tier numbers are from Cloudflare docs as read earlier and not re-verified today.

| Use | Which products | Why |
|---|---|---|
| Workers AI (done: one scoped token per product, `CF_AI_TOKEN_<PROJECT>`, tested 200) | SIR AI first, then Jobs, Study, Portfolio, Laptop, HQ | extra free model lane (gpt-oss-120b, llama-3.3-70b, qwen2.5-coder-32b), 10,000 neurons per day for the whole account |
| Turnstile (bot check without a CAPTCHA wall) | SIR AI sign-up, every public form (Portfolio contact, support forms) | stops spam sign-ups and fake leads, free |
| R2 object storage (S3 compatible, keys saved) | SIR AI user files and backups, Study materials, ModPack and installer downloads | no egress fees, 10 GB free |
| Web Analytics | every public site | privacy friendly visitor numbers for the owner pages; Portfolio already uses it |
| Email Routing | support@ and hello@ for every product once a domain is bought | forwards to the owner inbox, free |
| D1 and KV | small shared data (waitlists, feature flags, rate limit counters) | free tier, edge fast |
| DNS and CDN | when the real domains are bought | one place for all products |
| Workers cron triggers | scheduled jobs that must run when the laptop is off | free tier |

Safety: the full-access token is for HQ only. Products only ever get a scoped token (Workers AI read and write today). If another scope is needed, HQ creates a new token named `<project>-<use>` through the API. Rolling the full-access token after setup is the owner's call.
