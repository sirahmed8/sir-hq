# DEEP PLAN & MASTER SPEC: SIR Controller
**Project**: SIR Controller (`D:/Projects/SIR Controller`)  
**Mission**: Sovereign Game Controller Mapper, Ultra-Low Latency Virtual Gamepad & PC Gaming Optimizer  
**Consolidation**: Unifies `SIR Controller (v1)` and `SIR Optimizer` (with modernized x360ce integration)  
**Anti-Cheat Invariant**: 100% clean user-space virtual XInput/ViGEm emulation; zero code injection or memory hooking  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Product Purpose
SIR Controller is a high-performance game controller emulation, input remapping, and PC gaming optimization companion built for Ahmed Alaa. It bridges non-standard gamepads, generic USB controllers, DualShock/DualSense controllers, and keyboard/mouse setups into clean, low-latency Xbox 360 / Xbox One virtual XInput controllers. By merging the system tuning capabilities of `SIR Optimizer`, it additionally configures sub-millisecond timer resolution (0.5ms), disables Nagle's TCP latency delays for online games, and automatically switches controller profiles based on the detected active game.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Controller/legacy/`)
1. **`SIR Controller (v1)`**: Virtual controller configuration tool utilizing legacy x360ce mappings, DirectInput device enumerators, and button assignment files.
2. **`SIR Optimizer`**: Windows optimization utility providing 0.5ms high-resolution timer tuning, network adapter packet coalescing disablement, and background service throttling.

### 2.2 What is Valuable to Port
- **Virtual Gamepad Emulation Layer**: Modernized integration with standard Virtual Gamepad Emulation Framework (ViGEmBus) for rock-solid virtual Xbox 360 controller creation.
- **Precision Stick Calibration Math**: Radial deadzone calculation, anti-deadzone offset, exponential sensitivity response curves, and trigger actuation points.
- **Sub-Millisecond Windows Timer Utility**: Safe Win32 `timeBeginPeriod(1)` driver maintaining strict 0.5ms system timer resolution during active gaming sessions.

### 2.3 What Must Be Discarded
- Dangerous DLL hook injections (`xinput1_3.dll` dropped into game folders) that trigger instant modern anti-cheat bans.
- Permanent registry modifications that cannot be cleanly undone.

---

## 3. Architecture & Design Identity

### 3.1 Technical Architecture
- **Core Engine**: C# / .NET 8 / Rust native background service interfacing with Windows Raw Input, DirectInput, and ViGEmBus driver.
- **Web UI & Dashboard**: Next.js 14 / Tauri desktop client with real-time 3D controller visualizer rendered in Three.js / Canvas.
- **Latency Monitoring Subsystem**: Real-time polling rate tester sampling controller input intervals at 250Hz, 500Hz, and 1000Hz (1ms).
- **Profile Dispatcher**: Windows process watcher dynamically activating tailored game profiles (e.g. GTA V, Rocket League, FIFA) on window focus.

### 3.2 Design Identity
- **Brand Aesthetic**: High-Performance Cybernetic Apex & Electric Indigo. Surgical, tactile, lightning-fast, and responsive.
- **Palette**:
  - Primary Electric Indigo: `#6366F1` (Indigo 500) / `#4F46E5` (Indigo 600)
  - Secondary Neon Amber: `#F59E0B` (Amber 500)
  - Dark Surface Base: Deep Apex Obsidian (`#06080F` / `#0D111E`)
  - Elevated Glass: Translucent Indigo Glass (`rgba(13, 17, 30, 0.75)` with `backdrop-filter: blur(14px)`)
  - High-Contrast Text: `#EEF2FF`
  - **Zero Yellow Buttons**: Enforced indigo, emerald, and slate semantic tokens.
- **Typography**: Precision gaming typography (`Inter`, `Cairo`, `JetBrains Mono` for latency milliseconds and axis floats).
- **Motion Personality**: Dynamic Island spring transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), live 60fps stick deflection meters, active-only tab labels.
- **Bespoke Emblem**: Vector SVG streamlined game controller silhouette intersected by high-frequency latency wave.

---

## 4. Dependencies, Cross-Project Links & Risks
- **Provides**: Gaming latency tuning and controller profiles to `SIR Laptop Manager`, `SIR ModPack`, and `SIR Mods for GTA V`.
- **Consumes**: Game detection events from `SIR Laptop Manager` Game Mode.
- **Risks**: Anti-cheat heuristics; Bluetooth packet drop and wireless jitter; device disconnect crashes.

---

## 5. The First 25 Prioritized Tasks

