import reflex as rx
import prueba_func.constants as const
from prueba_func.model.Featured import Featured
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.model.MODELOS import MODELOS

from .SupabaseAPI import SupabaseAPI
from  prueba_func.api.Muebles_api import MueblesAPI
from  prueba_func.api.Modelos_api import ModelosAPI




SUPABASE_API = SupabaseAPI()
muebles_api_instance = MueblesAPI()
modelos_api_intance= ModelosAPI()

async def repo () -> str:
    return const.CATALOGO


async def live( user: str) -> bool:
    if user=="esteban":
        return True
    return False

async def api_Muebles() -> list[MUEBLES]:
    return muebles_api_instance.Muebles()

async def api_Modelos() -> list[MODELOS]:
    return modelos_api_intance.Modelos()



async def api_SQL_Modelos() -> list[MODELOS,MUEBLES]:
    return SUPABASE_API.SQL_Modelos()



async def featured() -> list[Featured]:
    return SUPABASE_API.featured()

