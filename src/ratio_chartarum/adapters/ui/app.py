from pathlib import Path

from textual.app import App
from textual.binding import Binding
from typing_extensions import override

from ratio_chartarum.adapters.ui.screens.achievements_screen import AchievementsScreen
from ratio_chartarum.adapters.ui.screens.board_screen import GameBoardScreen
from ratio_chartarum.adapters.ui.screens.classic_mode_screen import ClassicModeScreen
from ratio_chartarum.adapters.ui.screens.credits_screen import CreditsScreen
from ratio_chartarum.adapters.ui.screens.custom_mode_screen import CustomModeScreen
from ratio_chartarum.adapters.ui.screens.desk_mode_selection_screen import DeskModeSelectionScreen
from ratio_chartarum.adapters.ui.screens.infinite_mode_screen import InfiniteModeScreen
from ratio_chartarum.adapters.ui.screens.main_menu_screen import MainMenuScreen
from ratio_chartarum.adapters.ui.screens.game_mode_selection_screen import GameModeSelectionScreen
from ratio_chartarum.adapters.ui.screens.profile_selection_screen import ProfileSelectionScreen
from ratio_chartarum.adapters.ui.screens.random_mode_screen import RandomModeScreen
from ratio_chartarum.adapters.ui.screens.settings_screen import SettingsScreen
from ratio_chartarum.adapters.ui.screens.stats_screen import StatsScreen


class RatioChartarum(App):
    BINDINGS = [Binding("d", "toggle_dark", "Toggle dark mode")]

    CSS_PATH = Path(__file__).parent / "ratio-chartarum.css"

    SCREENS = {
        MainMenuScreen.ROUTE: MainMenuScreen,

        GameModeSelectionScreen.ROUTE: GameModeSelectionScreen,
        DeskModeSelectionScreen.ROUTE: DeskModeSelectionScreen,
        SettingsScreen.ROUTE: SettingsScreen,
        CreditsScreen.ROUTE: CreditsScreen,

        ProfileSelectionScreen.ROUTE: ProfileSelectionScreen,
        AchievementsScreen.ROUTE: AchievementsScreen,
        StatsScreen.ROUTE: SettingsScreen,

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
