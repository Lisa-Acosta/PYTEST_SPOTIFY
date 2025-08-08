import requests
from behave import given, when, then
from token_manager import get_access_token
from config import BASE_URL

@given("tengo un token válido")
def step_impl(context):
    context.token = get_access_token()

@when('consulto la playlist con ID "{playlist_id}"')
def step_impl(context, playlist_id):
    url = f"{BASE_URL}/playlists/{playlist_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    context.response = requests.get(url, headers=headers)

@when('consulto el artista con ID "{artist_id}"')
def step_impl(context, artist_id):
    url = f"{BASE_URL}/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    context.response = requests.get(url, headers=headers)

@when('consulto la canción con ID "{track_id}"')
def step_impl(context, track_id):
    url = f"{BASE_URL}/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    context.response = requests.get(url, headers=headers)

@then("la respuesta debe tener código 200")
def step_impl(context):
    assert context.response.status_code == 200, f"Error: {context.response.text}"
