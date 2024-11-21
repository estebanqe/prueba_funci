import reflex as rx
# from prueba_func.model.MUEBLES import MUEBLES
# from prueba_func.api.api import api_Muebles

# class State(rx.State):
#     # Lista de muebles correctamente tipada
#     muebles: list[MUEBLES] = []  # La lista de muebles, inicialmente vacía
#     tab_selected: str = "tab0"  # La pestaña seleccionada
#     error: str = ""  # Variable para manejar errores

#     def change_tab(self, value: str):
#         """Actualiza la pestaña seleccionada."""
#         self.tab_selected = value

#     async def initialize(self):
#         """Carga inicial de datos."""
#         await self.load_muebles()
    
#     async def load_muebles(self):
#         """Carga los muebles usando la función api_Muebles."""
#         try:
#             # Se asegura de que muebles sea una lista de objetos MUEBLES
#             self.muebles = await api_Muebles()
#             if not self.muebles:
#                 self.error = "No se encontraron muebles en la base de datos."
#         except Exception as e:
#             self.error = f"Error al cargar muebles: {str(e)}"

# def doc_prueba(MUEBLES=[]):
#     """Genera la interfaz de usuario para los muebles."""
#     return rx.container(
#         rx.cond(
#             State.error != "",
#             rx.text(State.error, color="red"),  # Muestra el mensaje de error si ocurre
#             rx.cond(
#                 State.muebles,  # Verifica si la lista de muebles no está vacía
#                 rx.tabs.root(
#                     rx.tabs.list(
#                         rx.foreach(
#                             State.muebles,
#                             lambda mueble, index: rx.tabs.trigger(
#                                 mueble.mueble, value=f"tab{index}", color="white"
#                             )
#                         )
#                     ),
#                     rx.foreach(
#                         State.muebles,
#                         lambda mueble, index: rx.tabs.content(
#                             rx.vstack(
#                                 rx.heading(mueble.mueble, color="white"),
#                                 rx.image(
#                                     src=mueble.url_image,
#                                     height="200px",
#                                     width="auto",
#                                 ),
#                                 rx.text(mueble.descripcion, color="white"),
#                             ),
#                             value=f"tab{index}"
#                         )
#                     ),
#                     value=State.tab_selected,
#                     on_change=State.change_tab,
#                     default_value="tab0"
#                 ),
#                 rx.text("Cargando muebles...", color="gray")
#             )
#         )
#     )















# import reflex as rx

# class State(rx.State):
#     # Define las listas como variables de estado
#     nombres: list[str] = ["Escrotorio", "Velador", "Mueble TV"]  
#     imagenes: list[str] = [
#         "https://krmdgbcxyzatizbztubr.supabase.co/storage/v1/object/public/prueba_imagen/escritorio-melamina.jpg",
#         "https://krmdgbcxyzatizbztubr.supabase.co/storage/v1/object/public/prueba_imagen/muestras_muebles/velador_muestra.webp",
#         "https://krmdgbcxyzatizbztubr.supabase.co/storage/v1/object/public/prueba_imagen/muestras_muebles/mueble_tv_muestra.jpg",
#     ]
#     tab_selected: str = "tab1"

#     def change_tab(self, value: str):
#         self.tab_selected = value

# def doc_prueba():
#     return rx.container(
#         rx.tabs.root(
#             rx.tabs.list(
#                 rx.foreach(
#                     State.nombres,
#                     lambda nombre, index: rx.tabs.trigger(
#                         nombre,
#                         value=f"tab{index}",color="white"
#                     )
#                 )
#             ),
#             rx.foreach(
#                 State.nombres,
#                 lambda nombre, index: rx.tabs.content(
#                     rx.vstack(
#                         rx.heading(nombre,color="white"),
#                         rx.image(
#                             src=State.imagenes[index],
#                             height="200px",
#                             width="auto",
                            
#                         )
#                     ),
#                     value=f"tab{index}",color="white"
#                 )
#             ),
#             value=State.tab_selected,
#             on_change=State.change_tab,
#             default_value="tab0"
#         )
#     )










import reflex as rx
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.api.api import api_Muebles

SUPABASE_API = SupabaseAPI()

class State(rx.State):
    muebles: list[MUEBLES] = []
    tab_selected: str = "tab0"

    async def load_muebles(self):
        # Cargar los muebles desde la API
        self.muebles = await api_Muebles()

    def change_tab(self, value: str):
        self.tab_selected = value

# Usamos on_mount para cargar los datos al montar el componente
def doc_prueba():
    return rx.container(
       
        # Componente de Tabs
        rx.tabs.root(
            rx.tabs.list(
                rx.foreach(
                    State.muebles,
                    lambda mueble, index: rx.tabs.trigger(
                        mueble.mueble,  # Usamos el nombre del mueble como título de la pestaña
                        value=f"tab{index}",
                        color="white"
                    )
                )
            ),
            
            rx.foreach(
                State.muebles,
                lambda mueble, index: rx.tabs.content(
                    rx.vstack(
                        rx.heading(mueble.mueble, color="white"),
                        rx.image(
                            src=mueble.url_image,
                            height="200px",
                            width="auto",
                        ),
                        rx.text(mueble.descripcion, color="white")
                    ),
                    value=f"tab{index}",
                )
            ),
            value=State.tab_selected,
            on_change=State.change_tab,
            default_value="tab0",
            on_mount=State.load_muebles,
        ),
    )