"""Browser half of an Antigravity account switch (used after 'Continue with Google' was clicked in the app).

Usage: python agy-chooser.py <email>
Finds the Google account-chooser tab opened by Antigravity (through the SIR Autonomy bridge and its Chrome extension),
clicks the account with that email, then clicks 'Sign in' on the 'Make sure that you downloaded this app' page.
No password is typed: it only works for accounts that are already signed in in this Chrome.
Prints OK <email> when Google shows 'successfully authenticated', otherwise a reason and exit code 1.
"""
import json, subprocess, sys, time

PY = "D:/Projects/_SIR/tools/sir-autonomy/.venv/Scripts/python.exe"
CTL = "D:/Projects/_SIR/tools/sir-autonomy/sir_ctl.py"


def ctl(*args):
    out = subprocess.run([PY, CTL, *args], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    return json.loads(out)


def find_tab():
    for t in ctl("browser", "tabs")["result"]:
        if "accounts.google.com" in t["url"] and ("accountchooser" in t["url"] or "oauth" in t["url"]):
            return t["id"]
    for t in ctl("browser", "tabs")["result"]:
        if "antigravity.google" in t["url"]:
            return t["id"]
    return None


def snap(tab):
    return ctl("browser", "snapshot", str(tab))["result"]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    email = sys.argv[1].lower()
    tab = None
    for _ in range(20):
        tab = find_tab()
        if tab:
            break
        time.sleep(1.5)
    if not tab:
        print("no Google sign-in tab found (did you click 'Continue with Google' in Antigravity?)")
        return 1
    for _ in range(6):
        s = snap(tab)
        text = s["snapshot"]
        if "successfully authenticated" in text:
            print("OK", email)
            return 0
        lines = text.split("\n")
        if "Choose an account" in text:
            ref = next((l.split("]")[0].split("[")[1] for l in lines if email in l.lower() and "<link>" in l), None)
            if not ref:
                print("account not in the chooser:", email)
                return 1
            ctl("browser", "click", ref, str(tab))
        elif "Make sure that you downloaded this app" in text:
            ref = next((l.split("]")[0].split("[")[1] for l in lines if "<button> Sign in" in l), None)
            if not ref:
                print("no Sign in button")
                return 1
            ctl("browser", "click", ref, str(tab))
        elif "password" in text.lower() or "2-step" in text.lower() or "verify it" in text.lower():
            print("Google asks for a password or 2FA: this part needs the owner")
            return 1
        time.sleep(3)
    print("did not reach the success page")
    return 1


if __name__ == "__main__":
    sys.exit(main())
