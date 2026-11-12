# Phone power-off investigation (r65, 2026-11-13)

Device: `ronf6d5hrkqsuoaa` — Redmi rubypro (Redmi Note 12 Pro 5G, 22101316UG), Android 14, MIUI/HyperOS `OS2.0.16.0.UMOMIXM`, kernel 4.19.191 MTK mt6877.

## Verdict

The phone does NOT die by itself from battery or heat. Both recorded shutdowns are clean, software-requested power-offs (`shutdown,userrequested`). Nothing on the PC or in any agent calls adb power commands. The most likely causes are on the phone itself: MIUI "Scheduled power on/off" (定时开关机, handled by `com.miui.powerkeeper`) or the very-long-press power button (`power_button_very_long_press=1`), including accidental pocket presses. Not ours to fix; owner check steps at the end.

## Evidence

### Boot/shutdown history (persistent props)

```
$ adb shell getprop persist.sys.boot.reason.history
shutdown,userrequested,1794509497
shutdown,userrequested,1794220933
```

Two recorded shutdowns, 288,564 s (~3 days 8 h) apart. Both `shutdown,userrequested` = `PowerManager.shutdown()` path (power menu, scheduled power off, or `svc power shutdown`). Current boot reason: `sys.boot.reason = shutdown,userrequested`, `sys.boot.reason.last = shutdown,userrequested`, `ro.boot.bootreason = reboot` (bootloader view), `persist.vendor.aeev.last.boot.reason = shutdown,userrequested`.

### Battery — ruled out

```
$ adb shell dumpsys battery
  status: 5 (Full), health: 2 (Good), level: 100, voltage: 4384, temperature: 265 (26.5 C), USB powered: true
```

Battery full and charging, gauge healthy, cell temp normal.

### Thermal — ruled out

```
$ adb shell dumpsys thermalservice
Thermal Status: 0   (no throttling/shutdown)
CPU/GPU/NPU ~28-54 C, SKIN 34.9 C, BATTERY 26.5 C — all normal
```

In the pre-shutdown kernel log `thermal_level = 0` on every sample.

### Kernel log of the last shutdown (dropbox SYSTEM_LAST_KMSG)

`adb shell dumpsys dropbox --print` holds the previous boot's kernel ring. Its last ~20 s show:

- Normal battery/charger/thermal traffic, battery 100 %, `thermal_level = 0`.
- `mt6358-pmic ... Reg[0x91c]=0x1,name=pwrkey` — a power-key (pwrkey) PMIC interrupt ~2.5 s before shutdown.
- Then `device_shutdown` → `__arm64_sys_reboot` → `reboot: Restarting system`, `battery_shutdown!!`, orderly driver shutdowns. This is the standard Android shutdown path; on this device `machine_power_off` is not implemented so the kernel falls back to `kernel_restart`, which is why kmsg says "Restarting system" while Android records `shutdown,userrequested`.

Interpretation: a software power-off was requested ~2.5 s after a physical power-key press. That matches either a deliberate long-press (MIUI "very long press" action) or an accidental press in a pocket/bag.

### Scheduled power — prime suspect

`adb shell dumpsys alarm` shows recurring MIUI powerkeeper alarms:

- `*alarm*:miui.intent.action.powerkeeper_schedule` — RTC, daily ~07:00
- `*alarm*:com.miui.powerkeeper.clean_app`, `night_clean`, daily RTC_WAKEUP ~18:00

MIUI's "Scheduled power on/off" feature lives in `com.miui.powerkeeper`/`com.miui.securitycenter` and issues exactly this `shutdown,userrequested` path. Its configuration is in app-private storage (not readable without root), so presence of the daily schedule alarm plus recurring unattended shutdowns points here. The two recorded shutdowns are ~3.3 days apart at different hours, so if a schedule is set it may be irregular or the phone was off/asleep at fire time.

### PC side — ruled out

- `Get-ScheduledTask`: only `AHome-GameMode` and `AHome-Services` match; both run PowerShell build/watchdog scripts (`infra-daemons/ahome-gamemode.ps1`, `ahome-service-supervisor.ps1`) — no adb/power commands in them.
- `grep` over `infra-daemons/*.ps1|vbs|py` and `_SIR/scripts`: no `adb reboot`, `adb shell svc power`, `reboot -p`, or shutdown calls. The only "shutdown" hit is unrelated signal handling in `_SIR/scripts/serve-control-room.py`.
- No agent on this PC issues power commands to the phone.

## What to check on the phone (owner, one minute)

1. Settings → Passwords & security / Security app (手机管家) → look for "Scheduled power on/off" or "Power schedule" (定时开关机): if ON, note the times and turn it OFF.
2. Settings → Additional settings → Buttons: check "Press and hold power button" is not set to power off directly (`power_button_very_long_press` is enabled on this device).

If it still powers off after both are off, capture `adb shell getprop persist.sys.boot.reason.history` again after the next event — the timestamps will show whether it correlates with a fixed time (schedule) or random times (button).
