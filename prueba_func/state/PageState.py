# import reflex as rx
# from prueba_func.api.api import live, featured, Herrajes, Muebles, Muebles_fila
# from prueba_func.model.Featured import Featured
# from prueba_func.model.HERRAJES import HERRAJES
# from prueba_func.model.MUEBLES import MUEBLES
# USER = "esteban"

# class PageState(rx.State):
    
#     is_live: bool
#     featured_info: list[Featured]
#     herraje_info: list[HERRAJES] = []
#     mueble_info: list[MUEBLES] = []
#     mueble_fila_info : list [MUEBLES] = []

    
#     async def check_live(self):
#         self.is_live = await live(USER)

#     async def featured_links(self):
#         self.featured_info = await featured()
        
#     async def herrajes_links(self):
#         self.herraje_info = await Herrajes()
        
#     async def muebles_links(self):
#         self.mueble_info = await Muebles()
    
    
#     async def cargar_muebles(self):
#         self.mueble_fila_info = await Muebles_fila()


    
    
    
import reflex as rx
from prueba_func.api.api import live, featured, Herrajes, Muebles, Muebles_fila, Muebles_imagen
from prueba_func.model.Featured import Featured
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES

USER = "esteban"

class PageState(rx.State):
    is_live: bool
    featured_info: list[Featured] = []
    herraje_info: list[HERRAJES] = []
    mueble_info: list[MUEBLES] = []
    mueble_fila_info: list[str] = []  # Lista de nombres de muebles
    mueble_imagen_info: list[MUEBLES] = []
    
    async def initialize_state(self):
        await self.check_live()
        await self.featured_links()
        await self.herrajes_links()
        await self.muebles_links()
        await self.cargar_muebles()
        await self.imagen_muebles()

    async def check_live(self):
        self.is_live = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()

    async def herrajes_links(self):
        self.herraje_info = await Herrajes()

    async def muebles_links(self):
        self.mueble_info = await Muebles()

    async def cargar_muebles(self):
        self.mueble_fila_info = await Muebles_fila()
        
    async def imagen_muebles(self):
        self.mueble_imagen_info = await Muebles_imagen()
