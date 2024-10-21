# herraje_link.py
import reflex as rx
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing, Color
from prueba_func.model.var_herraje import var_herraje  # Asegúrate de que este modelo esté correctamente importado

def herrajes_links(var_herraje_item: var_herraje) -> rx.Component:
    return rx.hstack(
            rx.text(
                f"herraje: {var_herraje_item.herraje}",
                size=Spacing.SMALL.value,  # Ajusta el tamaño según tus necesidades
                style=styles.button_body_style
            ),
            rx.text(
                f"Unidades: {var_herraje_item.unidades}",  # Mostrando las unidades
                size=Spacing.SMALL.value,
                style=styles.button_body_style
            ),
            rx.text(
                f"Valor: ${var_herraje_item.valor:.2f}",  # Mostrando el valor con formato
                size=Spacing.SMALL.value,
                style=styles.button_body_style
            ),
            spacing=Spacing.VERY_BIG.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        )    
