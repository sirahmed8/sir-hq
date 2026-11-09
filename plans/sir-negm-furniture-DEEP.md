# DEEP PLAN & MASTER SPEC: SIR Negm Furniture
**Project**: SIR Negm Furniture (`D:/Projects/SIR Negm Furniture`)  
**Status**: **FROZEN BY OWNER ORDER (2026-11-09)**. Friend's commercial project.  
**Rule**: **PLAN ONLY. ZERO BUILD CODE, ZERO CI, ZERO DEPLOYMENT.**  
**Deliverable**: Complete turn-key handoff pack for the friend's AI agent.  
**Version**: 1.0.0 (Strictly enforced)  
**Standard**: `_SIR/standard/23-premium-code-bar.md` & `_SIR/plans/GEMINI_QUALITY_CHARTER.md`

---

## 1. Executive Summary & Handoff Charter
SIR Negm Furniture is a bespoke luxury furniture commerce platform and interactive 3D room layout studio built for Ahmed's friend ("Negm Furniture"). Per explicit owner instructions on 2026-11-09, **this project is strictly frozen**: no SIR agent writes product code, configures CI workflows, or deploys instances to hosting accounts. Instead, SIR HQ prepares a comprehensive, turn-key **Handoff Pack** (architecture blueprints, prompt instructions for the friend's AI agent, data schemas, and clean setup scripts) so the friend can clone and build it independently.

---

## 2. Legacy Forensic Audit & Porting Analysis

### 2.1 Existing Legacy Assets (`SIR Negm Furniture/legacy/`)
1. **`Negm Furniture`**: WordPress/WooCommerce export with bespoke luxury furniture product catalog, photography, pricing tables, fabric variations, and customer inquiry forms.
2. **`floor-plan-generator-nov`**: React & Three.js canvas prototype allowing users to drag and drop furniture pieces onto a 2D floor plan with isometric 3D preview.

### 2.2 What is Valuable to Extract for the Handoff Pack
- **Catalog Data & Models**: 3D GLTF models, dimensions (height, width, depth in cm), material variations (velvet, leather, oak, walnut), and high-resolution photography.
- **Floor Plan Engine Core**: Mathematical room boundary calculations, wall collision detection, and canvas coordinate transformations.
- **Direct WhatsApp Order Bridge**: Pre-formatted WhatsApp order message generator detailing selected items, dimensions, fabric codes, and delivery address.

### 2.3 What Must Be Discarded
- Bloated WordPress database dumps, PHP plugins, and insecure WooCommerce endpoints.
- Hardcoded phone numbers and unverified production API keys.

---

## 3. Architecture & Design Identity for Handoff

### 3.1 Recommended Architecture (For Friend's Agent)
- **Frontend**: Next.js 14 App Router, Three.js / React Three Fiber for 3D room rendering, Tailwind CSS.
- **Backend / CMS**: Headless Strapi or Supabase PostgreSQL database for product inventory.
- **Commerce / Checkout**: Direct WhatsApp business checkout + regional payment gateway (Paymob / Fawry).
- **Deployment**: Vercel frontend + Supabase backend (to be provisioned by the friend).

### 3.2 Design Identity
- **Brand Aesthetic**: Luxury Artisanal Atelier. Warm, architectural, tactile, and prestigious.
- **Palette**:
  - Primary Bronze Gold: `#D97706` (Amber 600) / `#B45309` (Amber 700)
  - Secondary Warm Sand: `#F59E0B` (Amber 500)
  - Dark Surface Base: Deep Charcoal Obsidian (`#0F1115` / `#16191E`)
  - Elevated Glass: Translucent Bronze Slate (`rgba(22, 25, 30, 0.8)`)
- **Typography**: Editorial typography (`Cinzel` / `Playfair Display` for headlines, `Cairo` for Arabic, `Inter` for technical specifications).
- **Emblem**: Vector SVG interlocking geometric carpenter's square and golden ratio spiral.

---

## 4. Dependencies & Security Isolation
- **Isolation**: Zero SIR infrastructure shared. No Firebase, no Cloudflare, no shared secrets.
- **Handoff Target**: Stored exclusively within the private git repository until transferred to the friend.

---

## 5. The 25 Handoff Pack & Architecture Tasks (For Friend's Agent)

