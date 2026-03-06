# domain/game/entities/game.py

from uuid import UUID, uuid4
from dataclasses import dataclass, field

from ratio_chartarum.domain.game.value_objects.phase import Phase
from ratio_chartarum.domain.game.entities.deck import Deck


@dataclass
class Game:
    id: UUID
    player_deck: Deck
    cpu_deck: Deck

    phase: Phase = field(default=Phase.BASE_TYPE_SELECTION)
    base_type: str | None = None
    player_base_id: UUID | None = None
    cpu_base_id: UUID | None = None

    # ---------------------------------------------------------
    # Factory
    # ---------------------------------------------------------

    @classmethod
    def create_new(cls, player_deck: Deck, cpu_deck: Deck) -> "Game":
        return cls(
            id=uuid4(),
            player_deck=player_deck,
            cpu_deck=cpu_deck,
            phase=Phase.BASE_TYPE_SELECTION,
        )

    # ---------------------------------------------------------
    # Behavior
    # ---------------------------------------------------------

    def choose_base_type(self, base_type: str) -> None:
        if self.phase != Phase.BASE_TYPE_SELECTION:
            raise ValueError("Cannot choose base type in current phase")

        if base_type not in {"fortaleza", "flota", "random"}:
            raise ValueError("Invalid base type")

        self.base_type = base_type
        self.phase = Phase.BASE_SELECTION

    # ---------------------------------------------------------

    def select_player_base(self, base_id: UUID) -> None:
        if self.phase != Phase.BASE_SELECTION:
            raise ValueError("Cannot select base in current phase")

        self.player_base_id = base_id

        # La CPU debería ya tener base seleccionada por aplicación
        if self.cpu_base_id is not None:
            self.phase = Phase.BOARD

    # ---------------------------------------------------------

    def select_cpu_base(self, base_id: UUID) -> None:
        if self.phase != Phase.BASE_SELECTION:
            raise ValueError("Cannot select CPU base in current phase")

        self.cpu_base_id = base_id

        if self.player_base_id is not None:
            self.phase = Phase.BOARD

    # ---------------------------------------------------------

    def is_ready(self) -> bool:
        return self.phase == Phase.BOARD