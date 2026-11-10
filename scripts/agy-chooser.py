"""Browser half of an Antigravity account switch (used after 'Continue with Google' was clicked in the app).

Usage: python agy-chooser.py <email> [--dry-run]
Finds the Google account-chooser tab opened by Antigravity (through the SIR Autonomy bridge and its Chrome extension),
validates the email against strict owner account guardrails, clicks the account with that email,
then clicks 'Sign in' on the 'Make sure that you downloaded this app' page.
No password is typed: it only works for accounts that are already signed in in this Chrome.
Prints OK <email> when Google shows 'successfully authenticated', otherwise a reason and non-zero exit code.
"""
import json
import subprocess
import sys
import time

# Windows silent subprocess flag to prevent CMD window flashes
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

PY = "D:/Projects/_SIR/tools/sir-autonomy/.venv/Scripts/python.exe"
CTL = "D:/Projects/_SIR/tools/sir-autonomy/sir_ctl.py"

# Strict positive allowlist: only approved owner accounts may be selected automatically
APPROVED_OWNER_ACCOUNTS = (
    "a7medorabe7",
    "ahmedalaa2006.7.6",
    "1sir1ahmed1",
    "a01083835229",
    "mashoyatal3abed",
    # Owner's own free accounts in the second Chrome profile (his list, ops/ACCOUNT_ROTATION.md "Owner notes 2026-11-10";
    # he asked on 2026-11-10 for automatic switching between them). alshikh138200 stays excluded.
    "sirahmed0115757",
    "sirahmedalaa2006",
    "sir1ahmed2006",
    "ahmed1orabi2006",
    "ahmedalaaorabi2006",
    "ahmedalaaorabe2006",
    "ahmedalaaorabe",
    "ahmedalaaeldinorabe",
)


def is_account_permitted(email: str) -> tuple[bool, str]:
    """Validates that the target email matches the strict owner account allowlist."""
    clean = email.strip().lower()
    if not clean:
        return False, "empty email"
    local_part = clean.split("@")[0]
    if local_part in APPROVED_OWNER_ACCOUNTS:
        return True, "ok"
    return False, f"UNAUTHORIZED ACCOUNT: '{email}' is not in APPROVED_OWNER_ACCOUNTS."


def ctl(*args) -> dict:
    """Executes sir_ctl.py silently and parses JSON safely."""
    try:
        proc = subprocess.run(
            [PY, CTL, *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
            creationflags=CREATE_NO_WINDOW,
        )
        out = (proc.stdout or "").strip()
        if not out:
            return {"ok": False, "error": proc.stderr.strip() or "empty bridge response", "result": []}
        data = json.loads(out)
        if isinstance(data, dict):
            return data
        return {"ok": True, "result": data}
    except json.JSONDecodeError as exc:
        return {"ok": False, "error": f"malformed JSON from bridge: {exc}", "result": []}
    except Exception as exc:
        return {"ok": False, "error": str(exc), "result": []}


def find_tab() -> str | None:
    """Finds the active Google OAuth account chooser or Antigravity auth tab."""
    resp = ctl("browser", "tabs")
    tabs = resp.get("result")
    if not isinstance(tabs, list):
        return None
    for t in tabs:
        url = str(t.get("url", ""))
        if "accounts.google.com" in url and ("accountchooser" in url or "oauth" in url):
            return str(t["id"])
    for t in tabs:
        url = str(t.get("url", ""))
        if "antigravity.google" in url:
            return str(t["id"])
    return None


def snap(tab: str) -> dict:
    """Retrieves DOM snapshot of the target tab."""
    resp = ctl("browser", "snapshot", str(tab))
    res = resp.get("result")
    if isinstance(res, dict):
        return res
    return {"snapshot": ""}


def parse_snapshot_action(text: str, email: str) -> tuple[str, str | None]:
    """
    Determines the next action from a page snapshot.
    Returns (action_type, element_ref).
    action_type in: 'authenticated', 'click_account', 'click_signin', 'needs_owner', 'account_missing', 'signin_missing', 'wait'
    """
    if "successfully authenticated" in text:
        return "authenticated", None

    lines = text.split("\n")
    if "Choose an account" in text:
        ref = next(
            (l.split("]")[0].split("[")[1] for l in lines if email in l.lower() and "<link>" in l and "[" in l and "]" in l),
            None,
        )
        if not ref:
            return "account_missing", None
        return "click_account", ref

    if "Make sure that you downloaded this app" in text:
        ref = next(
            (l.split("]")[0].split("[")[1] for l in lines if "<button> Sign in" in l and "[" in l and "]" in l),
            None,
        )
        if not ref:
            return "signin_missing", None
        return "click_signin", ref

    lower_text = text.lower()
    if "password" in lower_text or "2-step" in lower_text or "verify it" in lower_text:
        return "needs_owner", None

    return "wait", None


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 2

    dry_run = "--dry-run" in args
    clean_args = [a for a in args if not a.startswith("--")]
    if not clean_args:
        print("Error: email argument is required.")
        return 2

    email = clean_args[0].lower()
    permitted, reason = is_account_permitted(email)
    if not permitted:
        print(reason, file=sys.stderr)
        return 3

    if dry_run:
        print(f"[DRY-RUN] Account '{email}' is permitted. Ready to search tabs.")
        return 0

    tab = None
    for _ in range(20):
        tab = find_tab()
        if tab:
            break
        time.sleep(1.5)
    if not tab:
        print(
            "no Google sign-in tab found (is SIR Autonomy extension connected, or use scripts/agy-oauth-url.py)"
        )
        return 1

    for _ in range(6):
        s = snap(tab)
        text = s.get("snapshot", "")
        action, ref = parse_snapshot_action(text, email)

        if action == "authenticated":
            print("OK", email)
            return 0
        elif action == "click_account" and ref:
            ctl("browser", "click", ref, str(tab))
        elif action == "account_missing":
            print("account not in the chooser:", email)
            return 1
        elif action == "click_signin" and ref:
            ctl("browser", "click", ref, str(tab))
        elif action == "signin_missing":
            print("no Sign in button")
            return 1
        elif action == "needs_owner":
            print("Google asks for a password or 2FA: this part needs the owner")
            return 1

        time.sleep(3)

    print("did not reach the success page")
    return 1


if __name__ == "__main__":
    sys.exit(main())
