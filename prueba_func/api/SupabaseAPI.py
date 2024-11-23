import os
import dotenv
from supabase import create_client, Client
from prueba_func.model.Featured import Featured 
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES
from prueba_func.model.MODELOS import MODELOS




class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    
    
    def Muebles(self) -> list[MUEBLES]:
        
        response = self.supabase.table("MUEBLES").select("*").order("mueble").limit(50).execute()

        mueble_data = []
        
        if len(response.data) > 0:
            for mueble_item in response.data:
                mueble_data.append(
                    MUEBLES(
                        mueble=mueble_item["mueble"],
                        descripcion=mueble_item["descripcion"],
                        url_image=mueble_item["url_image"]
                    )
                )

        return mueble_data
    
    
    def Modelos(self) -> list[MODELOS]:
        
        response = self.supabase.table("MODELOS").select("*").order("modelo").limit(50).execute()

        modelo_data = []
        
        if len(response.data) > 0:
            for modelo_item in response.data:
                modelo_data.append(
                    MODELOS(
                        modelo=modelo_item["modelo"],
                        descripcion=modelo_item["descripcion"],
                        url_image=modelo_item["url_image"],
                        id_muebles=modelo_item["id_muebles"]
                    )
                )

        return modelo_data
    
    
   
    # def SQL_Modelos(self) -> list[MUEBLES,MODELOS]:
    # # Ejecutar la consulta SQL personalizada con JOIN
    #     response = self.supabase.query("""
    #         SELECT 
    #         "MUEBLES".mueble,
    #         "MUEBLES".descripcion,
    #         "MUEBLES".url_image,
    #         "MODELOS".modelo,
    #         "MODELOS".url_image AS imagen_modelo
    #         FROM
    #         "MUEBLES"
    #         INNER JOIN "MODELOS" ON "MUEBLES".id = "MODELOS".id_muebles
    #         WHERE "MUEBLES".id = 1;
    #     """).execute()

    #     # Crear una lista para almacenar los muebles procesados
    #     sql_mueble_data = []

    #     # Verificar si la consulta devolvió datos
    #     if len(response.data) > 0:
    #         for mueble_item in response.data:
    #             # Agregar cada elemento al mueble_data como un objeto de tipo MODELOS
    #             sql_mueble_data.append(
    #                 MUEBLES,MODELOS(
    #                     mueble=mueble_item["mueble"],
    #                     descripcion=mueble_item["descripcion"],
    #                     url_image=mueble_item["url_image"],
    #                     modelo=mueble_item["modelo"],
    #                     imagen_modelo=mueble_item["imagen_modelo"]
    #                 )
    #             )

    #     return sql_mueble_data



    
    
    
    
    
    
    
    
    
    
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
    

    def Herrajes(self) -> list[HERRAJES]:
        
        response = self.supabase.table("HERRAJES").select("*").order("herraje").limit(10).execute()

        herraje_data = []
        
        if len(response.data) > 0:
            for herraje_item in response.data:
                herraje_data.append(
                    HERRAJES(
                        herraje=herraje_item["herraje"],
                        descripcion=herraje_item["descripcion"],
                        # valor=herraje_item["valor"]
                    )
                )

        return herraje_data
    
    
    
    