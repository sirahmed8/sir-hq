"""Platform matrices for the readiness kit. State: required | optional | skip. Every optional/skip carries the reason (module 20: skip only
when impossible or forbidden; the project chat records an ADR when it changes a state)."""

R, O, S = "required", "optional", "skip"

PLATFORM_NAMES = [
    ("web", "Web (Cloudflare)"),
    ("pwa", "PWA (installable, offline)"),
    ("windows", "Windows"),
    ("macos", "macOS"),
    ("linux", "Linux"),
    ("android", "Android phone and tablet"),
    ("ios", "iPhone"),
    ("ipados", "iPad"),
    ("wearos", "Wear OS"),
    ("watchos", "watchOS"),
    ("android_tv", "Android TV / Google TV"),
    ("tvos", "Apple TV"),
    ("android_auto", "Android Auto"),
    ("carplay", "CarPlay"),
    ("widgets", "Widgets and Live Activities"),
    ("browser_ext", "Browser extension"),
    ("docker", "Docker / self-host"),
]

BUILD_TOOL = {
    "web": "Next.js or Vite on Cloudflare Pages/Workers; test with Playwright and Lighthouse",
    "pwa": "Service worker + manifest; offline tests in Playwright",
    "windows": "Electron (electron-builder, NSIS + MSIX) or Tauri; installer tested on Windows 11",
    "macos": "Same Electron app on a macOS CI runner (unsigned DMG until an Apple account exists)",
    "linux": "electron-builder AppImage + .deb on a Linux CI runner; .desktop entry",
    "android": "Expo/React Native (EAS or local Gradle); APK/AAB tested on emulator API 36 and Ahmed's phone",
    "ios": "Expo on a cloud macOS runner; unsigned .ipa for SideStore until a paid account exists",
    "ipados": "Same Expo app with iPad layouts; simulator tests",
    "wearos": "Jetpack Compose for Wear OS target sharing the backend",
    "watchos": "SwiftUI watch target through an Expo config plugin",
    "android_tv": "react-native-tvos build (EXPO_TV=1) with D-pad focus; TV emulator API 31+",
    "tvos": "Same TV fork; tvOS simulator on cloud macOS",
    "android_auto": "Car App Library, allowed categories only; Desktop Head Unit",
    "carplay": "CarPlay templates; needs Apple's entitlement (paid account)",
    "widgets": "Android Glance + iOS WidgetKit/Live Activities through config plugins",
    "browser_ext": "Manifest V3, least privilege; Edge and Firefox stores first",
    "docker": "Dockerfile + compose; image scanned and pinned by digest",
}


def matrix(**over):
    """Start from 'skip' for everything, then apply {platform: (state, reason)}."""
    m = {k: (S, "no real use case for this product") for k, _ in PLATFORM_NAMES}
    for k, v in over.items():
        m[k] = v
    return m


WEB_SAAS = matrix(
    web=(R, "main product surface"),
    pwa=(R, "installable and offline for patchy connections"),
    windows=(
        O,
        "installable PWA first; Electron wrapper only if a desktop-only feature appears",
    ),
    macos=(O, "PWA covers it"),
    linux=(O, "PWA covers it"),
    android=(R, "most users are on Android"),
    ios=(R, "same Expo app"),
    ipados=(R, "same Expo app, tablet layouts"),
    wearos=(O, "glanceable reminders only if the plan needs it (ADR)"),
    watchos=(O, "same, ADR"),
    android_tv=(O, "only with a real big-screen use (ADR)"),
    tvos=(O, "same"),
    android_auto=(S, "no allowed car category fits"),
    carplay=(S, "no allowed car category fits"),
    widgets=(R, "home-screen and lock-screen glance of the next thing that matters"),
    browser_ext=(S, "no browser use case"),
)

POS_DESKTOP = matrix(
    web=(R, "owner portal, reports, subscription"),
    pwa=(O, "owner portal on a phone"),
    windows=(R, "the cashier runs on Windows, offline first"),
    macos=(O, "shops on Mac are rare; same Electron app"),
    linux=(O, "AppImage from the same Electron app"),
    android=(R, "tablet cashier and owner phone app (later wave)"),
    ios=(O, "owner phone app"),
    ipados=(O, "tablet cashier"),
    android_tv=(R, "customer-facing order/queue display (module 20)"),
    tvos=(O, "same display on Apple TV"),
    widgets=(O, "today's sales glance for the owner"),
    docker=(O, "branch server for multi-till shops"),
)

DESKTOP_ENGINE = matrix(
    web=(R, "landing, docs, account, dashboard"),
    windows=(R, "main target: local engine and GPU"),
    macos=(R, "same Electron shell; engine ports checked by ADR"),
    linux=(R, "AppImage and .deb"),
    android=(O, "companion for remote control and review (ADR)"),
    ios=(O, "companion (ADR)"),
    widgets=(O, "render progress"),
    docker=(O, "headless engine for the cloud render queue"),
)

WINDOWS_TOOL = matrix(
    web=(R, "product site, account, profile sync"),
    windows=(R, "the product: drivers, mapping, optimization"),
    macos=(S, "game-controller drivers and Windows tuning are Windows-only"),
    linux=(O, "controller mapping may port; optimizer will not"),
    android=(O, "phone remote and profile viewer"),
    widgets=(S, "no use"),
)

INTERNAL_OPS = matrix(
    windows=(R, "Ahmed's PC"),
    web=(O, "local dashboard on 127.0.0.1 only"),
    android=(O, "phone status through Remote Control"),
)

PRIVATE_LOCAL = matrix(
    windows=(R, "runs on Ahmed's PC"),
    web=(O, "local UI served on 127.0.0.1, never public"),
    pwa=(O, "phones reach it through the private tunnel"),
    android=(O, "PWA or bridge bot"),
    ios=(O, "PWA or bridge bot"),
    widgets=(O, "glance of today's items"),
)

STATIC_SITE = matrix(
    web=(R, "the product"),
    pwa=(O, "only if offline browsing matters"),
)

GAME_MOD = matrix(
    web=(R, "hub, downloads, accounts"),
    windows=(R, "the games run on Windows PC"),
    linux=(O, "Minecraft launcher only; GTA V is Windows-only"),
    macos=(O, "Minecraft launcher only"),
    android=(O, "companion: server status, news (ADR)"),
)

SELF_HOST = matrix(
    web=(R, "the workspace UI"),
    pwa=(R, "installable client"),
    windows=(R, "Electron packaging"),
    macos=(O, "Electron packaging"),
    linux=(R, "AppImage, .deb and Docker"),
    docker=(R, "main self-host path"),
    android=(O, "PWA first"),
)

LIFE_APP = matrix(
    web=(R, "web companion and PWA"),
    pwa=(R, "offline first"),
    android=(R, "main device"),
    ios=(R, "same Expo app"),
    ipados=(R, "tablet layouts"),
    wearos=(R, "prayer, water and medication reminders on the wrist"),
    watchos=(R, "same"),
    widgets=(R, "next prayer, water, medication"),
    android_tv=(O, "adhkar and Quran wird on a big screen (ADR)"),
    android_auto=(O, "audio adhkar category only (ADR)"),
    carplay=(O, "audio category, needs entitlement (ADR)"),
    windows=(O, "PWA"),
    macos=(O, "PWA"),
    linux=(O, "PWA"),
)

PLATFORM_KIT = matrix(web=(R, "docs site for the kit"), docker=(O, "CI image"))
