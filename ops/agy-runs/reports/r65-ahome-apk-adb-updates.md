# r65 — AHome APK / ADB / phone power-off / update system

Worker: Devin CLI. Date: 2026-11-13. Repo: `D:\Projects\AHome` (branch `main`).
Brief: `D:/Projects/_SIR/ops/briefs/r65-ahome-apk-adb-updates.prompt.txt`.

## Result summary

- **A (release APK + adb install + launch + screenshot): PARTIAL / BLOCKED.** Signed release APK v1.0.0 built and on the phone's Download folder, but `adb install -r` fails with `INSTALL_FAILED_USER_RESTRICTED` because the phone is PIN-locked (`mDreamingLockscreen=true`). Owner action written to `_SIR/ops/OWNER_ACTIONS.md`. Launch and screenshot are pending that single unlock.
- **B (phone power-off investigation): DONE.** Report at `_SIR/ops/reports/phone-poweroff-report.md`, committed to sir-hq as `c90c156` and pushed. Verdict: two clean software-requested shutdowns ~3.3 days apart; battery, thermals, PC scripts/tasks and AHome daemons all ruled out. Most likely MIUI scheduled power on/off or a very long power-button press. Nothing of ours to fix.
- **C (update system): DONE, code complete, committed `482a988`, pushed to `main`.** Telegram APK+changelog delivery, in-app update card wired to a real native install path (REQUEST_INSTALL_PACKAGES + FileProvider), remote versioned config with rollback guard, changelog generated from commits, fake-version test hook preserved for test builds. Verified with tsc, eslint, Gradle compile, and the node test suite (1029 pass; 6 failures are all missing-Playwright-WebKit environment issues, unrelated).

CI note: the CI quota flag (`_SIR/ops/ci-quota-exhausted.flag`) still applies, so local verification was the gate, per the worker manual.

## A — release APK

### Keystore
- Created with `scripts/make-android-keystore.ps1` (rejects in-repo paths by design).
- Location (outside repo, never committed): `D:\Projects\Android\signing\ahome-release.jks`, properties at `D:\Projects\Android\signing\keystore.properties` (read via env var `AHOME_KEYSTORE_PROPERTIES`). 4096-bit RSA, alias `ahome`, ~25-year validity. Password never printed or stored in git.

### Build
- `versionName` stays `1.0.0`; `versionCode` derives from git commit count (existing scheme).
- Gradle release build succeeded. Output: `apps/mobile-capacitor/shell/android/app/build/outputs/apk/release/app-release.apk` (~5.2 MB, signed; cert SHA-256 begins `5d5044d4`).
- Copied to `dist/AHome-v1.0.0.apk` (gitignored).

### Device delivery
- `adb devices` → `ronf6d5hrkqsuoaa device` (Redmi rubypro, Android 14 / HyperOS).
- `adb push` to `/sdcard/Download/AHome-v1.0.0.apk` succeeded.
- `adb install -r` retried twice (second attempt ~01:30 after `input keyevent KEYCODE_WAKEUP`): both fail `Failure [INSTALL_FAILED_USER_RESTRICTED: Install canceled by user]` because `dumpsys window` shows `mDreamingLockscreen=true`. MIUI cancels package installs while the keyguard is showing.
- The earlier debug app was uninstalled for the signature migration (release cert ≠ debug cert); its data was WebView storage only — all real AHome data is server-side. No user data was deleted by this round.
- Owner action in `_SIR/ops/OWNER_ACTIONS.md`: unlock the phone once (PIN/face), then either tap `AHome-v1.0.0.apk` in Download or leave it unlocked; next run does `adb install -r` + launch + `adb exec-out screencap -p`.

## B — phone power-off investigation

Full evidence in `_SIR/ops/reports/phone-poweroff-report.md`. Key findings:

- `persist.sys.boot.reason.history`: `shutdown,userrequested` twice, ~3.3 days apart (epoch 1794509497, 1794220933).
- `SYSTEM_LAST_KMSG` (Dropbox): orderly shutdown — charger/fuel-gauge shutdown, `device_shutdown`, `__arm64_sys_reboot`, `reboot: Restarting system`. Not a crash, not a battery cutoff.
- `dumpsys battery`: 100%, ~4384 mV, 26.5 °C, health good. Thermal status 0, no thermal shutdown.
- PC Task Scheduler: `AHome-GameMode`, `AHome-Services` run `run-hidden.vbs`, `ahome-gamemode.ps1`, `ahome-service-supervisor.ps1 -Watch`. Grep of `infra-daemons`/`scripts` found no `adb reboot`, `shutdown`, `svc power`, or similar. No agent calls power commands.
- Conclusion: software-requested shutdowns consistent with MIUI/HyperOS scheduled power on/off or an unusually long power-button press. Nothing attributable to AHome; nothing to fix.

## C — update system (commit `482a988`)

### Android native bridge — `MainActivity.java` + `AndroidManifest.xml`
- Added `android.permission.REQUEST_INSTALL_PACKAGES`.
- New `AHomeNative` JavascriptInterface methods:
  - `getAppVersion()` → `{versionName, versionCode}` so the web layer compares real installed builds.
  - `postUpdateNotification(json)` → posts on new channel `ahome_updates`; tap opens `https://t.me/Personal1AI1Bot?start=update` (the bot chat that already has the APK + changelog).
  - `installAppUpdate(json)` → downloads the APK to `cacheDir/updates/` on the bridge thread, verifies SHA-256 when supplied, then on the UI thread exposes it via the existing FileProvider (`${applicationId}.fileprovider`, `cache-path` already covers the cache dir) and fires `ACTION_VIEW` with `application/vnd.android.package-archive`. Falls back to opening the URL if the provider fails. Deletes partial files on error/mismatch.
