document.getElementById("initTime").innerText = new Date().toLocaleTimeString();

const statusDot = document.getElementById("statusDot");
const statusText = document.getElementById("statusText");
const activeTabInfo = document.getElementById("activeTabInfo");
const logContainer = document.getElementById("logContainer");

async function updateActiveTab() {
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (tab) {
      activeTabInfo.innerText = `${tab.title || "Untitled"}\n${tab.url || ""}`;
    } else {
      activeTabInfo.innerText = "No active tab detected";
    }
  } catch (err) {
    activeTabInfo.innerText = "Error: " + err.message;
  }
}

function appendLog(action, details, timestamp) {
  const item = document.createElement("div");
  item.className = "log-item";
  item.innerHTML = `
    <span class="log-action">${action}</span>
    <span title="${details}">${details.slice(0, 24)}</span>
    <span class="log-time">${timestamp || new Date().toLocaleTimeString()}</span>
  `;
  logContainer.prepend(item);
}

// Listen to service worker broadcasts
chrome.runtime.onMessage.addListener((message) => {
  if (message.type === "ACTIVITY_LOG") {
    const { action, details, timestamp } = message.payload;
    appendLog(action, details, timestamp);
    if (action === "CONNECTED") {
      statusDot.className = "dot connected";
      statusText.innerText = "Bridge Active";
    } else if (action === "DISCONNECTED") {
      statusDot.className = "dot";
      statusText.innerText = "Connecting...";
    }
  }
});

// Query SW status on load
chrome.runtime.sendMessage({ type: "GET_STATUS" }, (res) => {
  if (res && res.connected) {
    statusDot.className = "dot connected";
    statusText.innerText = "Bridge Active";
  } else {
    statusDot.className = "dot";
    statusText.innerText = "Offline (start bridge)";
  }
});

document.getElementById("btnRefreshTab").addEventListener("click", updateActiveTab);
document.getElementById("btnSnapshot").addEventListener("click", async () => {
  appendLog("USER_TEST", "Manual snapshot requested", new Date().toLocaleTimeString());
});

updateActiveTab();
