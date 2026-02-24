# src/ui.py
from textual.app import App
from textual.widgets import Header, Footer, Static

class JuegoApp(App):
    """Juego básico de ejemplo con Textual"""
    
    async def on_mount(self):
        """Se ejecuta al iniciar la app"""
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(Static("¡Bienvenido a mi juego de terminal!"), edge="left")

    async def on_key(self, event):
        """Captura teclas, por ejemplo 'q' para salir"""
        if event.key == "q":
            await self.action_quit()