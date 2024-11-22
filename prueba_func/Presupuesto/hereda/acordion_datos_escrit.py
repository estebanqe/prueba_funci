import reflex as rx
from prueba_func.api.SupabaseAPI import SupabaseAPI
from prueba_func.model.MODELOS import MODELOS
from prueba_func.estilo.estilo import Size, Spacing, TextColor
from prueba_func.Presupuesto.botton_modelos_mela import botton_modelos_mela
from prueba_func.Presupuesto.hereda.acordion_opc_disen import acordion_material_melamina
from prueba_func.api.api import api_Modelos

# Instancia de Supabase API
SUPABASE_API = SupabaseAPI()

class ModeloState(rx.State):
    """State para manejar modelos y selección en el acordeón."""

    modelos: list[MODELOS] = []
    acor_selected: str = "acor_0"

    async def load_modelos(self):
        """Carga modelos desde la API."""
        try:
            print("Cargando modelos...")
            self.modelos = await api_Modelos()
            print(f"Modelos cargados: {len(self.modelos)}")
        except Exception as e:
            print(f"Error al cargar modelos: {e}")
            self.modelos = []  # Estado consistente si ocurre un error

    def change_selected(self, value: str):
        """Cambia el elemento seleccionado en el acordeón."""
        print(f"Nuevo valor seleccionado: {value}")
        self.acor_selected = value  # Actualiza el estado seleccionado


    def get_selected_model(self):
        """Obtiene el modelo correspondiente al valor seleccionado."""
        # Busca el modelo correspondiente al valor seleccionado en el acordeón
        selected_model = next((modelo for modelo in self.modelos if f"item_{modelo.id}" == self.acor_selected), None)
        return selected_model


def acordion_datos_escrit() -> rx.Component:
    """Construye el componente del acordeón."""
    return rx.container(
        rx.text(
            ModeloState.acor_selected,  # Directamente del estado
            color="white",  
        ),
        rx.accordion.root(
            # Renderizar dinámicamente los items del acordeón
            rx.foreach(
                ModeloState.modelos,
                lambda modelo, index: rx.accordion.item(
                    header=rx.accordion.header(
                        rx.cond(
                            modelo.modelo,
                            modelo.modelo,  # Si modelo.modelo tiene valor
                            "Sin nombre",    # Si modelo.modelo es None o vacío
                        ),
                        color="white",
                    ),
                    content=rx.accordion.content(
                        rx.vstack(
                            rx.image(
                                src=modelo.url_image,
                                height="200px",
                            ),
                            rx.text(
                                modelo.descripcion,
                                color="white",
                            ),
                        ),
                    ),
                    value=f"item_{index}",
                ),
            ),
            collapsible=True,
            width="100%",
            variant="ghost",
            # Cambia el estado cuando se selecciona un elemento
            on_value_change=lambda value: ModeloState.change_selected(value),
            type="single",  # Permite múltiples secciones abiertas
        ),
        padding="2em",
        # Llama a la función asincrónica en el evento on_mount
        on_mount=ModeloState.load_modelos,
        async_handlers=["on_mount"],  # Marca on_mount como asincrónico
    )
