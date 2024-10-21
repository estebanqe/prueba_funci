import prueba_func.constants as const
from prueba_func.model.Featured import Featured
from prueba_func.model.var_herraje import var_herraje
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

async def Herrajes() -> list[var_herraje]:
    return SUPABASE_API.Herrajes()

