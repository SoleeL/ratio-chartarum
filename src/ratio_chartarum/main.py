# src/main.py

from textual.app import App

from ui import JuegoApp

if __name__ == "__main__":
    app: App = JuegoApp()
    app.run()
