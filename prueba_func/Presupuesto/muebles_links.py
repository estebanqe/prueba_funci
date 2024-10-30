import reflex as rx
import prueba_func.constants as const
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
from prueba_func.components.link_material import link_material
from prueba_func.state.PageState import PageState

def muebles_links() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.foreach(
                PageState.mueble_fila_info,
                lambda mueble: rx.tabs.trigger(rx.text(mueble), value=mueble,color=TextColor.BODY.value)
            )
        ),
        rx.foreach(
            PageState.mueble_fila_info,
            lambda mueble: rx.tabs.content(
                rx.text(f"Descripción para {mueble}",color=TextColor.BODY.value),
                rx.vstack(
                    rx.button(f"el botton de {mueble} #1",color=TextColor.BODY.value),
                     link_material(
                        "Mueble",
                        "dimension 2.12 x 2.44 m",
                        "/modelos/escritorio-melamina.jpg"
                    ),
                ),
                rx.button(f"el botton de {mueble} #2",color=TextColor.BODY.value),
                value=mueble,
                align_items="start",
                width="100%",
            )
        ),
        default_value=rx.cond(
            PageState.mueble_fila_info,
            PageState.mueble_fila_info[0],
            ""
        )
    )
