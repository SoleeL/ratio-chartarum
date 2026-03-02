from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static
from typing_extensions import Self, override

from ratio_chartarum.adapters.ui.screens.achievements_screen import AchievementsScreen
from ratio_chartarum.adapters.ui.screens.credits_screen import CreditsScreen
from ratio_chartarum.adapters.ui.screens.desk_mode_selection_screen import DeskModeSelectionScreen
from ratio_chartarum.adapters.ui.screens.game_mode_selection_screen import GameModeSelectionScreen
from ratio_chartarum.adapters.ui.screens.profile_selection_screen import ProfileSelectionScreen
from ratio_chartarum.adapters.ui.screens.settings_screen import SettingsScreen
from ratio_chartarum.adapters.ui.screens.stats_screen import StatsScreen


class MainMenuScreen(Screen):
    ROUTE = "main_menu"

    BTN_PLAY_ID = "play"
    BTN_DECKS_ID = "decks"
    BTN_SETTINGS_ID = "settings"
    BTN_CREDITS_ID = "credits"

    BTN_PROFILE_ID = "profile"
    BTN_ACHIEVEMENTS_ID = "achievements"
    BTN_STATS_ID = "stats"

    BTN_EXIT_ID = "exit"

    NAVIGATION_MAP = {
        BTN_PLAY_ID: GameModeSelectionScreen.ROUTE,
        BTN_DECKS_ID: DeskModeSelectionScreen.ROUTE,
        BTN_SETTINGS_ID: SettingsScreen.ROUTE,
        BTN_CREDITS_ID: CreditsScreen.ROUTE,

        BTN_PROFILE_ID: ProfileSelectionScreen.ROUTE,
        BTN_ACHIEVEMENTS_ID: AchievementsScreen.ROUTE,
        BTN_STATS_ID: StatsScreen.ROUTE,
    }

    @override
    def compose(self: Self) -> ComposeResult:
        yield Header()

        yield Static("RATIO CHARTARUM", id="title")

        with Container():
            with Vertical(id="main-menu"):
                yield Button("Jugar", id=self.BTN_PLAY_ID)
                yield Button("Editar mazos", id=self.BTN_DECKS_ID)
                yield Button("Ajustes", id=self.BTN_SETTINGS_ID)
                yield Button("Créditos", id=self.BTN_CREDITS_ID)
                yield Button("Salir", id=self.BTN_EXIT_ID)

            with Vertical(id="secondary-menu"):
                yield Button("Perfil: Carlos", id=self.BTN_PROFILE_ID)
                yield Button("Logros", id=self.BTN_ACHIEVEMENTS_ID)
                yield Button("Estadísticas", id=self.BTN_STATS_ID)

        yield Footer()

    def on_button_pressed(self: Self, event: Button.Pressed) -> None:
        if event.button.id in self.NAVIGATION_MAP:
            self.app.push_screen(self.NAVIGATION_MAP[event.button.id])
        elif event.button.id == self.BTN_EXIT_ID:
            self.app.exit()
