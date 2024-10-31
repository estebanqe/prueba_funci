import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.components.title import title
from prueba_func.Presupuesto.hereda.acordion_datos_escrit import acordion_datos_escrit
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size

# Función para mostrar las opciones de muebles en pestañas
def modelos_melamina() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger(
                "Escritorio", value="escritorio",
                color=TextColor.BODY.value
            ),
            rx.tabs.trigger(
                "Velador", value="velador",
                color=TextColor.BODY.value
            ),
            rx.tabs.trigger(
                "Mueble de TV", value="mueble_tv",
                color=TextColor.BODY.value
            ),
        ),
        # Contenido de la pestaña "Escritorio"
        rx.tabs.content(
            rx.vstack(
                botton_modelos_mela(
                    "Escritorio",
                    "Tenemos 3 opciones para ti",
                    "/modelos/escritorio-melamina.jpg",
                ),
                acordion_datos_escrit(),
                spacing=Spacing.VERY_SMALL.value,
                margin_top=Size.DEFAULT.value,
                width="100%",
                justify="center",
                align="center",
            ),
            value="escritorio",
        ),
        # Contenido de la pestaña "Velador"
        rx.tabs.content(
            rx.vstack(
                rx.text("Detalles sobre el Velador: tamaño, color, material."),
                rx.button("Calcular Precio", on_click=lambda: rx.window_alert("Calculando precio del Velador...")),
                rx.button("Agregar al Carrito", on_click=lambda: rx.window_alert("Velador agregado al carrito.")),
                rx.button("Ver Más Detalles", on_click=lambda: rx.window_alert("Mostrando más detalles del Velador...")),
            ),
            value="velador"
        ),
        # Contenido de la pestaña "Mueble de TV"
        rx.tabs.content(
            rx.vstack(
                rx.text("Detalles sobre el Mueble de TV: tamaño, color, material."),
                rx.button("Calcular Precio", on_click=lambda: rx.window_alert("Calculando precio del Mueble de TV...")),
                rx.button("Agregar al Carrito", on_click=lambda: rx.window_alert("Mueble de TV agregado al carrito.")),
                rx.button("Ver Más Detalles", on_click=lambda: rx.window_alert("Mostrando más detalles del Mueble de TV...")),
            ),
            value="mueble_tv",
        ),
        default_value="escritorio",
        orientation="horizontal",
        spacing=Spacing.DEFAULT.value,
        # color_scheme="cyan",
    )


def herrajes_links (var_herraje_item: HERRAJES) -> rx.Component:
    return rx.hstack(
            rx.text(
                f"herraje: {var_herraje_item.herraje}",
                size=Spacing.SMALL.value,  # Ajusta el tamaño según tus necesidades
                style=styles.button_body_style
            ),
            rx.text(
                f"descripcion: {var_herraje_item.descripcion}",  # Mostrando las unidades
                size=Spacing.SMALL.value,
                style=styles.button_body_style
            ),
            # rx.text(
            #     f"Valor: ${var_herraje_item.valor:.2f}",  # Mostrando el valor con formato
            #     size=Spacing.SMALL.value,
            #     style=styles.button_body_style
            # ),
            spacing=Spacing.VERY_BIG.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        )    





import reflex as rx
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
from prueba_func.api.api import live, featured, Herrajes, Muebles
from prueba_func.model.MUEBLES import MUEBLES




class TabsState(rx.State):
    """The app state."""

    value = "tab1"
    tab_selected = ""

    def change_value(self, val):
        self.tab_selected = f"{val} clicked!"
        self.value = val


def muebles_links() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.text(f"{TabsState.value}  clicked !"),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Tab 1", value="tab1",color=TextColor.BODY.value),
                    rx.tabs.trigger("Tab 2", value="tab2",color=TextColor.BODY.value),
                ),
                rx.tabs.content(
                    rx.text("items on tab 1"),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.text("items on tab 2"),
                    value="tab2",
                ),
                default_value="tab1",
                value=TabsState.value,
                on_change=lambda x: TabsState.change_value(
                    x
                ),
            ),
            direction="column",
            spacing="2",
            color=TextColor.BODY.value
        ),
        padding="2em",
        font_size="2em",
        text_align="center",
    )
    



import reflex as rx
from typing import List
from prueba_func.api.api import Muebles  # Importa la función que obtiene los muebles
from prueba_func.model.MUEBLES import MUEBLES  # Importa el modelo MUEBLES
from prueba_func.estilo.estilo import TextColor  # Asegúrate de tener el color adecuado

class PageState(rx.State):
    mueble_info: List[MUEBLES] = []  # Lista para almacenar los muebles

    def load_muebles(self) -> None:
        """Cargar muebles desde la API."""
        try:
            self.mueble_info = Muebles()  # Carga los muebles desde la API
            print("Muebles cargados:", self.mueble_info)  # Debugging: Imprime los muebles cargados
        except Exception as e:
            print(f"Error al cargar muebles: {e}")  # Manejo de errores

def muebles_ui(mueble: MUEBLES) -> rx.Component:
    """Muestra un mueble en la interfaz de usuario."""
    return rx.box(
        rx.text(mueble.descripcion, font_size="1.25em"),
        padding="1em",
        border="1px solid black",
        border_radius="0.5em",
        margin="0.5em"
    )

def muebles_links() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.text("Listado de Muebles", color=TextColor.BODY.value),
            rx.tabs.root(
                rx.tabs.list(
                    rx.foreach(
                        PageState.mueble_info,
                        lambda mueble: rx.tabs.trigger(
                            mueble.mueble,  # Utiliza el atributo mueble como título del tab
                            value=mueble.mueble  # Establece el valor del tab
                        )
                    )
                ),
                rx.tabs.content(
                    rx.foreach(
                        PageState.mueble_info,
                        lambda mueble: rx.box(
                            rx.text(mueble.descripcion, font_size="1.25em"),  # Muestra la descripción
                            value=mueble.mueble  # Asegúrate de que esto sea el valor que quieres
                        )
                    )
                ),
            ),
            direction="column",
            spacing="2",
        ),
        padding="2em",
        font_size="1em",
        text_align="center",
    )

# Llama a la carga de muebles al montar el componente
on_mount = PageState.load_muebles






rx.grid(
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense "legible" and "readable"
        are often used synonymously, typographically they are separate but
        related concepts.""",
                size="2",
                trim="both",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2",
                trim="both",
            ),
            padding="8px",
            padding_right="48px",
            direction="column",
            spacing="4",
        ),
        type="always",
        scrollbars="vertical",
        style={"height": 150},
    ),
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense "legible" and "readable"
        are often used synonymously, typographically they are separate but
        related concepts.""",
                size="2",
                trim="both",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2",
                trim="both",
            ),
            padding="8px",
            spacing="4",
            style={"width": 700},
        ),
        type="always",
        scrollbars="horizontal",
        style={"height": 150},
    ),
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense "legible" and "readable"
        are often used synonymously, typographically they are separate but
        related concepts.""",
                size="2",
                trim="both",
            ),
            rx.text(
                """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as "the
        quality of being decipherable and recognisable". For instance, if a "b"
        and an "h", or a "3" and an "8", are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
                size="2",
                trim="both",
            ),
            padding="8px",
            spacing="4",
            style={"width": 400},
        ),
        type="always",
        scrollbars="both",
        style={"height": 150},
    ),
    columns="3",
    spacing="2",
)




codigo sin impresion 





import reflex as rx
import prueba_func.constants as const
from prueba_func.estilo.estilo import Color, TextColor, Spacing, Size
from prueba_func.components.link_material import link_material
from prueba_func.Presupuesto.muestra_muebles_link import muestra_muebles_link
from prueba_func.components.title import title
from prueba_func.state.PageState import PageState

def muebles_links() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
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
                            rx.foreach(
                                PageState.mueble_imagen_info,
                                lambda image: 
                                    rx.image(
                                        src=image,
                                        width="100px",
                                        height="auto"
                                    )
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

