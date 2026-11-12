# pulse-engineering

Tools: claude, codex, cursor, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\pulse-engineering\SKILL.md (35 lines, read in full)

## Summary
The engineering standard for Ahmed's PulseTools ecosystem: PowerSync (Win32 thermal/power profile sync for Lenovo Legion/LOQ/Yoga), SysPulse Optimizer (portable zero-install Windows tuning), and PulseTools Web (Next.js 16 showcase with downloads + Firebase). Fixes rules: version locked at 1.0.0, <3ms native P/Invoke scheme switching, anti-flicker protocols, and a specific glassmorphism web aesthetic.

## When to use / not use
Use only for PulseTools-family projects (PowerSync, SysPulse, PulseTools Web). Not a general Windows or Next.js standard — applying its aesthetic rules (rounded-3xl glassmorphism) to other products would violate their own design systems.

## Inputs, outputs, dependencies
Input: work on a PulseTools component. Output: code conforming to the listed performance/design rules. Needs: Win32/P/Invoke for desktop tools, Next.js 16 for web, Firebase integration module.

## Key rules
1. Version discipline: everything stays v1.0.0 (Production Candidate / Developer Preview) until full enterprise release — no v2/v3 bumps.
2. Native performance: direct P/Invoke (powrprof/kernel32/user32) over child processes; thermal/scheme switches <3ms with zero UI blocking; offload disk writes/logging to ThreadPool.QueueUserWorkItem; bake .ico into .exe via /win32icon.
3. Anti-flicker: sync display brightness before power-scheme switches; atomic debounce on WMI duplicate events; throttle to 60Hz on battery Quiet Mode.
4. Web: glassmorphism dark aesthetic, rounded-3xl cards / rounded-2xl buttons, active:scale-[0.98] tactile press, spring transitions <200ms.
5. Zero fake data: staged real downloads in public/downloads/, modular Firebase in src/lib/firebase.ts.

## Risks / owner items
- Hardcoded to specific laptop lines (Legion/LOQ/Yoga) and Ahmed's aesthetic taste — not portable.
- "<3ms" and "zero UI blocking" are claims requiring measurement; the skill states targets without verification tooling.
- Glassmorphism/rounded-heavy style may conflict with the broader SIR anti-slop design rules (purposeful radii, no clichés) — product-specific override, use only here.

## Category and tags
build, ops, mobile — windows, win32, nextjs, desktop-utility, performance, owner-specific.

## Revision note
Identical across tools; single 35-line product-family standard.
