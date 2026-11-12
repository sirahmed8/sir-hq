# localization (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\localization\SKILL.md` (26 KB; unity plugin; `references/` + `resources/` exist). Unity Localization package setup.

## Summary
End-to-end Unity Localization (`com.unity.localization`) configuration: package check via `Packages/packages-lock.json` (not manifest — lock records resolved; `Client.Add` is async so poll the lock file across calls, then verify `Type.GetType("...LocalizationSettings, Unity.Localization")` returns ready); settings/locale setup (`FindAssets` MUST be folder-scoped `"Assets"` to avoid package assets, create `Assets/Localization/LocalizationSettings.asset` if missing, `AddLocale`); safe table population (match by `Locale.Identifier.Code` — `GetLocales()` order is NOT guaranteed; Asset Tables keyed by asset GUID; always `EditorUtility.SetDirty` + `RaiseCollectionModified` + `SaveAssets` after edits); UI binding (fully qualify `UnityEngine.UI.*` to avoid CS0118; destroy-then-recreate single canvas instances; runtime locale = `LocalizationSettings.SelectedLocale` — NEVER hand-roll locale state or debug dropdowns; preview locale = Localization Scene Controls window, a different mechanism; bind via public `LocalizeStringEvent` + `OnUpdateString`, NOT internal TMP/UGUI plugin classes; `LayoutRebuilder.ForceRebuildLayoutImmediate` after text changes); CJK support (no TMP fallbacks — per-locale Asset Table font swap with locale-correct fonts like msyh/msgothic/malgun, never substitute Western fonts; TMP Essential Resources must be imported non-interactively via `AssetDatabase.ImportPackage` — the menu item opens a blocking dialog; dynamic multi-atlas fonts; add EVERY atlas texture AND the material as sub-assets and verify via `LoadAllAssetsAtPath`; every Asset Table asset must be Addressable and NOT under `Resources/`; `LocalizedTmpFont` over `LocalizedAsset<TMP_FontAsset>`; rebuild Addressables after table changes; tofu-check zh-Hans/ja/ko before finishing).

## When to use / when NOT
Use for adding languages, String/Asset Tables, UI translation, or CJK font support in a Unity project. Not for non-Unity i18n or for runtime string management outside the Localization package.

## Inputs, outputs, tools
- Inputs: Unity project, target locales, source text/assets, CJK font files.
- Outputs: LocalizationSettings asset, populated tables, font assets, Addressables groups, localized UI bindings.
- Tools: `com.unity.localization` package, UnityEditor APIs (`AssetDatabase`, `Client`, `PackageManager`), TMP, Addressables, Localization Scene Controls.

## 5 most important rules
1. Verify package via `packages-lock.json` + type-load poll; `Client.Add`/`ImportPackage` are async — poll across calls, never busy-wait.
2. `FindAssets` always scoped to `"Assets"` — unscoped searches hit read-only packages.
3. Runtime locale switching ONLY via `LocalizationSettings.SelectedLocale` (+ startup `SpecificLocaleSelector`); never hand-rolled locale state; preview vs runtime are different mechanisms.
4. After table edits: `SetDirty` + `RaiseCollectionModified` + `SaveAssets` or the Editor shows stale data.
5. CJK: per-locale Asset Table fonts (no fallbacks), dynamic multi-atlas, save ALL atlas textures + material and verify on disk via `LoadAllAssetsAtPath`; nothing in `Resources/`; tofu-check all CJK locales before done.

## Risks / owner notes
Silent failure modes everywhere: wrong-locale data from unordered `GetLocales()`, unsaved materials, tofu boxes, `Resources/` addressable errors. Font files must be properly licensed for commercial use. Many steps need a live Editor or careful file polling.

## Category and tags
Category: mobile. Tags: unity, localization, i18n, cjk, tmp-fonts, addressables, string-tables.
