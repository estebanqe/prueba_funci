import reflex as rx
import prueba_func.constants as const
#from prueba_func.components.newsletter 
from prueba_func.components.featured_link import featured_link
from prueba_func.model.Featured import Featured
from prueba_func.routes import Route
from prueba_func.components.link_button import link_button
from prueba_func.components.title import title
from prueba_func.estilo.estilo import Color, Spacing
from prueba_func.state.PageState import PageState

def index_links(featured=list[Featured]) -> rx.Component:
    return rx.vstack(
        title("Nueva Pagina"),
        link_button(
            "pagina nueva",
            "Nueva descripcion de la pagina nueva ",
            "/icons/facebook.svg",
            Route.COURSES.value,
            False
        ),
        
        link_button(
            "Facebook",
            """Madera y Melamina: Donde la Creatividad Encuentra su Hogar.""",
            "/icons/facebook.svg",
            const.FACEBOOK
        ),
        
        link_button(
            "Instagram",
            """Diseño en Madera: Crea Tu Espacio Perfecto con Nosotros.""",
            "/icons/instagram.svg",
            const.INSTAGRAM
            ),
        link_button(
            "Youtube",
            """Estilo Personalizado, Calidad Artesanal: Nuestro Compromiso.""",
            "/icons/youtube.svg",
            const.YOUTUBE
            ),
        link_button(
            "Tik-Tok",
            """Tu Visión, Nuestra Creación: Experiencia en Madera y Melamina.""",
            "/icons/linkedin.svg",
            const.LINKEDLINK
            ),
        
#    rx.cond(
#        featured,
#        rx.vstack(
#            title("Destacado"),
#            rx.foreach(
#                featured,
#                featured_link
#            )
#        )
#    ),
        
    rx.cond(
            PageState.featured_info,
            rx.vstack(
                title("Destacado"),
                rx.flex(
                    rx.foreach(
                        PageState.featured_info,
                        featured_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value
                ),
                spacing=Spacing.DEFAULT.value
            )
        ),
        
        
        title("Cátalogo"),
        link_button(
            "Maderas Personalisadas",
            """Madera: Transformando Ideas en Realidad.""",
            "/icons/madera1.svg",
            const.MADERA_PERSONALIZADA
        ),
        link_button(
            "Tablas de Picar",
            """Tablas de Picar: Elegancia y Funcionalidad en Cada Corte.""",
            "/icons/madera2.svg",
            const.TABLA_PICAR
        ),
        link_button(
            "Muebles Personalizados",
            """Hecho para Ti: Muebles que Cuentan tu Historia.""",
            "/icons/madera3.svg",
            const.MUEBLES_PERSONLAZADOS
            ),
        link_button(
            "Amoblado de Áreas Específicas",
            """Amoblado a tu Medida, Espacios con Propósito.""",
            "/icons/madera4.svg",
            const.AMOBLADO_AREA
            ),
        
        title("Contacto"),
        link_button(
            "WhatsApp",
            "respuesta rápida y de preferencia",
            "/icons/whatsapp.svg",
            const.WHATSAPP
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
            
            
        width="100%",
        spacing=Spacing.DEFAULT.value,
        #on_mount=PageState.featured_links
    )   