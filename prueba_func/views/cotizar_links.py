import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.components.link_button import link_button
from prueba_func.Presupuesto.mostrar_columna import mostrar_columna
from prueba_func.components.title import title
from prueba_func.estilo.estilo import Color, Spacing
from prueba_func.Presupuesto.hereda.modelos_melamina import modelos_melamina
from prueba_func.state.PageState import PageState
from prueba_func.Presupuesto.muestra_muebles_link import muestra_muebles_link
from prueba_func.Presupuesto.doc_prueba import doc_prueba
from prueba_func.Presupuesto.muebles_links import muebles_links
from prueba_func.model.MUEBLES import MUEBLES




def cotizar_links(HERRAJES=[], MUEBLES=[]) -> rx.Component:
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
        rx.cond(
            PageState.mueble_info,
            rx.vstack(
                title("Destacado"),
                rx.box(
                    rx.foreach(
                        PageState.mueble_info,
                        muestra_muebles_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value
                ),
                spacing=Spacing.DEFAULT.value
            )
        ),

        title("Modelos"),
        modelos_melamina(),
        
        
        # rx.cond(
        #     PageState.imagen_fila_info,
        #     rx.vstack(
        #         title("Destacado"),
        #         rx.box(
        #             rx.vstack(
        #                 rx.foreach(
        #                     PageState.imagen_fila_info,
        #                     doc_prueba,
        #                 ),
        #             ),
        #             flex_direction=["column", "row"],
        #             spacing=Spacing.DEFAULT.value
        #         ),
        #         spacing=Spacing.DEFAULT.value,
        #         width="200%",
        #     )
        # ), 
        
        
        title("muestra de datos de columna"),
        mostrar_columna(),
          
        
        title("prueba"),
        # rx.cond(
        #     PageState.mueble_info,
        #     rx.vstack(
        #         title("ejemplo de prueba"),
        #         rx.box(
        #             rx.foreach(
        #                 PageState.mueble_info,
        #                 doc_prueba
        #             ),
        #             flex_direction=["column", "row"],
        #             spacing=Spacing.DEFAULT.value
        #         ),
        #         spacing=Spacing.DEFAULT.value
        #     )
        # ),
        doc_prueba(),

        
  
          
          
        # Título para los Muebles y el componente dinámico de muebles_links
        title("Muebles"),
        muebles_links(),  # Llama al componente muebles_links que contiene los tabs

        width="100%",
        spacing=Spacing.DEFAULT.value,
        on_mount=PageState.cargar_muebles,  # Llama a cargar los muebles al montar la página
    )
