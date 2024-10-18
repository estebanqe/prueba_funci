import reflex as rx
import prueba_func.estilo.estilo as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style
    )