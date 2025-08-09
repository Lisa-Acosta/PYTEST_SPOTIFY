Feature: Pruebas con API de Spotify

  Scenario: Consultar una playlist
    Given tengo un token valido
    When consulto la playlist con ID "0XFj1zpfbqAao86cuwhz8w"
    Then la respuesta debe tener codigo 200

  Scenario: Consultar un artista
    Given tengo un token valido
    When consulto el artista con ID "0TnOYISbd1XYRBk9myaseg"
    Then la respuesta debe tener codigo 200

  Scenario: Consultar una cancion
    Given tengo un token valido
    When consulto la cancion con ID "7iAqvWLgZzXvH38lA06QZg"
    Then la respuesta debe tener codigo 200

  Scenario: Reproducir y pausar una cancion
    Given tengo un token valido
    When reproduzco la cancion con URI "spotify:track:7iAqvWLgZzXvH38lA06QZg"
    Then debo poder pausarla


