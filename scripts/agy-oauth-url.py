"""Print the newest Antigravity Google OAuth account-chooser URL from Chrome history.

Used when the SIR Autonomy extension is not connected: Antigravity opens the chooser in the owner's Chrome; Chrome writes it to the
History database after a few seconds. This script polls a copy of the database until a URL newer than the given start time
(default: now) appears, then prints it (one line). Usage: python agy-oauth-url.py [seconds_to_wait]
"""
import glob, os, re, shutil, sqlite3, sys, tempfile, time

EPOCH_DIFF = 11644473600  # seconds between 1601 and 1970


def newest(after_chrome_time: int):
    base = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    best = (0, "")
    for hist in glob.glob(base + r"\*\History"):
        tmp = os.path.join(tempfile.gettempdir(), "agy_hist_copy.db")
        try:
            shutil.copy(hist, tmp)
            con = sqlite3.connect(tmp)
            rows = con.execute(
                "select url,last_visit_time from urls where url like '%accountchooser%redirect_uri%' "
                "order by last_visit_time desc limit 1").fetchall()
            con.close()
        except Exception:
            continue
        for url, ts in rows:
            if ts > best[0]:
                best = (ts, url)
    return best if best[0] > after_chrome_time else (0, "")


def main() -> int:
    wait = int(sys.argv[1]) if len(sys.argv) > 1 else 90
    start = int((time.time() - 5 + EPOCH_DIFF) * 1_000_000)
    deadline = time.time() + wait
    while time.time() < deadline:
        ts, url = newest(start)
        if url:
            port = re.search(r"localhost%3A(\d+)", url)
            sys.stderr.write(f"port {port.group(1) if port else '?'}\n")
            print(url)
            return 0
        time.sleep(3)
    sys.stderr.write("no new chooser URL found\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
