import reflex as rx
from prueba_func.api.api import live, featured, Herrajes, api_Muebles, Muebles_fila, Imagen_fila,Descripcion_fila
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
    imagen_fila_info: list[str] = []
    descripcion_fila_info: list[str] = []  # 
    
        
    
    async def initialize_state(self):
        await self.check_live()
        await self.featured_links()
        await self.herrajes_links()
        await self.muebles_links()
        await self.cargar_muebles()
        await self.cargar_ima()
        await self.cargar_descripcion()

    async def check_live(self):
        self.is_live = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()

    async def herrajes_links(self):
        self.herraje_info = await Herrajes()

    async def muebles_links(self):
        self.mueble_info = await api_Muebles()
        print(self.mueble_info)
        
    
    async def cargar_muebles(self):
        self.mueble_fila_info = await Muebles_fila()
        print(self.imagen_fila_info)

    async def cargar_ima(self):
            self.imagen_fila_info = await Imagen_fila()
            print(self.imagen_fila_info)
            
    async def cargar_descripcion(self):
        self.descripcion_fila_info = await Descripcion_fila()
        print(self.descripcion_fila_info)