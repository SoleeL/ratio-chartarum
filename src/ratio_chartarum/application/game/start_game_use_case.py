# application/game/start_game_use_case.py

from dataclasses import dataclass
from uuid import UUID

from ratio_chartarum.application.ports.deck_repository_port import DeckRepositoryPort
from ratio_chartarum.application.ports.game_repository_port import GameRepositoryPort
from ratio_chartarum.application.ports.random_port import RandomPort
from ratio_chartarum.domain.game.entities.game import Game


@dataclass(frozen=True)
class StartGameResult:
    game_id: UUID


class StartGameUseCase:

    def __init__(
            self,
            deck_repository: DeckRepositoryPort,
            game_repository: GameRepositoryPort,
            random_port: RandomPort,
    ) -> None:
        self._deck_repository = deck_repository
        self._game_repository = game_repository
        self._random = random_port

    # ---------------------------------------------------------

    def execute(self, player_deck_id: UUID) -> StartGameResult:
        # 1️⃣ Obtener deck del jugador
        player_deck = self._deck_repository.get_by_id(player_deck_id)

        if player_deck is None:
            raise ValueError("Player deck not found")

        # 2️⃣ Obtener deck CPU aleatorio
        cpu_deck = self._deck_repository.get_random(exclude_id=player_deck_id)

        if cpu_deck is None:
            raise ValueError("No CPU deck available")

        # 3️⃣ Crear entidad Game (dominio decide estado inicial)
        game = Game.create_new(
            player_deck=player_deck,
            cpu_deck=cpu_deck,
        )

        # 4️⃣ Persistir
        self._game_repository.save(game)

        # 5️⃣ Retornar DTO
        return StartGameResult(game_id=game.id)
