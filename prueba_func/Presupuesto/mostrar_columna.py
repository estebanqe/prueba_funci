import reflex as rx
from prueba_func.state.PageState import PageState

def mostrar_columna() -> rx.Component:
    return rx.vstack(
        # Renderizar lista de muebles
        
        
        rx.cond(
            PageState.mueble_fila_info,  # Verifica si hay elementos en la lista
            rx.foreach(
                PageState.mueble_fila_info,  # Itera sobre la lista de muebles
                lambda mueble: rx.text(f"Mueble: {mueble}",color='white'),
            ),
            rx.text("No hay muebles disponibles.", color="white"),  # Si no hay elementos
        ),
        
        
        rx.cond(
            PageState.imagen_fila_info,  # Verifica si hay elementos en la lista
            rx.foreach(
                PageState.imagen_fila_info,  # Itera sobre la lista de URLs de imágenes
                lambda url_image: 
                    rx.link(f"URL de la imagen: {url_image}")
                    # rx.link(
                    #     rx.image(src=url_image, alt="url_image", width="100px"), 
                    #     href=url_image
                    # ),
            ),
            rx.text("No hay imágenes disponibles.", color="white"),  # Si no hay elementos
        ),
        
        
        
        rx.cond(
            PageState.descripcion_fila_info,  # Verifica si hay elementos en la lista
            rx.foreach(
                PageState.descripcion_fila_info,  # Itera sobre la lista de muebles
                lambda descripcion: rx.text(f"Mueble: {descripcion}",color='white'),
            ),
            rx.text("No hay descripciones disponibles.", color="white"),  # Si no hay elementos
        ),
        
        
        
        spacing="lg",
        align_items="stretch",
        class_name="fadein-animation"
    )