### CT-101 | Clean ViGEmBus Virtual Xbox 360 Controller Driver Bridge
- **Files**: `src/driver/vigem_bridge.cs`, `src/driver/virtual_controller.py`
- **Steps**: Initialize user-mode ViGEmBus client; create virtual Xbox 360 device; map raw button presses to XInput reports.
- **Acceptance**: Windows Device Manager recognizes virtual Xbox 360 controller with zero driver signature warnings.

### CT-102 | Interactive 3D Real-Time Controller Diagnostic Visualizer
- **Files**: `src/components/controller/ControllerVisualizer.tsx`
- **Steps**: Render interactive 3D model of controller; animate button presses, analog stick XY deflection, and analog trigger depth in real time.
- **Acceptance**: Moving physical analog stick deflects 3D stick in browser with sub-5ms rendering latency.

### CT-103 | Sub-Millisecond Windows High-Precision Timer Resolution Engine
- **Files**: `src/optimizer/timer_resolution.py`, `src/optimizer/win32_timer.c`
- **Steps**: Call `NtSetTimerResolution` / `timeBeginPeriod` setting clock resolution to 0.5ms; restore system default (15.6ms) on exit.
- **Acceptance**: Timer diagnostic utility confirms stable 0.500ms system resolution during active gaming.

### CT-104 | Dynamic Island Active-Only Tab Navigation
- **Files**: `src/components/nav/TabBar.tsx`, `src/app/globals.css`
- **Steps**: Unified navigation bar (Controller, Calibration, Optimizer, Profiles, Settings) displaying text label only on active tab.
- **Acceptance**: Inactive tabs collapse to monochrome SVG icons; active tab smoothly reveals text label.

### CT-105 | Precision Radial Deadzone & Anti-Deadzone Calibrator
- **Files**: `src/lib/stickCalibration.ts`, `src/components/controller/DeadzoneLab.tsx`
- **Steps**: Mathematical radial deadzone normalization preventing stick drift; anti-deadzone offset to overcome hardcoded game deadzones.
- **Acceptance**: Live canvas plots raw vs calibrated coordinates with customizable inner and outer circular boundaries.

### CT-106 | Exponential & S-Curve Analog Stick Sensitivity Customizer
- **Files**: `src/lib/sensitivityCurves.ts`
- **Steps**: Implement Linear, Exponential, Aggressive, and Smooth S-Curve lookup tables for analog aiming sticks.
- **Acceptance**: Switching response curve updates mathematical deflection graph live with tactile feel.

### CT-107 | Bluetooth Input Polling Rate & Jitter Diagnostic Tool
- **Files**: `src/diagnostics/polling_rate_tester.py`
- **Steps**: Sample hardware input report timestamps over 1,000 packets; calculate average polling rate (Hz) and jitter variance (ms).
- **Acceptance**: Displays live polling rate gauge (e.g. "500 Hz - 2.0ms latency ±0.1ms jitter").

### CT-108 | Automatic Active Game Process Profile Switcher
- **Files**: `src/profiles/process_watcher.py`, `src/profiles/profile_manager.py`
- **Steps**: Monitor active foreground window; automatically load associated controller profile (e.g. GTA V profile on `gta5.exe`).
- **Acceptance**: Switching to game window switches controller mapping in under 50ms with subtle desktop toast.

### CT-109 | Windows Network Latency & Nagle Algorithm Optimizer
- **Files**: `src/optimizer/network_tweaks.py`
- **Steps**: Configure `TcpAckFrequency=1` and `TCPNoDelay=1` on active gaming network adapter; provide 1-click restore backup.
- **Acceptance**: Validates registry modifications with complete rollback script tested.

### CT-110 | Rapid-Fire & Macro Safe Action Remapper
- **Files**: `src/lib/inputRemapper.ts`
- **Steps**: Allow remapping buttons, button combinations (e.g. L1+R1 -> Special), and toggleable rapid-fire triggers for single-player accessibility.
- **Acceptance**: Remapped keys dispatch correctly to virtual controller report with configurable burst frequency.

### CT-111 | Trigger Actuation Point & Hair-Trigger Mode
- **Files**: `src/lib/triggerCalibration.ts`, `src/components/controller/TriggerLab.tsx`
- **Steps**: Digital hair-trigger mode activating 100% trigger signal upon detecting 1mm of physical pull.
- **Acceptance**: Hair-trigger setting registers full trigger actuation instantly for competitive shooters.

### CT-112 | Bespoke Vector SVG Controller Brand Assets
- **Files**: `public/logo.svg`, `public/favicon.svg`
- **Steps**: Design streamlined controller silhouette intersected by latency frequency wave; render multi-size favicons and PWA icons.
- **Acceptance**: Crisp vector rendering across desktop launcher and web header.

