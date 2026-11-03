// SIR Autonomy - Background Service Worker (Hardened Connection Engine)
const BRIDGE_WS_URL = "ws://127.0.0.1:18991/ws";
const BRIDGE_HEALTH_URL = "http://127.0.0.1:18991/health";
const BRIDGE_ASK_URL = "http://127.0.0.1:18991/ask";

let ws = null;
let reconnectTimer = null;
let isConnecting = false;
let isConnected = false;
let reconnectAttempts = 0;

// Setup side panel behavior
chrome.runtime.onInstalled.addListener(() => {
  chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch(() => {});
  ensureOffscreen();
  connectToBridge();
});

chrome.runtime.onStartup.addListener(() => {
  ensureOffscreen();
  connectToBridge();
});

// Ensure offscreen keepalive exists
async function ensureOffscreen() {
  try {
    const hasDoc = await chrome.offscreen.hasDocument();
    if (!hasDoc) {
      await chrome.offscreen.createDocument({
        url: "offscreen.html",
        reasons: ["BLOBS"],
        justification: "Maintain connection to local agent daemon"
      });
    }
  } catch (err) {
    // Already active
  }
}

// Broadcast log to sidepanel
function logEvent(action, details) {
  chrome.runtime.sendMessage({
    type: "ACTIVITY_LOG",
    payload: { action, details, timestamp: new Date().toLocaleTimeString() }
  }).catch(() => {});
}

// Health probe before attempting WebSocket
async function isBridgeHealthy() {
  try {
    const controller = new AbortController();
    const id = setTimeout(() => controller.abort(), 1200);
    const res = await fetch(BRIDGE_HEALTH_URL, {
      method: "GET",
      signal: controller.signal,
      cache: "no-store"
    }).catch(() => null);
    clearTimeout(id);
    return Boolean(res && res.ok);
  } catch {
    return false;
  }
}

// Connect to local bridge daemon
async function connectToBridge() {
  if (ws && (ws.readyState === WebSocket.OPEN || ws.readyState === WebSocket.CONNECTING)) {
    return;
  }
  if (isConnecting) return;
  isConnecting = true;

  const healthy = await isBridgeHealthy();
  if (!healthy) {
    isConnecting = false;
    if (isConnected) {
      isConnected = false;
      logEvent("STATUS", "Bridge daemon offline on 127.0.0.1:18991");
    }
    scheduleReconnect();
    return;
  }

  try {
    ws = new WebSocket(BRIDGE_WS_URL);
    if (ws.addEventListener) {
      ws.addEventListener("error", () => {
        try { if (ws) ws.close(); } catch {}
        ws = null;
        isConnecting = false;
      });
    }
  } catch (e) {
    isConnecting = false;
    scheduleReconnect();
    return;
  }

  ws.onopen = () => {
    isConnecting = false;
    isConnected = true;
    reconnectAttempts = 0;
    logEvent("CONNECTED", "Bridge connected at " + BRIDGE_WS_URL);
    ws.send(JSON.stringify({
      type: "register",
      client: "sir_chrome_extension",
      version: "1.0.0"
    }));
  };

  ws.onmessage = async (event) => {
    let msg;
    try {
      msg = JSON.parse(event.data);
    } catch (e) {
      return;
    }

    const { id, command, params } = msg;
    try {
      const result = await handleCommand(command, params || {});
      logEvent(command.toUpperCase(), "Success");
      ws.send(JSON.stringify({ id, success: true, result }));
    } catch (err) {
      logEvent(command.toUpperCase(), "Error: " + err.message);
      ws.send(JSON.stringify({ id, success: false, error: err.message }));
    }
  };

  ws.onclose = () => {
    isConnecting = false;
    ws = null;
    if (isConnected) {
      isConnected = false;
      logEvent("DISCONNECTED", "Connection closed, retrying...");
    }
    scheduleReconnect();
  };

  ws.onerror = () => {
    try {
      if (ws) ws.close();
    } catch {}
    ws = null;
    isConnecting = false;
  };
}

function scheduleReconnect() {
  if (reconnectTimer) clearTimeout(reconnectTimer);
  reconnectAttempts++;
  // If bridge daemon is offline, do NOT spam reconnects to keep Chrome extensions error badge completely clean.
  // Connection will resume cleanly when user opens the side panel or clicks reconnect.
  if (reconnectAttempts > 1) {
    isConnecting = false;
    return;
  }
  reconnectTimer = setTimeout(() => {
    connectToBridge();
  }, 5000);
}

