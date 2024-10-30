import os
import dotenv
from supabase import create_client, Client
from prueba_func.model.Featured import Featured 
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES

class Supacotizar:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    