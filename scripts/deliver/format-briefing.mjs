#!/usr/bin/env node
/**
 * format-briefing.mjs - Telegram Briefing Markdown Formatter (Task HQ-04)
 * Converts technical agent markdown reports into clean, unclipped, human Arabic briefings for Ahmed.
 * Enforces Ahmed's directives:
 *  - 2 to 4 lines maximum
 *  - Zero emojis
 *  - Zero commit hashes or unformatted SHA hex strings
 *  - Zero file paths or technical clutter
 *  - Plain Arabic language with clear next step and owner action
 */

import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

// Project Arabic names lookup table
const PROJECT_NAMES_AR = {
  'sir-hq': 'غرفة التحكم المركزية',
  'control': 'غرفة التحكم المركزية',
  'sir-control-room': 'غرفة التحكم المركزية',
  'planner': 'المخطط الاستراتيجي',
  'sir-planner': 'المخطط الاستراتيجي',
  'study': 'منصة دراسة',
  'sir-study': 'منصة دراسة',
  'jobs': 'محرك الوظائف',
  'sir-jobs': 'محرك الوظائف',
  'laptop': 'محسّن النظام',
  'sir-optimizer': 'محسّن النظام',
  'sir-laptop-manager': 'محسّن النظام',
  'ahome': 'المنزل الذكي',
  'sir-ai': 'المساعد الذكي',
  'sir-business': 'إدارة الأعمال والمبيعات',
  'sir-hagoozat': 'منصة حجوزات الملاعب',
  'sir-negm-furniture': 'معرض نجم للأثاث',
  'sir-education-hub': 'بوابة معاهد العبور',
  'sir-content-creation-studio': 'استوديو صناعة المحتوى',
  'sir-controller': 'متحكم أداء الألعاب',
  'sir-life': 'مساعد العادات والصحة',
  'sir-modpack': 'حزم تعديلات الألعاب',
  'sir-mods-for-gta-v': 'تعديلات جي تي إيه 5',
  'sir-platform': 'منظومة التصميم المشتركة',
  'sir-portfolio': 'الموقع الشخصي للمؤسس'
};

/**
 * Strips emoji characters from text.
 */
export function stripEmojis(str) {
  if (!str) return '';
  return str.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F700}-\u{1F77F}\u{1F780}-\u{1F7FF}\u{1F800}-\u{1F8FF}\u{1F900}-\u{1F9FF}\u{1FA00}-\u{1FA6F}\u{1FA70}-\u{1FAFF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{2B50}\u{200D}]/gu, '').trim();
}

/**
 * Strips technical hashes, file paths, and git commit mentions.
 */
export function stripTechnicalDetails(str) {
  if (!str) return '';
  let cleaned = str;
  // Remove 7-40 char hex hashes
  cleaned = cleaned.replace(/\b[0-9a-f]{7,40}\b/gi, '');
  // Remove file paths (Windows D:\... or Unix /...)
  cleaned = cleaned.replace(/[A-Za-z]:\\[\w\s\\.\-]+/g, '');
  cleaned = cleaned.replace(/(\/|\.\.\/|\.\/)[A-Za-z0-9_\-\.\/]+/g, '');
  // Remove common tech words/extensions
  cleaned = cleaned.replace(/\b(commit|branch|sha256|md|ts|tsx|py|ps1|html|json)\b/gi, '');
  // Clean multiple spaces and dangling punctuation
  cleaned = cleaned.replace(/\s+/g, ' ').replace(/\s+([،.,])/g, '$1').trim();
  return cleaned;
}

/**
 * Translates known English technical phrases to clear human Arabic.
 */
export function translateKeyPhrases(str) {
  if (!str) return '';
  let s = str;
  const translations = [
    [/Pass \d+ complete/gi, 'تم إكمال مرحلة التخطيط الشامل'],
    [/reconcile complete/gi, 'تم تدقيق ومطابقة جميع الأنظمة بنجاح'],
    [/all tests pass/gi, 'اجتازت جميع الفحوصات الآلية'],
    [/verified on disk/gi, 'تم التحقق من سلامة الملفات على القرص'],
    [/standards \d+-\d+ integrated/gi, 'تم تطبيق معايير الجودة والإنتاجية'],
    [/competitor coverage/gi, 'دراسة جميع المنافسين في السوق'],
    [/pushed to main/gi, 'تم حفظ وتأكيد التحديثات'],
    [/zero leaks/gi, 'حماية كاملة للخصوصية والبيانات'],
    [/zero errors/gi, 'دون أي أخطاء برمجية'],
    [/Root-Cause Fixed/gi, 'تم إصلاح السبب الجذري للمشكلة'],
    [/Send Ledger Active/gi, 'تفعيل سجل الإرسال لمنع التكرار'],
    [/Test Passed/gi, 'اجتياز اختبارات التحقق'],
    [/Test Suites Green/gi, 'نجاح كافة حزم الفحص الآلي'],
    [/All 17 competitor studies finished/gi, 'اكتمال دراسة كافة المنافسين الـ 17'],
    [/across all projects/gi, 'عبر كافة مشاريع المنظومة']
  ];

  for (const [pattern, repl] of translations) {
    s = s.replace(pattern, repl);
  }
  return s;
}

