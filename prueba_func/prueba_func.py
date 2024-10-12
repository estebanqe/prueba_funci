import reflex as rx
import prueba_func.constants as const
import prueba_func.estilo.estilo as styles
from prueba_func.pages.index import index
from prueba_func.pages.courses import courses
#from prueba_func.api.api import repo, live, featured, schedule

class State(rx.State):
    """Define your app state here"""


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)
#app.api.add_api_route("/repo", repo)
#app.api.add_api_route("/live/{user}", live)
#app.api.add_api_route("/featured", featured)
#app.api.add_api_route("/schedule", schedule)