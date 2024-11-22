import reflex as rx
import prueba_func.constants as const
from prueba_func.model.Featured import Featured
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.model.MODELOS import MODELOS

from .SupabaseAPI import SupabaseAPI



SUPABASE_API = SupabaseAPI()

async def repo () -> str:
    return const.CATALOGO


async def live( user: str) -> bool:
    if user=="esteban":
        return True
    return False

async def api_Muebles() -> list[MUEBLES]:
    return SUPABASE_API.Muebles()

async def api_Modelos() -> list[MODELOS]:
    return SUPABASE_API.Modelos()




async def featured() -> list[Featured]:
    return SUPABASE_API.featured()

async def Herrajes() -> list[HERRAJES]:
    return SUPABASE_API.Herrajes()


