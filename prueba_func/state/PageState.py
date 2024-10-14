import reflex as rx
from prueba_func.api.api import live

USER = "esteban"

class PageState(rx.State):
    
    is_live: bool
    
    async def check_live(self):
        self.is_live = await live(USER)