### CT-113 | DirectInput to XInput Generic USB Gamepad Auto-Mapper
- **Files**: `src/driver/dinput_mapper.py`
- **Steps**: Enumerate legacy DirectInput controllers; provide pre-configured mapping templates for generic retro gamepads.
- **Acceptance**: Generic $5 USB gamepad maps seamlessly to virtual Xbox 360 controller with functioning D-Pad.

### CT-114 | GPU Pre-Render Queue & DWM Flip Model Optimizer
- **Files**: `src/optimizer/gpu_tweaks.py`
- **Steps**: Configure DXGI flip model and low-latency pre-rendered frame queues in Windows graphics subsystem.
- **Acceptance**: Reduces display presentation latency in borderless windowed games without tearing.

### CT-115 | Safe Disconnect & Hotplug Reconnection Engine
- **Files**: `src/driver/hotplug_manager.py`
- **Steps**: Listen for Windows `WM_DEVICECHANGE` events; handle sudden USB/Bluetooth disconnects gracefully without crashing service.
- **Acceptance**: Unplugging and replugging controller restores virtual mapping instantly without restarting app.

### CT-116 | DualSense / DualShock Haptic & Lightbar Controller
- **Files**: `src/driver/dualsense_bridge.py`
- **Steps**: Read battery percentage from Sony controllers; control RGB lightbar color and test haptic rumble actuators.
- **Acceptance**: Slider adjusts lightbar color live and triggers dual-motor rumble test.

### CT-117 | Safe Standalone Revert & Golden Snapshot Script
- **Files**: `scripts/restore_all_defaults.ps1`
- **Steps**: Standalone PowerShell script restoring all system timer, network, and registry settings to exact Windows default values.
- **Acceptance**: Running restore script returns all modified registry keys to clean original state.

### CT-118 | Multi-Controller Split-Screen Port Assignment Lab
- **Files**: `src/components/controller/PortAssignment.tsx`
- **Steps**: Assign up to 4 physical gamepads to specific virtual Xbox player slots (Player 1, 2, 3, 4) with LED ring indicator.
- **Acceptance**: Visual player slot indicator clearly displays which controller controls Player 1.

### CT-119 | Multi-Screen Responsive Verification (320px to 4K)
- **Files**: `tests/responsive_controller.test.mjs`
- **Steps**: Playwright tests verifying controller visualizer, calibration labs, and profile lists across 5 viewports.
- **Acceptance**: Zero horizontal overflow and zero button clipping across all test viewports.

### CT-120 | Background Service CPU & Memory Leak Watchdog
- **Files**: `src/diagnostics/service_watchdog.py`
- **Steps**: Background daemon monitoring SIR Controller service memory consumption; guarantees memory footprint stays <35MB.
- **Acceptance**: Service runs 24 hours continuously with memory bounded below 35MB.

### CT-121 | Offline First Desktop PWA Service Worker Engine
- **Files**: `public/sw.js`, `public/manifest.json`
- **Steps**: Cache controller calibration lab offline; enable full gamepad testing with zero internet connectivity.
- **Acceptance**: Disconnecting network allows full controller calibration and testing.

### CT-122 | Dark Obsidian & High-Contrast Cyber Theme Engine
- **Files**: `src/hooks/useControllerTheme.ts`
- **Steps**: Flawless zero-flash theme engine; cybernetic dark theme tuned for gaming battlestations.
- **Acceptance**: Theme switch triggers with zero white flash and updates all CSS variables.

### CT-123 | Automated Game Launcher Integration
- **Files**: `src/launcher/game_launcher.py`
- **Steps**: Launch games with optimized timer resolution, controller profile, and process priorities in a single 1-click command.
- **Acceptance**: Tapping "Play GTA V" sets 0.5ms timer, activates profile, and launches game executable.

### CT-124 | Silent Windows Logon Scheduled Task Installer
- **Files**: `scripts/install-autostart.ps1`, `scripts/dev-start.vbs`
- **Steps**: Register `SIR_Controller_Daemon` scheduled task running windowless via `pythonw.exe` on user login.
- **Acceptance**: Daemon starts silently on boot with zero console windows.

### CT-125 | End-to-End Automated Controller Verification Suite
- **Files**: `scripts/verify.ps1`, `tests/test_controller_integrity.py`
- **Steps**: Run linter, typecheck, virtual driver checks, timer resolution tests, and verify gates.
- **Acceptance**: `verify.ps1` runs in under 3 seconds with 100% green gates.
