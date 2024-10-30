import reflex as rx
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
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
                value=mueble
            )
        ),
        default_value=rx.cond(
            PageState.mueble_fila_info,
            PageState.mueble_fila_info[0],
            ""
        )
    )
