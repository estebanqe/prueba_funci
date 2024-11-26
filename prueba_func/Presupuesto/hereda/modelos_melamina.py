import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.components.title import title
from prueba_func.Presupuesto.hereda.acordion_modelos import acordion_modelos
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
                acordion_modelos(),
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
