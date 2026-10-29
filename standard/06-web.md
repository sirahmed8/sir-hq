# 06 — Web

- Next.js App Router with TypeScript strict. Server Components by default. Server Actions and route handlers validate input with Zod and check auth.
- **Routing and i18n:** a prefix per locale (`/ar`, `/en`, `/zh`, `/hi`), correct `dir` and `lang`, `hreflang` for every locale plus `x-default`, localized metadata and per-locale sitemaps.
- **SEO:** metadata, sitemap, robots, JSON-LD structured data, OG images, canonical URLs. Full playbook in module 16.
- **Performance budgets** (75th percentile, mobile): LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; Lighthouse ≥ 90 in every category. Per-route JS budget enforced in CI. `next/image` with AVIF/WebP and explicit sizes; `next/font` with subset Arabic and Latin fonts; heavy components (charts, 3D, editors) code-split.
- **PWA** where it adds value: installable, offline fallback page.
- **Legal routes** in every locale: `/privacy`, `/terms`, `/eula` (when an app ships), `/refunds` (if paid), `/cookies`, `/data-deletion`, `/licenses`. No dead `#` links anywhere.
- **Cookie consent** with "Reject all" exactly as prominent as "Accept all"; no non-essential trackers before opt-in.
- **Footer:** brand and entity name, jurisdiction (Egypt), support contact, app version, and a copyright year computed at runtime (`new Date().getFullYear()`), never hard-coded.
- **Security headers** through middleware or config (module 04). Error boundaries, custom 404 and 500 pages.
- **Vercel:** a preview deploy for every PR, production from `main` only, environment variables separated per environment, instant rollback available.
