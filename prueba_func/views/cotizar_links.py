import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
from prueba_func.components.link_button import link_button
from prueba_func.components.link_material import link_material
from prueba_func.components.title import title
from prueba_func.estilo.estilo import Color, Spacing
from prueba_func.api.form_ex import form_example


def cotizar_links() -> rx.Component:
    return rx.vstack(
        title("Enlaces"),
        link_button(
            "Cotiza tu producto",
            "Consulta mis tutoriales para aprender programación",
            "/icons/book-solid.svg",
            Route.COTIZAR.value,
            False,
            Color.SECONDARY.value
        ),
         link_button(
            "Catalago de Materiales",
            "Consulta mis tutoriales para aprender programación",
            "/icons/book-solid.svg",
            Route.COURSES.value,
            False,
            Color.SECONDARY.value
        ),
        
        title("Presupuesto"),
        
        form_example(),
        
       
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )