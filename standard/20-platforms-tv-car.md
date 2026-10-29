# 20 — TV and car apps, widgets, XR, Linux and extensions (core platforms)

- **Principle:** these platforms are core, not extras. Every product gets the widest legitimate coverage from the same codebase and shared logic. Skip a platform only when it's technically impossible or forbidden by platform policy, and write the reason in an ADR.
- **TV (Android TV / Google TV and Apple TV):**
  - Every product gets a TV app built around a real TV use: lean-back content, or for business products a big-screen dashboard or customer-facing display (order status, promotions, queue numbers).
  - Built from the same Expo app with the TV fork of React Native (`react-native-tvos`, version matched to the Expo SDK) and the `@react-native-tvos/config-tv` plugin. Set `EXPO_TV=1` before `npx expo prebuild --clean`; use separate EAS profiles (for example `preview_tv`) with `EXPO_TV=1` in `env`. Not every Expo module works on TV; check Expo's TV guide.
  - Design for 10-foot viewing: big type, high contrast, D-pad and remote focus navigation with an obvious focus state, as little text entry as possible, lean-back content (video, audio, browsing).
  - Android TV needs the TV launcher intent and a TV banner. Apple TV needs top-shelf imagery, and a separate tvOS provisioning profile for devices (EAS doesn't create it).
  - Test on the Android TV emulator (API 31+ image) and the tvOS simulator (cloud macOS).
- **Cars:**
  - **Android Auto / Android Automotive OS** through the Car App Library, only in its categories: media (audio), messaging, calling, navigation, points of interest (parking, charging, fuel), IoT, weather. Test with the Desktop Head Unit.
  - **CarPlay** categories: audio, video (while parked only), messaging and VoIP (through SiriKit), navigation, EV charging, fueling, parking, public safety, quick food ordering, voice-based conversational apps, driving-task apps. Request the CarPlay entitlement from Apple once the paid developer account exists (the reinvestment ladder in `D:\Projects\_SIR\phases\08-business.md`, 8.0), and use the CarPlay templates from Apple's guidelines.
  - Small iOS widgets and Live Activities appear in CarPlay automatically. Mark any that aren't suitable while driving as not optimized for CarPlay.
  - Driver safety first: voice-first, glanceable, nothing distracting.
- **Widgets and Live Activities:** iOS widgets (home screen, lock screen, StandBy); Live Activities and the Dynamic Island for ongoing events (bookings, deliveries, prayer countdowns, workouts); Android home-screen widgets (Jetpack Glance). Add them as native targets through config plugins, sharing data through app groups (iOS) and the same backend.
- **XR:** iPad apps can run on Apple Vision Pro, and large-screen Android apps on Android XR, in compatibility mode. Keep that availability on unless something breaks, and make sure layouts handle free-form windows.
- **Linux:** AppImage and `.deb` from the same Electron app (electron-builder on a Linux CI runner), with a proper `.desktop` entry and icons.
- **Chromebooks:** the Android app (keyboard, mouse and resizable windows supported) plus the PWA.
- **Browser extensions** (Manifest V3) where they add real value, for example SIR Deals price checks. Use the installed Chrome-extension builder skills, least-privilege permissions, and the store policies. Publish on the free Edge and Firefox add-on stores first; the Chrome Web Store charges a one-time registration fee (reinvestment ladder).
- **Later, when a product calls for it:** smart-TV web platforms (Samsung Tizen, LG webOS), Fire TV (the Android TV build), messaging bots (WhatsApp, Telegram) through official APIs.
