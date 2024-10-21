import os
import dotenv
from supabase import create_client, Client
from prueba_func.model.Featured import Featured 
from prueba_func.model.var_herraje import var_herraje
class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def featured(self) -> list[Featured]:

        response = self.supabase.table("featured").select("*").order("init_date", desc=True).limit(2).execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                featured_data.append(
                    Featured(
                        title=featured_item["title"],
                        image=featured_item["image"],
                        url=featured_item["url"]
                    )
                )

        return featured_data
    

    def Herrajes(self) -> list[var_herraje]:
        
        response = self.supabase.table("Herrajes").select("*").order("herraje", desc=True).limit(5).execute()

        print("Respuesta de Supabase:", response.data)
        # print("Error de Supabase:", response.error)

        herraje_data = []
        
        if len(response.data) > 0:
            for herraje_item in response.data:
                herraje_data.append(
                    var_herraje(
                        herraje=herraje_item["herraje"],
                        unidades=herraje_item["unidades"],
                        valor=herraje_item["valor"]
                    )
                )

        return herraje_data
