import reflex as rx
import prueba_func.constants as const
from prueba_func.components.link_button import link_button
from prueba_func.components.title import title
#from prueba_func.components.newsletter import newsletter
from prueba_func.estilo.estilo import Color, Spacing


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Contacto"),
        link_button(
            "WhatsApp",
            "respuesta rápida y de preferencia",
            "/icons/whatsapp.svg",
            const.WHATSAPP,
            highlight_color=Color.SECONDARY.value
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        #newsletter(),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )