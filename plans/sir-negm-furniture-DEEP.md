# DEEP PLAN & MASTER SPEC: SIR Negm Furniture
**Project**: SIR Negm Furniture (`D:/Projects/SIR Negm Furniture`)  
**Status**: **ACTIVE PLAN PROJECT (Unfrozen per Owner Order 2026-11-09)**.  
**Rule**: **PLANS ONLY FOR NOW**. Elevated to the highest quality bar, ready for turnkey handover to Ahmed's friend. No building code, CI, or deployment until explicitly ordered by owner.  
**Target Handover**: Ahmed's Friend & Negm Furniture Brand  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: Standards 23 to 27 (`23-premium-code-bar.md` to `27-visibility.md`)

---

## 1. Executive Summary & Brand Charter
SIR Negm Furniture is a premier digital atelier and 3D WebGL room visualization suite engineered for "Negm Furniture"—a high-end bespoke furniture brand based in Egypt. Previously held in a frozen state, the owner updated instructions on 2026-11-09: **Negm Furniture is active for planning**, to be elevated to the exact same rigorous architectural and market-grade standards as all other SIR products, with a complete turn-key package prepared for handover to his friend.

### Core Product Capabilities:
1. **Interactive 3D WebGL Room Studio**: Drag-and-drop custom furniture pieces onto customizable room floor plans with real-time PBR fabric, wood, and leather material customization.
2. **WebXR Instant Mobile AR**: One-click projected AR preview allowing clients to inspect sofas and dining sets in their actual living spaces at 100% physical scale.
3. **Bespoke Manufacturing Order & Deposit Gateway**: Custom dimensions calculator with integrated 50% Paymob deposit checkout and automated production milestone tracking.
4. **Turnkey Friend Handoff Portal**: Intuitive Arabic management dashboard allowing Ahmed's friend to manage catalog items, update prices, upload swatches, and track customer inquiries without technical expertise.

---

## 2. Legacy Forensic Audit & Porting Strategy

### 2.1 Existing Legacy Assets (`SIR Negm Furniture/legacy/`)
1. **`Negm Furniture`**: WooCommerce store dump containing product catalog, dimensions, photography, fabric types, and past customer inquiries.
2. **`floor-plan-generator-nov`**: React & Three.js 2D/3D floor plan layout prototype with boundary collision detection and camera controls.

### 2.2 Reusable Architecture vs. Legacy Discard
- **Extract & Standardize**: High-poly 3D models converted to optimized `.gltf` / `.webp` Draco-compressed assets; room coordinate collision algorithms; WhatsApp order payload format.
- **Strictly Discarded**: PHP/WordPress dependencies, slow WooCommerce plugins, hardcoded phone numbers, unvalidated API keys.

---

## 3. Technology Stack & Design System

- **Frontend Core**: Next.js 15 (App Router, React 19) + Three.js / React Three Fiber / Drei.
- **Styling**: Tailwind CSS v4 + CSS Logical Properties (RTL first).
- **Backend / Persistence**: Supabase PostgreSQL + Cloudflare R2 for 3D GLTF asset hosting.
- **Commerce**: Paymob (Cards, Mobile Wallets, Meeza) + Meta WhatsApp Cloud API.
- **Design Tokens**:
  - Primary Bronze Gold: `#D97706` (Amber 600)
  - Secondary Warm Sand: `#F59E0B` (Amber 500)
  - Surface Base: Deep Charcoal Obsidian (`#0F1115` / `#16191E`)
  - Elevated Glass: Translucent Bronze Slate (`rgba(22, 25, 30, 0.8)`)
  - Typography: `Alexandria` & `Cairo` for Arabic; `Playfair Display` & `Inter` for Latin.

---

## 4. Prioritized Engineering Backlog (First 25 Tasks)

