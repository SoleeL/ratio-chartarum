class StartGameUseCase:

    def __init__(self, engine: GameEngine):
        self.engine = engine

    def execute(self, player_deck_id: UUID):
        self.engine.select_cpu_deck()
        self.engine.advance_phase()