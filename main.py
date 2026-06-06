import requests

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
    return requests.post(url, json=data, headers=headers)
