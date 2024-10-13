import reflex as rx
import prueba_func.estilo.estilo as style
from prueba_func.routes import Route
from prueba_func.estilo.estilo import Size
from prueba_func.estilo.colors import Color



def navbar() -> rx.Component:
    return rx.hstack(            #encabezado
            rx.link(     
                rx.box(
                    rx.text("Amorcito",as_="span",color=Color.PRIMARY.value),
                    rx.text(" te amo",as_="span",color=Color.SECONDARY.value),
                    style=style.navbar_title_style
                ),
                href=Route.INDEX.value,
            ),   
            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=Size.BIG.value,
            padding_y=Size.DEFAULT.value,
            z_index="999",                                  #para que siempre apareciera arriba
            top="0"                                         #para que se mantenga la parte superior estatica
        )