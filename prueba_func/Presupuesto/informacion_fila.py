import reflex as rx
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
from prueba_func.components.link_material import link_material
from prueba_func.Presupuesto.muestra_muebles_link import muestra_muebles_link
from prueba_func.components.title import title
from prueba_func.state.PageState import PageState
from prueba_func.model.MUEBLES import MUEBLES







def informacion_fila (imagen_item: MUEBLES) -> rx.Component:
    return rx.hstack(
            rx.text(
                f"imagen: {imagen_item.image}",
                size=Spacing.SMALL.value,  # Ajusta el tamaño según tus necesidades
                style=styles.button_body_style
            ),
            rx.text(
                f"descripcion: {imagen_item.descripcion}",  # Mostrando las unidades
                size=Spacing.SMALL.value,
                style=styles.button_body_style
            ),
            # rx.text(
            #     f"Valor: ${var_herraje_item.valor:.2f}",  # Mostrando el valor con formato
            #     size=Spacing.SMALL.value,
            #     style=styles.button_body_style
            # ),
            spacing=Spacing.VERY_BIG.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        )    
