from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from ratio_chartarum.application.ports.game_repository_port import GameRepositoryPort

@dataclass(frozen=True)
class GameStateDTO:
    game_id: UUID
    phase: str

    player_deck_name: str
    cpu_deck_name: str

    base_type: Optional[str]
    player_base_id: Optional[UUID]
    cpu_base_id: Optional[UUID]

    is_ready: bool

class GetGameStateUseCase:

    def __init__(self, game_repository: GameRepositoryPort) -> None:
        self._game_repository = game_repository

    # ---------------------------------------------------------

    def execute(self, game_id: UUID) -> GameStateDTO:

        game = self._game_repository.get_by_id(game_id)
        if game is None:
            raise ValueError("Game not found")

        return GameStateDTO(
            game_id=game.id,
            phase=game.phase.value,

            player_deck_name=game.player_deck.name,
            cpu_deck_name=game.cpu_deck.name,

            base_type=game.base_type,
            player_base_id=game.player_base_id,
            cpu_base_id=game.cpu_base_id,

            is_ready=game.is_ready(),
        )