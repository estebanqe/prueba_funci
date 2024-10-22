import reflex as rx
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing,TextColor
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.Presupuesto.hereda.acordion_opc_disen import acordion_material_melamina



def acordion_datos_escrit() -> rx.Component:
    return rx.accordion.root(
            rx.accordion.item(
                header=rx.accordion.header("escritorio cajon lateral"),  # Utiliza el header correcto
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
                header=rx.accordion.header("escritorio cajon superior"),  # Utiliza el header correcto
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
