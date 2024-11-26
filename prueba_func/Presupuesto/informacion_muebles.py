import reflex as rx
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing, Color
from prueba_func.model.MUEBLES import MUEBLES


def informacion_muebles(muestra_muebles: MUEBLES) -> rx.Component:
    

    return rx.link(
        rx.vstack(
            rx.image(
                src=muestra_muebles.url_image,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width=Size.VERY_BIG.value,
                height="100%",
                alt=f"Imagen destacada para: {muestra_muebles.mueble}"
            ),
            rx.text(
                muestra_muebles.mueble,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Spacing.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
    )