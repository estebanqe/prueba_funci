import reflex as rx
from prueba_func.estilo.estilo import Size, Spacing

def Link_sponsor(imagen: str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(   
            src=imagen,
            height="3.5em",     #alto del logo
            width="auto",
            # aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )