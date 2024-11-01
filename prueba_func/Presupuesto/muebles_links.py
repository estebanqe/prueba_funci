import reflex as rx
import prueba_func.constants as const
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
from prueba_func.components.link_material import link_material
from prueba_func.Presupuesto.muestra_muebles_link import muestra_muebles_link
from prueba_func.components.title import title
from prueba_func.state.PageState import PageState
from prueba_func.api.SupabaseAPI import SupabaseAPI



def muebles_links() -> rx.Component:
    # Imprimir el contenido de los estados para depuración
    print("Contenido de mueble_fila_info:", PageState.mueble_fila_info)
    print("Contenido de mueble_imagen_info:", PageState.mueble_imagen_info)

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
                                PageState.mueble_imagen_info,
                                rx.foreach(
                                    PageState.mueble_imagen_info,
                                    lambda image: 
                                        rx.image(
                                            src=PageState.mueble_imagen_info,
                                            width="100px",
                                            height="auto"
                                        )
                                ),
                                rx.text("No hay imágenes disponibles.",color=TextColor.BODY.value)  # Mensaje si no hay imágenes
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
