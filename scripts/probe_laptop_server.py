import http.client
import json

def test_req(method, path, headers=None):
    conn = http.client.HTTPConnection("127.0.0.1", 8765, timeout=5)
    hdrs = headers or {}
    conn.request(method, path, headers=hdrs)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8", errors="replace")
    conn.close()
    return resp.status, resp.reason, dict(resp.getheaders()), body

print("=== 1. HOST HEADER TESTS ===")
test_hosts = [
    ("127.0.0.1:8765", "Valid loopback with port"),
    ("127.0.0.1", "Valid loopback without port"),
    ("localhost:8765", "Valid localhost with port"),
    ("localhost", "Valid localhost without port"),
    ("[::1]:8765", "Valid IPv6 loopback with port"),
    ("[::1]", "Valid IPv6 loopback without port"),
    ("ahmed.tail9e9aa7.ts.net:8765", "Tailscale domain with port"),
    ("ahmed.tail9e9aa7.ts.net", "Tailscale domain without port"),
    ("100.85.112.10:8765", "Tailscale IP with port"),
    ("100.85.112.10", "Tailscale IP without port"),
    ("evil.com", "Malicious external domain"),
    ("attacker.tail9e9aa7.ts.net:8765", "Subdomain spoofing attempt"),
    ("", "Empty Host header"),
]

for host, desc in test_hosts:
    st, reas, hdrs, b = test_req("GET", "/", {"Host": host} if host else {})
    print(f"Host: '{host}' ({desc}) -> {st} {reas}")

print("\n=== 2. TAILSCALE-USER-LOGIN IDENTITY TESTS ===")
user_tests = [
    ("a7medorabe7@gmail.com", "Authorized owner email"),
    ("A7MEDORABE7@GMAIL.COM", "Authorized owner uppercase"),
    ("intruder@example.com", "Unauthorized user email"),
    ("habiba@gmail.com", "Unauthorized non-owner user"),
    ("", "Absent/empty header"),
]

for user, desc in user_tests:
    hdrs = {"Host": "127.0.0.1:8765"}
    if user:
        hdrs["Tailscale-User-Login"] = user
    st, reas, resp_hdrs, b = test_req("GET", "/api/health", hdrs)
    print(f"User: '{user}' ({desc}) -> {st} {reas} (body preview: {b[:60]})")

print("\n=== 3. SECURITY HEADERS ON STATIC /index.html ===")
st, reas, hdrs, b = test_req("GET", "/", {"Host": "127.0.0.1:8765"})
print(f"GET / Status: {st} {reas}")
for h in ["content-type", "x-content-type-options", "x-frame-options", "referrer-policy", "permissions-policy", "content-security-policy", "cache-control"]:
    print(f"  {h}: {hdrs.get(h, 'MISSING')}")

print("\n=== 4. POST CSRF / ORIGIN / TOKEN TESTS ===")
# Valid token extraction
st, reas, hdrs, b = test_req("GET", "/api/session", {"Host": "127.0.0.1:8765"})
token = json.loads(b).get("token")
print(f"Obtained session token: {token[:8]}...")

post_tests = [
    ("Missing Origin", {}, {"Host": "127.0.0.1:8765", "X-SIR-Confirm-Token": token}),
    ("Illegal Origin", {"Origin": "https://evil.com"}, {"Host": "127.0.0.1:8765", "Origin": "https://evil.com", "X-SIR-Confirm-Token": token}),
    ("Valid Origin HTTP", {"Origin": "http://127.0.0.1:8765"}, {"Host": "127.0.0.1:8765", "Origin": "http://127.0.0.1:8765", "X-SIR-Confirm-Token": token}),
    ("Valid Origin Tailscale HTTPS", {"Origin": "https://ahmed.tail9e9aa7.ts.net:8765"}, {"Host": "ahmed.tail9e9aa7.ts.net:8765", "Origin": "https://ahmed.tail9e9aa7.ts.net:8765", "X-SIR-Confirm-Token": token}),
    ("Invalid Token", {"Origin": "http://127.0.0.1:8765"}, {"Host": "127.0.0.1:8765", "Origin": "http://127.0.0.1:8765", "X-SIR-Confirm-Token": "bad_token"}),
]

for desc, origin_hdr, full_hdrs in post_tests:
    conn = http.client.HTTPConnection("127.0.0.1", 8765, timeout=5)
    body_data = json.dumps({"confirm": False})
    full_hdrs["Content-Length"] = str(len(body_data))
    full_hdrs["Content-Type"] = "application/json"
    conn.request("POST", "/api/look/fix-gap", body=body_data, headers=full_hdrs)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8", errors="replace")
    conn.close()
    print(f"POST test ({desc}) -> {resp.status} {resp.reason}: {body[:80]}")
