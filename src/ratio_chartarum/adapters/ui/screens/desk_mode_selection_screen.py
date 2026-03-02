from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from typing_extensions import override, Self


class DeskModeSelectionScreen(Screen):
    ROUTE = "deck_mode_selection"

    BTN_BACK_ID = "back"

    @override
    def compose(self: Self) -> ComposeResult:
        yield Header()
        yield Static("Deck Mode Selection Screen")
        yield Button("Volver", id=self.BTN_BACK_ID)
        yield Footer()

    def on_button_pressed(self: Self, event: Button.Pressed) -> None:
        if event.button.id == self.BTN_BACK_ID:
            self.app.pop_screen()