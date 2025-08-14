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
  - [🧪 Ejemplos](#-ejemplos)
  - [⚙️ Configuración](#️-configuración)

## ✨ Características

- Automatización de pruebas para endpoints de la API de Spotify
- Uso de Pytest para la ejecución de tests
- Configuración sencilla mediante variables de entorno
- Ejemplos de pruebas y reportes de resultados

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener:

- Python 3.8 o superior instalado
- Una cuenta de Spotify para obtener credenciales de API
- Si quieres ejecutar todos los endpoints de la Api, también tienes que tener una cuenta de Spotify Premium

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
behave 
```

## 🧪 Ejemplos

Puedes encontrar ejemplos de pruebas en la carpeta `steps/`.

## ⚙️ Configuración

Asegúrate de completar el archivo `.env` con tus credenciales de la API de Spotify.


