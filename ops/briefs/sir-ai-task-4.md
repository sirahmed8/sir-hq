# SIR AI — Task 4: Phone Remote Capacitor Shell (Android)

**Version:** 1.0.0
**Date:** 2026-11-12
**Source:** `ops/briefs/sir-ai-tasks.md` Task 4
**Target:** Free CLI agents via HQ autopilot

---

## Brief

Wrap the existing web PWA (`apps/web`) in Capacitor for Android.

**Features:**
- Daily-rhythm surface: plan (Fajr), check-ins (midday/evening), Isha summary — all read-only from Firestore
- Live desktop task list via `users/{uid}/devices/{desktopId}/commands` with real-time listeners
- Buttons: Pause / Resume / Approve (write to `users/{uid}/approvals/{id}` with idempotency key)
- Web Push with quick-reply actions: "Send / Edit / Later" (Service Worker + Push API, VAPID keys in env)
- QR pairing: phone scans QR on desktop → writes device record with 10-min expiry, single-use
- Offline queue: writes to IndexedDB with idempotency keys; syncs on reconnect (replay with deduplication)
- Capacitor config: Android permissions for camera (QR), notifications, network
- Build: `gradlew assembleRelease` produces signed AAB (debug keystore for dev, release keystore from owner later)

---

## Acceptance Test

1. `npm run cap:android:build` → AAB builds without errors.
2. Install on physical device/emulator → app opens, shows daily rhythm (plan + 2 check-ins + summary) from Firestore.
3. Desktop agent running → phone shows live task list (command ID, status, output tail).
4. Tap "Pause" on a running task → desktop agent receives approval → task pauses → phone updates status.
5. Web Push: send test push → notification appears with "Send / Edit / Later" → tap "Send" → `/approve` fires.
6. QR pairing: desktop shows QR → phone scans → device linked → 10-min expiry enforced (second scan fails).
7. Offline: airplane mode → create check-in response → reconnect → syncs to Firestore with idempotency key (no duplicate).
8. 16-combo sweep (320/390/768/1280 × ar/en × light/dark) → 0 horizontal scroll, 0 findings.
9. Evidence: build log + device screenshots in `.sir/evidence/task-4/`.

---

## Dependencies

- Task 1 (Memory Notes), Task 2 (Connector Marketplace), Task 3 (Automations) — core schemas and web app must be stable
- `apps/web` PWA already working (T-060 done)
- Firestore collections `devices`, `commands`, `approvals` already exist with rules (T-063, T-064 done)

---

## Implementation Plan

1. **Capacitor setup**: `npm install @capacitor/core @capacitor/cli @capacitor/android`, `npx cap init`, configure `capacitor.config.ts`
2. **Android project**: `npx cap add android`, sync, configure `android/app/src/main/AndroidManifest.xml` permissions (CAMERA, INTERNET, VIBRATE, POST_NOTIFICATIONS, FOREGROUND_SERVICE)
3. **Daily rhythm screen**: new route `#/phone/daily` in web app, reads `users/{uid}/plan/main`, `users/{uid}/checkins/{date}`
4. **Live task list**: listener on `users/{uid}/devices/{desktopId}/commands`, real-time updates
5. **Action buttons**: Pause/Resume/Approve write to `commands/{id}` and `approvals/{id}` with idempotency keys
6. **Web Push**: Service Worker registration, VAPID keys, push subscription, quick-reply actions
7. **QR pairing**: QR code generation on desktop (`/phone/pair`), camera scanning on phone, write to `devices/{id}` with 10-min expiry
8. **Offline queue**: IndexedDB store with idempotency keys, sync on reconnect with deduplication
9. **Build script**: `npm run cap:android:build` → `gradlew assembleRelease`
10. **Sweep**: 16-combo browser test on web version, device screenshots for evidence

---

## Evidence Required

- Build log showing successful AAB production
- 16-combo screenshots (320/390/768/1280 × ar/en × light/dark) in `.sir/evidence/task-4/`
- Device/emulator screenshots showing daily rhythm, live task list, QR pairing, push notification
- Acceptance test log

---

## Quality Gates

- TypeScript strict, ESLint clean
- All existing tests pass
- No new lint/type errors
- Version stays 1.0.0
- No emoji, no em-dashes in copy
- Five UI states on every screen
- Arabic RTL + English LTR, light + dark