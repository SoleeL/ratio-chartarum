from uuid import UUID
from random import choice
from typing import Iterable

from ratio_chartarum.application.ports.deck_repository_port import DeckRepositoryPort
from ratio_chartarum.domain.game.entities.deck import Deck


class InMemoryDeckRepository(DeckRepositoryPort):

    def __init__(self) -> None:
        self._decks: dict[UUID, Deck] = {}

    def get_by_id(self, deck_id: UUID) -> Deck | None:
        return self._decks.get(deck_id)

    def get_random(self, exclude_id: UUID | None = None) -> Deck | None:
        decks = [
            deck for deck_id, deck in self._decks.items()
            if deck_id != exclude_id
        ]
        return choice(decks) if decks else None

    def list_all(self) -> Iterable[Deck]:
        return self._decks.values()

    # helper para desarrollo
    def add(self, deck: Deck) -> None:
        self._decks[deck.id] = deck