from fastapi import FastAPI
import requests

app = FastAPI()

SUPABASE_URL = "https://awzyowlisedimhpgmppj.supabase.co"
SUPABASE_KEY = "ISI_KEY_KAMU"

def send_to_supabase(table, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    return requests.post(url, json=data, headers=headers)

@app.get("/")
def home():
    return {"status": "AI running"}

@app.post("/ai/fraud")
def ai_fraud(data: dict):
    score = len(str(data)) * 3

    result = {
        "user_id": data.get("user_id"),
        "fraud_score": score
    }

    send_to_supabase("ai_predictions", result)

    return result

@app.post("/ai/pricing")
def ai_pricing(data: dict):
    base = data.get("price", 10000)
    final = base * 1.2

    result = {
        "service_id": data.get("service_id"),
        "final_price": final
    }

    send_to_supabase("dynamic_pricing", result)

    return result
