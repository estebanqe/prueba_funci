import reflex as rx
from prueba_func.state.PageState import PageState
from prueba_func.Presupuesto.hereda.acordion_datos_escrit import ModeloState
from prueba_func.routes import Route
from prueba_func.estilo.estilo import Color, Spacing   
from prueba_func.components.link_button import link_button
from prueba_func.components.title import title 
from prueba_func.Presupuesto.hereda.modelos_melamina import modelos_melamina
from prueba_func.Presupuesto.doc_prueba import doc_prueba
from prueba_func.Presupuesto.muebles_links import muebles_links

from prueba_func.Presupuesto.muestra_muebles_link import muestra_muebles_link
from prueba_func.Presupuesto.mostrar_columna import muestra_modelos_link





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
     

        # title("Modelos"),
        # modelos_melamina(),
        
       
        # title("prueba con mi papai"),
        # doc_prueba(),
        
        
         # Título para los Muebles y el componente dinámico de muebles_links
        title("Muebles"),
        muebles_links(),  # Llama al componente muebles_links que contiene los tabs


        title("muestra de valores"), 
        rx.cond(
            PageState.mueble_info,
            rx.vstack(
                rx.flex(
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
        
        
        title("modelos"),
        rx.cond(
            ModeloState.modelos,
            rx.vstack(
                
                rx.flex(
                    
                    rx.foreach(
                        ModeloState.modelos,
                          muestra_modelos_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value
                ),
                spacing=Spacing.DEFAULT.value
            )
        ),
      
          
          
       
        width="100%",
        spacing=Spacing.DEFAULT.value,
       
    )
