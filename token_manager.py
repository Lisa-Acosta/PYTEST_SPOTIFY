import base64
import requests
from config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al renovar token: {response.text}")

    return response.json()["access_token"]
