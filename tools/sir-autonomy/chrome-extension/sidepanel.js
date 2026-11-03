// Antigravity AI Companion & Bridge Engine Side Panel Controller
let activeTab = null;
let isRecognizing = false;
let recognition = null;
let currentEventCount = 0;

// DOM Elements
const tabCompanion = document.getElementById("tabCompanion");
const tabEngine = document.getElementById("tabEngine");
const viewCompanion = document.getElementById("viewCompanion");
const viewEngine = document.getElementById("viewEngine");

const statusDot = document.getElementById("statusDot");
const statusLabel = document.getElementById("statusLabel");
const activeTabBadge = document.getElementById("activeTabBadge");
const engineTabTitle = document.getElementById("engineTabTitle");
const engineTabUrl = document.getElementById("engineTabUrl");
const tabCountBadge = document.getElementById("tabCountBadge");

const chatStream = document.getElementById("chatStream");
const emptyState = document.getElementById("emptyState");
const promptInput = document.getElementById("promptInput");
const btnSend = document.getElementById("btnSend");
const btnMic = document.getElementById("btnMic");
const btnPageContext = document.getElementById("btnPageContext");

const logList = document.getElementById("logList");
const logCount = document.getElementById("logCount");

// View Switching
tabCompanion.addEventListener("click", () => {
  tabCompanion.classList.add("active");
  tabEngine.classList.remove("active");
  viewCompanion.classList.add("active");
  viewEngine.classList.remove("active");
});

tabEngine.addEventListener("click", () => {
  tabEngine.classList.add("active");
  tabCompanion.classList.remove("active");
  viewEngine.classList.add("active");
  viewCompanion.classList.remove("active");
});

// Update active tab display
async function refreshActiveTab() {
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (tab) {
      activeTab = tab;
      const title = tab.title || "Untitled Tab";
      const url = tab.url || "";
      activeTabBadge.innerText = `${title.slice(0, 36)}...`;
      activeTabBadge.title = `${title}\n${url}`;
      engineTabTitle.innerText = title;
      engineTabUrl.innerText = url;
    }
    const allTabs = await chrome.tabs.query({});
    tabCountBadge.innerText = `${allTabs.length} Tabs`;
  } catch (err) {
    activeTabBadge.innerText = "No tab detected";
  }
}

// Activity Logging
function appendLog(cmd, desc) {
  currentEventCount++;
  logCount.innerText = `${currentEventCount} events`;
  const item = document.createElement("div");
  item.className = "log-entry";
  item.innerHTML = `
    <span class="log-cmd">${cmd}</span>
    <span class="log-desc" title="${desc}">${desc.slice(0, 28)}</span>
  `;
  logList.prepend(item);
}

// Check Connection Status
function checkStatus() {
  chrome.runtime.sendMessage({ type: "GET_STATUS" }, (res) => {
    if (res && res.connected) {
      statusDot.className = "dot connected";
      statusLabel.innerText = "Connected";
    } else {
      statusDot.className = "dot";
      statusLabel.innerText = res && res.reconnecting ? "Reconnecting..." : "Offline";
    }
  });
}

// Listen to service worker broadcasts
chrome.runtime.onMessage.addListener((message) => {
  if (message.type === "ACTIVITY_LOG") {
    const { action, details } = message.payload;
    appendLog(action, details);
    if (action === "CONNECTED") {
      statusDot.className = "dot connected";
      statusLabel.innerText = "Connected";
    } else if (action === "DISCONNECTED") {
      statusDot.className = "dot";
      statusLabel.innerText = "Reconnecting...";
    }
  }
});

// Chat Stream Rendering
function appendUserMessage(text) {
  if (emptyState) emptyState.style.display = "none";
  const msgDiv = document.createElement("div");
  msgDiv.className = "msg user";
  msgDiv.innerHTML = `<div class="msg-bubble">${escapeHtml(text)}</div>`;
  chatStream.appendChild(msgDiv);
  chatStream.scrollTop = chatStream.scrollHeight;
}

function appendAssistantMessage(text, isHtml = false) {
  if (emptyState) emptyState.style.display = "none";
  const msgDiv = document.createElement("div");
  msgDiv.className = "msg assistant";
  const formatted = isHtml ? text : formatMarkdown(text);
  msgDiv.innerHTML = `<div class="msg-bubble">${formatted}</div>`;
  chatStream.appendChild(msgDiv);
  chatStream.scrollTop = chatStream.scrollHeight;
}

function appendTypingIndicator() {
  const indDiv = document.createElement("div");
  indDiv.className = "msg assistant";
  indDiv.id = "typingIndicator";
  indDiv.innerHTML = `<div class="msg-bubble" style="opacity: 0.7;">Thinking... ✦</div>`;
  chatStream.appendChild(indDiv);
  chatStream.scrollTop = chatStream.scrollHeight;
  return indDiv;
}

function removeTypingIndicator() {
  const ind = document.getElementById("typingIndicator");
  if (ind) ind.remove();
}

