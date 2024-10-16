import reflex as rx
import prueba_func.utils as utils
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size
from prueba_func.components.navbar import navbar
from prueba_func.components.footer import footer
from prueba_func.views.header import header
from prueba_func.views.index_links import index_links
from prueba_func.views.sponsors import sponsors
import prueba_func.state.PageState as PageState
from prueba_func.state.PageState import PageState


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
    on_load=[PageState.check_live, PageState.featured_links]
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    live=PageState.is_live
                ),
                index_links(PageState.featured_info),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                
            )
        ),
        footer(),
        
    )