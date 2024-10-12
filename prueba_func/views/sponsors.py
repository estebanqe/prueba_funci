import reflex as rx
import prueba_func.constants as const
from prueba_func.estilo.estilo import Size, Spacing
from prueba_func.components.title import title
from prueba_func.components.link_sponsor import Link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Creyente & Hijos"),
          rx.flex(
               Link_sponsor(
                    "/AvatarC.png",
                    const.CARPINTERIA, 
                    "Avatar"        
               ),
               Link_sponsor(
                    "/logocrebla.png",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"
                            
               ),
           spacing=Spacing.BIG.value,
           flex_direction=["column", "row"]

          ),
       
        width="100%",
        align_items="start",
        spacing=Spacing.DEFAULT.value
    )