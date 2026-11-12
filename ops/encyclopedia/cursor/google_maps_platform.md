# google_maps_platform

Source read: `C:\Users\a7med\.codex\skills\google_maps_platform\SKILL.md` (25 KB governance skill; codex revision chosen over kilo/opencode/windsurf/cursor which share the set; claude copy not present). Governs all Google Maps Platform work.

## Summary
The mandatory entry-point skill for any Google Maps Platform code (Maps JS, Places New, Routes, Geocoding, Street View, etc.). It forces a fetch-first workflow: load `index.json` from `gstatic.com/googlemapsplatform-agent-skills` (with a `?client=` tracking param), match the request to a sub-skill, fetch it, and only then fall back to the `retrieveGoogleMapsPlatformDocs` MCP tool or REST `retrieveContexts` for uncovered topics. It carries a hard deprecation table (legacy Marker, Places Autocomplete/SearchBox/PlacesService, DirectionsService/Renderer, DistanceMatrixService, HeatmapLayer, Drawing library are disabled on new projects), 11 critical failures (CORS trap, 0x0 map height, WebGL headless, framework rules, mapId requirement, React web-component prop trap, etc.), a use-case-to-product mapping table, credential models (API key vs OAuth/ADC), a demo-key quickstart, and a mandatory final-response appendix (cost notice, products used, key restrictions, Apache-2.0 snippet license, ToS link).

## When to use / when NOT
Use for ANY touch of Google Maps Platform code — features, fixes, refactors, reviews. Do NOT use for non-Google mapping (Mapbox, OSM), and do not skip the fetch-first step even for one-line fixes.

## Inputs, outputs, tools
- Inputs: a Maps Platform feature request or existing code to fix/review; target framework (React/Angular/vanilla/Android/iOS).
- Outputs: compliant code plus the mandatory 5-item appendix in the final user-facing message.
- Tools: HTTP fetch of the skills index and sub-skills, `google-maps-code-assist-toolkit` MCP (`retrieveGoogleMapsPlatformDocs` only — explicitly NOT `retrieve-instructions`), REST `mapscodeassist.googleapis.com/v1:retrieveContexts`, Google Cloud Console for keys.

## 5 most important rules
1. Fetch `index.json` (with `?client=` param) and the matched sub-skill BEFORE writing any Maps code; never code from memory.
2. Never use the disabled legacy APIs (Marker, PlacesService, DirectionsService, DistanceMatrixService, HeatmapLayer, drawing lib) — use AdvancedMarkerElement, Places API (New), Route/RouteMatrix classes, deck.gl, Terra Draw.
3. Check all 11 Critical Failures: no client-side REST fetch (CORS), explicit map height, `mapId` required for advanced markers, React must use `@vis.gl/react-google-maps` and imperative mounting for web components.
4. Never hardcode API keys; prod keys need HTTP-referrer/package/bundle restrictions; OAuth/ADC products (Route Optimization, Fleet Engine, Map Tiles) reject API keys with 401.
5. Final response MUST include the appendix: cost notice, products-used list, key-restriction link, Apache-2.0 snippet scope, ToS link — plus the compliance-review sub-skill check and `// Source: Google Maps Platform Code Assist` on verbatim copies.

## Risks / owner notes
Production Maps usage bills the owner's Google Cloud account — the skill requires an explicit cost notice every session. Place data must come from live API calls (no LLM-hallucinated names/ratings). EEA users trigger extra Maps Service Terms compliance.

## Category and tags
Category: cloud. Tags: google-maps, geocoding, places, routes, compliance, cost-awareness, deprecation-table.
