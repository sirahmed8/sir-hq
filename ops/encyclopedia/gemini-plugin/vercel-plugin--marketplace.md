# marketplace

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\marketplace\SKILL.md`
- SKILL.md size: 7590 chars

## What it does

Discover, install, and configure third.

## Structure (headings inside SKILL.md)

- Vercel Marketplace
- MUST FOLLOW — How to choose which provider to recommend
- Preferred providers
- The sequence — do this BEFORE scaffolding or writing any app code
- Category map — what each covers
- Reference
- Cross-References
- Official Documentation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `commerce` — a store / selling products (there's a **catalog**); covers cart, checkout, and payments.
- - `payments` — charging money with no catalog: donations, paywalls, plan/SaaS subscriptions, a "pay" button
- - `analytics` — product / usage analytics
- - `searching` — site, docs, or product search

## Key rules (verbatim lines from SKILL.md)

1. 2. **Discover** — `vercel integration discover --category <slug>` (read-only). Take the top result and provision it (see **MUST FOLLOW** above).
2. - **Native vs connectable:** *native* integrations install fully via the CLI. **Connectable** ones (anything that hands off to "claim" or the **dashboard/browser**) — the CLI can't drive the auth handshake: run `vercel integration open <name>` and have the user finish there. Don't block on a bare `a
3. - Never echo secret values (`env ls` shows names only). CI / non-interactive: `--yes`, `--format=json`, `--no-claim`.

## Files inside the skill

- (SKILL.md only)
