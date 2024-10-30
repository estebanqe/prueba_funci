# herraje_link.py
import reflex as rx
import prueba_func.estilo.estilo as styles
from prueba_func.estilo.estilo import Size, Spacing, Color,TextColor
from prueba_func.model.HERRAJES import HERRAJES  # Asegúrate de que este modelo esté correctamente importado

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
            
            spacing=Spacing.VERY_BIG.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        )    
