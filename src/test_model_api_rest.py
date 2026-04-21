import requests
import os

from dotenv import load_dotenv


load_dotenv()


OPENWEBUI_URL = os.getenv("OPENWEBUI_URL", "http://localhost:3000")
API_KEY       = os.getenv("USER_API_KEY", "12345678")
MODEL         = "mistralai/Ministral-3-14B-Reasoning-2512"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":  "application/json"
}

# ── Test 2: Chat completion ──────────────────────────────────
print("\n=== Chat Test ===")
payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "Dame un programa en Python que imprima 'Hola, mundo!'"}
    ]
}
r = requests.post(
    f"{OPENWEBUI_URL}/api/chat/completions",
    headers=headers,
    json=payload
)
if r.status_code == 200:
    reply = r.json()["choices"][0]["message"]["content"]
    print(f"  ✅ Response: {reply}")
else:
    print(f"  ❌ Error {r.status_code}: {r.text}")
