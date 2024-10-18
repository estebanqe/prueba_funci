import reflex as rx
from prueba_func.estilo.estilo import Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            height=Size.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )