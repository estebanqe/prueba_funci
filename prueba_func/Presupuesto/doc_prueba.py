import reflex as rx
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.api.api import api_Muebles

SUPABASE_API = SupabaseAPI()

class State(rx.State):
    muebles: list[MUEBLES] = []
    tab_selected: str = "tab0"

    async def load_muebles(self):
        # Cargar los muebles desde la API
        self.muebles = await api_Muebles()

    def change_tab(self, value: str):
        self.tab_selected = value

# Usamos on_mount para cargar los datos al montar el componente
def doc_prueba():
    return rx.container(
        
       rx.scroll_area(
            # Componente de Tabs
            rx.tabs.root(
                
                    rx.tabs.list(
                        rx.foreach(
                            State.muebles,
                            lambda mueble, index: 
                                rx.tabs.trigger(
                                    mueble.mueble,  # Usamos el nombre del mueble como título de la pestaña
                                    value=f"tab{index}",
                                    color="white"
                                )
                        )
                    ),
                
                
                
                rx.foreach(
                    State.muebles,
                    lambda mueble, index: rx.tabs.content(
                        rx.vstack(
                            rx.heading(mueble.mueble, color="white"),
                            rx.image(
                                src=mueble.url_image,
                                height="200px",
                                width="auto",
                            ),
                            rx.text(mueble.descripcion, color="white")
                        ),
                        value=f"tab{index}",
                    )
                ),
                value=State.tab_selected,
                on_change=State.change_tab,
                default_value="tab0",
                on_mount=State.load_muebles,
            ),
        scrollbars="horizontal",
        type="always",
       ),
    )