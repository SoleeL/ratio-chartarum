# tests/test_main.py

from main import main


def test_main_runs() -> None:
    # Solo verificamos que se pueda importar sin error
    assert callable(main)
