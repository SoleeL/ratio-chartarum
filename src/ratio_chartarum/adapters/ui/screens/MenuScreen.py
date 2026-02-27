from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static
from typing_extensions import Self, override

from ratio_chartarum.adapters.ui.screens.GameModeScreen import GameModeScreen


class MenuScreen(Screen):
    @override
    def compose(self: Self) -> ComposeResult:
        yield Header()

        yield Static("RATIO CHARTARUM", id="title")

        with Container():
            with Vertical(id="main-menu"):
                yield Button("Jugar", id="play")
                yield Button("Editar mazos", id="decks")
                yield Button("Ajustes", id="settings")
                yield Button("Créditos", id="credits")
                yield Button("Salir", id="exit")

            with Vertical(id="secondary-menu"):
                yield Button("Perfil: Carlos", id="profile")
                yield Button("Logros", id="achievements")
                yield Button("Estadísticas", id="stats")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "play":
            self.app.push_screen(GameModeScreen())
