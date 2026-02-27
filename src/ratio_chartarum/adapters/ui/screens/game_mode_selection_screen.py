from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override

from ratio_chartarum.adapters.ui.screens.classic_mode_screen import ClassicModeScreen
from ratio_chartarum.adapters.ui.screens.custom_mode_screen import CustomModeScreen
from ratio_chartarum.adapters.ui.screens.infinite_mode_screen import InfiniteModeScreen
from ratio_chartarum.adapters.ui.screens.random_mode_screen import RandomModeScreen


class GameModeSelectionScreen(Screen):
    ROUTE = "game_mode_selection"

    BTN_CLASSIC_ID = "classic"
    BTN_RANDOM_ID = "random"
    BTN_INFINITE_ID = "infinite"
    BTN_CUSTOM_ID = "custom"

    BTN_BACK_ID = "back"

    NAVIGATION_MAP = {
        BTN_CLASSIC_ID: ClassicModeScreen.ROUTE,
        BTN_RANDOM_ID: RandomModeScreen.ROUTE,
        BTN_INFINITE_ID: InfiniteModeScreen.ROUTE,
        BTN_CUSTOM_ID: CustomModeScreen.ROUTE
    }

    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Selecciona un modo de juego:", id="mode-title")
        yield Button("Deck Clásico", id=self.BTN_CLASSIC_ID)
        yield Button("Deck Aleatorio", id=self.BTN_RANDOM_ID)
        yield Button("Deck Infinito", id=self.BTN_INFINITE_ID)
        yield Button("Deck Personalizado", id=self.BTN_CUSTOM_ID)
        yield Button("Volver", id=self.BTN_BACK_ID)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id in self.NAVIGATION_MAP:
            self.app.push_screen(self.NAVIGATION_MAP[event.button.id])
        elif event.button.id == self.BTN_BACK_ID:
            self.app.pop_screen()
