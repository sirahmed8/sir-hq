# levelplay-unity-integration (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\levelplay-unity-integration\SKILL.md` (38 KB workflow spine; `references/` has 12 files: banner/interstitial/rewarded-api, initialization-api, dependency-resolution, privacy-settings, ios-setup, ilrd-api, best-practices, testing-and-validation, troubleshooting, migration-sdk-9).

## Summary
Strictly sequential LevelPlay (Unity ad mediation, ex-IronSource) integration workflow for Unity projects, one checkpoint at a time. Step 0 routes new vs migration (5 scenarios A-E incl. SDK upgrade, init/ad-unit API migration, Maven Central `is.com` shutdown fix, Unity Ads migration) vs troubleshooting. Then: verify Unity project (Assets/+ProjectSettings/), ask optimization goal (revenue/UX/balanced → drives Step 8 strategy), install "Ads Mediation" UPM package (`com.unity.services.levelplay` — verify in BOTH `manifest.json` AND `packages-lock.json`, a hard gate: never write LevelPlay code until the lock file shows it, never hand-edit the lock file), resolve native deps via MDR/UEDM/EDM4U (critical — compiles in Editor, fails at Android/iOS build; switch build target first; AD_ID permission for API 33+), collect App Key + ad unit IDs from platform.ironsrc.com dashboard, optional AdMob keys, privacy/regulation settings BEFORE init if GDPR/CCPA/COPPA applies (SDK-version-dependent APIs), initialize (re-check lock file, confirm prerequisites, offer 4 code-organization options, ILRD wiring differs by SDK 9.5.0+ vs 9.4.x), recommend ad-unit strategy mapped to the Step-2 goal, implement only the chosen formats (Rewarded/Interstitial/Banner) with best-practices patterns (persistent GameObject, DestroyAd in OnDestroy, event unsubscription, placement caps), then mock-ad/Test-Suite validation.

## When to use / when NOT
Use for ANY LevelPlay/Ads Mediation work in a Unity project: fresh install, SDK 9 migration, Unity Ads/IronSource migration, ad units, privacy compliance, build failures. Not for other mediation SDKs (skill forbids characterizing competitors) or non-Unity engines.

## Inputs, outputs, tools
- Inputs: Unity project, target platform(s), optimization goal, LevelPlay dashboard credentials (App Key, ad unit IDs), AdMob keys if used.
- Outputs: installed+resolved SDK, initializer MonoBehaviour, per-format ad managers, privacy config, test validation.
- Tools: Unity Package Manager, Network Manager (adapters), dependency resolvers (MDR/UEDM/EDM4U), LevelPlay dashboard, platform.ironsrc.com.

## 5 most important rules
1. HARD GATE: `com.unity.services.levelplay` must appear in `Packages/packages-lock.json` before ANY LevelPlay code — check the file, not the Package Manager window or memory; never hand-write the lock entry.
2. One step at a time: ask only current-step questions, wait at each checkpoint; re-confirm init before ad code and initialization log before ad units.
3. Native dependency resolution is mandatory for device builds and must run for EACH target platform; switch active build target first.
4. Privacy settings (GDPR/CCPA/COPPA, ATT on iOS) are configured BEFORE `LevelPlay.Init`, with SDK-version-correct APIs (9.5.0+ global consent boolean).
5. ILRD: SDK 9.5.0+ wires per-ad-instance `OnAdImpressionDataReady` (global event deprecated); ≤9.4.x subscribes globally before Init. Mock ads don't fire ILRD — needs device build.

## Risks / owner notes
Real ad revenue and legal exposure: privacy/consent config is a legal matter (skill disclaims legal advice). Dashboard credentials are owner secrets. Generated C# is for the user to save, not inline-executed. iOS needs ATT/SKAdNetwork; Android needs AD_ID permission.

## Category and tags
Category: mobile. Tags: unity, levelplay, ads, mediation, monetization, privacy-gdpr, migration, build-troubleshooting.
