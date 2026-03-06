# application/ports/deck_repository_port.py

from uuid import UUID
from typing import Protocol, Iterable

from ratio_chartarum.domain.game.entities.deck import Deck


class DeckRepositoryPort(Protocol):

    def get_by_id(self, deck_id: UUID) -> Deck | None:
        """Obtiene un deck por su ID."""
        ...

    def get_random(self, exclude_id: UUID | None = None) -> Deck | None:
        """
        Obtiene un deck aleatorio.
        Puede excluir un ID (por ejemplo el del jugador).
        """
        ...

    def list_all(self) -> Iterable[Deck]:
        """Lista todos los decks disponibles."""
        ...