# website-traffic-analytics (claude revision)

## Summary
website-traffic-analytics is a compact analytics-audit framework for web properties across GA4/Plausible/PostHog/Cloudflare. Three sections: (1) metric taxonomy — unique visitors, engagement rate formula (engaged session = >10s OR conversion OR >=2 pageviews), bounce-rate diagnosis (>65% on informational pages signals weak intent match, LCP>2.5s, or CLS>0.1), and acquisition channel breakdown (direct/organic/referral/social/paid); (2) a funnel-leak mermaid (landing → >15s engagement → pricing/feature exploration → checkout click → conversion) with a per-step drop-off diagnostic table (hero fails 5-second test → trust badges missing → pricing confusion/Hick's Law → form friction); (3) SEO diagnostics — brand vs non-brand ratio (healthy >=40% non-brand), top-pages intent alignment, Core Web Vitals correlation with rank drops.

## When to use / when NOT
Use when auditing site traffic, visitor telemetry, bounce rate, SEO acquisition or conversion funnels. It's a diagnostic framework, not an API integration skill — it doesn't pull GA4 data itself; pair with analytics MCPs/tools for actual numbers. Do NOT use for implementing analytics tracking code (that's a different task).

## Inputs, outputs, tools
- Inputs: analytics data from whichever provider the site uses, funnel definitions.
- Outputs: metric calculations, funnel drop-off diagnosis, SEO health assessment.
- Tools: none built in — works over data from GA4/Plausible/PostHog/Cloudflare provided by the user or MCPs.

## 5 most important rules
1. Bounce rate >65% on informational pages = intent-match/LCP/CLS problem, not a "bad metric".
2. Engaged session has a precise definition (>10s, conversion, or >=2 pageviews) — use it, not raw sessions.
3. Diagnose funnel leaks step-by-step with the named causes per transition (stranger test, trust signals, Hick's Law, form friction).
4. Healthy organic acquisition keeps >=40% non-brand queries — brand-heavy means SEO dependency risk.
5. Correlate CWV (LCP/INP/CLS) with rank and bounce data before recommending content fixes.

## Risks / things needing the owner
No side effects — analysis only. Risk is misdiagnosis if applied without real analytics data; the skill supplies the framework, the user/MCP supplies numbers. No owner actions.

## Category / tags
data · analytics, seo, conversion, funnel, ga4

## Revisions
Single source read: `C:\Users\a7med\.claude\skills\website-traffic-analytics\SKILL.md` (57 lines). Slice lists six tools; claude revision preferred.
