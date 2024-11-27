import reflex as rx
from prueba_func.state.PageState import MuebleState,ModelosState
from prueba_func.estilo.estilo import Spacing, Size
from prueba_func.Presupuesto.hereda.acordion_modelos import acordion_modelos



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
                #  padding_top=Size.SMALL.value,
                padding_y=Size.SMALL.value
            ),
            # padding_y=Size.SMALL.value,
            
            rx.foreach(
                MuebleState.muebles,
                lambda mueble, index: 
                    rx.tabs.content(
                        
                        rx.hstack(
                            
                            rx.vstack(
                                rx.heading(mueble.mueble, color="white",width="100%",),
                                rx.text(mueble.id, color="white"),
                                rx.image(
                                    src=mueble.url_image,
                                    height="auto",
                                    width="250px",
                                ),
                                rx.text(mueble.descripcion, color="white"),
                                
                            ),
                            
                            
                            
                            acordion_modelos(mueble.id),
                           
                            padding_y=Size.DEFAULT.value
                            
                        ),
                        
                    value=f"tab{index}",
                    # padding_left=Size.VERY_BIG.value,
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