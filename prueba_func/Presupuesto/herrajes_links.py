import reflex as rx
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing, TextColor
from prueba_func.model.Herrajes_list import Herrajes_list


def herrajes_links(herra: Herrajes_list) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.text(
                herra.herraje,
                herra.unidades,
                herra.valor,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Spacing.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
          
    )