Feature: Pruebas con API de Spotify
Background: Autenticación
  Given tengo un token valido

  Scenario: Consultar una playlist
    When consulto la playlist con ID "0XFj1zpfbqAao86cuwhz8w"
    Then la respuesta tiene codigo 200

  Scenario: Consultar un artista
    When consulto el artista con ID "0TnOYISbd1XYRBk9myaseg"
    Then la respuesta tiene codigo 200

  Scenario: Consultar una cancion
    When consulto la cancion con ID "7iAqvWLgZzXvH38lA06QZg"
    Then la respuesta tiene codigo 200

  Scenario Outline: Reproducir y pausar una cancion
    When reproduzco la cancion con URI "<Uris>"
    Then puedo pausarla

  Examples:
    | Uris                                 |
    | spotify:track:7iAqvWLgZzXvH38lA06QZg | 
    | spotify:track:0Pg5lYYzwkhioVLUpAFzTX |