| # | Task Title | Target Files | Steps & Scope | Acceptance Criteria |
|---|---|---|---|---|
| **01** | WebGL 3D Room Studio Canvas | `src/components/3d/RoomStudio.tsx` | Setup R3F Canvas with PBR lighting, shadows, and orbit controls. | Renders 3D floor grid at 60fps with smooth camera rotation. |
| **02** | Draco-Compressed GLTF Furniture Loader | `src/services/3d/gltfLoader.ts` | Author GLTF loader with Draco decompression and progress cache. | Loads sofa model (< 2MB) in under 800ms with zero memory leak. |
| **03** | Real-Time Fabric & Leather Switcher | `src/components/3d/MaterialSwitcher.tsx` | Shader material swapper updating roughness, normal, and albedo maps. | Clicking fabric swatch updates sofa texture smoothly in < 100ms. |
| **04** | WebXR Mobile AR Placement Button | `src/components/3d/ArPlacement.tsx` | Integrates WebXR Device API and Apple QuickLook `.usdz` export. | Tapping button on mobile opens camera feed with 1:1 scale model. |
| **05** | Custom Room Dimension Slider | `src/components/studio/RoomConfig.tsx` | Interactive width/length/height sliders updating room walls dynamically. | Wall mesh scales smoothly without distorting baseboard textures. |
| **06** | 2D/3D Dual-View Toggle | `src/components/studio/ViewToggle.tsx` | Orthographic top-down 2D floor plan vs. perspective 3D camera flip. | Smooth spring camera transition between top-down and 3D views. |
| **07** | Furniture Collision & Wall Snapping | `src/services/physics/snappingEngine.ts` | Bounding box raycasting snapping furniture to nearest wall within 15cm. | Dragging sofa near wall snaps back edge flush against wall. |
| **08** | Arabic Dynamic Island Navigation Island | `src/components/ui/StudioIsland.tsx` | Spring-animated floating bar with Save, Share, AR, and Order pills. | Easing uses cubic-bezier(0.16, 1, 0.3, 1); active tabs expand. |
| **09** | WhatsApp Pre-Filled Order Generator | `src/services/export/whatsappOrder.ts` | Encodes room layout screenshot, SKU, fabric codes, and client dimensions. | Generates clean WhatsApp URL opening direct chat with Negm sales. |
| **10** | Paymob 50% Manufacturing Deposit Checkout| `src/services/payments/depositPaymob.ts` | Creates Paymob checkout session with "Launching Soon" fallback. | Renders payment modal; logs deposit reference ID. |
| **11** | Customer Quotation PDF Generator | `src/services/pdf/quoteGenerator.ts` | Generates branded PDF quotation with dimensions, render snapshot, and terms. | Client can download clean PDF quote in Arabic and English. |
| **12** | Client Production Milestone Tracker | `src/components/tracking/OrderTracker.tsx` | Visual progress bar: (Woodworking -> Upholstery -> QC -> Delivery). | Client enters order ID and sees live milestone and photo updates. |
| **13** | Friend Turnkey Arabic Admin Dashboard | `src/components/admin/FriendDashboard.tsx` | Simplified Arabic portal for adding furniture products and photos. | Non-technical friend can upload product and set price in < 2 mins. |
| **14** | Mobile Safari WebGL Context Recovery | `src/components/3d/ContextRecovery.tsx` | Handles `webglcontextlost` gracefully with 360-degree turntable fallback. | Simulating WebGL context loss triggers clean fallback without crash. |
| **15** | Wood Finish Stain Customizer | `src/components/3d/WoodStainPicker.tsx` | Real-time PBR shader switcher for Walnut, Natural Oak, Mahogany, and Ash. | Visual grain changes realistically with roughness variation. |
| **16** | Modular Sectional Sofa Reconfigurator | `src/components/3d/SectionalBuilder.tsx` | Add/remove chaise lounge, 2-seater, and corner modules dynamically. | Modular units snap together seamlessly with shared upholstery. |
| **17** | Lighting Environment Presets | `src/components/3d/EnvironmentPresets.tsx` | Toggle Daylight (5500K), Warm Evening (3000K), and Studio Showroom. | HDRI ambient map updates lighting and shadows organically. |
| **18** | Dimension Label Measurement Overlays | `src/components/3d/DimensionLabels.tsx` | Floating 3D HTML labels displaying width, depth, and height in cm. | Labels billboard to face camera and hide when occluded. |
| **19** | R2 3D Model CDN Sync Daemon | `scripts/sync_models_r2.py` | Uploads compressed GLTF assets to Cloudflare R2 bucket with cache tags. | Scripts upload models and verify public CDN URLs. |
| **20** | Offline Floor Plan LocalStorage Sync | `src/services/storage/localProject.ts` | Auto-saves room draft to browser IndexedDB every 15 seconds. | Refreshing page restores client's customized room state perfectly. |
| **21** | Client Moodboard & Color Palette Extractor| `src/components/studio/PaletteExtractor.tsx`| Extracts dominant colors from uploaded living room photo to suggest fabrics. | Uploading living room photo highlights matching velvet swatches. |
| **22** | Damietta Workshop Order Spec Sheet | `src/services/export/workshopSpecSheet.ts`| Generates technical carpentry cut-list and upholstery yardage spec. | Outputs printable factory cut sheet for workshop artisans. |
| **23** | Customer Review & Photo Gallery | `src/components/reviews/PhotoGallery.tsx` | Masonry grid of real client living rooms with verified buyer badges. | Responsive image gallery with high-speed LCP optimization. |
| **24** | Turnkey Setup & Friend Handover Guide | `docs/HANDOVER_GUIDE_FOR_FRIEND.md` | Plain-language Arabic and English manual explaining daily operations. | Complete step-by-step guide tested for zero technical jargon. |
| **25** | Comprehensive E2E Playwright Test Suite | `tests/e2e/furnitureStudio.spec.ts` | End-to-end smoke test verifying 3D load, fabric switch, and WhatsApp quote. | All Playwright tests pass green with 0 errors. |

