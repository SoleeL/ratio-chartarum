# Ratio Chartarum: Terminal Card Game

Este documento explica cómo configurar el entorno de desarrollo, instalar dependencias y trabajar en el proyecto.

---

## 1. Requisitos

- **Python 3.10.12+**
- **pip** actualizado
- **virtualenv** opcional pero recomendado
- Sistema Linux / MacOS / Windows

---

## 2. Crear y activar el entorno virtual

```bash
# Linux / Mac
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Instalar dependencias

Instala las dependencias principales para ejecutar el juego:

```bash
pip install --upgrade pip
pip install .
```

Para instalar dependencias de desarrollo (linting, tests, tipado estático):

```bash
pip install .[dev]
```

Esto instalará:

textual>=0.27 → Biblioteca para interfaces en terminal

mypy>=1.5 → Comprobación de tipos

pytest>=7.0 → Tests automáticos

## 4. Ejecutar el juego

Con el entorno virtual activado, ejecuta:

```bash
ratio-chartarum
```

Esto llamará a la función main definida en mi_juego/main.py.

## 5. Desarrollo y testing

### 5.1 Comprobar tipos

```bash
mypy src/
```
### 5.2 Ejecutar tests

```bash
pytest
```
### 5.3 Construir paquete

Si quieres generar un paquete instalable:

```bash
python -m build
```

Esto creará un directorio dist/ con los archivos .tar.gz y .whl.

### 6. Estructura del proyecto

```
ratio-chartarum/
│
├─ mi_juego/
│   └─ main.py          # Punto de entrada del juego
├─ pyproject.toml       # Configuración de build y dependencias
├─ README.md
└─ tests/               # Tests unitarios
```