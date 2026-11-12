# netlify-forms (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-forms\SKILL.md`. Serverless form handling — deploy-time HTML detection, no backend code.

## Summary
Forms are detected by PARSING FINAL BUILT HTML at deploy — no runtime API. Mark `<form>` with `data-netlify="true"` (or bare `netlify`); `name` must be unique per site; Netlify strips the attribute and injects hidden `form-name` input; an `<input name="email">` sets notification Reply-to. Prerequisite: enable form detection once in UI (Forms > Enable form detection) — effective next deploy. JS-rendered/SSR/framework forms (Next.js, Nuxt, SvelteKit, Astro, Gatsby) are NEVER auto-detected — require TWO pieces: (1) static skeleton `public/__forms.html` with hidden `data-netlify` copy of each form + hidden `form-name` + every field with EXACT matching names, and (2) rendered form carrying matching hidden `form-name` input. SSR POST footgun: `fetch("/")` hits the SSR catch-all and never reaches form processing — POST to `/__forms.html` (the skeleton itself). Astro `prerender=false`/`output:"server"` routes are never scanned — use skeleton or prerendered page. Next.js Runtime v5: extract definitions to skeleton, submit via AJAX. AJAX pattern: `fetch("/__forms.html", {method:POST, urlencoded body})`. Also covers spam filtering (honeypot/reCAPTCHA), custom thank-you pages, notifications/ChatGPT automations on submission events, reading submissions via API, and debugging silently-failing forms.

## When to use / when NOT
Use for contact/lead/newsletter/file-upload forms on Netlify sites, AJAX submission, thank-you pages, spam protection, framework forms, submission notifications, or debugging missing submissions. NOT for fully custom backends (though submissions are also API-readable).

## Inputs, outputs, tools
- Inputs: HTML form markup, field names, skeleton file for JS-rendered forms.
- Outputs: detected forms in Netlify UI, stored submissions, notification emails.
- Tools: `data-netlify` attribute, `public/__forms.html` skeleton, Netlify Forms UI/API, honeypot/reCAPTCHA.

## 5 most important rules
1. Detection = built-HTML parse at deploy — enable detection in UI once first.
2. JS/SSR/framework forms need BOTH the static skeleton AND matching `form-name` hidden input with EXACT field names.
3. SSR must POST to `/__forms.html`, never `/` (catch-all swallows it).
4. `name` must be unique per site; include `<input name="email">` for Reply-to.
5. Missing skeleton or mismatched field names = submissions silently fail — the #1 debugging target.

## Risks / owner notes
Silent failure is the dominant failure mode (no skeleton, name mismatch, detection not enabled). Form spam needs honeypot/reCAPTCHA config. File-upload forms have size/type limits per plan.

## Category and tags
Category: cloud. Tags: netlify, forms, spam, ssr, nextjs, static-skeleton, notifications.
