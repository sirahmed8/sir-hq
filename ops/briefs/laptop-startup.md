Use your skills and tools as you see fit: plan first, use teamwork/sub-agents for independent parts, keep going until the done-when checks pass.

Task: Implement SIR Laptop Manager T-014 (Startup Registry & Scheduled Tasks Inspector).
Read: D:/Projects/SIR Laptop Manager/.sir/TASKS.md, PLAN.md, and ARCHITECTURE.md.
Work in D:/Projects/SIR Laptop Manager:
1. Implement `src/sir_laptop_manager/startup/`: inspect Windows Run registry keys (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, `HKLM\...`) and user scheduled tasks read-only.
2. Score real startup impact based on binary location, publisher, and known services without making any destructive modifications or deletions.
3. Write automated tests in `tests/test_startup_inspector.py` mocking registry and scheduled task queries; verify clean execution with `uv run pytest`.
4. Run `pwsh scripts/verify.ps1` and ensure 100% green (format, lint, strict mypy, pytest).
Done when: verify passes with 0 errors, full report written.
