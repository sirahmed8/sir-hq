// Keeps the Manifest V3 service worker alive 24/7 (modeled after Claude in Chrome)
setInterval(() => {
  chrome.runtime.sendMessage({ type: "SW_KEEPALIVE" }).catch(() => {
    // Service worker may be momentarily restarting
  });
}, 20000);