- Gradle `compileDebugJavaWithJavac` passes (one pre-existing deprecation note).

### Web layer
- `src/lib/nativeUpdate.ts` (new): typed, null-safe wrapper — `getInstalledVersion`, `postNativeUpdateNotification`, `installUpdateNative`. No-ops outside the native shell.
- `src/lib/pairing/appDownload.ts`: `AppVersion` gains optional `versionCode` and `changelog`; parser validates them.
- `src/components/island/activities/appUpdate.tsx`: real update detection — inside the shell it compares remote `versionCode` > installed `versionCode`; outside it keeps the previous build-fingerprint check. On detection it posts the system notification once per build (`ahome_update_notified_<buildId>` in localStorage). "Update Now" inside the shell runs the real native download+install (states downloading → installing/failed); browser path unchanged. Fake-version hooks kept: `?testUpdate=1` and the `ahome:test-fake-update` window event — test-build only, production version untouched.
- `src/lib/remoteConfig.ts` (new) + `public/config/app-config.json`: versioned remote flags (`configVersion`, `flags`, `minAppVersion`, optional `notice`). Fetched `cache:"no-store"`, schema-validated, last-good copy in localStorage, `configVersion` monotonicity guard = safe rollback; fetch/validation failure falls back to cache. `warmRemoteConfig()` is called from the island update effect so small fixes ship without an APK.

### Release pipeline scripts
- `scripts/gen-changelog.mjs` (new): builds the changelog from `git log` (skips merge/wip/checkpoint noise), writes `apps/web/public/changelog-latest.md`, prints to stdout. Verified: emits real commit entries.
- `scripts/publish-update.mjs` (new): `node scripts/publish-update.mjs <apk> [--telegram]` → copies APK to `apps/web/public/downloads/AHome-v<version>.apk`, writes `version.json` (file, version, versionCode, size, sha256, builtAt, changelog), and with `--telegram` calls the sender.
- `scripts/publish-apk.mjs`: now also writes `versionCode` into `version.json`.
- `infra-daemons/send-update.py` (new): reads `TELEGRAM_BOT_TOKEN`, `AHMED_CHAT_ID`, `HABIBA_CHAT_ID` from `apps/local-core/.env`, sends the APK as a document with the changelog caption to both chat ids via `sendDocument`. Bot identity is `@Personal1AI1Bot` (verified via `getMe`). Chat-id → person mapping reuses the env pins the gateway already uses.

### Verification evidence
- `npx tsc --noEmit` in `apps/web`: clean.
- `npx eslint` on the four touched web files: 0 errors (one pre-existing exhaustive-deps warning on the island card's useMemo).
- `gradlew :app:compileDebugJavaWithJavac`: BUILD OK.
- `node --test tests/*.test.mjs`: 1041 tests, 1029 pass, 6 fail — all six are Playwright WebKit tests failing with "Executable doesn't exist … webkit-2388" (browser binary not installed on this machine; pre-existing environment gap, unrelated to these changes).
- `node scripts/gen-changelog.mjs --count 8`: real commit list output.
- Commits: `482a988` on `main`, pushed to `origin/main` (`4efe3fc..482a988`).

### Not verified / open
- On-device install flow (`installAppUpdate` → package installer) is compiled and type-checked but not run on the phone — blocked by the same lock-screen issue as item A. First unlocked run should exercise it via `?testUpdate=1` on a debug build or a real publish.
- `send-update.py` was written against the existing `telegram_api.send_document` contract but not executed end-to-end (no release was published this round; version stays 1.0.0 and nothing was sent).
- The hosted `version.json` still describes the previous debug APK (`a903972f…`); it gets refreshed the next time `publish-update.mjs`/`publish-apk.mjs` runs before a Vercel deploy.

## Files touched this round

AHome repo (`482a988`):
- `apps/mobile-capacitor/shell/android/app/src/main/AndroidManifest.xml`
- `apps/mobile-capacitor/shell/android/app/src/main/java/app/sir/ahome/MainActivity.java`
- `apps/web/src/components/island/activities/appUpdate.tsx`
- `apps/web/src/lib/pairing/appDownload.ts`
- `apps/web/src/lib/nativeUpdate.ts` (new)
- `apps/web/src/lib/remoteConfig.ts` (new)
- `apps/web/public/config/app-config.json` (new)
- `apps/web/public/changelog-latest.md` (new, generated)
- `scripts/publish-update.mjs`, `scripts/gen-changelog.mjs` (new), `scripts/publish-apk.mjs`
- `infra-daemons/send-update.py` (new)

HQ repo (sir-hq `c90c156`, pushed): `_SIR/ops/reports/phone-poweroff-report.md`, `_SIR/ops/OWNER_ACTIONS.md` entry.

Local-only: `D:\Projects\AHome\.sir\CHECKPOINT.md` updated (`.sir/` is git-excluded).

## Recommended next steps
1. Owner unlocks the phone once → run `adb install -r dist/AHome-v1.0.0.apk`, launch `app.sir.ahome`, capture screenshot.
2. On that same unlocked session, install the new debug build and open `?testUpdate=1` to exercise notification + install path end to end.
3. When the owner approves a real release: bump nothing (version stays 1.0.0 until told), run `node scripts/publish-update.mjs dist/AHome-v1.0.0.apk --telegram`, then `vercel deploy` from `apps/web`.
4. Install Playwright WebKit (`npx playwright install webkit`) to clear the 6 environment test failures.
