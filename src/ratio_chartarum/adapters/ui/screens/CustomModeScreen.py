from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input, Static
from typing_extensions import Self, override


class CustomModeScreen(Screen):
    ROUTE = "custom_mode"
    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Configura tu Deck Personalizado:")
        yield Input(placeholder="Cantidad de cartas (1-60)", id="card-count")
        yield Input(placeholder="Otras configuraciones", id="deck-config")
        yield Button("Comenzar juego", id="start")
        yield Button("Volver", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            # Aquí recogerías inputs y generarías el deck
            card_count_input = self.query_one("#card-count", Input)
            deck_size = int(card_count_input.value or 0)
            self.deck = [f"Carta {i}" for i in range(1, deck_size + 1)]
        elif event.button.id == "back":
            self.app.pop_screen()
