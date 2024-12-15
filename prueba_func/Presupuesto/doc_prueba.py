import reflex as rx
from prueba_func.state.PageState import MuebleState,ModelosState
from prueba_func.estilo.estilo import Spacing, Size
from prueba_func.Presupuesto.acordion_modelos import acordion_modelos



def doc_prueba() -> rx.Component:
    return rx.container(
        # Componente de Tabs
        rx.tabs.root(
            rx.scroll_area(
                rx.tabs.list(
                    rx.foreach(
                        MuebleState.muebles,
                        lambda mueble, index: rx.tabs.trigger(
                            mueble.mueble,  # Usamos el nombre del mueble como título de la pestaña
                            value=f"tab{index}",
                            color="white"
                        )
                    ),
                    size="2",
                    width="100%",
                    padding=Size.SMALL.value,
                ),
                type="always",
                scrollbars="horizontal",
                style=rx.Style({
                    "background_color": rx.color("white", 7),
                    "border_color": rx.color("blue", 1),
                    
                }),
                padding_y=Size.SMALL.value,
                width="100%",
            ),
                        
            rx.foreach(
                MuebleState.muebles,
                lambda mueble, index: 
                    rx.tabs.content(
                        rx.box(
                            rx.hstack(
                                rx.box(
                                    rx.vstack(
                                        rx.heading(mueble.mueble, color="white",),
                                        rx.image(
                                            src=mueble.url_image,
                                            height="auto",
                                            width="250px",
                                        ),
                                        rx.text(mueble.descripcion, color="white"),
                                        width="200px",
                                        padding_top=Size.BIG.value,
                                        aling="center"    
                                    ),
                                ),
                                rx.box(
                                    acordion_modelos(mueble.id),
                                    width="300px",
                                ),
                                
                                padding_left=Size.SMALL.value,
                                flex_direction=["column", "row"],
                                width="100%",
                            ),
                            
                        ),
                        
                        width="100%", 
                        value=f"tab{index}",
                        
                    )
            ),
            value=MuebleState.tab_selected,
            on_change=MuebleState.change_tab,
            default_value="tab0",
            on_mount=MuebleState.load_muebles,
            orientation="horizontal",
            spacing=Spacing.BIG.value,
            width="100%",
            
        ),
        width="100%",
    )