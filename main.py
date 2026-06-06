from fastapi import FastAPI
import requests

app = FastAPI()

SUPABASE_URL = "https://awzyowlisedimhpgmppj.supabase.co/rest/v1/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3enlvd2xpc2VkaW1ocGdtcHBqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODAyNTMzOTUsImV4cCI6MjA5NTgyOTM5NX0.7662WWO8JpPSkILuVQIQZbJERMeGnzVye1DCpBFpDNw"

def send_to_supabase(table, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    response = requests.post(url, json=data, headers=headers)

    print("SUPABASE RESPONSE:", response.status_code, response.text)

    return response.json()

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
