# domain/game/entities/deck.py

from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class Deck:
    """
    Entidad del dominio que representa un mazo jugable.
    Es inmutable porque durante una partida no debería cambiar.
    """

    id: UUID
    name: str
    faction: str

    units: int
    accessories: int
    pilots: int
    orders: int

    wins: int = 0
    losses: int = 0

    # ---------------------------------------------------------
    # Domain behavior
    # ---------------------------------------------------------

    def total_cards(self) -> int:
        return self.units + self.accessories + self.pilots + self.orders

    def win_rate(self) -> float:
        total = self.wins + self.losses
        if total == 0:
            return 0.0
        return self.wins / total