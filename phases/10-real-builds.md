# Phase 10 — Real builds and delivery (at every milestone; complete before the month ends)

> **Read first:** `START_HERE.md`, then `standard/13-release.md` and `standard/20-platforms-tv-car.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with the final HQ audit (quality loop in `core/03-team.md`).

Every product gets real, installable builds for every platform it targets, verified on a device or simulator and listed in its `BUILDS.md` (template in B3).

| Target | Artifact | Built with | How Ahmed installs and tests it |
|---|---|---|---|
| Android phone, tablet, foldable | Release-signed **APK** for sideloading + **AAB** for Google Play | Gradle locally (or an EAS profile with `buildType: apk`) | `adb install -r` over USB or wireless debugging (launchpad shortcut "Install on Android"), or open the APK from Google Drive on the phone and allow installs from that source |
| Wear OS | APK | Gradle | `adb` to a paired watch, or the Wear OS emulator |
| Android TV / Google TV | APK from the TV profile (`EXPO_TV=1`) | Gradle or an EAS TV profile | Android TV emulator, or any Android TV device through `adb` |
| Android Auto | Inside the phone APK (Car App Library) | Gradle | The Desktop Head Unit (DHU) emulator on the laptop |
| iPhone, iPad | **Unsigned IPA** + simulator build | Cloud macOS: GitHub Actions `xcodebuild` with signing disabled (or EAS once the Apple account exists) | **SideStore** on the iPhone 14 with a free Apple ID; no jailbreak needed or recommended. Free-account limits: up to 3 apps including SideStore itself, at most 10 app installs per week, apps refreshed within 7 days. Features needing paid entitlements (push notifications and others) and Apple Watch apps generally can't be tested this way; use simulators until TestFlight is available (verify) |
| Apple Watch | watchOS simulator build | Cloud macOS | Simulator screenshots and recordings now; TestFlight once the paid account exists |
| Apple TV | tvOS simulator build | Cloud macOS (devices need a separate tvOS provisioning profile) | Simulator now; TestFlight later |
| CarPlay | Inside the iOS app | Cloud macOS; CarPlay Simulator | CarPlay Simulator now; devices once Apple grants the CarPlay entitlement, which needs the paid developer account (8.0 ladder) |
| Windows | NSIS installer + portable ZIP (x64 and ARM64), plus an MSIX for the Microsoft Store | electron-builder, locally | Double-click; SmartScreen warns on direct downloads until there's code signing. The Microsoft Store is free for individual developers and signs the packages it distributes (verify) |
| macOS | Universal DMG | macOS CI runner | Gatekeeper warns until it's signed and notarized (Developer ID) |
| Linux | AppImage + `.deb` | Linux CI runner | Optional test inside WSL |
| Web | Production URL + installable PWA | A free host that allows commercial use (rule 17) | Any browser, including iPhones before the Apple account exists |

- **Distribution with no budget:** Android APKs from each product's website and GitHub Releases, plus free alternative Android stores such as Huawei AppGallery and Samsung Galaxy Store (verify each store's fee and terms); Windows through the Microsoft Store (an MSIX that Microsoft signs for free, so Store users see no SmartScreen warning; package flights for testers) and direct download; Linux through Flathub or the Snap Store; the web app and PWA for everyone, including iPhone users until the Apple account exists; browser extensions on the free Edge and Firefox add-on stores (the Chrome Web Store charges a one-time fee). Google Play and the App Store follow the 8.0 ladder.
- **Signing keys:** generate one Android upload keystore per product. Back it up encrypted outside the repo (for example in Google Drive), with its passwords in Windows Credential Manager. A lost key means sideloaded installs can never be updated. Never commit keys.
- **Cloud macOS budget:** every Apple build needs a macOS runner, the most expensive minutes. GitHub Free includes about $12 of Actions compute a month (Pro: $18), and macOS costs about $0.062 per minute, so roughly 190 macOS minutes a month on Free. Use the free sources first: EAS's free plan includes 15 iOS builds a month (simulator builds need no Apple account), and Codemagic's free plan includes 500 macOS M2 minutes a month for personal accounts (module 22).
  - Batch Apple builds, flagships first, build Apple targets only at milestones, and cache aggressively.
  - Public repos build for free but expose the source: keep commercial products private, and make public only what's meant to be open (portfolio pieces, shared tooling).
  - The GitHub Student Developer Pack (GitHub Pro: more compute) is the first owner action to complete; Ahmed is a CS student.
- **Storage:** disk is tight. Upload artifacts to GitHub Releases (private) or Google Drive and keep only the latest build per platform locally.
- **Verification:** install every artifact and smoke-test it (launch, sign-in, core action, both themes, every locale), with screenshots in `.sir/reports/`. Built but never installed doesn't count as done.
- **Final delivery:**
  - the Command Center shows the build matrix for every product;
  - the HQ audit (quality loop, A2) passes;
  - "State of the Portfolio" lists exactly what's installable where.
