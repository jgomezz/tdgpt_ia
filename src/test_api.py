import requests
import os

from dotenv import load_dotenv


load_dotenv()


OPENWEBUI_URL = os.getenv("OPENWEBUI_URL", "http://localhost:3000")
API_KEY       = os.getenv("USER_API_KEY", "12345678")
#MODEL         = "llama3.3:70b"
MODEL         = "mistralai/Ministral-3-14B-Reasoning-2512"

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


'''

time curl -X POST "https://192.168.17.11:3000/api/chat/completions" \
     -H "Authorization: Bearer sk-b9c4e618d21142deb40de665f460f02f" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "ministral-3:14b",
       "messages": [
         {
           "role": "user",
                  "stream": true,

           "content": "Dame un programa en Python que imprima Hola, mundo!"
         }
       ]
     }'


'''