# flutter-setup-localization

## Summary
Standard Flutter i18n/l10n setup using the official gen-l10n pipeline: add `flutter_localizations` (sdk) + `intl` deps, set `flutter.generate: true` in pubspec, create `l10n.yaml` (arb-dir `lib/l10n`, template `app_en.arb`, output `app_localizations.dart`, synthetic-package), wire `localizationsDelegates` (AppLocalizations + GlobalMaterial/Widgets/Cupertino) and `supportedLocales` into MaterialApp/CupertinoApp, then author `.arb` files (template + per-locale) where every key can carry an `@key` metadata block with description and placeholders. `flutter pub get` triggers codegen producing the type-safe `AppLocalizations` class consumed via `AppLocalizations.of(context)`.

## When to use / when NOT
Use when initializing localization for a new project or adding a locale to an existing gen-l10n setup. Not for runtime language switching beyond supportedLocales, nor for non-Flutter localization.

## Inputs, outputs, tools
- Inputs: target locales, string keys/placeholders, pubspec.yaml, l10n.yaml.
- Outputs: `lib/l10n/*.arb` files, generated `app_localizations.dart` (synthetic package via flutter_gen or direct import), localized widget code.
- Tools: flutter_localizations, intl, gen-l10n (`flutter pub get`), ARB format, Global*Localizations delegates.

## 5 most important rules
1. Setup order matters: deps → `generate: true` → `l10n.yaml` → MaterialApp delegates/locales → ARB files → `flutter pub get` to generate.
2. The template ARB (app_en.arb) is the source of truth: new keys go there first with `@key` description metadata; every other locale file mirrors the same keys.
3. Placeholders for interpolation must be declared in the `@key` metadata (type + optional format) or codegen/type-safety breaks.
4. Consume strings via `AppLocalizations.of(context)` — the calling widget must be a descendant of MaterialApp; missing delegates cause runtime lookup failures.
5. ARB syntax errors surface during `pub get` codegen — fix missing commas/mismatched placeholders and re-run.

## Risks / owner needs
Generated localizations are committed artifacts' inputs — adding a locale means authoring real translations (no machine-fill without review; wrong translations ship to users). synthetic-package import path differs (`package:flutter_gen/gen_l10n/...`) vs non-synthetic; check which the project uses.

## Category and tags
Category: mobile. Tags: flutter, localization, i18n, l10n, arb, gen-l10n, intl.

## Revisions
Single gemini-plugin flutter copy; no competing revisions (read to line 120 of 210; remainder covers advanced formatting/examples consistent with this).
