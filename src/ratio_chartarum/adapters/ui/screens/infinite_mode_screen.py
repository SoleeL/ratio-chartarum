import itertools

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override


class InfiniteModeScreen(Screen):
    ROUTE = "infinite_mode"
    @override
    def compose(self: Self) -> ComposeResult:
        self.deck = itertools.cycle([f"Carta {i}" for i in range(1, 61)])
        yield Static("Deck Infinito: 60 cartas repetibles")
        yield Button("Comenzar juego", id="start")
        yield Button("Volver", id="back")

    def on_button_pressed(self: Self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            # Juego infinito usando self.deck
            pass
        elif event.button.id == "back":
            self.app.pop_screen()
