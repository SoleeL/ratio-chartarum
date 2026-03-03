from dataclasses import dataclass

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Static, Button, Footer
from typing_extensions import Self, override

from ratio_chartarum.adapters.ui.screens.game_board_screen import GameBoardScreen


@dataclass(slots=True)
class DeckSummary:
    id: str
    name: str
    wins: int
    losses: int
    faction: str
    units: int
    accessories: int
    pilots: int
    orders: int


def get_mock_decks() -> list[DeckSummary]:
    return [
        DeckSummary("d11", "Desk 1", 10, 3, "Facción Roja", 12, 5, 3, 8),
        DeckSummary("d12", "Desk 2", 4, 6, "Facción Azul", 10, 4, 2, 7),
        DeckSummary("d13", "Desk 3", 15, 2, "Facción Verde", 14, 6, 4, 9),
        DeckSummary("d14", "Desk 4", 7, 8, "Facción Amarilla", 11, 3, 3, 6),
        DeckSummary("d15", "Desk 5", 20, 1, "Facción Roja", 16, 8, 5, 10),
    ]


class DeskSelectionScreen(Screen):

    BTN_NEW_ID = "new_deck"
    BTN_BACK_ID = "back"

    def __init__(self) -> None:
        super().__init__()
        self.decks: list[DeckSummary] = get_mock_decks()

    @override
    def compose(self: Self) -> ComposeResult:
        yield Header()
        yield Static("Deck Selection Screen")

        # Botón crear nuevo
        yield Button("+ Nuevo deck", id=self.BTN_NEW_ID)

        # Listado dinámico
        for index, deck in enumerate(self.decks):
            yield Button(
                self._format_deck_label(deck),
                id=deck.id,
            )

        yield Button("Volver", id=self.BTN_BACK_ID)
        yield Footer()

    def _format_deck_label(self: Self, deck: DeckSummary) -> str:
        return (
            f"{deck.name} | "
            f"{deck.wins}W/{deck.losses}L | "
            f"{deck.faction} | "
            f"U:{deck.units} "
            f"A:{deck.accessories} "
            f"P:{deck.pilots} "
            f"O:{deck.orders}"
        )

    def on_button_pressed(self: Self, event: Button.Pressed) -> None:
        if event.button.id == self.BTN_NEW_ID:
            self.app.push_screen("deck_creation")  # TODO: Crear vista
        elif event.button.id.startswith("deck_"):
            self.app.push_screen(GameBoardScreen(deck_id=self.decks[event.button.id].id))
        elif event.button.id == self.BTN_BACK_ID:
            self.app.pop_screen()
