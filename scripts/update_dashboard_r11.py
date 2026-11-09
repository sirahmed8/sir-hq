import re

template_path = "D:/Projects/_SIR/plans/dashboard_template.html"

with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Header Actions
old_header_actions = """    <div class="header-actions">
      <button id="lang-btn" class="fb" aria-label="Toggle language">العربية</button>
      <button id="theme-btn" class="fb" aria-label="Toggle theme">Dark</button>
      <div class="sub num" id="stamp"></div>
      <span class="pill bad" id="offline-pill" style="display:none;font-size:11px;padding:2px 6px">Offline</span>
    </div>"""

new_header_actions = """    <div class="header-actions">
      <button id="menu-toggle-btn" class="fb menu-toggle-btn" aria-label="Open navigation drawer" aria-expanded="false" aria-controls="app-sidebar">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        <span id="txt-menu-btn">Menu</span>
      </button>
      <button id="settings-btn" class="fb settings-trigger-btn" aria-label="Settings and preferences" aria-expanded="false" aria-controls="settings-modal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        <span id="txt-settings-btn">Settings</span>
      </button>
      <div class="sub num" id="stamp"></div>
      <span class="pill bad" id="offline-pill" style="display:none;font-size:11px;padding:2px 6px">Offline</span>
    </div>"""

assert old_header_actions in html, "old_header_actions not found"
html = html.replace(old_header_actions, new_header_actions)

# 2. Add Settings modal, Mobile Quick Bar, Drawer Backdrop, App Layout and Sidebar
# We replace old <nav aria-label="Sections" id="main-nav"> ... </nav> with the new structure
nav_pattern = re.compile(r'\s*<nav aria-label="Sections" id="main-nav">.*?</nav>', re.DOTALL)
assert nav_pattern.search(html), "main-nav not found"

middle_structure = """
  <!-- Settings Popover Dialog -->
  <div id="settings-backdrop" class="modal-backdrop" aria-hidden="true"></div>
  <div id="settings-modal" class="settings-dialog" role="dialog" aria-modal="true" aria-labelledby="settings-title">
    <div class="settings-header">
      <h3 id="settings-title" style="margin:0;font-size:14px;font-weight:600;letter-spacing:0.02em">Settings &amp; Preferences</h3>
      <button id="settings-close-btn" class="settings-close-btn" aria-label="Close settings">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="settings-body">
      <div class="settings-group">
        <div class="settings-group-title" id="txt-set-appearance">Appearance</div>
        <div class="segmented-control" role="group" aria-label="Theme selection">
          <button class="seg-btn" data-theme-val="light" id="theme-btn-light">Light</button>
          <button class="seg-btn" data-theme-val="dark" id="theme-btn-dark">Dark</button>
          <button class="seg-btn" data-theme-val="system" id="theme-btn-system">System</button>
        </div>
      </div>
      <div class="settings-group">
        <div class="settings-group-title" id="txt-set-language">Language &amp; Direction</div>
        <div class="segmented-control" role="group" aria-label="Language selection">
          <button class="seg-btn" data-lang-val="en" id="lang-btn-en">English (LTR)</button>
          <button class="seg-btn" data-lang-val="ar" id="lang-btn-ar">العربية (RTL)</button>
        </div>
      </div>
      <div class="settings-group">
        <div class="settings-group-title" id="txt-set-density">Display Density</div>
        <div class="segmented-control" role="group" aria-label="Density selection">
          <button class="seg-btn active" data-density-val="comfortable" id="density-btn-comfort">Comfortable</button>
          <button class="seg-btn" data-density-val="compact" id="density-btn-compact">Compact</button>
        </div>
      </div>
      <div class="settings-group">
        <div class="settings-group-title" id="txt-set-telemetry">Telemetry &amp; Sync</div>
        <div style="font-size:12px;color:var(--muted);display:flex;flex-direction:column;gap:5px;margin-bottom:10px">
          <div><span id="txt-hash-lbl">Artifact Hash:</span> <bdi class="hash" id="set-artifact-hash"></bdi></div>
          <div><span id="txt-git-lbl">Git:</span> <bdi class="hash" id="set-git-hash"></bdi></div>
        </div>
        <button id="set-refresh-btn" class="fb" style="width:100%;justify-content:center;gap:8px">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
          <span id="txt-refresh-now">Refresh Telemetry Now</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Quick Navigation Bar (Top 4 sections + More) -->
  <nav class="mobile-quick-bar" aria-label="Quick navigation">
    <a href="#now" class="quick-pill active" id="qp-now"><span id="qp-now-text">Now</span></a>
    <a href="#handover" class="quick-pill" id="qp-handover"><span id="qp-handover-text">Handover</span></a>
    <a href="#ci-remote" class="quick-pill" id="qp-ci"><span id="qp-ci-text">CI</span></a>
    <a href="#projects" class="quick-pill" id="qp-projects"><span id="qp-projects-text">Projects</span></a>
    <button id="mobile-menu-trigger" class="quick-pill menu-btn" aria-label="Open full navigation drawer" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="14" height="14" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      <span id="txt-qp-more">More</span>
    </button>
  </nav>

  <div id="drawer-backdrop" class="drawer-backdrop" aria-hidden="true"></div>

  <!-- App Layout: Responsive Sidebar Rail + Main Content Area -->
  <div class="app-layout">
    <aside id="app-sidebar" class="sidebar" aria-label="Main Navigation">
      <div class="sidebar-header">
        <h3 id="txt-nav-title" style="margin:0;font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--muted)">Navigation</h3>
        <button id="drawer-close-btn" class="drawer-close-btn" aria-label="Close navigation drawer">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <nav class="sidebar-nav">
        <a href="#now" id="side-now" class="sidebar-link active">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <span id="side-now-text">Now</span>
        </a>
        <a href="#handover" id="side-handover" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          <span id="side-handover-text">Gemini Handover</span>
        </a>
        <a href="#ci-remote" id="side-ci" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/></svg>
          <span id="side-ci-text">CI &amp; Remote</span>
        </a>
        <a href="#ledgers" id="side-ledgers" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          <span id="side-ledgers-text">Ledgers</span>
        </a>
        <a href="#waves" id="side-waves" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          <span id="side-waves-text">Waves</span>
        </a>
        <a href="#projects" id="side-projects" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          <span id="side-projects-text">Projects</span>
        </a>
        <a href="#platforms" id="side-platforms" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          <span id="side-platforms-text">Platforms</span>
        </a>
        <a href="#accounts" id="side-accounts" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <span id="side-accounts-text">Accounts</span>
        </a>
        <a href="#workforce" id="side-workforce" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <span id="side-workforce-text">Workforce</span>
        </a>
        <a href="#activity" id="side-activity" class="sidebar-link">
          <svg class="sidebar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          <span id="side-activity-text">Activity</span>
        </a>
      </nav>
    </aside>

    <main class="main-content">
"""

