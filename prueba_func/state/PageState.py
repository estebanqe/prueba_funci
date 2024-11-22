import reflex as rx
from prueba_func.api.api import live, featured, Herrajes, api_Muebles
from prueba_func.model.Featured import Featured
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES

USER = "esteban"

class PageState(rx.State):
    is_live: bool
    featured_info: list[Featured] = []
    herraje_info: list[HERRAJES] = []
    mueble_info: list[MUEBLES] = []
    
    
        
    
    async def initialize_state(self):
        await self.check_live()
        await self.featured_links()
        await self.herrajes_links()
        await self.muebles_links()

    async def check_live(self):
        self.is_live = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()

    async def herrajes_links(self):
        self.herraje_info = await Herrajes()

    async def muebles_links(self):
        self.mueble_info = await api_Muebles()
        print(self.mueble_info)
        
    
    