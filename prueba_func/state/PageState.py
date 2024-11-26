import reflex as rx
import asyncio
from typing import List
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.api.api import live, featured, api_Muebles,api_Modelos
from prueba_func.model.Featured import Featured
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.model.MODELOS import MODELOS
from prueba_func.model.MuebleConModelo import MuebleConModelo



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

    def change_acor(self, value: str):
        self.acor_selected = value






# tenemos la clase para llamar la lista modelos y usarla en el accordeon de los modelos 

SUPABASE_API = SupabaseAPI()

class ModeloState(rx.State):
    """State para manejar modelos y selección en el acordeón."""

    modelos: list[MODELOS] = []
    acor_selected: str = "acor_0"

    async def load_modelos(self):
        """Carga modelos desde la API."""
        try:
            print("Cargando modelos...")
            self.modelos = await api_Modelos()
            print(f"Modelos cargados: {len(self.modelos)}")
        except Exception as e:
            print(f"Error al cargar modelos: {e}")
            self.modelos = []  # Estado consistente si ocurre un error

    def change_selected(self, value: str):
        """Cambia el elemento seleccionado en el acordeón."""
        print(f"Nuevo valor seleccionado: {value}")
        self.acor_selected = value  # Actualiza el estado seleccionado


    def get_selected_model(self):
        """Obtiene el modelo correspondiente al valor seleccionado."""
        # Busca el modelo correspondiente al valor seleccionado en el acordeón
        selected_model = next((modelo for modelo in self.modelos if f"item_{modelo.id}" == self.acor_selected), None)
        return selected_model











# buscamos la forma de mostrar la informacion del sql
class CargarQLState(rx.State):
    muebles_con_modelos: List[MuebleConModelo] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si necesitas hacer algo con parent_state, lo haces aquí
        self.parent_state = kwargs.get("parent_state", None)

    async def cargar_muebles_con_modelos(self, id_mueble: int):
        """Carga muebles con modelos relacionados desde Supabase."""
        try:
            response = await SUPABASE_API.client.table("MUEBLES").select(
                "mueble, descripcion, url_image, MODELOS(modelo, url_image)"
            ).eq("id", id_mueble).execute()

            if response.data:
                # Depuración: Ver los datos obtenidos
                print(f"Datos obtenidos de la base de datos: {response.data}")
                
                # Crear los objetos MuebleConModelo
                self.muebles_con_modelos = [
                    MuebleConModelo(
                        mueble=item["mueble"],
                        descripcion=item["descripcion"],
                        url_image_mueble=item["url_image"],
                        modelo=item["MODELOS"]["modelo"],
                        url_image_modelo=item["MODELOS"]["url_image"],
                    )
                    for item in response.data
                ]
                print(f"Objetos cargados: {self.muebles_con_modelos}")
            else:
                print(f"No se encontraron muebles con el ID {id_mueble}")

        except Exception as e:
            print(f"Error al cargar muebles con modelos: {e}")
            self.muebles_con_modelos = []

    def __str__(self):
        # Devolvemos una representación legible de la clase, incluyendo los muebles con modelos
        return f"CargarQLState(muebles_con_modelos={self.muebles_con_modelos})"
