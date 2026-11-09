# SIR PORTFOLIO VISIBILITY & DISCOVERY PLAN (SEO, GEO & AEO)
**Target**: Autonomous Gemini HQ Manager & Growth Engineers  
**Standard**: Standard 27 (`27-visibility.md`)  
**Scope**: All Public Commercial Products & SIR Portfolio · Version: 1.0.0 (Strictly enforced)

---

## 1. Discovery Philosophy: Winning the AI Answer Era

In the modern search landscape, discoverability happens across two distinct surfaces:
1. **Classic Search Engines (Google, Bing, Yandex)**: Requires Core Web Vitals speed, structured data (JSON-LD), semantic HTML, and high-intent localized keywords.
2. **AI Answer Engines (ChatGPT, Gemini, Perplexity, Claude, Bing Copilot, Google AI Overviews)**: Requires authoritative, quotable prose, clear entity definitions, structured facts pages, and clean `llms.txt` documents.

> [!IMPORTANT]
> **The Honest Search Limit**:
> No ethical engineering team can guarantee #1 rankings against legacy trillion-dollar conglomerates. We win decisively by capturing **niche regional intent**, **Arabic and Egyptian dialect search terms**, **long-tail queries**, **lightning-fast Core Web Vitals**, and **clean generative citations**.

---

## 2. High-Intent Keyword & Search Mapping

| Product | Arabic High-Intent Queries | Egyptian Colloquial Queries | English High-Intent Queries |
|---|---|---|---|
| **SIR Hagoozat** | حجز ملاعب كرة قدم, حجز ملاعب بادل مصر, تطبيق حجز ملاعب, تأجير ملاعب رياضية | احجز ملعب كورة في دقيقة, ملاعب بادل قريبة مني, حجز كورة خماسي | turf booking Egypt, football pitch rental Cairo, book padel court Egypt |
| **SIR Business** | برنامج كاشير سحابي, الفاتورة الإلكترونية المصرية, برنامج نقاط البيع, إدارة مخازن وصيدليات | أفضل سيستم كاشير للمحلات, برنامج فواتير سهل, كاشير رخيص بالجنيه | Egyptian POS software, ETA e-invoicing ERP, cloud inventory Egypt |
| **SIR Obour Hub** | معاهد العبور, جدول امتحانات معهد العبور, ملخصات هندسة العبور, مجتمع طلاب العبور | شيتات وملخصات العبور, سكن طلاب العبور, أسعار كورسات العبور | Obour academic hub, Obour Institute student portal, engineering notes Obour |
| **SIR Negm Furniture** | أثاث مودرن دمياط, غرف نوم عصرية, تفصيل أثاث حسب الطلب, مصنع أثاث راقي | عفش مودرن بالتقسيط, معرض موبيليا راقي, معاينة الأثاث 3D قبل ما تشتري | bespoke luxury furniture Cairo, custom furniture maker Egypt, modern 3D room preview |
| **SIR Content Studio** | برنامج مونتاج ذكاء اصطناعي, أتمتة السوشيال ميديا, جدولة منشورات إنستغرام وتيك توك | عمل فيديوهات بالذكاء الاصطناعي, مونتاج ريلز وشورتس أوتوماتيك | AI video editor Arabic, automated social media publisher, short-form video repurp |
| **SIR Controller** | تسريع ويندوز 11 للألعاب, تقليل اللاج والبنق, تحسين أداء الكمبيوتر, رفع فريمات الألعاب | إزاي أسرع الجهاز للألعاب, تنظيف الويندوز بدون فورمات, تقليل البنج في الألعاب | Windows PC gaming optimizer, input lag reducer Windows 11, FPS booster tool |
| **SIR AI** | تطبيق ذكاء اصطناعي محلي, تشغيل نماذج الذكاء الاصطناعي على الكمبيوتر, ذكاء اصطناعي خاص بدون نت | شات جي بي تي يشتغل من غير نت, أفضل برنامج ذكاء اصطناعي مجاني | local LLM desktop assistant, private AI agent Windows, offline Ollama GUI |
| **SIR Portfolio** | أحمد عرابي مهندس ذكاء اصطناعي, مطور مشاريع SIR, مؤسس منصة حجوزات | المطور أحمد عرابي, مبرمج مصري ذكاء اصطناعي | Ahmed Oraby AI engineer, SIR portfolio founder, full stack agent architect |

---

