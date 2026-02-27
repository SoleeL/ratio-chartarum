from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override


class ClassicModeScreen(Screen):
    @override
    def compose(self: Self) -> ComposeResult:
        self.deck = [f"Carta {i}" for i in range(1, 61)]
        yield Static(f"Deck Clásico: {len(self.deck)} cartas")
        yield Button("Comenzar juego", id="start")
        yield Button("Volver", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            # Inicia el juego con self.deck
            pass
        elif event.button.id == "back":
            self.app.pop_screen()
