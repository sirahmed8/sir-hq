Round r65 AHome (owner order 2026-11-12, free tools, cwd D:/Projects/AHome; source only under apps/ and tests, never open or send private content). Run after the r57 and r62 rounds of AHome are finished. Read AHome/.sir/CHECKPOINT.md first and follow the rescan rule.

A) When the current AHome round list is done: build the Android APK (release, signed with the project's local keystore, version stays 1.0.0) and install it on the Android phone connected to this computer through ADB (`adb devices` shows one device; use `adb install -r`), launch it and take a screenshot with adb to prove it runs. Never uninstall user data.

B) The phone powers off by itself every now and then: find out why. Check `adb shell dumpsys battery` and thermal, `adb logcat -b events` for shutdown reasons, `adb shell getprop sys.boot.reason`, any scheduled task or script on the PC that runs adb (grep scripts and the Windows Task Scheduler for adb, reboot, shutdown, svc power), and any agent that calls it. Write the finding to ops/reports/phone-poweroff-report.md with the cause or the best evidence, and fix it if it is ours.

C) Update system for later versions (design now, build step by step; the version number stays 1.0.0 until the owner says release). When a new version (1.0.1, 1.1 and so on) is published: 1) the Telegram bot sends the APK file with the changelog to the right person (the bot knows whether it is talking to Ahmed or Habiba from the chat id); 2) in the app a notification and a card in the app's own Dynamic Island component say "Update now" or "Later"; "Update now" opens the downloaded file so the Android package installer appears (REQUEST_INSTALL_PACKAGES, FileProvider), and if the app is closed, tapping the notification opens the Telegram bot chat that already received the APK; 3) small UI and bug fixes ship live without a new APK (remote-loaded web assets or remote config with a version check and safe rollback); 4) the changelog is generated from commits. Test the notification path with a fake higher version number on the test build only.

Evidence for every step (command output, adb screenshots), update .sir/CHECKPOINT.md after each step, commit and push to main.

## Log
