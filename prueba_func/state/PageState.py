import reflex as rx
from prueba_func.api.api import live, featured, Herrajes
from prueba_func.model.Featured import Featured
from prueba_func.model.var_herraje import var_herraje
USER = "esteban"

class PageState(rx.State):
    
    is_live: bool
    featured_info: list[Featured]
    herraje_info: list[var_herraje] = []

    
    async def check_live(self):
        self.is_live = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()
        
    async def herrajes_links(self):
        self.herraje_info = await Herrajes()
