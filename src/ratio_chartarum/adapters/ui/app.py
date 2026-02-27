from pathlib import Path

from textual.app import App
from textual.binding import Binding
from typing_extensions import override

from ratio_chartarum.adapters.ui.screens.BoardScreen import GameBoardScreen
from ratio_chartarum.adapters.ui.screens.ClassicModeScreen import ClassicModeScreen
from ratio_chartarum.adapters.ui.screens.CustomModeScreen import CustomModeScreen
from ratio_chartarum.adapters.ui.screens.InfiniteModeScreen import InfiniteModeScreen
from ratio_chartarum.adapters.ui.screens.MainMenuScreen import MainMenuScreen
from ratio_chartarum.adapters.ui.screens.ModeSelectionScreen import ModeSelectionScreen
from ratio_chartarum.adapters.ui.screens.RandomModeScreen import RandomModeScreen


class RatioChartarum(App):
    BINDINGS = [Binding("d", "toggle_dark", "Toggle dark mode")]

    CSS_PATH = Path(__file__).parent / "ratio-chartarum.css"

    SCREENS = {
        MainMenuScreen.ROUTE: MainMenuScreen,

        ModeSelectionScreen.ROUTE: ModeSelectionScreen,

        ClassicModeScreen.ROUTE: ClassicModeScreen,
        RandomModeScreen.ROUTE: RandomModeScreen,
        InfiniteModeScreen.ROUTE: InfiniteModeScreen,
        CustomModeScreen.ROUTE: CustomModeScreen,

        GameBoardScreen.ROUTE: GameBoardScreen,
    }

    def on_mount(self) -> None:
        self.push_screen(MainMenuScreen.ROUTE)

    @override
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
