# Phase 4 — The the shared standards kit (foundation before rollout)

> **Read first:** `START_HERE.md`, then `standard/README.md`, `standard/02-architecture.md`, `standard/03-data-backend.md` and `standard/04-security-privacy.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with `phases/05-upgrade-waves.md`.

**4.1 `D:\Projects\_SIR\standard\` (git repo `sir-standard`).** The standard already ships as files in this folder: `README.md`, `agent-files.md` (the AGENTS, CLAUDE and GEMINI templates), modules `01`–`22` and `project-templates.md`. Make the folder a git repo and add a `sync-standard` script that copies the modules into each project's `docs/sir/standard/` and stamps `STANDARD_VERSION` (it starts at 1.0.0). Projects never edit their copy; changes go to the master and are synced out.

**4.2 `D:\Projects\_SIR\platform\` (git repo `sir-platform`).** A pnpm + Turborepo monorepo containing:

- the shared `@sir/*` packages (module 02),
- the product template and the `create-sir-product` scaffolder,
- CI workflow templates,
- the brand and icon pipeline,
- a component gallery: Storybook for web and desktop, a gallery screen for mobile.

Publish the packages privately (GitHub Packages) with SemVer, so products pin versions and upgrade through Renovate or Dependabot PRs.

**4.3 Golden path.** Take one Wave-1 product all the way before touching the rest:

- prove the zero-cost stack from module 22 (Firebase on the free plan; Cloudflare for hosting, server code and files; Cloudinary for media; all inside the free limits), with the security job, notifications, the owner dashboard and the support suite working;
- prove the AI core from module 10: the flagship AI feature and the assistant running through the AI gateway, with at least three cloud providers in the fallback chain plus an on-device path, and evaluation sets passing for each provider;
- submit the Windows build to the Microsoft Store (MSIX) to learn the certification path;
- web on a preview deployment, Windows installer, macOS build in CI, Android on emulators plus an AAB, iOS cloud-build config (and a simulator build if possible), iPad layout, and a watch companion if it applies;
- legal pages and consent, icons, launchers, docs, CI gates green.

Then fix the template with everything you learned. Only then roll out.
