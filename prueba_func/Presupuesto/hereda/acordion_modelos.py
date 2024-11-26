import reflex as rx
from prueba_func.state.PageState import ModeloState,ModelosState
from prueba_func.estilo.estilo import Size, Spacing, TextColor
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.Presupuesto.hereda.acordion_opc_disen import acordion_material_melamina


def acordion_modelos() -> rx.Component:
    return rx.container(
        rx.accordion.root(
            rx.foreach(
                ModelosState.modelos,
                lambda modelo, index: rx.accordion.item(
                    header=rx.accordion.header(
                        rx.cond(
                            modelo.modelo,
                            modelo.modelo,  # Si modelo.modelo tiene valor
                            "Sin nombre",    # Si modelo.modelo es None o vacío
                        ),
                        color="white",
                        width="300px",
                    ),
                    content=rx.accordion.content(
                        rx.vstack(
                            rx.image(
                                src=modelo.url_image,
                                height="auto",
                                width="200px",
                            ),
                            rx.text(
                                modelo.descripcion,
                                color="white",
                                width="100%",
                            ),
                        ),
                    ),
                    value=f"item_{index}",
                    width="100%",
                    aling="center",
                    # flex_direction=["column", "row"],
                ),
            ),
            collapsible=True,
            width="100%",
            type="single",
            on_value_change=ModelosState.change_acor,
            default_value="item_0",
            variant="ghost",
            on_mount=ModelosState.load_modelos,
        ),
        width="100%",
        # padding="2em",
    )