// Target tab resolution
async function getTargetTab(tabId) {
  if (tabId) {
    return await chrome.tabs.get(tabId);
  }
  const [activeTab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (activeTab) return activeTab;
  const [anyActive] = await chrome.tabs.query({ active: true });
  if (anyActive) return anyActive;
  const [firstTab] = await chrome.tabs.query({});
  if (firstTab) return firstTab;
  throw new Error("No browser tab available");
}

// Inject DOM engine if needed
async function ensureEngineInjected(tabId) {
  try {
    await chrome.scripting.executeScript({
      target: { tabId },
      files: ["content-dom.js"]
    });
  } catch (err) {
    throw new Error(`Failed to inject DOM engine into tab ${tabId}: ${err.message}`);
  }
}

// Extract page text for AI companion
async function extractPageText(tabId) {
  try {
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId },
      func: () => {
        const title = document.title || "";
        const url = window.location.href;
        const bodyText = document.body ? (document.body.innerText || "") : "";
        return `Title: ${title}\nURL: ${url}\n\nContent:\n${bodyText.slice(0, 10000)}`;
      }
    });
    return result;
  } catch (err) {
    return `Error reading page: ${err.message}`;
  }
}

// Command dispatcher
async function handleCommand(cmd, params) {
  switch (cmd) {
    case "tabs_list": {
      const tabs = await chrome.tabs.query({});
      return tabs.map(t => ({
        id: t.id,
        title: t.title,
        url: t.url,
        active: t.active,
        windowId: t.windowId
      }));
    }

    case "tab_new": {
      const tab = await chrome.tabs.create({ url: params.url || "about:blank" });
      return { id: tab.id, url: tab.url };
    }

    case "tab_close": {
      const tab = await getTargetTab(params.tabId);
      await chrome.tabs.remove(tab.id);
      return { closed: tab.id };
    }

    case "tab_activate": {
      const tab = await getTargetTab(params.tabId);
      await chrome.tabs.update(tab.id, { active: true });
      await chrome.windows.update(tab.windowId, { focused: true });
      return { activated: tab.id };
    }

    case "navigate": {
      const tab = await getTargetTab(params.tabId);
      const url = params.url;
      await chrome.tabs.update(tab.id, { url });
      return { tabId: tab.id, url };
    }

    case "snapshot": {
      const tab = await getTargetTab(params.tabId);
      await ensureEngineInjected(tab.id);
      const [{ result }] = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (opts) => window.__sirGenerateSnapshot(opts),
        args: [params]
      });
      return { tabId: tab.id, title: tab.title, url: tab.url, snapshot: result };
    }

    case "click": {
      const tab = await getTargetTab(params.tabId);
      await ensureEngineInjected(tab.id);
      const [{ result }] = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (target) => window.__sirClick(target),
        args: [params.target]
      });
      return result;
    }

    case "fill": {
      const tab = await getTargetTab(params.tabId);
      await ensureEngineInjected(tab.id);
      const [{ result }] = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (target, val) => window.__sirFill(target, val),
        args: [params.target, params.value || ""]
      });
      return result;
    }

    case "scroll": {
      const tab = await getTargetTab(params.tabId);
      await ensureEngineInjected(tab.id);
      const [{ result }] = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (target, dx, dy) => window.__sirScroll(target, dx, dy),
        args: [params.target, params.dx || 0, params.dy || 300]
      });
      return result;
    }

    case "eval": {
      const tab = await getTargetTab(params.tabId);
      const expr = params.expression;
      const [{ result }] = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (code) => {
          return window.eval(code);
        },
        args: [expr]
      });
      return { result };
    }

    case "screenshot": {
      const tab = await getTargetTab(params.tabId);
      await chrome.tabs.update(tab.id, { active: true });
      const dataUrl = await chrome.tabs.captureVisibleTab(tab.windowId, { format: "png" });
      return { tabId: tab.id, dataUrl };
    }

    default:
      throw new Error(`Unknown command: ${cmd}`);
  }
}

// Runtime message listener for Side Panel UI & Keepalive
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "SW_KEEPALIVE") {
    sendResponse({ status: "alive", time: Date.now() });
    return true;
  }

  if (message.type === "GET_STATUS") {
    sendResponse({
      connected: ws && ws.readyState === WebSocket.OPEN,
      url: BRIDGE_WS_URL,
      reconnecting: isConnecting
    });
    return true;
  }

  if (message.type === "RECONNECT_NOW") {
    reconnectAttempts = 0;
    connectToBridge();
    sendResponse({ status: "initiated" });
    return true;
  }

  if (message.type === "GET_PAGE_TEXT") {
    (async () => {
      try {
        const tab = await getTargetTab();
        const text = await extractPageText(tab.id);
        sendResponse({ success: true, text, title: tab.title, url: tab.url });
      } catch (e) {
        sendResponse({ success: false, error: e.message });
      }
    })();
    return true;
  }

  if (message.type === "RUN_COMMAND") {
    (async () => {
      try {
        const result = await handleCommand(message.command, message.params || {});
        sendResponse({ success: true, result });
      } catch (e) {
        sendResponse({ success: false, error: e.message });
      }
    })();
    return true;
  }

  if (message.type === "ASK_AI") {
    (async () => {
      try {
        const res = await fetch(BRIDGE_ASK_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(message.payload)
        });
        const data = await res.json();
        sendResponse(data);
      } catch (err) {
        sendResponse({ success: false, error: err.message });
      }
    })();
    return true;
  }
});

// Initial startup
connectToBridge();
ensureOffscreen();
