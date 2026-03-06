# application/game/select_base_use_case.py

from uuid import UUID
from dataclasses import dataclass

from ratio_chartarum.application.ports.game_repository_port import GameRepositoryPort
from ratio_chartarum.application.ports.random_port import RandomPort


@dataclass(frozen=True)
class SelectBaseResult:
    game_id: UUID
    player_base_id: UUID
    cpu_base_id: UUID
    phase: str


class SelectBaseUseCase:

    def __init__(
        self,
        game_repository: GameRepositoryPort,
        random_port: RandomPort,
    ) -> None:
        self._game_repository = game_repository
        self._random = random_port

    # ---------------------------------------------------------

    def execute(
        self,
        game_id: UUID,
        player_base_id: UUID,
        available_cpu_base_ids: list[UUID],
    ) -> SelectBaseResult:

        # 1️⃣ Obtener partida
        game = self._game_repository.get_by_id(game_id)
        if game is None:
            raise ValueError("Game not found")

        # 2️⃣ Seleccionar base CPU aleatoriamente
        if not available_cpu_base_ids:
            raise ValueError("No CPU bases available")

        cpu_base_id = self._random.choice(available_cpu_base_ids)

        # 3️⃣ Delegar validaciones al dominio
        game.select_cpu_base(cpu_base_id)
        game.select_player_base(player_base_id)

        # 4️⃣ Persistir cambios
        self._game_repository.save(game)

        # 5️⃣ Retornar resultado
        return SelectBaseResult(
            game_id=game.id,
            player_base_id=player_base_id,
            cpu_base_id=cpu_base_id,
            phase=game.phase.value,
        )