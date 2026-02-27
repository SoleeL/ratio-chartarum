from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override

from ratio_chartarum.adapters.ui.screens import BoardScreen


class MenuScreen(Screen):
    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Menu")
        yield Button("Ir a juego", id="go")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go":
            self.app.push_screen(BoardScreen())
