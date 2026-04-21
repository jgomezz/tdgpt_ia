import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEBUI_URL = os.getenv("OPENWEBUI_URL", "http://localhost:3000")
API_KEY       = os.getenv("USER_API_KEY", "12345678")
# MODEL         = "mistralai/Ministral-3-14B-Reasoning-2512"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":  "application/json"
}

# ── Test 1: List models ──────────────────────────────────────
print("=== Available Models ===")
r = requests.get(f"{OPENWEBUI_URL}/api/v1/models", headers=headers)
if r.status_code == 200:
    models = r.json().get("data", [])
    for m in models:
        print(f"  ✅ {m['id']}")
else:
    print(f"  ❌ Error {r.status_code}: {r.text}")