### NF-101 | Master Handoff Readme & Friend's Agent Instruction Prompt
- **Files**: `HANDOFF.md`, `prompts/agent_kickoff.prompt.txt`
- **Steps**: Author comprehensive handoff guide explaining project setup, tech stack selection, environment variables, and initial prompt for the friend's AI agent.
- **Acceptance**: Provides 1-click prompt that enables any external coding agent to bootstrap the project cleanly.

### NF-102 | Product Catalog JSON Schema & Clean Dataset Extraction
- **Files**: `data/products_schema.json`, `data/extracted_catalog.json`
- **Steps**: Extract and normalize products from legacy WordPress dump into clean JSON schema (SKU, title, dimensions, materials, price, images).
- **Acceptance**: 100% valid JSON validating against schema with zero missing dimension values.

### NF-103 | 3D Furniture Asset Optimization Pipeline Spec
- **Files**: `docs/3D_ASSET_PIPELINE.md`, `scripts/optimize_gltf.mjs`
- **Steps**: Document specifications for converting 3D models to Draco-compressed `.glb` under 2MB for fast mobile loading.
- **Acceptance**: Pipeline script optimizes sample 3D sofa model from 18MB to 1.4MB without visual degradation.

### NF-104 | 2D/3D Room Canvas Architecture Specification
- **Files**: `docs/FLOOR_PLAN_ARCHITECTURE.md`
- **Steps**: Document coordinate system, wall polygon extrusion, snap-to-grid math, and camera orbit controls for React Three Fiber.
- **Acceptance**: Complete mathematical model specified for 2D-to-3D projection.

### NF-105 | WhatsApp Business Checkout Payload Generator Spec
- **Files**: `specs/whatsapp_checkout_spec.md`
- **Steps**: Design URL-encoded WhatsApp message template with itemized cart list, calculated total, and custom fabric choices.
- **Acceptance**: Generates valid `https://wa.me/` deep links with structured Arabic order message.

### NF-106 | Bespoke Brand SVG Logo & Identity Vector Assets
- **Files**: `assets/brand/logo.svg`, `assets/brand/favicon.svg`
- **Steps**: Craft vector logo featuring golden carpenter's joint and typography; export to standard icon sizes.
- **Acceptance**: Clean vector SVG rendering crisply across dark and light backgrounds.

### NF-107 | Room Lighting & Photorealistic Shadow Shader Spec
- **Files**: `specs/threejs_lighting_spec.md`
- **Steps**: Document ambient occlusion, contact shadows, and realistic PBR wood/fabric material shaders.
- **Acceptance**: Shader configuration produces soft realistic shadows under furniture models.

### NF-108 | Responsive Dynamic Island Navigation Layout Spec
- **Files**: `specs/ui_design_system.md`
- **Steps**: Define design tokens, Dynamic Island active-only navigation, and mobile bottom sheet specifications.
- **Acceptance**: Complete CSS token map defined for bronze, sand, and charcoal surfaces.

### NF-109 | Supabase Database Schema Migration Scripts
- **Files**: `database/migrations/001_initial_schema.sql`
- **Steps**: Author PostgreSQL DDL schema for categories, products, finishes, orders, and customer inquiries with RLS rules.
- **Acceptance**: Clean SQL migration runs without errors on vanilla PostgreSQL 15+.

### NF-110 | Multi-Language Arabic/English Localization Dictionary
- **Files**: `locales/ar.json`, `locales/en.json`
- **Steps**: Create exhaustive bilingual translation dictionary covering furniture terminology (sofa, credenza, boucle, brass, lacquer).
- **Acceptance**: 100% parity across Arabic and English translation keys.

### NF-111 | Custom Dimension & Made-to-Measure Cost Calculator Spec
- **Files**: `specs/custom_pricing_formula.md`
- **Steps**: Mathematical formula calculating pricing adjustments based on non-standard width/depth dimensions and premium fabric multipliers.
- **Acceptance**: Correctly computes pricing delta with configurable margin buffers.

### NF-112 | Augmented Reality (WebXR & Apple QuickLook) Blueprint
- **Files**: `specs/ar_quicklook_spec.md`
- **Steps**: Specification for generating iOS `.usdz` and Android `model-viewer` tags for live camera AR projection in customer rooms.
- **Acceptance**: Documents exact meta tags and file requirements for 1-tap mobile AR preview.

