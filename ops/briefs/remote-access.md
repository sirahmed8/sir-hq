# BRIEF: Secure Remote Access from Phone (Tailscale Private Mesh)
**Author:** SIR Control Room  
**Date:** 2026-11-09  
**Status:** Implemented & Operational  
**Audience:** All SIR Project Agents (HQ, SIR Jobs, SIR Study, SIR Laptop Manager)

---

## 1. Objective
Ahmed wants to securely open his local developer and operations dashboards directly from his iPhone when away from his laptop, with stable, persistent URLs and zero exposure to the public internet.

Target Services:
1. **SIR Jobs Review Dashboard:** `:3456`
2. **SIR Study Cram Guides & Countdown:** `:3300`
3. **SIR Laptop Manager Ops UI:** `:8765`
4. **SIR Control Room Dashboard:** `:8899`

---

## 2. Security Architecture: Zero-Trust Tailnet
- **No Open Ports to Public Internet:** No NAT router port forwarding, no DDNS, no exposed raw IPs.
- **Mutual WireGuard Authentication:** End-to-end encryption authenticated through Ahmed's personal Tailscale tailnet (`a7medorabe7@gmail.com`).
- **Loopback Isolation Maintained:** All local servers remain bound strictly to `127.0.0.1`.
- **Automatic Trusted TLS/HTTPS:** `tailscale serve` terminates TLS using valid Let's Encrypt certificates provisioned automatically for MagicDNS domain `ahmed.tail9e9aa7.ts.net`.
- **The Sovereign Privacy Wall:** **AHome and Habiba personal data NEVER touch this bridge.** AHome retains its dedicated encrypted pairing and private architecture.

---

## 3. Persistent Stable Endpoint Map
| Service | Local Loopback Target | Tailscale Secure Phone URL | Purpose |
|---|---|---|---|
| **SIR Jobs** | `http://127.0.0.1:3456` | `https://ahmed.tail9e9aa7.ts.net:3456/` | Review and stage remote jobs, inspect proposals, check match metrics |
| **SIR Study** | `http://127.0.0.1:3300` | `https://ahmed.tail9e9aa7.ts.net:3300/` | Interactive exam countdown, 25-Q SAD quiz, flashcards, Anki review |
| **SIR Laptop Manager** | `http://127.0.0.1:8765` | `https://ahmed.tail9e9aa7.ts.net:8765/` | Battery & thermal gauges, process monitor, Windhawk mods, care tools |
| **SIR Control Room** | `http://127.0.0.1:8899` | `https://ahmed.tail9e9aa7.ts.net:8899/` | Global portfolio health across 16 projects, task trees, live agent queues |

---

## 4. How Project Chats Must Coordinate
1. When starting a local service in dev mode, keep it bound to `127.0.0.1` on its assigned port (`3456`, `3300`, `8765`, `8899`).
2. Do not change local port assignments.
3. Tailscale's background serve proxy intercepts inbound tailnet requests and forwards them directly to the local port.
4. If a server is restarted or crashes, Tailscale serve retains its proxy mapping; as soon as the port listens again, remote requests resume seamlessly without reconnection steps.
