# application/game/choose_base_type_use_case.py

from uuid import UUID
from dataclasses import dataclass

from ratio_chartarum.application.ports.game_repository_port import GameRepositoryPort
from ratio_chartarum.application.ports.random_port import RandomPort


@dataclass(frozen=True)
class ChooseBaseTypeResult:
    game_id: UUID
    base_type: str


class ChooseBaseTypeUseCase:

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
        base_type: str,
    ) -> ChooseBaseTypeResult:

        # 1️⃣ Obtener partida
        game = self._game_repository.get_by_id(game_id)
        if game is None:
            raise ValueError("Game not found")

        # 2️⃣ Resolver azar si corresponde
        resolved_base_type = base_type

        if base_type == "random":
            resolved_base_type = self._random.choice(
                ["fortaleza", "flota"]
            )

        # 3️⃣ Delegar validación al dominio
        game.choose_base_type(resolved_base_type)

        # 4️⃣ Persistir
        self._game_repository.save(game)

        # 5️⃣ Retornar resultado
        return ChooseBaseTypeResult(
            game_id=game.id,
            base_type=resolved_base_type,
        )