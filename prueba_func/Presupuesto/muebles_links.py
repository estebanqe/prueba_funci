import reflex as rx
import prueba_func.constants as const
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
from prueba_func.state.PageState import PageState


def muebles_links() -> rx.Component:
    

    return rx.tabs.root(
        rx.tabs.list(
            rx.cond(
                PageState.mueble_fila_info,
                rx.foreach(
                    PageState.mueble_fila_info,
                    lambda mueble: 
                        rx.tabs.trigger(
                            rx.text(mueble),
                            value=mueble,
                            color=TextColor.BODY.value,
                            padding_right=Size.VERY_BIG.value,
                            align="center"  # Corrección de 'aling' a 'align'
                        )
                ),
                rx.text("No hay muebles disponibles.")  # Mensaje si no hay muebles
            )
        ),
        
        rx.foreach(
            PageState.mueble_fila_info,
            lambda mueble:
                rx.tabs.content(
                    rx.text(
                        f"Descripción para {mueble}",
                        color=TextColor.BODY.value,
                        padding_left=Size.VERY_BIG.value
                    ),  
                    rx.vstack(
                        rx.button(
                            f"el botón de {mueble} #1",
                            color=TextColor.BODY.value
                        ),
                        
                        # Lista de imágenes del mueble en un contenedor vertical
                        rx.vstack(
                            rx.cond(
                                PageState.imagen_fila_info,  # Verifica si existe información en mueble_imagen_info
                                rx.foreach(
                                    PageState.imagen_fila_info,  # Itera sobre las imágenes
                                    lambda image: 
                                        rx.image(
                                            src= PageState.imagen_fila_info[0],  # Cada imagen en la lista
                                            width="100px",
                                            height="auto"
                                        )
                                ),
                                rx.text("No hay imágenes disponibles.", color=TextColor.BODY.value)  # Si no hay imágenes
                            ),
                            spacing=Spacing.SMALL.value,  # Espaciado entre imágenes
                            align_items="center",
                            width="100%",
                        ),
                        rx.button(
                            f"el botón de {mueble} #2",
                            color=TextColor.BODY.value
                        ),
                        
                        rx.image(
                            src="https://krmdgbcxyzatizbztubr.supabase.co/storage/v1/object/public/prueba_imagen/muestras_muebles/velador_muestra.webp",
                            border_radius=Size.DEFAULT.value,
                            background=Color.CONTENT.value,
                            width="100%",
                        ),
                    ),
                    value=mueble,
                    align_items="start",
                    width="100%",
                )
        ),
        
        rx.spacer(), 
        default_value=rx.cond(
            PageState.mueble_fila_info,
            PageState.mueble_fila_info[0],
            ""
        ),
        orientation="vertical",
        spacing=Spacing.BIG.value,
    )

    