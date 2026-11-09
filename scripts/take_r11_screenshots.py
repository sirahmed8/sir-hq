import subprocess
import tempfile
import os
import shutil

shots = [
    ("r11-control-desktop-en.png", "1440,900", "http://127.0.0.1:8899/dashboard.html"),
    ("r11-control-desktop-ar.png", "1440,900", "http://127.0.0.1:8899/dashboard.html?lang=ar"),
    ("r11-control-settings-en.png", "1440,900", "http://127.0.0.1:8899/dashboard.html?open=settings"),
    ("r11-control-settings-ar.png", "1440,900", "http://127.0.0.1:8899/dashboard.html?lang=ar&open=settings"),
    ("r11-control-mobile-en.png", "390,844", "http://127.0.0.1:8899/dashboard.html"),
    ("r11-control-mobile-ar.png", "390,844", "http://127.0.0.1:8899/dashboard.html?lang=ar"),
    ("r11-control-drawer-mobile.png", "390,844", "http://127.0.0.1:8899/dashboard.html?open=drawer"),
    ("r11-control-drawer-mobile-ar.png", "390,844", "http://127.0.0.1:8899/dashboard.html?lang=ar&open=drawer"),
]

chrome_exe = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
out_dir = "D:/Projects/_SIR/ops"

for fname, dims, url in shots:
    tmp_dir = tempfile.mkdtemp(prefix="chrome_snap_")
    out_path = os.path.join(out_dir, fname)
    cmd = [
        chrome_exe,
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={tmp_dir}",
        f"--window-size={dims}",
        f"--screenshot={out_path}",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=1000",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    size = os.path.getsize(out_path) if os.path.exists(out_path) else 0
    print(f"Captured {fname} ({dims}) -> {size:,} bytes")
    try:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    except Exception:
        pass

print("All screenshots captured successfully!")
