import reflex as rx
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.estilo.estilo import Color, Spacing, TextColor,Size
from prueba_func.api.api import api_Muebles
from prueba_func.Presupuesto.hereda.acordion_datos_escrit import acordion_datos_escrit

SUPABASE_API = SupabaseAPI()

class State(rx.State):
    muebles: list[MUEBLES] = []
    tab_selected: str = "tab0"

    async def load_muebles(self):
        # Cargar los muebles desde la API
        self.muebles = await api_Muebles()

    def change_tab(self, value: str):
        self.tab_selected = value

def muebles_links() -> rx.Component:
    return rx.container(
       
        # Componente de Tabs
        rx.tabs.root(
            rx.tabs.list(
                rx.foreach(
                    State.muebles,
                    lambda mueble, index: rx.tabs.trigger(
                        mueble.mueble,  # Usamos el nombre del mueble como título de la pestaña
                        value=f"tab{index}",
                        color="white"
                    )
                    
                ),
                size="2",
                width="100%",
                padding=Size.SMALL.value,
                
            ),
            
            rx.foreach(
                State.muebles,
                lambda mueble, index: 
                    rx.tabs.content(
                        rx.hstack(
                            rx.vstack(
                                rx.heading(mueble.mueble, color="white",width="100%",),
                                rx.image(
                                    src=mueble.url_image,
                                    height="auto",
                                    width="350px",
                                ),
                                rx.text(mueble.descripcion, color="white"),
                                
                            ),
                            
                            acordion_datos_escrit(),
                           
                            
                            
                        ),
                        
                    value=f"tab{index}",
                    # padding_left=Size.VERY_BIG.value,
                )
            ),
            value=State.tab_selected,
            on_change=State.change_tab,
            default_value="tab0",
            on_mount=State.load_muebles,
            orientation="horizontal",
            spacing=Spacing.BIG.value,
        ),
        
    )