import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")
BASE_URL = "https://api.spotify.com/v1"
