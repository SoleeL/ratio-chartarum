from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override


class ModeSelectionScreen(Screen):
    ROUTE = "mode_selection"

    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Selecciona un modo de juego:", id="mode-title")
        yield Button("Deck Clásico", id="classic")
        yield Button("Deck Aleatorio", id="random")
        yield Button("Deck Infinito", id="infinite")
        yield Button("Deck Personalizado", id="custom")
        yield Button("Volver", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        mapping = {
            "classic": "classic-mode",
            "random": "random-mode",
            "infinite": "infinite-mode",
            "custom": "custom-mode",
        }
        if event.button.id in mapping:
            self.app.push_screen(mapping[event.button.id])
        elif event.button.id == "back":
            self.app.pop_screen()
