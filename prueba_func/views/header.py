import reflex as rx
import datetime
import prueba_func.constants as const
from prueba_func.estilo.estilo import Size,Spacing
from prueba_func.estilo.colors import Color, TextColor
from prueba_func.components.link_icon import link_icon
from prueba_func.components.info_text import info_text
from prueba_func.components.link_button import link_button
# from prueba_func.state.PageState import PageState


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                 #rx.cond(
                    # PageState.live_status.live,
                    rx.link(
                        rx.image(
                            src="/AvatarC.png",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value
                        ),
                        href=const.CATALOGO,
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.SMALL.value,
                        bg=Color.PURPLE.value,
                        position="absolute",
                        bottom="0",
                        right="0"
                    ),
                #),
                rx.avatar(
                    name="Julio. César Quiña",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/AvatarC.png",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
                # position="relative"
            ),
                
            rx.vstack(
                rx.heading(
                    "CREYENTE",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "J. César. & Hijos",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM,
                        "email@email.com"
                    ),
                    link_icon(
                        "/icons/facebook.svg",
                        const.FACEBOOK,
                        "facebook"
                    ),
                    link_icon(
                        "/icons/book-solid.svg",
                        const.CATALOGO,
                        "catalogo"
                    ),
                    link_icon(
                        "/icons/whatsapp.svg",
                        const.WHATSAPP,
                        "whatssap"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value,

                ),
                spacing=Spacing.ZERO.value,
                align_items="start",
            ),
            align="end",
            spacing=Spacing.DEFAULT.value,
            
        ),      
        rx.cond(  
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),#crea un espacio ficticio entre texto
                    info_text(
                        "ateción","al detalle"
                    ),
                    rx.spacer(), 
                    info_text(
                        "trabajo","certificado"
                    ),
                    width="100%",
                ),
                rx.text(
                    f"""
                    Bienvenido a nuestro sitio especializado en trabajos en madera y melamina. Desde muebles a medida hasta soluciones de almacenamiento, fusionamos la tradición con la innovación para crear piezas únicas que realzan cualquier espacio. ¡Explore nuestro portafolio y dé vida a sus proyectos con nosotros!""",
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",  
                spacing=Spacing.BIG.value,
                
            )
            
        ),  
        width="100%",
        spacing=Spacing.BIG.value,                     #espacion entre las 2 secciones
        align_items="start", #alinear todo al inicio
        
    )
    
def experience() -> int:
    return datetime.date.today().year - 2020
    