from dependency_injector import containers, providers

# Repositories
from ratio_chartarum.adapters.persistence.in_memory_deck_repository import (InMemoryDeckRepository)
from ratio_chartarum.application.game.choose_base_type_use_case import (
    ChooseBaseTypeUseCase,
)
from ratio_chartarum.application.game.get_game_state_use_case import (
    GetGameStateUseCase,
)
from ratio_chartarum.application.game.select_base_use_case import SelectBaseUseCase
# Use cases
from ratio_chartarum.application.game.start_game_use_case import StartGameUseCase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "ratio_chartarum.adapters.ui",
        ]
    )

    # repositories
    deck_repository = providers.Singleton(
        InMemoryDeckRepository
    )

    # use cases
    start_game_use_case = providers.Factory(
        StartGameUseCase,
        deck_repository=deck_repository,
    )

    choose_base_type_use_case = providers.Factory(
        ChooseBaseTypeUseCase,
    )

    select_base_use_case = providers.Factory(
        SelectBaseUseCase,
    )

    get_game_state_use_case = providers.Factory(
        GetGameStateUseCase,
    )
