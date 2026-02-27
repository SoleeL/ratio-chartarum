from pathlib import Path

from textual.app import App
from textual.binding import Binding
from typing_extensions import override

from ratio_chartarum.adapters.ui.screens.BoardScreen import BoardScreen
from ratio_chartarum.adapters.ui.screens.MenuScreen import MenuScreen


class RatioChartarum(App):
    BINDINGS = [Binding("d", "toggle_dark", "Toggle dark mode")]

    CSS_PATH = Path(__file__).parent / "ratio-chartarum.css"

    SCREENS = {"menu": MenuScreen, "board": BoardScreen}

    def on_mount(self) -> None:
        self.push_screen("menu")

    # @on(events.Key)
    # async def on_key(self: Self, event: events.Key) -> None:
    #     if event.key == "q":
    #         await self.action_quit()

    @override
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
