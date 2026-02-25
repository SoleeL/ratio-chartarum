# src/ui.py
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class JuegoApp(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("¡Bienvenido a mi juego de terminal!")

    async def on_key(self, event):
        if event.key == "q":
            await self.action_quit()