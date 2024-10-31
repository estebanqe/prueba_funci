import reflex as rx
import prueba_func.constants as const
from prueba_func.model.Featured import Featured
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES
from .SupabaseAPI import SupabaseAPI
from .Supacotizar import Supacotizar

SUPACOTIZAR = Supacotizar()
SUPABASE_API = SupabaseAPI()

async def repo () -> str:
    return const.CATALOGO


async def live( user: str) -> bool:
    if user=="esteban":
        return True
    return False


async def featured() -> list[Featured]:
    return SUPABASE_API.featured()

async def Herrajes() -> list[HERRAJES]:
    return SUPABASE_API.Herrajes()

async def Muebles() -> list[MUEBLES]:
    return SUPABASE_API.Muebles()

async def Muebles_fila() -> list[MUEBLES]:
    return SUPABASE_API.obtener_muebles()


async def Muebles_imagen() -> list[MUEBLES]:
    return SUPABASE_API.muestra_muebles()
