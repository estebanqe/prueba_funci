import reflex as rx
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing,TextColor
from prueba_func.Presupuesto.color_material import color_material
from prueba_func.Presupuesto.grosor_material import grosor_material



def acordion_opc_disen() -> rx.Component:
    return rx.accordion.root(
            rx.accordion.item(
                header=rx.accordion.header("material"),  # Utiliza el header correcto
                content=rx.accordion.content(
                    rx.vstack(
                        color_material(),
                        grosor_material(),
                        spacing=Spacing.VERY_SMALL.value,
                        width="100%",
                        justify="center",
                        align="center"
                    ),
                ),
            ),
            rx.accordion.item(
                header=rx.accordion.header("filos"),  # Utiliza el header correcto
                content=rx.accordion.content(
                    rx.vstack(
                        rx.list(
                            rx.list.item("color"),
                            rx.list.item("tipo"),
                        ),
      
                        spacing=Spacing.VERY_SMALL.value,
                        width="100%",
                        justify="center",
                        align="center"
                    ),
                ),
            ),  
            
            rx.accordion.item(
                header=rx.accordion.header("personalizacion"),  # Utiliza el header correcto
                content=rx.accordion.content(
                    rx.vstack(
                        rx.list(
                            rx.list.item("puertas"),
                            rx.list.item("tipo de abertura"),
                        ),
                        spacing=Spacing.VERY_SMALL.value,
                        width="100%",
                        justify="center",
                        align="center"
                    ),
                ),
            ),  
            
            spacing=Spacing.VERY_SMALL.value,
            collapsible=True,
            width="100%",
            type="single",
            variant="ghost"
        )
