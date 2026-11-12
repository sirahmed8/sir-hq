# domains (Vercel)

## Summary
Domain lifecycle skill for Vercel: public Registrar API for unauthenticated discovery (search 1–200 exact names returning availability+pricing together; TLD metadata, term pricing, availability, contact requirements), CLI for account/project ops (`vercel domains ls|inspect|add|verify|move|rm`, `dns ls|inspect|add|update|rm`, `domains buy|transfer-in|renew|auto-renew|search|check|price`), and the authenticated Registrar REST API (`/v1/registrar/*`) for purchases/transfers/renewals/nameservers/contacts with async order inspection.

## When to use / when NOT
Use for searching/registering/transferring/connecting/verifying domains and DNS on Vercel. Registration, team ownership, project assignment, and authoritative DNS are SEPARATE concerns — connecting an owned domain needs no purchase. Do NOT use `vercel dns` for records at external DNS providers, and don't confuse CLI `search` (keyword) with API `search` (exact names).

## Inputs, outputs, tools
- Inputs: domain names/keywords, project/team scope, registrant info, expected prices.
- Outputs: availability/price quotes, connected domains, DNS records, registrar orders.
- Tools: curl to api.vercel.com public endpoints, `vercel`/`vc` CLI, Registrar API with Bearer token + teamId.

## 5 most important rules
1. Search before asking for credentials — the public endpoint needs no account.
2. `available: false` means unavailable OR unconfirmed — never claim someone owns it; missing price is unknown, not zero; quotes change before purchase.
3. `domains add` connects; it does not buy or transfer. `--force` on verify can detach a domain from another project — only when intended.
4. Purchases: CLI 63.1.0+ runs prompt-free with `--scope --json` (price quote first without `--amount`, then approved `--amount`); CLI never retries charges — `domains inspect` before resubmitting; keep registrant data/tokens/transfer codes out of logs.
5. Use real expected DNS values per domain+project — never hardcode universal A/CNAME; preserve MX/email TXT records when changing nameservers.

## Risks / things needing the owner
buy/transfer-in/renew are REAL charges — explicit authorization for exact domain, term, price, renewal preference required; prepare the quote first. Transfer codes and registrant PII are sensitive. Async orders need status polling.

## Category / tags
cloud · vercel, domains, dns, registrar, devops

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\domains\SKILL.md`. Only gemini-plugin holds it.
