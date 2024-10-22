import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.components.link_button import link_button
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.components.title import title
from prueba_func.estilo.estilo import Color, Spacing
from prueba_func.Presupuesto.hereda.modelos_melamina import modelos_melamina
from prueba_func.state.PageState import PageState
from prueba_func.Presupuesto.herrajes_links import herrajes_links

def cotizar_links() -> rx.Component:
    return rx.vstack(
        link_button(
            "Pagina Principal",
            "nuestros catalogos y contactos",
            "/icons/book-solid.svg",
            Route.INDEX.value,
            False,
            Color.SECONDARY.value
        ),
        link_button(
            "Catálogo de Materiales",
            "Explora el catálogo completo de materiales disponibles",
            "/icons/book-solid.svg",
            Route.COURSES.value,
            False,
            Color.SECONDARY.value
        ),
        title("Modelos"),
        modelos_melamina(),
        
       
    rx.cond(
        PageState.herraje_info,
        rx.vstack(
            title("Destacado"),
            rx.box(
                rx.vstack(
                    rx.foreach(
                        PageState.herraje_info,
                        herrajes_links
                    ),
                ),
                
                flex_direction=["column", "row"],
                spacing=Spacing.DEFAULT.value
            ),
            spacing=Spacing.DEFAULT.value,
            width="200%",
        )
    ), 
        
        
        width="100%",
        spacing=Spacing.DEFAULT.value,
        on_mount=PageState.herrajes_links  
    )
