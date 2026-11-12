# levelplay-unity-integration

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\levelplay-unity-integration\SKILL.md`
- SKILL.md size: 38043 chars

## What it does

Integrates the LevelPlay ad mediation SDK via the Ads Mediation package. Use when the user asks about adding rewarded, interstitial, or banner ads, mediation or ad privacy setup, Android or iOS ad dependency build failures, or migrating from Unity Ads or IronSource APIs.

## Structure (headings inside SKILL.md)

- LevelPlay Unity package/SDK Integration
- Integration Workflow
- 0. New Integration or Migration?
- 1. Verify Unity Environment
- 2. Understand Business Goals
- 3. Install LevelPlay SDK via UPM
- 4. Resolve Native Dependencies (Critical)
- 5. Get App Key and Ad Unit IDs
- 6. Configure AdMob Keys (If Using AdMob Network)
- 6.5. Privacy & Regulation Settings (If Required)
- 7. Initialize LevelPlay SDK
- 8. Recommend Ad Unit Strategy
- 9. Implement Ad Units
- 10. Testing and Validation
- Adding More Ad Formats Later
- Best Practices
- Common Issues and Solutions
- When to Read Detailed References
- Examples
- Core Rules (reminder)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2. Select Unity Registry dropdown or Services tab
- - Missing Step 5: They won't have credentials to initialize → Direct to Step 5
- - **SDK 9.5.0+ (current):** add nothing to the initializer — ILRD is delivered per ad instance via `OnAdImpressionDataReady`, wired when each ad is created in Step 9. The global `LevelPlay.OnImpressionDataReady` event is **deprecated on 9.5.0+ and generates a compiler warning** — do not use it.
- - **Revenue-focused** → **Revenue Strategy.** Rewarded (primary monetization, multiple high-value moments) → Interstitial (secondary; at transitions; frequency cap 3–5 min) → Banner (persistent during gameplay). Bid floors are an optional revenue lever configured in Step 9. Implementation priority: 

## Key rules (verbatim lines from SKILL.md)

1. 4. Confirm the package name matches exactly: the correct package is titled **Ads Mediation**. Do not install either of these packages:
2. - **`Packages/packages-lock.json`** records what Unity actually *resolved*. The same id must appear
3. - Package id absent from `packages-lock.json`: code will show `CS0246` namespace errors → Direct to Step 3. This one you established yourself; do not ask the user to overrule it.
4. - Do not provide C# code until they confirm all steps are complete
5. - **Option 1 (new script):** If ATT was set up in Step 6.5 (iOS), use the `LevelPlayInitializer.cs` from `references/ios-setup.md` Part 3 (the `IEnumerator Start()` coroutine variant) instead of the plain template.

## Files inside the skill

- `references/banner-api.md` — "Banner Ads API Reference"
- `references/best-practices.md` — "LevelPlay Ad Unit Implementation Best Practices"
- `references/dependency-resolution.md` — "LevelPlay Native Dependency Resolution"
- `references/ilrd-api.md` — "Impression Level Revenue (ILR) Integration"
- `references/initialization-api.md` — "LevelPlay SDK Initialization API"
- `references/interstitial-api.md` — "Interstitial Ads API Reference"
- `references/ios-setup.md` — "iOS-Specific Setup for LevelPlay"
- `references/migration-sdk-9.md` — "LevelPlay SDK 9.x.x Migration Guide"
- `references/privacy-settings.md` — "Privacy and Regulation Settings"
- `references/rewarded-api.md` — "Rewarded Ads API Reference"
- `references/testing-and-validation.md` — "LevelPlay Testing and Validation"
- `references/troubleshooting.md` — "LevelPlay Common Issues and Solutions"
