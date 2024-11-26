import reflex as rx
import prueba_func.utils as utils
import prueba_func.estilo.estilo as styles
from prueba_func.routes import Route
from prueba_func.components.navbar import navbar
from prueba_func.components.footer import footer
from prueba_func.views.header import header
from prueba_func.views.cotizar_links import cotizar_links
from prueba_func.views.sponsors import sponsors
from prueba_func.estilo.estilo import Size
from prueba_func.state.PageState import PageState


@rx.page(
    route=Route.COTIZAR.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta,
    on_load=[PageState.muebles_links,PageState.modelo_links]
)
def cotizar() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                cotizar_links(
                    PageState.mueble_info,
                    PageState.modelo_info,
                    
                ),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )