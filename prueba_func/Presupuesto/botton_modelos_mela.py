import reflex as rx
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing

def botton_modelos_mela (title: str,
                body: str,
                image: str,
                # url: str,
                # is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:

    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.SUPER_VERY_BIG.value,
                height=Size.SUPER_VERY_BIG.value,
                margin=Size.MEDIUM.value,
                alt=title,
                
            ),
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.LARGE.value,
                    style=styles.button_title_style
                ),
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value,
                    style=styles.button_body_style
                ),
                align_items="center",
                spacing=Spacing.VERY_SMALL.value,
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value
            ),
            align="center",
            width="100%",
            justify="center"
        ),
        border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        # on_click=rx.redirect(path=url, external=is_external)
    )