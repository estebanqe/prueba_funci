import reflex as rx
from prueba_func.estilo.estilo import Size
from prueba_func.estilo.colors import Color, TextColor 

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )