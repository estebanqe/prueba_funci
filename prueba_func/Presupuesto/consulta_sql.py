import reflex as rx
from prueba_func.estilo.estilo import Size, Spacing, Color
import prueba_func.estilo.estilo as styles
from prueba_func.state.PageState import CargarQLState
from prueba_func.model.MuebleConModelo import MuebleConModelo


def mostrar_muebles_con_modelos(sql_modelo: MuebleConModelo) -> rx.Component:
    """Genera un componente para mostrar un mueble con su modelo relacionado."""
    return rx.container(
        rx.vstack(
            # Texto con el nombre del mueble
            rx.text(
                sql_modelo.mueble,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style,
            ),
            # Imagen del mueble
            rx.image(
                src=sql_modelo.url_image_mueble,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width=Size.VERY_BIG.value,
                height="100%",
            ),
            # Descripción del mueble
            rx.text(
                sql_modelo.descripcion,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style,
            ),
            # Imagen del modelo relacionado
            rx.image(
                src=sql_modelo.url_image_modelo,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width=Size.VERY_BIG.value,
                height="100%",
            ),
            # Nombre del modelo relacionado
            rx.text(
                sql_modelo.modelo,  # Aquí corriges el texto a mostrar, era `sql_modelo.url_image_modelo`
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style,
            ),
        ),
        padding=Spacing.DEFAULT.value, 
        border_radius=Size.DEFAULT.value,
        width="100%",
    )
