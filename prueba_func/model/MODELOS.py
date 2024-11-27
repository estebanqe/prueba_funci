import reflex as rx

class MODELOS(rx.Model, table=True):
    modelo: str
    url_image: str
    descripcion: str 
    id_muebles: int