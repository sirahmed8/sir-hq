# Verification sweep: all projects

Owner request (2026-11-14): verify all tasks/rounds marked done are actually verified; find unverified or half-done work.
1. For each project in D:/Projects (SIR AI, SIR Jobs, SIR Study, SIR Portfolio, SIR Control Room, SIR Laptop Manager, SIR Education Hub, SIR Business, SIR Hagoozat, SIR Deals, SIR Cars, SIR Movies, SIR Handyman, SIR Access Map, SIR Price Finder, SIR Game Deals, SIR Life, SIR Controller, SIR Content Creation Studio, SIR ModPack, AHome skip-private-content): read .sir/CHECKPOINT.md "Open promises"/"Next step" and TASKS.md unchecked items.
2. Spot-check the 10 most recent commits per active project: does each have evidence (test output/screenshot) or is it claimed-only?
3. Produce a report at _SIR/ops/verifications/sweep-2026-11-14.md listing: verified-ok, claimed-but-unverified, actually-broken, next concrete step per project. Commit report to _SIR main.