html = nav_pattern.sub(middle_structure, html, count=1)

# 3. Close <main> and .app-layout right before </div><!-- /.wrap --> and <script>
old_end_pattern = """  <section id="activity" class="panel">
    <h2 id="txt-act-title">Latest activity</h2>
    <div class="log" id="log"></div>
  </section>
</div>

<script>"""

new_end_structure = """  <section id="activity" class="panel">
    <h2 id="txt-act-title">Latest activity</h2>
    <div class="log" id="log"></div>
  </section>
    </main>
  </div>
</div>

<script>"""

assert old_end_pattern in html, "old_end_pattern not found"
html = html.replace(old_end_pattern, new_end_structure)

# 4. Check CSS additions for buttons and pills
css_additions = """
/* Mobile Quick Bar pills */
.quick-pill {
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
}
.quick-pill:hover {
  color: var(--ink);
  border-color: var(--accent);
}
.quick-pill:active {
  transform: scale(0.97);
}
.quick-pill.active {
  color: var(--accent);
  border-color: var(--accent);
  background: var(--accent-soft);
}
.quick-pill.menu-btn {
  flex: 0 0 auto;
  padding: 8px 14px;
}
.menu-toggle-btn {
  display: none;
}
@media (max-width: 1023px) {
  .menu-toggle-btn {
    display: inline-flex;
  }
}
.settings-trigger-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.settings-close-btn, .drawer-close-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  min-width: 44px;
  min-height: 44px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--bg);
  color: var(--muted);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.settings-close-btn:hover, .drawer-close-btn:hover {
  color: var(--ink);
  background: var(--surface);
}
.settings-close-btn:active, .drawer-close-btn:active {
  transform: scale(0.95);
}
"""

if "/* Mobile Quick Bar pills */" not in html:
    html = html.replace("/* Grids & Cards */", css_additions + "\n/* Grids & Cards */")

with open(template_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML structure updated successfully!")
