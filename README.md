# Spotify API Automation

Automatización de la API de Spotify con Python y Pytest para el trabajo final del curso Nahual de APIs con IA.

## 📋 Tabla de Contenidos

- [Spotify API Automation](#spotify-api-automation)
  - [📋 Tabla de Contenidos](#-tabla-de-contenidos)
  - [✨ Características](#-características)
  - [🔧 Requisitos Previos](#-requisitos-previos)
    - [Crear y activar entorno virtual](#crear-y-activar-entorno-virtual)
  - [🚀 Instalación](#-instalación)
    - [Clonar el repositorio](#clonar-el-repositorio)
    - [Instalar dependencias](#instalar-dependencias)
    - [Configurar variables de entorno](#configurar-variables-de-entorno)
  - [💻 Uso](#-uso)
    - [Ejecutar pruebas](#ejecutar-pruebas)
    - [Ejecutar el proyecto principal](#ejecutar-el-proyecto-principal)
  - [🧪 Ejemplos](#-ejemplos)
  - [⚙️ Configuración](#️-configuración)
  - [🤝 Contribuir](#-contribuir)

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

Puedes encontrar ejemplos de pruebas en la carpeta `steps/`.

## ⚙️ Configuración

Asegúrate de completar el archivo `.env` con tus credenciales de la API de Spotify.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

