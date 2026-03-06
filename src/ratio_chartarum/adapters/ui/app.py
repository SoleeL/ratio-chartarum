from pathlib import Path

from textual.app import App
from textual.binding import Binding
from typing_extensions import override, Self

from ratio_chartarum.adapters.ui.screens.main_menu_screen import MainMenuScreen


class RatioChartarum(App):
    BINDINGS = [Binding("d", "toggle_dark", "Toggle dark mode")]

    CSS_PATH = Path(__file__).parent / "ratio-chartarum.css"

    def __init__(self, container):
        super().__init__()
        self.container = container

    def on_mount(self: Self) -> None:
        self.push_screen(MainMenuScreen())

    @override
    def action_toggle_dark(self: Self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
