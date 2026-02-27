from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Footer, Header, Static
from typing_extensions import Self, override


class BoardScreen(Screen):
    @override
    def compose(self: Self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(Static("Aquí va el tablero del juego", id="board-placeholder"))
        yield Footer()
