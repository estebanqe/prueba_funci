import reflex as rx
from pydantic import BaseModel

class MODELOS(rx.Model):
    modelo: str
    url_image: str
    descripcion: str 
    id_muebles: int