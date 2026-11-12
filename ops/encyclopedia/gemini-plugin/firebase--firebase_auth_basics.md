# firebase-auth-basics

## Summary
Guide for setting up Firebase Authentication: users identified by `uid` with email/displayName/photoURL/emailVerified; providers (email/password, federated Google/Facebook/etc., phone, anonymous, custom); ID tokens (1h JWT) vs refresh tokens for service access. Provisioning via `firebase.json` auth block (CLI-deployable providers: anonymous, emailPassword, googleSignIn) then `firebase deploy --only auth`, or console for other providers; client SDK setup per platform (web/flutter/android/ios references); security rules via `request.auth`.

## When to use / when NOT
Use for any sign-in, account management, or auth-aware security rules work. Do NOT enable non-CLI providers by editing firebase.json alone — they need the console. Not for custom JWT systems unrelated to Firebase Auth.

## Inputs, outputs, tools
- Inputs: chosen providers, brand display name/support email/redirect URIs for Google Sign-In, target platforms.
- Outputs: deployed auth config (`deploy --only auth`), client SDK integration, auth-aware rules.
- Tools: `firebase.json` auth block, `npx -y firebase-tools@latest deploy --only auth`, Firebase console providers page, per-platform client SDK references (client_sdk_web/android, flutter_setup, ios_setup, security_rules).

## 5 most important rules
1. After editing firebase.json auth config you MUST run `firebase deploy --only auth` — without it providers don't auto-generate OAuth clients and sign-in fails.
2. Google Sign-In is the recommended secure default provider; CLI can enable only anonymous, email/password and googleSignIn — everything else goes through the console.
3. Authorized domains must be bare hosts — `localhost`, NOT `http://localhost:9090`; missing domain causes `[firebase_auth/unauthorized-domain]` popup errors.
4. ID tokens are short-lived (1h) — use refresh tokens for new ones; `request.auth` in Firestore/Storage rules is the auth-aware security mechanism.
5. Complete prerequisites first: firebase-basics skill (project + CLI login) before any auth setup.

## Risks / owner needs
OAuth consent screens, authorized domains and provider enablement may need console/owner access. Anonymous auth can be upgraded by linking later — plan account-merging UX.

## Category and tags
Category: security. Tags: firebase, authentication, oauth, google-sign-in, security-rules, identity.

## Revisions
Identical across the 7 tools; claude copy used.
