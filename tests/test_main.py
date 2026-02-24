# tests/test_main.py
from mi_juego.main import main

def test_main_runs():
    # Solo verificamos que se pueda importar sin error
    assert callable(main)