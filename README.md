# Spotify API Automation

Automatización de la API de Spotify con Python y Pytest para el trabajo final del curso Nahual de APIs con IA.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Configuración](#configuración)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)

## ✨ Características

- Automatización de pruebas para endpoints de la API de Spotify
- Uso de Pytest para la ejecución de tests
- Configuración sencilla mediante variables de entorno
- Ejemplos de pruebas y reportes de resultados

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener:

- Python 3.8 o superior instalado
- Una cuenta de Spotify para obtener credenciales de API

### Crear y activar entorno virtual

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Mac/Linux
source venv/bin/activate
```

## 🚀 Instalación

### Clonar el repositorio

```bash
git clone https://github.com/Lisa-Acosta/PYTEST-SPOTIFY
cd PYTEST-SPOTIFY
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno

```bash
cp .env.example .env
# Edita el archivo .env con tus credenciales de Spotify
```

## 💻 Uso

### Ejecutar pruebas

```bash
pytest
```

### Ejecutar el proyecto principal

```bash
python main.py
```

## 🧪 Ejemplos

Puedes encontrar ejemplos de pruebas en la carpeta `tests/`.

## ⚙️ Configuración

Asegúrate de completar el archivo `.env` con tus credenciales de la API de Spotify.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

### Guías de contribución

- Sigue las convenciones de código del proyecto
- Añade tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario

## 🙏 Agradecimientos

- [Recurso o persona que te ayudó](https://ejemplo.com)
- [Librería o herramienta utilizada](https://ejemplo.com)
- [Inspiración o referencia](https://ejemplo.com)

## 📊 Estado del Proyecto

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🗺️ Roadmap

- [x] Automatización de pruebas básicas
- [ ] Integración continua
- [ ] Mejoras en la cobertura de pruebas
- [ ] Documentación avanzada

## 📞 Contacto

Para dudas o sugerencias,