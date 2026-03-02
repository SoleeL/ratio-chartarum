from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from typing_extensions import Self, override


class ClassicModeScreen(Screen):
    ROUTE = "classic_mode"

    BTN_CONTINUE_ID = "continue-game"
    BTN_NEW_ID = "new-game"
    BTN_BACK_ID = "back"

    @override
    def compose(self: Self) -> ComposeResult:
        yield Static("Deck Clásico: Mazo de 60 cartas")
        yield Button("Continuar partida", id=self.BTN_CONTINUE_ID)
        yield Button("Nueva partida", id=self.BTN_NEW_ID)
        yield Button("Volver", id=self.BTN_BACK_ID)

    def on_button_pressed(self: Self, event: Button.Pressed) -> None:
        if event.button.id == self.BTN_CONTINUE_ID:
            # Navegar para seleccionar una partida guardada
            pass
        elif event.button.id == self.BTN_NEW_ID:
            # Navegar para seleccionar una partida guardada
            pass
        elif event.button.id == self.BTN_BACK_ID:
            self.app.pop_screen()
