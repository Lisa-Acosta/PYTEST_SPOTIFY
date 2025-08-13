from behave import given, when, then
import requests
import time
import json
import logging
from token_manager import get_access_token
import os

# Token temporal de .env
REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")

# Configuración de logging
logging.basicConfig(filename="spotify_responses.log", level=logging.INFO, encoding="utf-8")

# Helper para imprimir y loguear respuestas
def print_json_response(response):
    try:
        content = json.dumps(response.json(), indent=2, ensure_ascii=False)
    except ValueError:
        content = f"Respuesta no JSON: {response.text}"
    print(content)  # Para --no-capture
    logging.info(content)

# Helper para construir headers con token
def get_headers(token):
    return {"Authorization": f"Bearer {token}"}

# Helper para requests a Spotify
def spotify_request(method, endpoint, token, **kwargs):
    url = f"https://api.spotify.com/v1/{endpoint}"
    response = requests.request(method, url, headers=get_headers(token), **kwargs)
    print_json_response(response)
    return response

#@given('tengo un token valido')
#def step_given_token(context):
    # Obtiene un token renovado si el actual está vencido
    #context.token = get_access_token()

@given('tengo un token valido')
def step_impl(context):
    context.token = REFRESH_TOKEN

@when('consulto la playlist con ID "{playlist_id}"')
def step_get_playlist(context, playlist_id):
    context.response = spotify_request("GET", f"playlists/{playlist_id}", context.token)

@when('consulto el artista con ID "{artist_id}"')
def step_get_artist(context, artist_id):
    context.response = spotify_request("GET", f"artists/{artist_id}", context.token)

@when('consulto la cancion con ID "{track_id}"')
def step_get_track(context, track_id):
    context.response = spotify_request("GET", f"tracks/{track_id}", context.token)

@when('reproduzco la cancion con URI "{track_uri}"')
def step_play_song(context, track_uri):
    data = {"uris": [track_uri]}
    context.response = spotify_request("PUT", "me/player/play", context.token, json=data)
    time.sleep(25)  # Espera de reproducción

@then("puedo pausarla")
def step_pause_song(context):
    response = spotify_request("PUT", "me/player/pause", context.token)
    assert response.status_code in [200, 204], f"No se pudo pausar: {response.status_code} - {response.text}"

@then('la respuesta tiene codigo 200')
def step_status_200(context):
    assert context.response.status_code == 200, f"Código devuelto: {context.response.status_code}"
