# firebase-hosting-basics

## Summary
Pointer skill for classic Firebase Hosting — CDN-backed static/dynamic content hosting with SSL, preview channels, GitHub Actions integration, and Cloud Functions/Run rewrites for dynamic content. It is deliberately thin: behavior details live in references/configuration.md (public dirs, redirects, rewrites, headers), references/deploying.md (deploy, preview channels, releases), plus an emulation command. Includes the Hosting-vs-App-Hosting decision guide (static/SPA/CLI-control vs SSR/ISR/git-push).

## When to use / when NOT
Use for static sites, SPAs without SSR, custom domains, preview channels. Do NOT use for Next.js/Angular SSR or ISR (firebase-app-hosting-basics). Read the reference docs — the SKILL.md alone does not contain the config syntax.

## Inputs, outputs, tools
- Inputs: static build output dir, firebase.json hosting config, deploy intent.
- Outputs: deployed site on Firebase CDN, preview channel URLs, release history.
- Tools: `firebase.json` hosting block, `npx -y firebase-tools@latest deploy`, `emulators:start --only hosting` (localhost:5000), GitHub Actions integration.

## 5 most important rules
1. Choose Hosting for static/SPA content; App Hosting for SSR frameworks — don't mix them up.
2. All real configuration detail (rewrites to Functions/Run, headers, redirects) is in references/configuration.md — load it before editing firebase.json.
3. Deploy mechanics, preview channels and release management are in references/deploying.md.
4. Test locally first with `emulators:start --only hosting` (port 5000 default).
5. SIR dual-hosting rule: every public site is also deployed to Vercel — Firebase Hosting is one of two required hosts.

## Risks / owner needs
Custom domains need DNS/console access (owner). Preview channels and GitHub integration need repo/CI permissions.

## Category and tags
Category: cloud. Tags: firebase, hosting, static-site, spa, cdn, deploy, preview-channels.

## Revisions
Identical across the 7 tools; claude copy used.
