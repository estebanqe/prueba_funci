import reflex as rx

class Featured(rx.Model, table=True):
    title: str
    image: str
    url: str