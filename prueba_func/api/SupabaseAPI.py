import os
import dotenv
from supabase import create_client, Client
from prueba_func.model.Featured import Featured 
from prueba_func.model.HERRAJES import HERRAJES
from prueba_func.model.MUEBLES import MUEBLES
from PIL import Image
import requests



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
    

    def Herrajes(self) -> list[HERRAJES]:
        
        response = self.supabase.table("HERRAJES").select("*").order("herraje").limit(10).execute()

        print("Respuesta de Supabase:", response.data)
        # print("Error de Supabase:", response.error)

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
    
    
    def Muebles(self) -> list[MUEBLES]:
        
        response = self.supabase.table("MUEBLES").select("*").order("mueble").limit(50).execute()

        print("Respuesta de Supabase:", response.data)
        # print("Error de Supabase:", response.error)

        mueble_data = []
        
        if len(response.data) > 0:
            for mueble_item in response.data:
                mueble_data.append(
                    MUEBLES(
                        mueble=mueble_item["mueble"],
                        descripcion=mueble_item["descripcion"],
                        image=mueble_item["image"]
                        # valor=herraje_item["valor"]
                    )
                )

        return mueble_data
   
    
    def obtener_muebles(self) -> list[MUEBLES]:
    # """Función para obtener los datos de la columna 'mueble' de la tabla 'MUEBLES' en Supabase."""
        try:
            # Realiza la consulta en Supabase
            response = self.supabase.table("MUEBLES").select("mueble").execute()
            # Obtiene solo los nombres de los muebles como una lista
            muebles_fila = [registro["mueble"] for registro in response.data]
            return muebles_fila
        except Exception as e:
            print(f"Error obteniendo muebles: {e}")
            return []

   
   
    def muestra_muebles(self) -> list[Image.Image]:
        try:
            # Realiza la consulta a Supabase para obtener las imágenes
            response = self.supabase.table("MUEBLES").select("image").execute()
            
            # Regresa una lista de imágenes
            imagen_mueble = [imagen_reg["image"] for imagen_reg in response.data]
            
            loaded_images = []  # Lista para almacenar las imágenes cargadas

            # Itera sobre cada URL de imagen
            for url in imagen_mueble:
                try:
                    # Carga la imagen desde la URL
                    image_new = Image.open(requests.get(url, stream=True).raw)
                    loaded_images.append(image_new)  # Almacena la imagen cargada
                except Exception as img_error:
                    print(f"Error al cargar la imagen desde {url}: {img_error}")
                    loaded_images.append(None)  # Agrega None si hay un error

            return loaded_images  # Retorna la lista de imágenes cargadas
        except Exception as e:
            print(f"Error obteniendo imagen muebles: {e}")
            return []