function escapeHtml(str) {
  return str.replace(/[&<>"']/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[m]);
}

function formatMarkdown(text) {
  let html = escapeHtml(text);
  // Bold
  html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  // Inline code
  html = html.replace(/`([^`]+)`/g, "<code style='background: rgba(255,255,255,0.08); padding: 2px 4px; border-radius: 4px;'>$1</code>");
  // Line breaks
  html = html.replace(/\n/g, "<br>");
  return html;
}

// Send Chat Message
async function sendMessage(customPrompt = null, withPageContext = true) {
  const prompt = (customPrompt || promptInput.value).trim();
  if (!prompt) return;

  promptInput.value = "";
  appendUserMessage(prompt);
  const ind = appendTypingIndicator();

  let pageContext = "";
  if (withPageContext) {
    try {
      const pageRes = await new Promise((resolve) => {
        chrome.runtime.sendMessage({ type: "GET_PAGE_TEXT" }, resolve);
      });
      if (pageRes && pageRes.success) {
        pageContext = pageRes.text;
      }
    } catch (e) {
      // Continue without context
    }
  }

  chrome.runtime.sendMessage({
    type: "ASK_AI",
    payload: {
      prompt: prompt,
      page_context: pageContext,
      model: "qwen2.5:1.5b"
    }
  }, (res) => {
    removeTypingIndicator();
    if (res && res.success) {
      appendAssistantMessage(res.answer);
    } else {
      const err = res ? (res.error || res.fallback || "Bridge server unreachable") : "No response from AI bridge";
      appendAssistantMessage(`⚠️ **Error**: ${err}\n\n*Make sure SIR Autonomy daemon is running.*`);
    }
  });
}

// Voice Recognition
if ("webkitSpeechRecognition" in window) {
  recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = "en-US";

  recognition.onstart = () => {
    isRecognizing = true;
    btnMic.classList.add("listening");
  };

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    promptInput.value = (promptInput.value + " " + transcript).trim();
  };

  recognition.onend = () => {
    isRecognizing = false;
    btnMic.classList.remove("listening");
  };

  recognition.onerror = () => {
    isRecognizing = false;
    btnMic.classList.remove("listening");
  };
}

btnMic.addEventListener("click", () => {
  if (!recognition) {
    alert("Speech recognition not supported in this browser.");
    return;
  }
  if (isRecognizing) {
    recognition.stop();
  } else {
    recognition.start();
  }
});

// Quick Chips
document.getElementById("chipSummarize").addEventListener("click", () => {
  sendMessage("Please provide a concise, high-level summary of the main points on this page.", true);
});

document.getElementById("chipExtract").addEventListener("click", () => {
  sendMessage("Extract all key data points, forms, and actionable links from this page.", true);
});

document.getElementById("chipScreenshot").addEventListener("click", () => {
  chrome.runtime.sendMessage({ type: "RUN_COMMAND", command: "screenshot", params: {} }, (res) => {
    if (res && res.success && res.result.dataUrl) {
      appendUserMessage("Capture tab snapshot");
      appendAssistantMessage(`<div>Captured tab snapshot:</div><img src="${res.result.dataUrl}" style="max-width: 100%; border-radius: 8px; margin-top: 6px; border: 1px solid var(--border);" />`, true);
    } else {
      appendAssistantMessage("⚠️ Failed to capture screenshot");
    }
  });
});

document.getElementById("chipDesktop").addEventListener("click", async () => {
  try {
    appendUserMessage("Full desktop screenshot");
    const ind = appendTypingIndicator();
    const res = await fetch("http://127.0.0.1:18991/computer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "screenshot" })
    });
    removeTypingIndicator();
    const data = await res.json();
    if (data.success && data.result.image_base64) {
      appendAssistantMessage(`<div>Captured interactive Windows desktop:</div><img src="data:image/png;base64,${data.result.image_base64}" style="max-width: 100%; border-radius: 8px; margin-top: 6px; border: 1px solid var(--border);" />`, true);
    } else {
      appendAssistantMessage(`⚠️ Desktop screenshot failed: ${data.error || "Unknown error"}`);
    }
  } catch (err) {
    removeTypingIndicator();
    appendAssistantMessage(`⚠️ Error communicating with bridge: ${err.message}`);
  }
});

// Event Listeners
btnSend.addEventListener("click", () => sendMessage());
promptInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// Engine View Buttons
document.getElementById("btnRefreshActiveTab").addEventListener("click", refreshActiveTab);

document.getElementById("btnInspectSnapshot").addEventListener("click", () => {
  chrome.runtime.sendMessage({ type: "RUN_COMMAND", command: "snapshot", params: { depth: 4 } }, (res) => {
    if (res && res.success) {
      appendLog("SNAPSHOT", `Nodes: ${res.result.snapshot.elements ? res.result.snapshot.elements.length : 0}`);
      tabCompanion.click();
      appendAssistantMessage(`### DOM Snapshot Inspect\n**Title**: ${res.result.title}\n**URL**: ${res.result.url}\n\n\`\`\`json\n${JSON.stringify(res.result.snapshot, null, 2).slice(0, 1500)}...\n\`\`\``);
    }
  });
});

document.getElementById("btnCaptureScreen").addEventListener("click", () => {
  document.getElementById("chipScreenshot").click();
});

document.getElementById("btnListAllTabs").addEventListener("click", () => {
  chrome.runtime.sendMessage({ type: "RUN_COMMAND", command: "tabs_list", params: {} }, (res) => {
    if (res && res.success) {
      appendLog("TABS_LIST", `Found ${res.result.length} tabs`);
      tabCompanion.click();
      let msg = `### Open Browser Tabs (${res.result.length})\n\n`;
      res.result.forEach((t, i) => {
        msg += `${i + 1}. **${t.title}**\n   ${t.url}\n`;
      });
      appendAssistantMessage(msg);
    }
  });
});

document.getElementById("btnDesktopSnap").addEventListener("click", () => {
  document.getElementById("chipDesktop").click();
});

document.getElementById("btnReconnectBridge").addEventListener("click", () => {
  statusLabel.innerText = "Reconnecting...";
  chrome.runtime.sendMessage({ type: "RECONNECT_NOW" }, () => {
    setTimeout(checkStatus, 1000);
  });
});

// Auto-size textarea
promptInput.addEventListener("input", function() {
  this.style.height = "auto";
  this.style.height = (this.scrollHeight) + "px";
});

// Initial boot
refreshActiveTab();
checkStatus();
setInterval(checkStatus, 4000);
