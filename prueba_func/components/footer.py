import reflex as rx
import datetime
import prueba_func.constants as const
from prueba_func.estilo.estilo import Size, Spacing
from prueba_func.estilo.colors import Color, TextColor
from prueba_func.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logocrebla.png",
            height=Size.VERY_BIG.value,     #alto del logo
            width=Size.VERY_BIG.value,      #ancho del logo
            alt="logotipo de la marca",  #esto es para personas ividentes
        ),
        rx.link(
            rx.box(
                f"2020-{datetime.date.today().year} ",
                rx.text(
                    "trabajo con excelencia",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " Creyente.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.CATALOGO,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                # rx.image(
                #     src="/AvatarC.png",
                #     height=Size.LARGE.value,
                #     width=Size.LARGE.value,
                #     alt="Avatar"
                # ),
                rx.text(
                    "Innovación en Madera: Inspirando Espacios, Creando Historias para ti.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.CATALOGO,
            is_external=True
        ),
        
        # float_button(
        #    icon=rx.image(src="/AvatarC.png"),
        #    href=const.CATALOGO
        # ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )