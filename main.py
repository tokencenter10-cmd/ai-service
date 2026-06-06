from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI running"}

@app.post("/fraud-check")
def fraud_check(data: dict):
    score = len(str(data)) * 2
    return {"fraud_score": score}

@app.post("/pricing")
def pricing(data: dict):
    base = data.get("base_price", 10000)
    multiplier = 1.2
    return {"final_price": base * multiplier}
