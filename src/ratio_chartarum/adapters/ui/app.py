from pathlib import Path
from typing import ClassVar

from textual import events, on
from textual._path import CSSPathType
from textual.app import App, ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Container, Vertical
from textual.widgets import Button, Footer, Header, Static
from typing_extensions import Self, override


class Game(App):
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("d", "toggle_dark", "Toggle dark mode")
    ]

    CSS_PATH: ClassVar[CSSPathType | None] = (
        Path(__file__).parent / "ratio-chartarum.css"
    )

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

    @on(events.Key)
    async def on_key(self: Self, event: events.Key) -> None:
        if event.key == "q":
            await self.action_quit()

    @override
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
