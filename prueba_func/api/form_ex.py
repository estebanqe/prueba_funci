import reflex as rx
# import prueba_func.utils as utils
# import prueba_func.estilo.estilo as styles
# from prueba_func.routes import Route
# from prueba_func.components.navbar import navbar
# from prueba_func.components.footer import footer
# from prueba_func.views.header import header
# from prueba_func.views.cotizar_links import cotizar_links
# from prueba_func.views.sponsors import sponsors
from prueba_func.estilo.estilo import TextColor




class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                    color=TextColor.BODY.value
                ),
                rx.button("Submit", type="submit")
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True
        ),
        rx.divider(),
        rx.heading(
            "Results"),
        rx.text(
            FormState.form_data.to_string(),
            color=TextColor.BODY.value
            )
    )
