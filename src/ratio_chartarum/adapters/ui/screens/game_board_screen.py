from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Footer, Header, Static
from typing_extensions import Self, override


class GameBoardScreen(Screen):

    def __init__(self, deck_id: str) -> None:
        super().__init__()
        self.deck_id: str = deck_id

    @override
    def compose(self: Self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static(
                f"Aquí va el tablero del juego (Deck ID: {self.deck_id})",
                id="board-placeholder",
            )
        )
        yield Footer()
