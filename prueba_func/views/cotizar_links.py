import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.components.link_button import link_button
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.components.title import title
from prueba_func.estilo.estilo import Color, TextColor, Spacing
# from prueba_func.Presupuesto.acordion_datos_escrit import acordion_datos_escrit
from prueba_func.Presupuesto.modelos_melamina import modelos_melamina


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
        # botton_modelos_mela(
        #     "Escritorio",
        #     "tenemos 3 opciones para ti",
        #     "/modelos/escritorio-melamina.jpg",
        #     const.TABLA_PICAR
        # ),
        rx.spacer(),      
        # acordion_datos(),
        rx.spacer(),
        modelos_melamina(),
        
        width="100%",
        spacing=Spacing.DEFAULT.value
    )
