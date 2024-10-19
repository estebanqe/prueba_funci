import reflex as rx
from prueba_func.routes import Route
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.components.title import title
from prueba_func.Presupuesto.acordion_datos_escrit import acordion_datos_escrit
from prueba_func.estilo.estilo import Color, TextColor, Spacing

# Función para mostrar el acordeón de opciones de muebles
def modelos_melamina() -> rx.Component:
    return rx.accordion.root(
        
        
      rx.accordion.item(
            header=rx.accordion.header("Escritorio"),  # Utiliza el header correcto
            content=rx.accordion.content(
                rx.vstack(
                    # title("Modelos"),
                    botton_modelos_mela(
                        "Escritorio",
                        "tenemos 3 opciones para ti",
                        "/modelos/escritorio-melamina.jpg",
                        # const.TABLA_PICAR
                    ),
                    acordion_datos_escrit(),
                    
                    spacing=Spacing.VERY_SMALL.value,
                    width="100%",
                    justify="center",
                    align="center"
                
                ),
                
            ),
        
            
            
            
            
            
            
            
            # content=rx.vstack(
            #     rx.text("Detalles sobre el Escritorio: tamaño, color, material."),
            #     rx.button("Calcular Precio", on_click=lambda: rx.window_alert("Calculando precio del Escritorio...")),
            #     rx.button("Agregar al Carrito", on_click=lambda: rx.window_alert("Escritorio agregado al carrito.")),
            #     rx.button("Ver Más Detalles", on_click=lambda: rx.window_alert("Mostrando más detalles del Escritorio...")),
            # ),
        ),
        
        
        
        # Opción 2: Velador
        rx.accordion.item(
            header="Velador",
            content=rx.vstack(
                rx.text("Detalles sobre el Velador: tamaño, color, material."),
                rx.button("Calcular Precio", on_click=lambda: rx.window_alert("Calculando precio del Velador...")),
                rx.button("Agregar al Carrito", on_click=lambda: rx.window_alert("Velador agregado al carrito.")),
                rx.button("Ver Más Detalles", on_click=lambda: rx.window_alert("Mostrando más detalles del Velador...")),
            ),
        ),
        
        
        # Opción 3: Mueble de TV
        rx.accordion.item(
            header="Mueble de TV",
            content=rx.box(
                rx.vstack(
                    rx.text("Detalles sobre el Mueble de TV: tamaño, color, material."),
                    rx.button("Calcular Precio", on_click=lambda: rx.window_alert("Calculando precio del Mueble de TV...")),
                    rx.button("Agregar al Carrito", on_click=lambda: rx.window_alert("Mueble de TV agregado al carrito.")),
                    rx.button("Ver Más Detalles", on_click=lambda: rx.window_alert("Mostrando más detalles del Mueble de TV...")),
                ),
            ),
        ),
        
        spacing=Spacing.VERY_SMALL.value,
        collapsible=True,
        width="100%",
        height="auto",
        type="multiple",
        variant="outline",
        justify="center"
    )
