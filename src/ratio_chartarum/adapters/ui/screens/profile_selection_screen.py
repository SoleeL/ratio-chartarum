from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Static, Button, Footer
from typing_extensions import override


class ProfileSelectionScreen(Screen):
    ROUTE = "profile_selection"

    BTN_BACK_ID = "back"

    @override
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Profile Selection Screen")
        yield Button("Volver", id=self.BTN_BACK_ID)
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == self.BTN_BACK_ID:
            self.app.pop_screen()