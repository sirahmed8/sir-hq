# netlify-forms

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-forms\SKILL.md`
- SKILL.md size: 11566 chars

## What it does

Serverless form handling on Netlify.

## Structure (headings inside SKILL.md)

- Netlify Forms
- Static HTML form
- JS-rendered / SSR / framework forms (Next.js, Nuxt, SvelteKit, Astro, Gatsby)
- AJAX submission
- File uploads
- Custom success page
- Spam prevention
- Email notifications & subject line
- Reading submissions via the API
- Submission summary (field order matters)
- Debugging missing submissions
- Constraints
- Netlify house rules (forms)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `SITE_RECAPTCHA_SECRET` — secret (scope: Runtime)
- - **Page through results using the `Link` header** — code that reads only the first response silently drops the rest.
- - For PII, export and delete data regularly.

## Key rules (verbatim lines from SKILL.md)

1. - `name` sets the form name in the UI and **must be unique per site**.
2. - **Body MUST be URL-encoded. JSON is NOT supported.**
3. - If the rendered form has no hidden `form-name` input, you MUST include a `form-name` field in the POST body.
4. - The honeypot field name and `g-recaptcha-response` (if used) must be in the body — automatic with `FormData()`.
5. - **First suspect: Akismet false positive.** A missing legitimate submission is usually spam-flagged — check the **Spam** list (or API `?state=spam`) and mark it verified. Do NOT build a custom recovery function or disable spam filtering as a first resort.

## Files inside the skill

- (SKILL.md only)
