# commercial-app-blueprint

## Summary
A conversion-architecture checklist for commercial web products: machine-readable discovery (`/llms.txt`, sitemap, robots, canonical, service silo pages), trust assets (above-fold CTA, sticky mobile CTA bar, guarantees, real social proof, thank-you route, LocalBusiness schema), and 12 mandatory interactive utilities (dark mode, Cmd+K palette, scroll-to-top, reading progress, copy buttons, skip link, password toggle, print CSS, tooltips, UTM persistence, FAQ accordion with JSON-LD, floating contact widget).

## When to use / when NOT
Use when building or auditing the public/commercial layer of a product site — landing pages, marketing pages, docs-adjacent pages. Do NOT use for in-app authenticated UX, backend work, or as a substitute for real content (it bans fake proof explicitly).

## Inputs, outputs, tools
- Inputs: the site/pages being built or audited.
- Outputs: implemented discovery files, conversion sections, and utility components.
- Tools: none external — guidance for HTML/JS/CSS implementation; mentions Radix tooltip and localStorage as examples.

## 5 most important rules
1. `/llms.txt` at root in clean Markdown for LLM crawlers; keep sitemap/robots/canonical correct.
2. One primary CTA above the fold; sticky mobile CTA appears only after the hero.
3. Social proof must be real — no fabricated names, headshots, or metrics; before/after needs verifiable numbers.
4. Every commercial site gets the 12 utilities — notably UTM capture persisted across route changes into form submissions, and FAQPage/LocalBusiness JSON-LD.
5. Print stylesheet and skip-to-content are non-negotiable accessibility/commercial basics.

## Risks / things needing the owner
It mandates business assets the owner must supply (real testimonials, guarantee terms, response-time promises, physical address for LocalBusiness). Adding trackers or schema claims (e.g. LocalBusiness) without real data would be fake — keep to what exists.

## Category / tags
web · marketing, conversion, seo, llms-txt, ux-utilities

## Revisions
Six tools hold it; bodies byte-identical, only `description` differs. Claude copy preferred for its trigger-style description.
