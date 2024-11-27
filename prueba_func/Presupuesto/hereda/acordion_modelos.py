import reflex as rx
from prueba_func.state.PageState import ModelosState
from prueba_func.estilo.estilo import Size, Spacing, TextColor
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.Presupuesto.hereda.acordion_opc_disen import acordion_material_melamina

def acordion_modelos(id_muebles) -> rx.Component:
    return rx.container(
        rx.accordion.root(
            rx.foreach(
                ModelosState.modelos,  # Iterar sobre todos los modelos
                lambda modelo, index: rx.cond(
                    modelo['id_muebles'] == id_muebles,  # Filtrar solo los modelos que coinciden con id_muebles
                    rx.accordion.item(
                        header=rx.accordion.header(
                            rx.cond(
                                modelo['modelo'],  # Si modelo.modelo tiene valor
                                modelo['modelo'],  # Mostrar modelo.modelo
                                "Sin un nombre",    # Si modelo.modelo es None o vacío
                            ),
                            color="white",
                            width="100%",
                        ),
                        content=rx.accordion.content(
                            rx.vstack(
                                # rx.text(
                                #     "modelo ",
                                #     modelo['id_muebles'],  # Asegurarse de convertir a string
                                #     color="white",
                                #     width="100%",
                                # ),
                                rx.image(
                                    src=modelo['url_image'],
                                    height="auto",
                                    width="200px",
                                ),
                                rx.text(
                                    modelo['descripcion'],
                                    color="white",
                                    width="100%",
                                ),
                            ),
                        ),
                        value=f"item_{index}",
                        width="100%",
                        align="center",
                    ),
                    None  # Si el modelo no cumple con la condición, no mostrar nada
                )
            ),
            collapsible=True,
            width="100%",
            type="single",
            on_value_change=ModelosState.change_acor,
            variant="ghost",
            on_mount=ModelosState.load_modelos,
        ),
        width="100%",
    )
