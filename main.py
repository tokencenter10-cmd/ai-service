from fastapi import FastAPI
import requests
import uuid

app = FastAPI()

SUPABASE_URL = "https://awzyowlisedimhpgmppj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3enlvd2xpc2VkaW1ocGdtcHBqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODAyNTMzOTUsImV4cCI6MjA5NTgyOTM5NX0.7662WWO8JpPSkILuVQIQZbJERMeGnzVye1DCpBFpDNw"

# =========================
# SUPABASE HELPER
# =========================
def send_to_supabase(table, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    response = requests.post(url, json=data, headers=headers)

    print("🔥 SUPABASE STATUS:", response.status_code)
    print("🔥 SUPABASE RESPONSE:", response.text)

    return {
        "status": response.status_code,
        "response": response.text
    }


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"status": "AI running"}


# =========================
# FRAUD DETECTION (FIXED)
# =========================
@app.post("/ai/fraud")
def ai_fraud(data: dict):

    score = len(str(data)) * 3

    behavior_score = max(0, 100 - score)

    reliability_score = 95 if score < 150 else 50

    piercing_multiplier = 1.0

    confidence = 90

    result = {
        "user_id": str(uuid.uuid4()),
        "model_version": "v1.0",
        "fraud_score": score,
        "behavior_score": behavior_score,
        "reliability_score": reliability_score,
         "pricing_multiplier": 1,
        "confidence": 90
    }

    db_result = send_to_supabase("ai_predictions", result)

    return {
        "ai_result": result,
        "supabase": db_result
    }


# =========================
# PRICING AI
# =========================
@app.post("/ai/pricing")
def ai_pricing(data: dict):

    base = data.get("price", 10000)
    final = base * 1.2

    result = {
        "service_id": str(uuid.uuid4()),  # FIX JUGA BIAR AMAN
        "final_price": final
    }

    db_result = send_to_supabase("dynamic_pricing", result)

    return {
        "ai_result": result,
        "supabase": db_result
    }
