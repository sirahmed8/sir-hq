# 08 — Watch apps (Wear OS and watchOS)

- **Scope:** glanceable, 2–5 second interactions. Notifications plus 1–3 core actions (log water, take medication, next prayer, check in, booking reminder). Battery-aware; works offline and syncs later.
- **Wear OS:** Kotlin + Compose for Wear OS, Material 3 Expressive for Wear, Tiles and Complications, the Data Layer API to sync with the phone app, standalone where it makes sense. Target API follows Google Play's Wear OS requirement (verify; it's lower than the phone requirement). Test on round and square emulators.
- **watchOS:** a SwiftUI watch target added to the Expo project through an Apple-targets config plugin; WatchConnectivity for phone sync; complications through WidgetKit; current watchOS design language. Built in the cloud on macOS.
- **Shared logic:** the watch apps call the same backend and follow the same domain rules (`packages/core` defines the contract). Never duplicate business rules in the watch code.
