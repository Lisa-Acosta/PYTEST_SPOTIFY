Feature: Pruebas con API de Spotify

  Scenario: Consultar una playlist
    Given tengo un token válido
    When consulto la playlist con ID "37i9dQZF1DXcBWIGoYBM5M"
    Then la respuesta debe tener código 200

  Scenario: Consultar un artista
    Given tengo un token válido
    When consulto el artista con ID "1Xyo4u8uXC1ZmMpatF05PJ"
    Then la respuesta debe tener código 200

  Scenario: Consultar una canción
    Given tengo un token válido
    When consulto la canción con ID "3n3Ppam7vgaVa1iaRUc9Lp"
    Then la respuesta debe tener código 200


