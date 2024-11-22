    

import reflex as rx
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.model.MODELOS import MODELOS
from prueba_func.estilo.estilo import Size, Spacing,TextColor
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.Presupuesto.hereda.acordion_opc_disen import acordion_material_melamina
from prueba_func.api.api import api_Modelos

SUPABASE_API = SupabaseAPI()

class State(rx.State):
    modelos: list[MODELOS] = []
    acor_selected: str = "tab0"

    async def load_modelos(self):
        # Cargar los muebles desde la API
        self.modelo = await api_Modelos()

    def change_acor(self, value: str):
        self.acor_selected = value

def acordion_datos_escrit() -> rx.Component:
    return rx.container(
        rx.accordion.root(
            rx.accordion.item(
                
                rx.foreach(
                        State.modelos,
                        lambda modelo, index: 
                            rx.accordion.header(
                                modelo.modelo,  # Usamos el nombre del mueble como título de la pestaña
                                value=f"tab{index}",
                                color="white"
                            )
                ),
                
                content=rx.accordion.content(
                    rx.vstack(
                    
                    botton_modelos_mela(
                        "Escritorio cajon lateral",
                        "tenemos 3 opciones para ti",
                        "/modelos/escritorio_cajon_lateral.jpeg",
                        ),
                        
                        spacing=Spacing.VERY_SMALL.value,
                        width="100%",
                        justify="center",
                        align="center"
                    ),
                    acordion_material_melamina(),
                ),
            ),
            rx.accordion.item(
                header=rx.accordion.header("escritorio cajon superior",color="white"),  # Utiliza el header correcto
                content=rx.accordion.content(
                    rx.vstack(
                    
                    botton_modelos_mela(
                        "Escritorio cajon superior",
                        "tenemos 3 opciones para ti",
                        "/modelos/escritorio_cajon_superior.jpg",
                        ),
                        width="100%",
                        justify="center",
                        align="center"
                    ),
                    acordion_material_melamina(),
                ),
            ), 
            collapsible=True,
            width="100%",
            type="multiple",
            variant="ghost"
        )
        
        ),
    
    
