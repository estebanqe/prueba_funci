import reflex as rx
import prueba_func.constants as const
from prueba_func.routes import Route
from prueba_func.components.link_button import link_button
from prueba_func.components.link_material import link_material
from prueba_func.components.title import title
from prueba_func.components.newsletter import newsletter
from prueba_func.estilo.estilo import Color, Spacing, Size


def courses_links() -> rx.Component:
    return rx.vstack(
        link_button(
            "Pagina Principal",
            "nuestros catalogos y contactos",
            "/icons/book-solid.svg",
            Route.INDEX.value,
            False,
            Color.SECONDARY.value
        ),
        title("Melamina en Diferentes Colores"),
        link_material(
            "Agave",
            "dimension 2.12 x 2.44 m",
            "/material/Agave.jpg"
        ),
        link_material(
            "Arupo",
            "dimension 2.12 x 2.44 m",
            "/material/Arupo.jpg"
        ),
        link_material(
            "Bardolino",
            "dimension 2.12 x 2.44 m",
            "/material/Bardolino.jpg"
        ),
        link_material(
            "Fumé",
            "dimension 2.12 x 2.44 m",
            "/material/Fumé.jpg"
        ),
        link_material(
            "Milán",
            "dimension 2.12 x 2.44 m",
            "/material/Milán.jpg"
        ),
        link_material(
            "Nazca",
            "dimension 2.12 x 2.44 m",
            "/material/Nazca.jpg"
        ),
        link_material(
            "Panela",
            "dimension 2.12 x 2.44 m",
            "/material/Panela.jpg"
        ),
        link_material(
            "Tivoli",
            "dimension 2.12 x 2.44 m",
            "/material/Tivoli.jpg"
        ),
         link_material(
            "Toquilla",
            "dimension 2.12 x 2.44 m",
            "/material/Toquilla.jpg"
        ),
        link_button(
            "Cotizacion",
            "cotizacion tu Productos",
            "/icons/book-solid.svg",
            Route.COTIZAR.value,
            False,
            Color.PRO.value
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
        padding_top=Size.BIG.value
    )