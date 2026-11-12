# firebase-remote-config-basics

## Summary
Guide for Firebase Remote Config on Android/iOS: a cloud template of key-value parameters and targeting conditions that changes app behavior without an app update. Covers prerequisites (project + mobile app, CLI for template management), SDK setup per platform, fetching strategies (activate-previous-then-fetch-next-startup pattern, real-time listeners), and template lifecycle via CLI: `remoteconfig:get -o remote_config.json` → edit JSON (parameters + conditions like device.country/percent) → MANDATORY user review → `deploy --only remoteconfig` → `remoteconfig:versions:list` verify. Includes troubleshooting for npx 403 and missing project context.

## When to use / when NOT
Use for feature flags, A/B parameters, remote model names, kill switches in Android/iOS apps. Mobile-focused — not for web Remote Config (different SDK path). Not for secrets — Remote Config values are client-visible.

## Inputs, outputs, tools
- Inputs: parameter/condition changes desired, target project id.
- Outputs: edited remote_config.json deployed as a new template version.
- Tools: `remoteconfig:get`, `remoteconfig:versions:list`, `deploy --only remoteconfig`, firebase.json `remoteconfig.template` mapping, per-platform SDK setup refs (android_setup, ios_setup).

## 5 most important rules
1. MANDATORY user review gate: after editing remote_config.json, STOP and ask the user to verify before deploying — never push template changes unreviewed.
2. Preferred fetch pattern: activate previously-fetched values at startup, fetch new values in background for next launch; use real-time listeners for instant updates.
3. Map the file first: if no firebase.json exists, create `{ "remoteconfig": { "template": "remote_config.json" } }` before `deploy --only remoteconfig`.
4. Always verify deployment with `remoteconfig:versions:list`.
5. Set in-app defaults so the app works offline/before first fetch; determine correct condition signals (device.country, percent rollouts) when editing conditions.

## Risks / owner needs
Template deploys affect ALL targeted users instantly — the review gate exists for this reason. Parameters are visible to clients; never put secrets in Remote Config. npx 403 fallback requires globally installed firebase-tools (owner-installed).

## Category and tags
Category: cloud. Tags: firebase, remote-config, feature-flags, mobile, android, ios, rollout.

## Revisions
Identical across the 7 tools; claude copy used.
