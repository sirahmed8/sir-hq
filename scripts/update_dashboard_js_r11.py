import re

template_path = "D:/Projects/_SIR/plans/dashboard_template.html"

with open(template_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update i18n dictionaries with all new keys
en_additions = """    menuBtn: "Menu",
    settingsBtn: "Settings",
    settingsTitle: "Settings & Preferences",
    settingsClose: "Close settings",
    appearanceGroup: "Appearance",
    themeLight: "Light",
    themeDark: "Dark",
    themeSystem: "System",
    languageGroup: "Language & Direction",
    langEn: "English (LTR)",
    langAr: "العربية (RTL)",
    densityGroup: "Display Density",
    densityComfortable: "Comfortable",
    densityCompact: "Compact",
    telemetryGroup: "Telemetry & Sync",
    artifactHashLabel: "Artifact Hash: ",
    gitLabel: "Git: ",
    refreshNow: "Refresh Telemetry Now",
    refreshing: "Refreshing...",
    navDrawerTitle: "Navigation",
    navDrawerClose: "Close navigation",
    moreNav: "More","""

ar_additions = """    menuBtn: "القائمة",
    settingsBtn: "الإعدادات",
    settingsTitle: "الإعدادات والتفضيلات",
    settingsClose: "إغلاق الإعدادات",
    appearanceGroup: "المظهر والسمة",
    themeLight: "فاتح",
    themeDark: "داكن",
    themeSystem: "تلقائي (النظام)",
    languageGroup: "اللغة والاتجاه",
    langEn: "الإنجليزية (LTR)",
    langAr: "العربية (RTL)",
    densityGroup: "كثافة العرض",
    densityComfortable: "مريح",
    densityCompact: "مضغوط",
    telemetryGroup: "المزامنة والبيانات الحية",
    artifactHashLabel: "معرف الأرتيفاكت: ",
    gitLabel: "إصدار Git: ",
    refreshNow: "تحديث البيانات الآن",
    refreshing: "جاري التحديث...",
    navDrawerTitle: "التنقل السريع",
    navDrawerClose: "إغلاق القائمة",
    moreNav: "المزيد","""

# Inject inside en: { and ar: {
code = code.replace('  en: {\n    btn: "العربية",', f'  en: {{\n{en_additions}\n    btn: "العربية",')
code = code.replace('  ar: {\n    btn: "English",', f'  ar: {{\n{ar_additions}\n    btn: "English",')

# 2. Replace old Theme controller with new Theme + Density + Settings Dialog controller
old_theme_ctrl = """// Theme controller
const savedTheme = localStorage.getItem("sir_theme") || "light";
document.documentElement.setAttribute("data-theme", savedTheme);
function updateThemeBtn() {
  const isDark = document.documentElement.getAttribute("data-theme") === "dark";
  const isAr = currentLang === "ar";
  $("#theme-btn").textContent = isDark ? (isAr ? "فاتح" : "Light") : (isAr ? "داكن" : "Dark");
}

$("#theme-btn").addEventListener("click", () => {
  const current = document.documentElement.getAttribute("data-theme");
  const next = current === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
  localStorage.setItem("sir_theme", next);
  updateThemeBtn();
});"""

new_pref_ctrl = """// Preferences Controller (Theme, Density, Dynamic Island Settings Dialog)
let themeMode = localStorage.getItem("sir_theme_mode") || localStorage.getItem("sir_theme") || "system";
let densityMode = localStorage.getItem("sir_density") || "comfortable";

function applyTheme(mode) {
  themeMode = mode;
  localStorage.setItem("sir_theme_mode", mode);
  localStorage.setItem("sir_theme", mode);
  const sysDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const effectiveTheme = mode === "system" ? (sysDark ? "dark" : "light") : mode;
  document.documentElement.setAttribute("data-theme", effectiveTheme);
  
  document.querySelectorAll("[data-theme-val]").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.themeVal === mode);
  });
}

function applyDensity(density) {
  densityMode = density;
  localStorage.setItem("sir_density", density);
  if (density === "compact") {
    document.documentElement.setAttribute("data-density", "compact");
  } else {
    document.documentElement.removeAttribute("data-density");
  }
  document.querySelectorAll("[data-density-val]").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.densityVal === density);
  });
}

// System color scheme change listener
if (window.matchMedia) {
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
    if (themeMode === "system") {
      document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
    }
  });
}

applyTheme(themeMode);
applyDensity(densityMode);

// Settings Popover / Dialog
const settingsModal = $("#settings-modal");
const settingsBackdrop = $("#settings-backdrop");
const settingsBtn = $("#settings-btn");
const settingsCloseBtn = $("#settings-close-btn");

function openSettings() {
  settingsModal.classList.add("open");
  settingsBackdrop.classList.add("open");
  settingsBtn.setAttribute("aria-expanded", "true");
}

function closeSettings() {
  settingsModal.classList.remove("open");
  settingsBackdrop.classList.remove("open");
  settingsBtn.setAttribute("aria-expanded", "false");
}

settingsBtn.addEventListener("click", () => {
  if (settingsModal.classList.contains("open")) {
    closeSettings();
  } else {
    openSettings();
  }
});
settingsCloseBtn.addEventListener("click", closeSettings);
settingsBackdrop.addEventListener("click", closeSettings);

// Side Menu Drawer (Responsive)
const sidebarEl = $("#app-sidebar");
const drawerBackdrop = $("#drawer-backdrop");
const menuToggleBtn = $("#menu-toggle-btn");
const mobileMenuTrigger = $("#mobile-menu-trigger");
const drawerCloseBtn = $("#drawer-close-btn");

function openSidebarDrawer() {
  sidebarEl.classList.add("open");
  drawerBackdrop.classList.add("open");
  if (menuToggleBtn) menuToggleBtn.setAttribute("aria-expanded", "true");
  if (mobileMenuTrigger) mobileMenuTrigger.setAttribute("aria-expanded", "true");
}

function closeSidebarDrawer() {
  sidebarEl.classList.remove("open");
  drawerBackdrop.classList.remove("open");
  if (menuToggleBtn) menuToggleBtn.setAttribute("aria-expanded", "false");
  if (mobileMenuTrigger) mobileMenuTrigger.setAttribute("aria-expanded", "false");
}

if (menuToggleBtn) menuToggleBtn.addEventListener("click", openSidebarDrawer);
if (mobileMenuTrigger) mobileMenuTrigger.addEventListener("click", openSidebarDrawer);
if (drawerCloseBtn) drawerCloseBtn.addEventListener("click", closeSidebarDrawer);
if (drawerBackdrop) drawerBackdrop.addEventListener("click", closeSidebarDrawer);

// Escape key to dismiss modals/drawers
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeSettings();
    closeSidebarDrawer();
  }
});

// Settings Modal theme & density buttons
document.querySelectorAll("[data-theme-val]").forEach(btn => {
  btn.addEventListener("click", () => applyTheme(btn.dataset.themeVal));
});
document.querySelectorAll("[data-density-val]").forEach(btn => {
  btn.addEventListener("click", () => applyDensity(btn.dataset.densityVal));
});

// Telemetry refresh button in Settings
$("#set-refresh-btn").addEventListener("click", () => {
  const btn = $("#set-refresh-btn");
  const txt = $("#txt-refresh-now");
  const t = i18n[currentLang] || i18n.en;
  btn.disabled = true;
  txt.textContent = t.refreshing;
  setTimeout(() => {
    window.location.reload();
  }, 450);
});"""

assert old_theme_ctrl in code, "old_theme_ctrl not found"
code = code.replace(old_theme_ctrl, new_pref_ctrl)

# 3. Update applyLang to update all new labels & sync language segmented buttons
old_apply_lang_start = """  $("#lang-btn").textContent = t.btn;
  $("#txt-label").textContent = t.label;
  $("#txt-title").textContent = t.title;
  $("#txt-desc").textContent = t.desc;"""

new_apply_lang_start = """  if ($("#txt-menu-btn")) $("#txt-menu-btn").textContent = t.menuBtn;
  if ($("#txt-settings-btn")) $("#txt-settings-btn").textContent = t.settingsBtn;
  if ($("#settings-btn")) $("#settings-btn").setAttribute("aria-label", t.settingsBtn);
  if ($("#settings-title")) $("#settings-title").textContent = t.settingsTitle;
  if ($("#settings-close-btn")) $("#settings-close-btn").setAttribute("aria-label", t.settingsClose);
  if ($("#txt-set-appearance")) $("#txt-set-appearance").textContent = t.appearanceGroup;
  if ($("#theme-btn-light")) $("#theme-btn-light").textContent = t.themeLight;
  if ($("#theme-btn-dark")) $("#theme-btn-dark").textContent = t.themeDark;
  if ($("#theme-btn-system")) $("#theme-btn-system").textContent = t.themeSystem;
  if ($("#txt-set-language")) $("#txt-set-language").textContent = t.languageGroup;
  if ($("#lang-btn-en")) {
    $("#lang-btn-en").textContent = t.langEn;
    $("#lang-btn-en").classList.toggle("active", lang === "en");
  }
  if ($("#lang-btn-ar")) {
    $("#lang-btn-ar").textContent = t.langAr;
    $("#lang-btn-ar").classList.toggle("active", lang === "ar");
  }
  if ($("#txt-set-density")) $("#txt-set-density").textContent = t.densityGroup;
  if ($("#density-btn-comfort")) $("#density-btn-comfort").textContent = t.densityComfortable;
  if ($("#density-btn-compact")) $("#density-btn-compact").textContent = t.densityCompact;
  if ($("#txt-set-telemetry")) $("#txt-set-telemetry").textContent = t.telemetryGroup;
  if ($("#txt-hash-lbl")) $("#txt-hash-lbl").textContent = t.artifactHashLabel;
  if ($("#txt-git-lbl")) $("#txt-git-lbl").textContent = t.gitLabel;
  if ($("#txt-refresh-now")) $("#txt-refresh-now").textContent = t.refreshNow;
  if ($("#set-artifact-hash")) $("#set-artifact-hash").textContent = D.content_hash || "--------";
  if ($("#set-git-hash")) $("#set-git-hash").textContent = D.git_short_hash || "main";

  if ($("#txt-nav-title")) $("#txt-nav-title").textContent = t.navDrawerTitle;
  if ($("#drawer-close-btn")) $("#drawer-close-btn").setAttribute("aria-label", t.navDrawerClose);
  if ($("#menu-toggle-btn")) $("#menu-toggle-btn").setAttribute("aria-label", t.menuBtn);
  if ($("#mobile-menu-trigger")) $("#mobile-menu-trigger").setAttribute("aria-label", t.navDrawerTitle);
  if ($("#txt-qp-more")) $("#txt-qp-more").textContent = t.moreNav;

  if ($("#side-now-text")) $("#side-now-text").textContent = t.navNow;
  if ($("#side-handover-text")) $("#side-handover-text").textContent = t.navHandover;
  if ($("#side-ci-text")) $("#side-ci-text").textContent = t.navCi;
  if ($("#side-ledgers-text")) $("#side-ledgers-text").textContent = t.navLedgers;
  if ($("#side-waves-text")) $("#side-waves-text").textContent = t.navWaves;
  if ($("#side-projects-text")) $("#side-projects-text").textContent = t.navProjects;
  if ($("#side-platforms-text")) $("#side-platforms-text").textContent = t.navPlatforms;
  if ($("#side-accounts-text")) $("#side-accounts-text").textContent = t.navAccounts;
  if ($("#side-workforce-text")) $("#side-workforce-text").textContent = t.navWorkforce;
  if ($("#side-activity-text")) $("#side-activity-text").textContent = t.navActivity;

  if ($("#qp-now-text")) $("#qp-now-text").textContent = t.navNow;
  if ($("#qp-handover-text")) $("#qp-handover-text").textContent = t.navHandover;
  if ($("#qp-ci-text")) $("#qp-ci-text").textContent = t.navCi;
  if ($("#qp-projects-text")) $("#qp-projects-text").textContent = t.navProjects;

  $("#txt-label").textContent = t.label;
  $("#txt-title").textContent = t.title;
  $("#txt-desc").textContent = t.desc;"""

assert old_apply_lang_start in code, "old_apply_lang_start not found"
code = code.replace(old_apply_lang_start, new_apply_lang_start)

# Remove the line calling updateThemeBtn(); inside applyLang
code = code.replace("  updateThemeBtn();\n", "")

# Remove old #lang-btn event listener and add language buttons listeners in settings modal
old_lang_btn_click = """$("#lang-btn").addEventListener("click", () => {
  applyLang(currentLang === "en" ? "ar" : "en");
});"""

new_lang_btn_clicks = """document.querySelectorAll("[data-lang-val]").forEach(btn => {
  btn.addEventListener("click", () => {
    applyLang(btn.dataset.langVal);
  });
});"""

assert old_lang_btn_click in code, "old_lang_btn_click not found"
code = code.replace(old_lang_btn_click, new_lang_btn_clicks)

# 4. Replace Dynamic Island Active Tab Controller with Responsive Sidebar & Quick Bar Controller
old_nav_ctrl = """// Dynamic Island Active Tab Controller
const navTabs = document.querySelectorAll("#main-nav .nav-tab");
function setActiveNavTab(targetId) {
  navTabs.forEach(tab => {
    const isTarget = tab.getAttribute("href") === targetId;
    tab.classList.toggle("active", isTarget);
    if (isTarget) {
      tab.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
    }
  });
}

navTabs.forEach(tab => {
  tab.addEventListener("click", () => {
    const href = tab.getAttribute("href");
    if (href && href.startsWith("#")) {
      setActiveNavTab(href);
    }
  });
});

if ("IntersectionObserver" in window) {
  const sectionIds = ["now", "handover", "ci-remote", "ledgers", "waves", "projects", "platforms", "accounts", "workforce", "activity"];
  const sectionEls = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && entry.intersectionRatio >= 0.2) {
        setActiveNavTab("#" + entry.target.id);
      }
    });
  }, { rootMargin: "-10% 0px -65% 0px", threshold: [0.2] });

  sectionEls.forEach(el => navObserver.observe(el));
}"""

new_nav_ctrl = """// Responsive Sidebar Rail & Mobile Quick Bar Controller
const sidebarLinks = document.querySelectorAll(".sidebar-link");
const quickPills = document.querySelectorAll(".quick-pill[href]");

function setActiveNavSection(targetId) {
  sidebarLinks.forEach(link => {
    const isTarget = link.getAttribute("href") === targetId;
    link.classList.toggle("active", isTarget);
  });
  quickPills.forEach(pill => {
    const isTarget = pill.getAttribute("href") === targetId;
    pill.classList.toggle("active", isTarget);
  });
}

sidebarLinks.forEach(link => {
  link.addEventListener("click", () => {
    const href = link.getAttribute("href");
    if (href && href.startsWith("#")) {
      setActiveNavSection(href);
      if (window.innerWidth < 1024) {
        closeSidebarDrawer();
      }
    }
  });
});

quickPills.forEach(pill => {
  pill.addEventListener("click", () => {
    const href = pill.getAttribute("href");
    if (href && href.startsWith("#")) {
      setActiveNavSection(href);
    }
  });
});

if ("IntersectionObserver" in window) {
  const sectionIds = ["now", "handover", "ci-remote", "ledgers", "waves", "projects", "platforms", "accounts", "workforce", "activity"];
  const sectionEls = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && entry.intersectionRatio >= 0.15) {
        setActiveNavSection("#" + entry.target.id);
      }
    });
  }, { rootMargin: "-10% 0px -60% 0px", threshold: [0.15] });

  sectionEls.forEach(el => navObserver.observe(el));
}"""

assert old_nav_ctrl in code, "old_nav_ctrl not found"
code = code.replace(old_nav_ctrl, new_nav_ctrl)

with open(template_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Dashboard template JavaScript successfully upgraded for Round 11!")