---

## 5. Mandatory Sections per Standards 24 to 27

### 5.1 Launch Package (Standard 24)
- **Platforms**: Responsive Web (Desktop, Tablet, Mobile) + PWA + WebXR Mobile AR.
- **Security & Privacy**: Client photos uploaded for room matching are processed client-side and never stored permanently without consent; Paymob webhooks signed via HMAC; strict rate limiting on quote requests.
- **Fair EGP Commercial Terms**:
  - Web 3D room planner and catalog are 100% free for all customers.
  - Bespoke manufacturing requires a 50% advance deposit via Paymob (Vodafone Cash, Cards, Meeza), with balance due upon delivery and inspection.
  - When live payment keys are absent, checkout displays "Deposits Launching Soon - Contact via WhatsApp" fallback.
- **Real Data Only**: All product dimensions, wood species, and fabric codes represent real Damietta carpentry specifications; zero placeholder items.
- **Plain-Language Owner Activation Checklist**:
  1. Buy Domain: `negmfurniture.com` or `negm-furniture.eg` (~500 EGP/year via local accredited registrar).
  2. Setup Paymob: Enter commercial registration details, paste `PAYMOB_API_KEY` into `.env`.
  3. Enter WhatsApp Business Number: Add friend's phone into `NEXT_PUBLIC_WHATSAPP_NUMBER`.
  4. Verify: Customize a sofa, tap "Order via WhatsApp", confirm WhatsApp message arrives on friend's phone with complete spec.

### 5.2 Market-Grade Compliance (Standard 25)
- **Competitor Study**: Documented in `plans/competitors/sir-negm-furniture.md` comparing against IKEA Egypt, Kabbani, and local Damietta workshops.
- **Regional Laws & Consumer Protection**: Complies with Egyptian Consumer Protection Law (Law 181/2018) for bespoke manufacturing contracts (clear delivery timeline, written specifications, 14-day defect warranty).
- **Privacy-First Analytics**: Opt-in anonymized telemetry measuring popular fabric choices and room dimensions; zero personal customer data captured.
- **Legal Pack with Lawyer Disclaimer**: Includes Terms of Custom Manufacturing, Delivery Policy, and Warranty Terms, marked *"AI-drafted for technical clarity; to be reviewed by a qualified Egyptian commercial lawyer before official commercial launch."*

### 5.3 Autonomous Operations (Standard 26)
- **In-Product Assistant**: "مساعد نجم للأثاث" - answers customer questions regarding wood types (beech wood vs. oak), fabric durability, cleaning methods, and delivery lead times in fluent Egyptian Arabic.
- **Operations Runbook**: Nightly database backups of custom orders, automated model compression pipeline, webhook reconciliation.
- **Telegram & WhatsApp Notifications**: Instant notification to the brand owner on WhatsApp when a customer completes a 3D layout or places a deposit.
- **Guard Rails**: Daily external AI API spending capped at $3.00/day.

### 5.4 Visibility & Discovery (Standard 27)
- **High-Intent Search Queries**:
  - Arabic: *"أثاث مودرن دمياط", "تفصيل أثاث حسب الطلب", "غرف نوم مودرن القاهرة", "معاينة الأثاث 3D"*
  - Egyptian Slang: *"عفش مودرن بالتقسيط", "معرض موبيليا راقي", "كنب كورنر عمولة"*
  - English: *"bespoke luxury furniture Cairo", "custom furniture Egypt 3D preview"*
- **Generative Engine Optimization (GEO)**: Hosts `llms.txt` and `/facts` detailing brand history, manufacturing materials, custom dimensions policy, and showroom locations.
- **JSON-LD Schema**: Implements `Product` and `LocalBusiness` schemas with validated review and pricing attributes.
