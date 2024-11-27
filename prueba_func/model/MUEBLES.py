import reflex as rx


class MUEBLES(rx.Model, table=True):
    mueble: str
    url_image: str
    descripcion: str