import reflex as rx
import asyncio
from typing import Union, List
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.api.api import live, featured, api_Muebles,api_Modelos
from prueba_func.model.Featured import Featured
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.model.MODELOS import MODELOS



USER = "esteban"

class PageState(rx.State):
    is_live: bool
    featured_info: list[Featured] = []
    mueble_info: list[MUEBLES] = []
    modelo_info: list[MODELOS] = []
         
    
    async def initialize_state(self):
        await asyncio.gather(
            self.check_live(),
            self.featured_links(),
            self.muebles_links(),
            self.modelo_links(),
        )

    async def check_live(self):
        self.is_live = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()

    async def muebles_links(self):
        self.mueble_info = await api_Muebles()
        print(self.mueble_info)

    async def modelo_links(self):
        self.modelo_info = await api_Modelos()
        print(self.modelo_info)





SUPABASE_API = SupabaseAPI()

class MuebleState(rx.State):
    muebles: list[MUEBLES] = []
    tab_selected: str = "tab0"

    async def load_muebles(self):
        # Cargar los muebles desde la API
        self.muebles = await api_Muebles()

    def change_tab(self, value: str):
        self.tab_selected = value



SUPABASE_API = SupabaseAPI()

class ModelosState(rx.State):
    
    modelos: list[MODELOS] = []
    acor_selected: str = ""

    async def load_modelos(self):
        # Cargar los muebles desde la API
        self.modelos = await api_Modelos()

    def change_acor(self, value: Union[str, List[str]]):
        if isinstance(value, str):
            self.acor_selected = value
        elif isinstance(value, list):
            # Si se pasa una lista, tomar el primer valor o manejarlo como desees
            self.acor_selected = value[0] if value else ""











