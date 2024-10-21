import reflex as rx


class var_herraje(rx.Model, table=True):
    
    herraje: str
    unidades: int
    valor: float