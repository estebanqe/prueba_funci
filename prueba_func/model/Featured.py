import reflex as rx
from pydantic import BaseModel

class Featured(rx.Model):
    title: str
    image: str
    url: str
