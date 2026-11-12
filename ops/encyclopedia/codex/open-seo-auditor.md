# open-seo-auditor

Tools: claude, codex, cursor, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\open-seo-auditor\SKILL.md (40 lines, read in full)

## Summary
An SEO + GEO (Generative Engine Optimization) checklist skill inspired by every-app/open-seo. It defines standards for being found by AI answer engines (definition blocks LLMs can quote, JSON-LD entity graphs, FAQPage schema, information-dense citations) plus a technical SEO audit protocol (robots.txt, sitemap, canonicals, heading hierarchy, OG/Twitter metadata) and a mobile/CWV checklist.

## When to use / not use
Use when auditing or improving a public website's search and AI-answer visibility. Not for paid-ads, social, or non-web products; it is a checklist, not a rank-tracking tool.

## Inputs, outputs, dependencies
Input: a website/codebase to audit. Output: findings against the GEO standards, technical SEO protocol, and mobile checklist. Needs: code access (meta tags, robots.txt, sitemap generation) — no external APIs required, though real ranking data would need a search tool it doesn't provide.

## Key rules
1. GEO: declarative definition blocks at the top of informational pages, entity-linked JSON-LD (Organization, Product, SoftwareApplication, Author), empirical data over fluffy prose, FAQPage schema.
2. Technical: robots.txt allows public routes and blocks /api//admin; programmatic sitemap.xml with accurate lastmod; self-referencing canonicals; exactly one h1 per page with unskipped nesting.
3. Social graph: complete Open Graph set plus Twitter summary_large_image (1200x630).
4. Mobile: overflow-x clip, 44x44px touch targets, CWV targets (LCP<2.5s, CLS<0.1, INP<200ms).

## Risks / owner items
- GEO "standards" are inferred best practices, not guaranteed ranking factors; presenting them as guaranteed AI-search visibility would overclaim.
- Checklist has no measurement tooling — CWV/SEO claims need real field data (CrUX/PageSpeed) to verify.

## Category and tags
web, business, research — seo, geo, ai-search, json-ld, technical-seo, audit.

## Revision note
Identical across tools; 40-line distilled checklist derived from the open-seo project.
