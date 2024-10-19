import prueba_func.constants as const
from prueba_func.model.Featured import Featured
from prueba_func.model.Herrajes_list import Herrajes_list
from .SupabaseAPI import SupabaseAPI


SUPABASE_API = SupabaseAPI()

async def repo () -> str:
    return const.CATALOGO


async def live( user: str) -> bool:
    if user=="esteban":
        return True
    return False


async def featured() -> list[Featured]:
    return SUPABASE_API.featured()

async def Herrajes() -> list[Featured]:
    return SUPABASE_API.Herrajes()

