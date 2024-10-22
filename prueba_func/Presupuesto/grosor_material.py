import reflex as rx

class FormSelectState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def grosor_material():
    return rx.card(
        rx.vstack(
            rx.heading("Grosor"),
            rx.form.root(
                rx.flex(
                    rx.select(
                        ["melamina 15mm", "melamina 18mm"],
                        default_value="melamina 15mm",
                        name="select",
                        required=True,
                    ),
                    rx.button(
                        "Submit", flex="1", type="aceptar"
                    ),
                    width="100%",
                    spacing="3",
                ),
                on_submit=FormSelectState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(
                    FormSelectState.form_data.to_string()
                ),
            ),
            align_items="left",
            width="100%",
        ),
        width="100%",
    )