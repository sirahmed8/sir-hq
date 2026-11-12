# PLAN NOTE: Accessibility Map (idea 26) — Module of SIR Life Part B
**SUPERSEDED on 2026-11-12 (round r53c).** The owner decided that every unplanned idea is its own small project, so the accessibility map is now its own product, SIR Access Map, and it is built last. The plan that matters is `D:/Projects/_SIR/plans/sir-access-map.md`; the decision and the reason are in `D:/Projects/_SIR/plans/BACKLOG_IDEAS_DECISIONS.md`. The text below is kept for the record only and must not be used as a plan. The reason the owner changed it: one folder, one repository, one Firebase project and one Desktop kit per product, and the map is a crowd-moderated place-claim product rather than a personal routine feature.

Created 2026-11-12 (r51-backlog-projects). Idea 26 from the owner's "أفكار برامج ومشاريع" note.

## Decision
**Not a separate product. Module inside SIR Life Part B.**

Reasons:
1. The accessibility map is a community life tool — it helps people navigate their daily life better, the same as SIR Life's mission (prayer times, habits, reminders).
2. The addressable market in Egypt is small relative to the cost of a dedicated product (own Firebase project, domain, store listing). The overhead is too high for the current portfolio size.
3. No obvious standalone commercial model: accessibility maps are typically non-profit or government-funded. Inside SIR Life Part B it is a free public-good feature that improves the product's value to users with disabilities and their families without requiring its own revenue.
4. The map data layer (Google Maps SDK or Mapbox free tier) is shared with other SIR Life location features (prayer direction, nearest mosque).

## Module scope (inside SIR Life Part B, M3+)
- Community-sourced POI map of accessible locations in Egypt: ramps, elevators, accessible bathrooms, parking, wide aisles.
- Submission flow: any registered SIR Life user submits a location with photos; the submission queue is moderated (AI + manual).
- Data model: `AccessibilityPOI` (location, type, features[], photos[], rating, verification_state, submitted_by_uid).
- Tags: wheelchair ramp, elevator, accessible bathroom, wide aisle, hearing loop, visual guide, Braille menu, prayer room, parking.
- Integration with SIR Life Part B's map view (same screen that shows prayer mosques nearby).
- PDPL compliance: submitter's UID is stored but never shown publicly; only the location and features are public.

## Owner action
None required at the planning stage. The module is added to SIR Life Part B's `.sir/TASKS.md` when Part B work starts.

## Note in SIR Life plan
Add this entry to `sir-life.md` section 6 (Screens and entities) under a future heading "Part B M3+ modules: Accessibility Map."
