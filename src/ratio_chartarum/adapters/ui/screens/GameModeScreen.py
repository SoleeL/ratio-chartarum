from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override

from ratio_chartarum.adapters.ui.screens.ClassicModeScreen import ClassicModeScreen
from ratio_chartarum.adapters.ui.screens.CustomModeScreen import CustomModeScreen
from ratio_chartarum.adapters.ui.screens.InfiniteModeScreen import InfiniteModeScreen
from ratio_chartarum.adapters.ui.screens.RandomModeScreen import RandomModeScreen


class GameModeScreen(Screen):
    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Selecciona un modo de juego:", id="mode-title")
        yield Button("Deck Aleatorio", id="random")
        yield Button("Deck Clásico", id="classic")
        yield Button("Deck Personalizado", id="custom")
        yield Button("Deck Infinito", id="infinite")
        yield Button("Volver", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        mapping = {
            "classic": ClassicModeScreen,
            "random": RandomModeScreen,
            "infinite": InfiniteModeScreen,
            "custom": CustomModeScreen,
        }
        if event.button.id in mapping:
            self.app.push_screen(mapping[event.button.id]())
        elif event.button.id == "back":
            self.app.pop_screen()
