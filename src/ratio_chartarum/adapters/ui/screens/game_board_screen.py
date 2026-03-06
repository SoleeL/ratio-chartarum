from uuid import UUID

from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Footer, Header, Static, Button
from typing_extensions import Self, override

from dependency_injector import containers, providers

from ratio_chartarum.application.game.start_game_use_case import StartGameUseCase
from ratio_chartarum.application.game.choose_base_type_use_case import ChooseBaseTypeUseCase
from ratio_chartarum.application.game.select_base_use_case import SelectBaseUseCase
from ratio_chartarum.application.game.get_game_state_use_case import GetGameStateUseCase

class GameBoardScreen(Screen):

    BINDINGS = [("q", "quit", "Quit")]

    def __init__(
        self,
        deck_id: UUID,
        start_game_uc: StartGameUseCase,
        choose_base_type_uc: ChooseBaseTypeUseCase,
        select_base_uc: SelectBaseUseCase,
        get_state_uc: GetGameStateUseCase,
    ) -> None:
        super().__init__()
        self.deck_id = deck_id

LEER DE NUEVO LA DI RECOMENDAD POR CHATGPT

        # Use cases (ports inward)
        self._start_game = self.app.start_game_uc
        self._choose_base_type = self.app.choose_base_type_uc
        self._select_base = self.app.select_base_uc
        self._get_state = self.app.get_state_uc

        self._game_id: UUID | None = None

    # ---------------------------------------------------------
    # LIFECYCLE
    # ---------------------------------------------------------

    async def on_mount(self) -> None:
        """
        Al montar la screen:
        - ejecutamos StartGame
        - obtenemos estado inicial
        - renderizamos
        """
        result = self._start_game.execute(self.deck_id)
        self._game_id = result.game_id
        self._render()

    # ---------------------------------------------------------
    # RENDER
    # ---------------------------------------------------------

    @override
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(id="content")
        yield Footer()

    def _render(self) -> None:
        """Renderiza según el estado actual del juego."""
        if self._game_id is None:
            return

        state = self._get_state.execute(self._game_id)

        container = self.query_one("#content", Container)
        container.remove_children()

        if state.phase == "BASE_TYPE_SELECTION":
            container.mount(
                Static("Selecciona tipo de BASE"),
                Button("Fortaleza", id="base_fortaleza"),
                Button("Flota", id="base_flota"),
                Button("Azar", id="base_random"),
            )

        elif state.phase == "BASE_SELECTION":
            container.mount(
                Static("Selecciona tu BASE específica"),
            )

            for base in state.available_bases:
                container.mount(
                    Button(base.name, id=f"base_{base.id}")
                )

        elif state.phase == "BOARD":
            container.mount(
                Static("Tablero listo para comenzar la batalla"),
            )

    # ---------------------------------------------------------
    # EVENTS
    # ---------------------------------------------------------

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if self._game_id is None:
            return

        button_id = event.button.id

        if button_id in {"base_fortaleza", "base_flota", "base_random"}:
            self._choose_base_type.execute(
                game_id=self._game_id,
                base_type=button_id.removeprefix("base_"),
            )
            self._render()
            return

        if button_id and button_id.startswith("base_"):
            base_id = UUID(button_id.removeprefix("base_"))
            self._select_base.execute(
                game_id=self._game_id,
                base_id=base_id,
            )
            self._render()
            return

    # ---------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------

    def action_quit(self) -> None:
        self.app.pop_screen()






# class GameBoardScreen(Screen):

    # ETAPAS:
    # 1. [Proceso en segundo plano] Seleccion aleatoria de faccion y deck contra el que se jugara (CPU)
    # 2. [Modal] Seleccion de tipo de BASE (Se basa en que una FLOTA ataca a una FORTALEZA):
    #   2.1. FORTALEZA (Base fija): Menor ataque, mayor defensa
    #   2.2. FLOTA (Base movil): Mayor ataque, menor defensa
    #   2.3. AZAR: Se selecciona el tipo de BASE aleatoriamente
    # 3. Seleccion de BASE especifica (Son lugares fisicos o conjunto de naves):
    #   3.1. [Proceso en segundo plano] Seleccion aleatoria de la BASE especifica con la que jugara la CPU
    #   3.2. [Modal] Seleccion de la base del jugador
    #       3.2.1. Listado de las bases disponibles segun el tipo de BASE
    #       3.2.2. Opcion de seleccion aleatoria segun el tipo de BASE
    # 4. Tras esto se presenta el tablero para comenzar a jugar

    # def __init__(self, deck_id: UUID) -> None:
    #     super().__init__()
    #     self.deck_id: UUID = deck_id
    #
    # @override
    # def compose(self: Self) -> ComposeResult:
    #     yield Header(show_clock=True)
    #     yield Container(
    #         Static(
    #             f"Aquí va el tablero del juego (Deck ID: {self.deck_id})",
    #             id="board-placeholder",
    #         )
    #     )
    #     yield Footer()
