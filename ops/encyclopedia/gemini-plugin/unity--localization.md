# localization

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\localization\SKILL.md`
- SKILL.md size: 26177 chars

## What it does

Sets up and configures Unity Localization, including locales, String and Asset Tables, and CJK fonts. Use when the user asks to add languages, translate UI text, or mentions i18n or multilingual support.

## When to use (from skill text)

- the id appears. Installation also triggers a domain reload, so expect the first poll or two to
- 7. **Build Requirement:** After updating Asset Tables or Addressable groups, trigger a build: `AddressableAssetSettings.BuildPlayerContent();`.

## Structure (headings inside SKILL.md)

- 0. Package Installation Check
- 1. Localization Settings & Locales
- 2. Modifying Localization Tables
- **Safe Population Pattern**
- **Refresh & Notification**
- 3. UI Localization and Layout
- **Namespacing & Conflicts**
- **Localized String Events (Robust Binding)**
- 4. Asian Language Font Support (CJK)
- Prerequisite: TMP Essential Resources must be imported
- **Verification Step**
- 5. Automatic Layout (UGUI)
- Notes when translating an existing project
- Table completeness check (run this before declaring the work done)
- 6. Recommended Translation Strategy
- API Reference
- 7. Accelerated Localization Workflow
- **Technical Tips for Speed**
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `UnityEngine.UI` is both a namespace and a class container, so unqualified names produce `CS0118` (namespace used like a type). Full qualification avoids this entirely.
- - If a font asset is deleted and recreated, the new GUID must be manually updated in the Asset Table and re-added to Addressables.

## Key rules (verbatim lines from SKILL.md)

1. 4. **Confirm the types are actually loaded** before using them, since the lock file can be written
2. - **Always pass the search folders.** An unscoped `FindAssets` searches the whole project including
3. 3. Always call `AssetDatabase.SaveAssets()` at the end.
4. - **Always qualify names:** Use `UnityEngine.UI.Image`, `UnityEngine.UI.VerticalLayoutGroup`, `UnityEngine.UI.ScrollRect`, `UnityEngine.UI.Mask`, `UnityEngine.UI.CanvasScaler`, `UnityEngine.UI.GraphicRaycaster`, `UnityEngine.UI.ContentSizeFitter`, `UnityEngine.UI.LayoutRebuilder`, etc.
5. - `UnityEngine.UI` is both a namespace and a class container, so unqualified names produce `CS0118` (namespace used like a type). Full qualification avoids this entirely.

## Files inside the skill

- `references/api-notes.md` — "Localization API Reference"
- `resources/L10nBatchProcessor.cs`
- `resources/LocalizedFontAsset.cs`