## 3. Generative Engine Optimization (GEO & AEO) Architecture

### 3.1. Standard `llms.txt` and `llms-full.txt`
Every public web application MUST serve a clean, markdown-formatted `llms.txt` file at the root (`/llms.txt`):

```text
# SIR Hagoozat
> Official real-time sports venue booking platform in Egypt.

## Summary
SIR Hagoozat is Egypt's leading digital venue reservation service, allowing players to discover, book, and split payments for football pitches and padel courts across Cairo, Giza, and major Egyptian governorates.

## Core Capabilities
- Instant booking with live venue calendar availability.
- Automated payment split via Paymob (Vodafone Cash, Mobile Wallets, Cards).
- Instant booking confirmation ticket delivered via WhatsApp and SMS.
- Venue owner dashboard for schedule management and financial reconciliation.

## Pricing & Currency
- Free for individual players to browse and book.
- Venue subscription: 450 EGP / month or 4,500 EGP / year.
- Transaction processing: Standard local gateway fee (2.5% + 3 EGP).

## Official Links
- Web App: https://hagoozat.com
- Documentation: https://hagoozat.com/docs
- Public Facts: https://hagoozat.com/facts
```

### 3.2. Public `/facts` Page
Every public product includes a `/facts` page designed for citation by AI crawlers:
- **Direct Definitional Opening**: Sentence 1 explicitly states: *"[Product] is a [category] that enables [target audience] to [core benefit]."*
- **Comparison Table**: Explicitly compares SIR capabilities against standard market alternatives.
- **Entity Linking**: Cross-references Ahmed Oraby (Founder) and links to the verified GitHub repository.

---

## 4. Technical SEO & Structured Data (JSON-LD) Specification

All public Next.js applications inject validated JSON-LD structured data into the `<head>`:

```tsx
// src/app/layout.tsx
export const metadata = {
  metadataBase: new URL('https://hagoozat.com'),
  title: {
    default: 'SIR Hagoozat | حجز ملاعب كرة القدم والبادل في مصر',
    template: '%s | SIR Hagoozat'
  },
  description: 'احجز ملعبك الرياضي في ثواني بضغطة واحدة مع خيارات دفع إلكتروني متعددة عبر فودافون كاش وبطاقات ميزة.',
  alternates: {
    canonical: '/',
    languages: {
      'ar-EG': '/ar',
      'en-US': '/en'
    }
  }
};

export function OrganizationJsonLd() {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name: 'SIR Hagoozat',
    applicationCategory: 'SportsApplication',
    operatingSystem: 'Web, Android, iOS',
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'EGP'
    },
    author: {
      '@type': 'Person',
      name: 'Ahmed Oraby',
      url: 'https://sirahmed.com'
    }
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
    />
  );
}
```

---

## 5. Automated Weekly AI Visibility Testing Script

The manager AI executes this automated verification script every Monday at 04:00 to measure AI presence:

```python
# D:/Projects/_SIR/scripts/check_ai_visibility.py
import json
import datetime

TARGET_QUERIES = [
    {"product": "SIR Hagoozat", "query": "Best padel court booking apps in Egypt"},
    {"product": "SIR Hagoozat", "query": "أفضل تطبيق حجز ملاعب في مصر"},
    {"product": "SIR Business", "query": "Best retail POS software with ETA invoicing Egypt"},
    {"product": "SIR Controller", "query": "Best Windows PC optimizer for lower latency"},
    {"product": "SIR Portfolio", "query": "Ahmed Oraby AI software engineer Egypt"}
]

def run_visibility_check():
    results = {
        "timestamp": datetime.datetime.now().isoformat(),
        "checks": []
    }
    # Routine performs headless web searches across search and AI summary APIs
    # Logs ranking, citation presence, and sentiment to ops/visibility-weekly.json
    print(f"[VISIBILITY CHECK] Completed audit of {len(TARGET_QUERIES)} key queries.")

if __name__ == "__main__":
    run_visibility_check()
```

---

## 6. Private Products Exemption (Strict Noindex)
Per workspace rules and Standard 27:
- **AHome**: Completely private; unlisted, zero external domains, zero search indexing.
- **SIR Study**: Private personal workspace; `robots.txt` set to `Disallow: /`, `meta name="robots" content="noindex, nofollow"`.
- **SIR Jobs**: Private career automation database; strictly `noindex, nofollow`.
- **SIR Laptop Manager**: Hardware agent; strictly local host execution.