### NF-113 | Showroom Appointment Booking Flow Specification
- **Files**: `specs/appointment_booking_spec.md`
- **Steps**: Architecture for customer showroom visit scheduler with date/time pickers and automated SMS/WhatsApp confirmations.
- **Acceptance**: Complete state machine defined from time slot selection to confirmation.

### NF-114 | Client Testimonial & Real Interior Project Gallery Spec
- **Files**: `specs/gallery_portfolio_spec.md`
- **Steps**: Blueprint for high-resolution masonry photo gallery with tagged furniture hotspots linking directly to catalog items.
- **Acceptance**: Interactive hotspot schema maps pixel coordinates to product SKUs.

### NF-115 | SEO & GEO Local Discovery Optimization Blueprint
- **Files**: `docs/SEO_STRATEGY.md`
- **Steps**: Schema.org JSON-LD structured data for LocalBusiness and Product schemas targeting Cairo/Giza bespoke furniture searches.
- **Acceptance**: Includes valid Google Rich Results test snippets.

### NF-116 | Docker Compose Self-Hosted Evaluation Stack
- **Files**: `docker-compose.yml`, `docs/DOCKER_GUIDE.md`
- **Steps**: Provide optional local Docker Compose stack running Next.js frontend, Strapi CMS, and PostgreSQL for offline testing.
- **Acceptance**: `docker compose up -d` boots entire environment locally in one command.

### NF-117 | Fabric Swatch Physical Sample Request Flow
- **Files**: `specs/sample_request_flow.md`
- **Steps**: Design user flow for requesting a physical swatch box of 5 fabric samples delivered to customer address.
- **Acceptance**: Complete form specification with address validation and delivery fee logic.

### NF-118 | High-Performance Image Optimization & CDN Caching Spec
- **Files**: `docs/IMAGE_PERFORMANCE_SPEC.md`
- **Steps**: Document responsive WebP/AVIF srcset generation, blur placeholders, and CDN caching headers for 4K showroom photos.
- **Acceptance**: Guarantees sub-1s LCP on 4G mobile connections.

### NF-119 | Interactive Color & Wood Finish Customizer Spec
- **Files**: `specs/material_picker_spec.md`
- **Steps**: Interactive UI component specification allowing real-time material swapping on 3D models with thumbnail swatches.
- **Acceptance**: Defines Three.js texture replacement pipeline without model reloading.

### NF-120 | Security Checklist for Commercial Production Deployment
- **Files**: `docs/SECURITY_CHECKLIST.md`
- **Steps**: Comprehensive security checklist covering OWASP Top 10, payment webhook HMAC signatures, CSP, and form sanitization.
- **Acceptance**: 20-point actionable pre-launch security audit table.

### NF-121 | Order Status Tracking Portal Specification
- **Files**: `specs/order_tracking_spec.md`
- **Steps**: Customer tracking interface where entering phone number and order ID displays manufacturing stage (Cutting, Carpentry, Upholstery, Delivery).
- **Acceptance**: Clean progress tracker UI specification with milestone timestamps.

### NF-122 | Environmental & Solid Wood Certification Badging
- **Files**: `specs/certifications_badges.md`
- **Steps**: Design tokens and badge specifications for kiln-dried beechwood, anti-termite treatment, and craftsmanship warranties.
- **Acceptance**: SVG badge assets and placement guidelines across product detail cards.

### NF-123 | PDF Showroom Lookbook & Tear Sheet Generator Spec
- **Files**: `specs/tear_sheet_pdf_spec.md`
- **Steps**: Automated specification for generating elegant, printable 1-page A4 architectural tear sheets for interior designers.
- **Acceptance**: Template layouts specified for product photo, dimensional CAD drawing, and material options.

### NF-124 | Clean Git Repository Handoff Archive Script
- **Files**: `scripts/prepare_handoff_archive.ps1`
- **Steps**: Script packaging all blueprints, schemas, assets, and kickoff prompts into clean standalone ZIP bundle for friend.
- **Acceptance**: Generates verified ZIP archive with zero internal SIR artifacts or sensitive keys.

### NF-125 | End-to-End Handoff Validation & Verification Check
- **Files**: `scripts/verify_handoff_pack.py`
- **Steps**: Automated verification script confirming all 24 handoff specifications, schemas, and brand assets exist and validate cleanly.
- **Acceptance**: Script confirms 100% handoff pack completeness.
