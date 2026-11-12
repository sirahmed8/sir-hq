# google-preferred-sources

Source read: `C:\Users\a7med\.codex\skills\google-preferred-sources\SKILL.md` (codex revision; kilo/opencode/windsurf/cursor listed).

## Summary
A short SEO skill for surfacing a site in Google AI Overviews, AI Mode, Google Discover, and Top Stories via "Preferred Sources" signals. It prescribes three concrete implementations: an auto-discovery RSS/Atom `<link rel="alternate">` in `<head>`, a "Follow on Google News" badge linking to the publisher's `news.google.com/publications/<ID>` page, and JSON-LD `NewsMediaOrganization`/`Organization` schema with a `sameAs` array. It closes with a technical checklist (feed registered, `robots.txt` crawler policy, canonicals, 1200x630 OG/Twitter cards).

## When to use / when NOT
Use when setting up or auditing publisher/discovery signals on a content site (blogs, news, docs with articles). Do NOT use for non-content sites, and treat the claimed ranking benefit as directional — Google does not guarantee AI Overview placement from these signals.

## Inputs, outputs, tools
- Inputs: the site's feed URL, Google News publisher ID, social/profile URLs for `sameAs`.
- Outputs: HTML head tags, a follow badge snippet, JSON-LD block, and a checklist audit.
- Tools: none — pure markup guidance (works in Next.js or plain HTML).

## 5 most important rules
1. Register the RSS/Atom feed via `<link rel="alternate" type="application/rss+xml">` in every page head.
2. Render a real, crawlable follow badge to the correct `news.google.com/publications/` URL — not a fake or dead link.
3. Ship `NewsMediaOrganization`/`Organization` JSON-LD with `sameAs` pointing at real Knowledge Graph entities.
4. Keep canonicals strict and OG/Twitter images at 1200x630.
5. Decide deliberately whether `robots.txt` allows `Google-Extended`/AI crawlers; do not block them accidentally.

## Risks / owner notes
The publisher ID must be the owner's real Google News publication — needs owner setup in Publisher Center if the site is not already registered. Claims about AI Overview ranking are aspirational, not guaranteed.

## Category and tags
Category: web. Tags: seo, google-news, rss, json-ld, ai-overviews, discover.
