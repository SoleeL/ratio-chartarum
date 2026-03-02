from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override


class RandomModeScreen(Screen):
    ROUTE = "random_mode"

    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Deck Aleatorio: 60 cartas generadas al azar")
        yield Button("Comenzar juego", id="start")
        yield Button("Volver", id="back")

    def on_button_pressed(self: Self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            # Lógica para iniciar juego aleatorio
            pass
        elif event.button.id == "back":
            self.app.pop_screen()
