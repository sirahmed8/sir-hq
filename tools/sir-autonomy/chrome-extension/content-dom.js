// SIR Autonomy - Page DOM & Accessibility Engine
(() => {
  if (window.__sirDOMInitialized) return;
  window.__sirDOMInitialized = true;

  window.__sirElementMap = new Map();
  let refCounter = 1;

  function isElementVisible(el) {
    if (!el || el.nodeType !== Node.ELEMENT_NODE) return false;
    const style = window.getComputedStyle(el);
    if (style.display === "none" || style.visibility === "hidden" || style.opacity === "0") return false;
    const rect = el.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  }

  function isInteractive(el) {
    const tag = el.tagName.toLowerCase();
    const role = el.getAttribute("role");
    if (["a", "button", "input", "select", "textarea"].includes(tag)) return true;
    if (["button", "link", "checkbox", "radio", "tab", "menuitem", "switch"].includes(role)) return true;
    if (el.hasAttribute("onclick") || el.getAttribute("tabindex") === "0") return true;
    return false;
  }

  function isSensitive(el) {
    const type = (el.getAttribute("type") || "").toLowerCase();
    const name = (el.getAttribute("name") || "").toLowerCase();
    const id = (el.getAttribute("id") || "").toLowerCase();
    const autocomplete = (el.getAttribute("autocomplete") || "").toLowerCase();
    return (
      type === "password" ||
      autocomplete.includes("password") ||
      autocomplete.includes("cc-number") ||
      autocomplete.includes("cc-csc") ||
      autocomplete.includes("one-time-code") ||
      name.includes("password") ||
      name.includes("cvv") ||
      id.includes("password")
    );
  }

  function resolveSel(sel) {
    if (!sel) return document.activeElement;
    try { return document.querySelector(sel); } catch (e) { return null; }
  }

  function dispatchKey(el, opts) {
    const key = opts.key || "Enter";
    const code = opts.code || key;
    const keyCode = opts.keyCode || (key === "Enter" ? 13 : key.length === 1 ? key.toUpperCase().charCodeAt(0) : 0);
    const which = opts.which || keyCode;
    const init = { key, code, keyCode, which, bubbles: true, cancelable: true, composed: true };
    el.dispatchEvent(new KeyboardEvent("keydown", init));
    el.dispatchEvent(new KeyboardEvent("keypress", init));
    el.dispatchEvent(new KeyboardEvent("keyup", init));
    return "key:" + key;
  }

  window.__sirActs = {
    focus(opts) {
      const el = resolveSel(opts.sel);
      if (!el) return "no-el";
      el.scrollIntoView({ block: "center" });
      el.focus();
      return el.tagName + "." + (el.className || "").toString().slice(0, 60);
    },
    active(opts) {
      const el = document.activeElement;
      return el ? el.tagName + "|" + (el.className || "").toString().slice(0, 80) + "|" + (el.id || "") : "none";
    },
    key(opts) {
      const el = resolveSel(opts.sel) || document.activeElement;
      if (!el) return "no-el";
      return dispatchKey(el, opts);
    },
    setText(opts) {
      const el = resolveSel(opts.sel);
      if (!el) return "no-el";
      el.focus();
      el.value = opts.text || "";
      el.dispatchEvent(new Event("input", { bubbles: true }));
      el.dispatchEvent(new Event("change", { bubbles: true }));
      return "set:" + (el.value || "").length;
    },
    cmSet(opts) {
      const el = resolveSel(opts.sel);
      if (!el) return "no-el";
      el.focus();
      el.value = opts.text || "";
      el.dispatchEvent(new InputEvent("input", { bubbles: true, inputType: "insertText", data: opts.text || "" }));
      return "cmset:" + el.value.length;
    },
    text(opts) {
      const el = resolveSel(opts.sel);
      if (!el) return "no-el";
      if ("value" in el) return String(el.value);
      return el.textContent || "";
    },
    cmText(opts) {
      const root = resolveSel(opts.sel) || document;
      const cms = root.querySelectorAll ? root.querySelectorAll(".CodeMirror") : [];
      const out = [];
      cms.forEach((cm) => {
        const pre = cm.querySelector(".CodeMirror-code");
        out.push(pre ? pre.textContent : "");
      });
      return JSON.stringify(out);
    },
    clickEl(opts) {
      const el = resolveSel(opts.sel);
      if (!el) return "no-el";
      el.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, cancelable: true }));
      el.focus();
      el.dispatchEvent(new MouseEvent("mouseup", { bubbles: true, cancelable: true }));
      el.click();
      return "clicked";
    },
  };

  window.__sirGenerateSnapshot = function(opts = {}) {
    window.__sirElementMap.clear();
    refCounter = 1;

    if (opts.act) {
      try {
        const acts = window.__sirActs;
        const fn = acts && acts[opts.act];
        if (!fn) return JSON.stringify({ ok: false, e: "unknown act " + opts.act });
        const v = fn(opts);
        return JSON.stringify({ ok: true, v: String(v) });
      } catch (e) {
        return JSON.stringify({ ok: false, e: String(e && e.message || e) });
      }
    }
    if (opts.exec) {
      return "CSP-BLOCKED";
    }
    if (opts.dumpCookies) {
      return document.cookie || "";
    }
    if (opts.dumpLS) {
      try {
        const out = {};
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i);
          out[k] = localStorage.getItem(k);
        }
        return JSON.stringify(out);
      } catch (e) {
        return "ERR:" + e.message;
      }
    }
    if (opts.dumpHTML) {
      const root = document.documentElement;
      return root ? root.outerHTML.slice(0, opts.maxChars || 400000) : "";
    }

    const maxChars = opts.maxChars || 40000;
    let output = `# Page: ${document.title}\n# URL: ${window.location.href}\n\n`;

    function walk(node, depth = 0) {
      if (!node || output.length > maxChars) return;
      if (node.nodeType === Node.TEXT_NODE) {
        const text = node.textContent.trim();
        if (text) {
          output += `${"  ".repeat(depth)}${text}\n`;
        }
        return;
      }
      if (node.nodeType !== Node.ELEMENT_NODE) return;
      if (!isElementVisible(node)) return;

      const tag = node.tagName.toLowerCase();
      if (["script", "style", "noscript", "svg"].includes(tag)) return;

      if (isInteractive(node)) {
        const ref = `ref_${refCounter++}`;
        window.__sirElementMap.set(ref, node);

        let label = (
          node.innerText ||
          node.getAttribute("aria-label") ||
          node.getAttribute("placeholder") ||
          node.getAttribute("value") ||
          node.getAttribute("title") ||
          ""
        ).trim().replace(/\s+/g, " ");

        if (isSensitive(node)) {
          label = "[REDACTED_SENSITIVE_INPUT]";
        }

        const role = node.getAttribute("role") || tag;
        const disabled = node.disabled ? " (disabled)" : "";
        output += `${"  ".repeat(depth)}[${ref}] <${role}> ${label}${disabled}\n`;
        return;
      }

      // Headings & landmarks
      if (/^h[1-6]$/.test(tag)) {
        const text = node.innerText.trim();
        if (text) {
          output += `${"  ".repeat(depth)}${"#".repeat(parseInt(tag[1]))} ${text}\n`;
        }
        return;
      }

      for (const child of node.childNodes) {
        walk(child, depth + 1);
      }
    }

    walk(document.body);
    return output;
  };

  window.__sirResolveElement = function(target) {
    if (!target) return null;
    if (typeof target === "string") {
      let key = target.trim();
      if (key.startsWith("[") && key.endsWith("]")) {
        key = key.slice(1, -1);
      }
      if (!key.startsWith("ref_") && /^\d+$/.test(key)) {
        key = `ref_${key}`;
      }
      if (window.__sirElementMap.has(key)) {
        return window.__sirElementMap.get(key);
      }
      // Try CSS selector
      try {
        const el = document.querySelector(target);
        if (el) return el;
      } catch (e) {}
    }
    return null;
  };

  function flashIndicator(el) {
    if (!el || !el.style) return;
    const oldOutline = el.style.outline;
    const oldTransition = el.style.transition;
    el.style.transition = "outline 0.15s ease";
    el.style.outline = "2px solid #38bdf8";
    setTimeout(() => {
      el.style.outline = oldOutline;
      el.style.transition = oldTransition;
    }, 450);
  }

  window.__sirClick = function(target) {
    const el = window.__sirResolveElement(target);
    if (!el) throw new Error(`Element not found for target: ${target}`);
    flashIndicator(el);
    el.scrollIntoView({ behavior: "smooth", block: "center" });
    el.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, cancelable: true }));
    el.focus();
    el.dispatchEvent(new MouseEvent("mouseup", { bubbles: true, cancelable: true }));
    el.click();
    return { success: true, target, tagName: el.tagName };
  };

  window.__sirFill = function(target, value) {
    const el = window.__sirResolveElement(target);
    if (!el) throw new Error(`Element not found for target: ${target}`);
    flashIndicator(el);
    el.scrollIntoView({ behavior: "smooth", block: "center" });
    el.focus();
    if (el.isContentEditable) {
      el.textContent = value;
      el.dispatchEvent(new InputEvent("input", { bubbles: true }));
    } else {
      el.value = value;
      el.dispatchEvent(new Event("input", { bubbles: true }));
      el.dispatchEvent(new Event("change", { bubbles: true }));
    }
    return { success: true, target, length: value.length };
  };

  window.__sirScroll = function(target, dx = 0, dy = 300) {
    if (target && target !== "window") {
      const el = window.__sirResolveElement(target);
      if (el) {
        el.scrollBy({ left: dx, top: dy, behavior: "smooth" });
        return { success: true, scrolled: "element", dx, dy };
      }
    }
    window.scrollBy({ left: dx, top: dy, behavior: "smooth" });
    return { success: true, scrolled: "window", dx, dy };
  };
})();
