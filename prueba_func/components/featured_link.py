import reflex as rx
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing, Color
from prueba_func.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width="100%",
                height="auto",
                alt=f"Imagen destacada para: {featured.title}"
            ),
            rx.text(
                featured.title,
                size=Spacing.VERY_SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Spacing.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
        href=featured.url,
        is_external=True
    )