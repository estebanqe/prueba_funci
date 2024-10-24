import reflex as rx

class FormSelectState(rx.State):
    form_data: dict = {}
    melamina_color: bool = False  # Variable booleana para almacenar la selección
    color_seleccionado: str = ""  # Almacenar solo el valor de la selección

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        # Almacena el color seleccionado directamente
        self.color_seleccionado = form_data.get("select", "")
        
        # Actualizamos la variable booleana según la selección
        self.melamina_color = (self.color_seleccionado == "melamina blanca")
        
        # Imprimimos "blanco" o "otro color" según el valor de la variable booleana
        if self.melamina_color:
            print("blanco")
        else:
            print("otro color")


def color_material():
    return rx.card(
        rx.vstack(
            rx.heading("Color"),
            rx.form.root(
                rx.flex(
                    # Dropdown menu para seleccionar el tipo de melamina
                    rx.select(
                        ["melamina blanca", "melamina de color"],
                        default_value="melamina blanca",
                        name="select",
                        required=True    
                    ),
                    # Botón para enviar el formulario
                    rx.button(
                        "Escogelo", flex="1", type="submit"
                    ),
                    width="100%",
                    spacing="3",
                ),
                on_submit=FormSelectState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            # Mostrar solo el valor seleccionado, sin la clave "select"
            rx.hstack(
                rx.heading("Escogiste:"),
                rx.badge(
                    FormSelectState.color_seleccionado  # Solo muestra el color seleccionado
                ),
            ),
            # Mostrar el valor de la variable booleana como "valor blanco" o "valor color" usando rx.cond
            rx.hstack(
                rx.heading("valor:"),
                rx.cond(
                    FormSelectState.melamina_color,
                    rx.badge("valor blanco"),
                    rx.badge("valor color")
                ),
            ),
            align_items="left",
            width="100%",
        ),
        width="100%",
    )