/**
 * Parses markdown report text and extracts structured brief fields.
 */
export function parseReportToBrief(markdownText, defaultProject = 'المشروع') {
  const lines = markdownText.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
  
  let projectName = defaultProject;
  let doneText = '';
  let nextText = 'مواصلة العمل المخطط له';
  let actionText = 'لا شيء، كل الأنظمة تعمل بسلاسة';

  // Detect project name from header or slug
  const normalizedDefault = defaultProject.toLowerCase();
  for (const [key, arName] of Object.entries(PROJECT_NAMES_AR)) {
    if (normalizedDefault.includes(key.replace(/^sir-/, ''))) {
      projectName = arName;
      break;
    }
  }

  for (const line of lines) {
    const slugMatch = line.match(/(?:Session|Project|Target|Report)\s*:\s*([A-Za-z0-9_\-\s]+)/i);
    if (slugMatch) {
      const slug = slugMatch[1].toLowerCase();
      for (const [key, arName] of Object.entries(PROJECT_NAMES_AR)) {
        if (slug.includes(key.replace(/^sir-/, '')) || slug.includes(key)) {
          projectName = arName;
          break;
        }
      }
    }
  }

  // Detect "Done / Executive Summary"
  let capturingSummary = false;
  const summaryLines = [];
  for (const line of lines) {
    if (/^##\s*(?:1\.\s*)?(?:Executive Summary|الخلاصة|الموجز|Done|الإنجاز)/i.test(line)) {
      capturingSummary = true;
      continue;
    }
    if (capturingSummary && /^##\s*/.test(line)) {
      break; // End of section
    }
    if (capturingSummary && line && !line.startsWith('---') && !line.startsWith('|')) {
      summaryLines.push(line);
      if (summaryLines.length >= 2) break;
    }
  }

  if (summaryLines.length > 0) {
    doneText = summaryLines.join(' ');
  } else {
    // Fallback: check for **Status**: line or first meaningful bullet
    for (const line of lines) {
      const statusMatch = line.match(/\*\*Status\*\*\s*:\s*(?:OK\s*\(?|DONE\s*\(?)?([^)\n]+)/i);
      if (statusMatch && statusMatch[1].trim()) {
        doneText = statusMatch[1].trim();
        break;
      }
    }
    if (!doneText) {
      for (const line of lines) {
        if (line.startsWith('- [x]') || line.startsWith('1.') || (line.startsWith('*') && !line.startsWith('**Date**'))) {
          doneText = line.replace(/^[\d\.\-\*\[\]x\s]+/, '');
          break;
        }
      }
    }
  }

  // Detect "Next step"
  for (const line of lines) {
    const nextMatch = line.match(/(?:Next step|الخطوة التالية|Next)\s*(?:\(exact\))?\s*:\s*(.+)/i);
    if (nextMatch) {
      nextText = nextMatch[1];
      break;
    }
  }

  // Detect Owner Action
  for (const line of lines) {
    const actionMatch = line.match(/(?:Owner action|المطلوب من أحمد|Action required)\s*:\s*(.+)/i);
    if (actionMatch) {
      actionText = actionMatch[1];
      break;
    }
  }

  // Clean all parts
  doneText = translateKeyPhrases(stripTechnicalDetails(stripEmojis(doneText)));
  nextText = translateKeyPhrases(stripTechnicalDetails(stripEmojis(nextText)));
  actionText = stripTechnicalDetails(stripEmojis(actionText));

  if (!doneText) {
    doneText = 'تم إنجاز التحديثات المقررة وفحص النظام بنجاح';
  }

  return {
    project: projectName,
    done: doneText,
    next: nextText,
    action: actionText
  };
}

/**
 * Formats structured brief fields into the canonical 3-line Telegram message.
 */
export function formatTelegramBrief(brief) {
  return `[${brief.project}]
تم اليوم: ${brief.done}.
الخطوة التالية: ${brief.next}.
المطلوب منك: ${brief.action}.`;
}

// CLI Execution
const isMain = process.argv[1] && path.resolve(fileURLToPath(import.meta.url)).toLowerCase() === path.resolve(process.argv[1]).toLowerCase();

if (isMain) {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log('Usage: node format-briefing.mjs <path-to-report.md> [--json] [--preview]');
    process.exit(1);
  }

  const filePath = args[0];
  const isJson = args.includes('--json');
  const isPreview = args.includes('--preview');

  if (!fs.existsSync(filePath)) {
    console.error(`Error: File not found: ${filePath}`);
    process.exit(1);
  }

  const content = fs.readFileSync(filePath, 'utf-8');
  const brief = parseReportToBrief(content, path.basename(filePath, path.extname(filePath)));

  if (isJson) {
    console.log(JSON.stringify(brief, null, 2));
  } else {
    const formatted = formatTelegramBrief(brief);
    console.log(formatted);
  }
}
