# firebase-app-hosting-basics

## Summary
Guide for deploying full-stack SSR frameworks (Next.js, Angular) to Firebase App Hosting — the git-push-to-deploy counterpart to classic Firebase Hosting. Covers choosing App Hosting vs Hosting (SSR/ISR/automated deploys vs static sites/CLI control), firebase.json `apphosting` block config, `apphosting.yaml` backend config, secrets via `apphosting:secrets`, CLI deploy, optional GitHub CI/CD backend connection, and local emulation.

## When to use / when NOT
Use for Next.js/Angular (or other supported full-stack frameworks) needing SSR, ISR, or zero-config git-push deploys. Do NOT use for static sites or SPAs without SSR (use firebase-hosting-basics instead). Requires the Blaze pay-as-you-go plan — direct the user to upgrade if not on it.

## Inputs, outputs, tools
- Inputs: a supported SSR framework project, Firebase project on Blaze plan, backendId, rootDir.
- Outputs: deployed App Hosting backend serving the SSR app; optional GitHub-connected CI/CD.
- Tools: `npx -y firebase-tools@latest deploy`, `apphosting:secrets` (set/grant secret access), `apphosting.yaml` config, Firebase Local Emulator Suite for testing; references configuration.md, cli_commands.md, emulation.md.

## 5 most important rules
1. App Hosting requires Blaze plan — verify/upgrade before anything else.
2. Pick the right product: static site or SPA without SSR → Firebase Hosting; SSR/ISR/full-stack framework → App Hosting.
3. Configure `firebase.json` with the `apphosting` block (backendId, rootDir, ignore list) and `apphosting.yaml` for backend settings before deploying.
4. Use `apphosting:secrets` commands to set secrets and grant the backend access — never commit secret values.
5. GitHub-connected automated deployment is optional and "not required" — recommended only for advanced users; plain `firebase deploy` works.

## Risks / owner needs
Blaze billing is owner territory (no-budget rule: agents prepare, owner buys). Secrets handling and domain/custom-domain decisions need care. SSR apps cost more than static hosting.

## Category and tags
Category: cloud. Tags: firebase, app-hosting, ssr, nextjs, angular, deploy, ci-cd.

## Revisions
Identical across the 7 tools; claude copy used.
