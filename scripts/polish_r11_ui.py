template_path = "D:/Projects/_SIR/plans/dashboard_template.html"

with open(template_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Fix header menu toggle button specificity
old_menu_btn_css = """.menu-toggle-btn {
  display: none;
}
@media (max-width: 1023px) {
  .menu-toggle-btn {
    display: inline-flex;
  }
}"""

new_menu_btn_css = """.header-actions .menu-toggle-btn {
  display: none !important;
}
@media (max-width: 1023px) {
  .header-actions .menu-toggle-btn {
    display: inline-flex !important;
  }
}"""

if old_menu_btn_css in text:
    text = text.replace(old_menu_btn_css, new_menu_btn_css)
    print("Fixed header menu toggle button specificity.")

# 2. Fix sidebar drawer positioning for LTR and RTL
old_sidebar_mobile_css = """  .sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    inset-inline-start: 0;
    width: 280px;
    z-index: 100;
    background: var(--surface);
    border-inline-end: 1px solid var(--line);
    border-radius: 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    padding: 16px;
    transform: translateX(-100%);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  [dir="rtl"] .sidebar {
    transform: translateX(100%);
  }
  .sidebar.open {
    transform: translateX(0) !important;
  }"""

new_sidebar_mobile_css = """  .sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: auto;
    width: 285px;
    z-index: 100;
    background: var(--surface);
    border-right: 1px solid var(--line);
    border-left: none;
    border-radius: 0;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    padding: 16px;
    transform: translateX(-100%);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  [dir="rtl"] .sidebar {
    left: auto;
    right: 0;
    border-left: 1px solid var(--line);
    border-right: none;
    transform: translateX(100%);
  }
  .sidebar.open {
    transform: translateX(0) !important;
  }"""

if old_sidebar_mobile_css in text:
    text = text.replace(old_sidebar_mobile_css, new_sidebar_mobile_css)
    print("Fixed sidebar mobile positioning for LTR/RTL.")

# 3. Compact quick pills on mobile for 390px viewport
old_quick_pill_css = """.quick-pill {
  flex: 1 1 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 44px;
  padding: 8px 12px;
  border-radius: 10px;
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--muted);
  font: 600 12px var(--f-display);
  text-decoration: none;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  user-select: none;
}"""

new_quick_pill_css = """.quick-pill {
  flex: 1 1 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  min-height: 44px;
  padding: 8px 8px;
  border-radius: 10px;
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--muted);
  font: 600 11.5px var(--f-display);
  text-decoration: none;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  user-select: none;
}"""

if old_quick_pill_css in text:
    text = text.replace(old_quick_pill_css, new_quick_pill_css)
    print("Polished quick pill sizing.")

# 4. Update short labels for quick pills in i18n
text = text.replace('    moreNav: "More",', '    moreNav: "More",\n    qpNow: "Now",\n    qpHandover: "Handover",\n    qpCi: "CI",\n    qpProjects: "Projects",')
text = text.replace('    moreNav: "المزيد",', '    moreNav: "المزيد",\n    qpNow: "الآن",\n    qpHandover: "التسليم",\n    qpCi: "الفحص",\n    qpProjects: "المشاريع",')

# 5. In applyLang, assign the concise labels to the quick pills
old_qp_apply = """  if ($("#qp-now-text")) $("#qp-now-text").textContent = t.navNow;
  if ($("#qp-handover-text")) $("#qp-handover-text").textContent = t.navHandover;
  if ($("#qp-ci-text")) $("#qp-ci-text").textContent = t.navCi;
  if ($("#qp-projects-text")) $("#qp-projects-text").textContent = t.navProjects;"""

new_qp_apply = """  if ($("#qp-now-text")) $("#qp-now-text").textContent = t.qpNow || t.navNow;
  if ($("#qp-handover-text")) $("#qp-handover-text").textContent = t.qpHandover || "Handover";
  if ($("#qp-ci-text")) $("#qp-ci-text").textContent = t.qpCi || "CI";
  if ($("#qp-projects-text")) $("#qp-projects-text").textContent = t.qpProjects || "Projects";"""

if old_qp_apply in text:
    text = text.replace(old_qp_apply, new_qp_apply)
    print("Updated applyLang quick pill concise labels.")

with open(template_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Polish script executed successfully!")
