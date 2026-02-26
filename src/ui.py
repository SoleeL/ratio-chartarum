# src/ui.py

from typing import ClassVar

from textual import events, on
from textual.app import App, ComposeResult
from textual.binding import Binding, BindingType
from textual.widgets import Footer, Header, Static
from typing_extensions import Self, override


class JuegoApp(App):
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("d", "toggle_dark", "Toggle dark mode")
    ]

    @override
    def compose(self: Self) -> ComposeResult:
        yield Header()
        yield Static("¡Bienvenido a mi juego de terminal!")
        yield Footer()

    @on(events.Key)
    async def on_key(self: Self, event: events.Key) -> None:
        if event.key == "q":
            await self.action_quit()

    @override
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
