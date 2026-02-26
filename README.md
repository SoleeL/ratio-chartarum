# Ratio Chartarum: Terminal Card Game

Juego de cartas en terminal construido con textual.

## 📦 Requisitos

- Python 3.10.12+
- pip actualizado
- Linux / macOS / Windows

## 👨‍💻 Desarrollo (recomendado)

Estas instrucciones son para trabajar activamente en el proyecto.

### 1️⃣ Crear entorno virtual (opcional pero recomendado)

#### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2️⃣ Instalar en modo editable

```bash
pip install --upgrade pip
pip install -e .[dev]
```

Esto:

1. Instala el paquete en modo editable
2. Instala dependencias de desarrollo (mypy, pytest, etc.)
3. Hace que ratio-chartarum use tu código actual (sin reinstalar)

### 3️⃣ Ejecutar en desarrollo

Usando el entrypoint instalado:

```bash
ratio-chartarum
```

- Usa el script generado por el paquete instalado
- Requiere haber ejecutado ```pip install -e .```
- Es la forma más limpia y similar a producción
- El modo ```-e``` hace que use tu código actual sin reinstalar

Alternativa sin instalar:

```bash
python -m src.main
```

- No requiere instalar el paquete
- Ejecuta el archivo directamente desde el directorio del proyecto
- Útil para pruebas rápidas
- No valida que el packaging (entrypoints, configuración del build) esté correcto

## 🧪 Herramientas de desarrollo

✔ Comprobación de linter

```bash
mypy src/
```

✔ Ejecutar tests

```bash
pytest
```

## 🧩 Extensiones recomendadas para VS Code

Para una experiencia de desarrollo completa (errores en vivo, autocompletado y análisis estático), se recomienda instalar:

- Python — Microsoft
  - ID: ms-python.python

- Pylance — Microsoft
  - ID: ms-python.vscode-pylance

- Mypy Type Checker — Microsoft
  - ID: ms-python.mypy-type-checker

Estas extensiones permiten:

- Detección de errores en tiempo real
- Integración automática con el entorno virtual (.venv)
- Análisis de tipos usando la configuración definida en mypy.ini

## 📦 Instalación para uso normal

Si solo quieres instalar y ejecutar el juego:

```bash
pip install .
ratio-chartarum
```

⚠️ Nota: Si modificas el código después, deberás reinstalar.

## 🏗 Construir paquete

```bash
python -m build
```

Generará archivos en dist/:

- ```.tar.gz```
- ```.whl```

## 📁 Estructura del proyecto

```bash
ratio-chartarum/
│
├─ src/
│   ├─ main.py
│   ├─ ui.py
│   └─ __init__.py
│
├─ tests/
├─ pyproject.toml
└─ README.md
```