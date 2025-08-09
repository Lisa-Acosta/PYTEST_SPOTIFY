from behave import given, when, then
import requests
import time
import json
import logging

# Token temporal pegado a mano
ACCESS_TOKEN = "BQA1ze2G3iuYB0VTGCfnFc9Wmutt4QW7ALHhba5Vv1LNeDAGm9aeLPJuBrFRw2By6zu8zDq14uaT261eqrnMIdCQi62DqUKia7Z2Hb_xjwv30k27YDKm8IDj_1w6CKf0aQoakLNXSP4BTwcvrBTpmXEZo7XwSl-nw9CagBYgWLQc1I6mh8D0HbbSDuoegQVuo1x7OdxEqYQEAMrT0UMyybZPfLOw6s4m7VHLPfWzGg"

logging.basicConfig(filename="spotify_responses.log", level=logging.INFO, encoding="utf-8")

def print_json_response(response):
    try:
        content = json.dumps(response.json(), indent=2, ensure_ascii=False)
    except ValueError:
        content = f"Respuesta no JSON: {response.text}"
    print(content)  # Para ver si usás --no-capture
    logging.info(content)

@given('tengo un token valido')
def step_impl(context):
    context.token = ACCESS_TOKEN

@when('consulto la playlist con ID "{playlist_id}"')
def step_impl(context, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    context.response = requests.get(url, headers=headers)
    print_json_response(context.response)


@when('consulto el artista con ID "{artist_id}"')
def step_impl(context, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    context.response = requests.get(url, headers=headers)
    print_json_response(context.response)


@when('consulto la cancion con ID "{track_id}"')
def step_impl(context, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    context.response = requests.get(url, headers=headers)
    print_json_response(context.response)


@when('reproduzco la cancion con URI "{track_uri}"')
def step_impl(context, track_uri):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = {"Authorization": f"Bearer {context.token}"}
    data = {"uris": [track_uri]}
    context.response = requests.put(url, headers=headers, json=data)
    print_json_response(context.response)
    time.sleep(30)  # Espera 30 segundos antes de continuar

@then("debo poder pausarla")
def step_pause_song(context):
    url = "https://api.spotify.com/v1/me/player/pause"
    headers = {"Authorization": f"Bearer {context.token}"}
    response = requests.put(url, headers=headers)
    print_json_response(response)
    assert response.status_code in [200, 204], f"No se pudo pausar: {response.status_code} - {response.text}"

@then('la respuesta debe tener codigo 200')
def step_impl(context):
    print_json_response(context.response)
    assert context.response.status_code == 200, f"Código devuelto: {context.response.status_code}"
