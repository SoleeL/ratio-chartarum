# application/ports/game_repository_port.py

from typing import Protocol, Iterable
from uuid import UUID

from ratio_chartarum.domain.game.entities.game import Game


class GameRepositoryPort(Protocol):
    """
    Puerto de salida para persistencia de partidas.
    La aplicación depende de esta abstracción,
    no de la implementación concreta.
    """

    def save(self, game: Game) -> None:
        """Guarda o actualiza una partida."""
        ...

    def get_by_id(self, game_id: UUID) -> Game | None:
        """Obtiene una partida por su ID."""
        ...

    def delete(self, game_id: UUID) -> None:
        """Elimina una partida."""
        ...

    def list_active(self) -> Iterable[Game]:
        """Lista partidas activas."""
        ...