# Inbox: SIR Laptop Manager
Newest first. Format and rules: README.md

- [ ] 2026-11-09 from jobs-r9 (SIR Jobs):
  notice: Round 9 Cross-Review of Laptop Manager complete. Full report with line numbers and reproduction proofs written to ops/agy-runs/reports/xreview-laptop-by-jobs.md.
  findings: (1) Severe synchronous latency (12.3s on /api/shortcuts/audit via per-shortcut powershell.exe spawn; 21.5s on /api/disk/deep-report via deep recursive multi-directory walks) causing HTTP timeouts and socket disconnects ([WinError 10054]); (2) Per-request tailscale.exe subprocess spawn in _host_ok() without TTL caching; (3) Battery wear returns has_battery: False on laptops where Win32_Battery leaves DesignCapacity blank; (4) Forced reflows on high-frequency mousemove in index.html; (5) Sub-44px touch targets (36px/38px) on .btn and .tab-btn; (6) Monolithic 2,624-line index.html god-component; (7) Hardcoded dummy sparkline data; (8) Synchronous window.confirm dialogs; (9) RTL horizontal arrow navigation inversion.

- [ ] 2026-11-09 from control-r9 (Control Room):
  notice: Round 9 Cross-Review of Laptop Manager remote access complete. Full report written to ops/agy-runs/reports/xreview-laptop-by-control.md.
  findings: (1) Missing security headers on GET / (X-Frame-Options, X-Content-Type-Options: nosniff, Referrer-Policy; server leaks Python 3.14.2); (2) Dynamic telemetry (/api/health) lacks Cache-Control: no-store; (3) Direct IP TLS fails with TLSV1_ALERT_INTERNAL_ERROR (MagicDNS ahmed.tail9e9aa7.ts.net:8765 required); (4) RFC 9110 status code deviations (403 vs 401 on missing token, 404 HTML vs 405 JSON on invalid method); (5) Missing native window.ononline/onoffline event listeners in index.html; (6) RTL tab indicator calculation displacement on horizontal scroll; (7) Mousemove spotlight listener runs getBoundingClientRect on all cards without rAF throttling.

- [x] 2026-11-09 from control-r6 (Control Room):
  directive: Owner order (Round 6) - Phone access https://ahmed.tail9e9aa7.ts.net:8765/ must work without 'Host header not allowed'. REMOVE any login or owner code screen: access control is Tailscale (tailnet only, `Tailscale-User-Login: a7medorabe7@gmail.com`) plus loopback. NO EMOJI anywhere in the UI. Track progress in ops/requests/laptop.md.
  resolution: Completed and verified in laptop-r6. Host allowlist active, Tailscale-User-Login identity authorized, zero emojis in UI, 144 unit tests passing, GitHub Actions CI green (run 42548596695).

