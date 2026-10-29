# 02 — Architecture and repo layout

**Default stack** (verify current stable versions; deviate only through an ADR):

| Layer | Default |
|---|---|
| Monorepo | pnpm workspaces + Turborepo |
| Web | Next.js (App Router), React, Tailwind with design tokens, Motion |
| Mobile | Expo (latest SDK), Expo Router, React Native New Architecture, `@expo/ui` (native SwiftUI and Jetpack Compose components), Reanimated, Gesture Handler, FlashList, expo-image |
| Desktop | Electron + electron-builder, renderer built from the shared web UI as a static SPA |
| Watch | Kotlin + Compose for Wear OS; SwiftUI watchOS target added to the Expo project through an Apple-targets config plugin |
| Backend | The zero-cost stack from module 22: Firebase on the free plan (Auth, Firestore, FCM, Remote Config, App Check, Crashlytics, Analytics); Cloudflare for web hosting, server code (Workers calling Firebase through its REST APIs), relational data (D1), files (R2), cache (KV), live state (Durable Objects) and jobs (Queues); Cloudinary for media. Cloud Functions only once earnings fund Firebase's paid plan (ADR). Prove the stack on the golden-path product first (`D:\Projects\_SIR\phases\04-platform.md`) |
| Validation | Zod schemas shared by client and server |
| Testing | Vitest, Testing Library, Playwright (web and Electron), Maestro (mobile), Firebase emulator suite |

**Product repo layout:**

```
<Product>/
  AGENTS.md  CLAUDE.md  GEMINI.md  README.md  CHANGELOG.md  SECURITY.md
  .sir/            project.yml, CHECKPOINT.md, BOARD.md, inbox/, reports/, decisions/, status.json
  .agents/rules/   .agents/skills/   .claude/   .github/
  apps/web  apps/desktop  apps/mobile (targets/ holds the watchOS app and widgets)  apps/wear
  packages/core     domain types, schemas, rules (pure)
  packages/data     typed Firestore/API access, converters, caching
  packages/features shared feature logic (hooks/services) used by web, desktop and mobile
  services/functions  backend, AI gateway, webhooks, scheduled jobs
  assets/brand     icon.svg, icon-foreground.svg, icon-monochrome.svg, palette.json, generated icons
  docs/            PRODUCT.md, ARCHITECTURE.md, CODEMAP.md, legal/, store/, sir/standard/
  tools/launcher   start-dev, build-installers, open-* scripts
  firebase.json  firestore.rules  firestore.indexes.json  storage.rules
```

**Shared `@sir/*` packages** (in `sir-platform`, published privately with SemVer):

- `@sir/config`: tsconfig, eslint, prettier, commitlint
- `@sir/tokens`: design tokens → CSS variables, React Native theme, Compose and SwiftUI exports
- `@sir/ui-web`, `@sir/ui-native`: components following the design system
- `@sir/i18n`: all project locales (default `ar`, `en`, `zh-Hans`, `hi`), RTL, ICU plurals, formatting, locale fonts
- `@sir/auth`, `@sir/firebase`: typed clients, auth flows, App Check
- `@sir/legal`: consent gate, document viewer, consent records
- `@sir/settings`: the shared Profile and Settings screens
- `@sir/ai`: client for the AI gateway
- `@sir/analytics`: consent-aware analytics, crash reporting
- `@sir/notifications`, `@sir/payments` (RevenueCat for in-app subscriptions; local gateways for physical goods and services), `@sir/testing`

**Rules:**

- Dependency direction is enforced (eslint boundaries or dependency-cruiser): apps → features → data → core. Apps never import each other.
- Share domain logic, schemas, tokens and API clients everywhere. Share UI between web and desktop. Mobile gets native-feeling UI built on the same logic, **never a WebView wrapper** (app stores reject thin web wrappers, and it feels cheap).
- Each product's personality comes from tokens, copy, illustrations and layout choices, not from forking shared components.
- **Provider adapters:** every outside service (auth, database, files, media, email, push, analytics, payments, AI) is reached through a small interface in `@sir/*`, so a provider can be replaced by configuration when a free tier changes or a better one appears (module 22). Product code never imports a provider SDK outside its adapter.
