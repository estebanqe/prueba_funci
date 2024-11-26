from prueba_func.api.Supacotizar import BaseAPI
from prueba_func.model.MODELOS import MODELOS

class ModelosAPI(BaseAPI):
     def Modelos(self) -> list[MODELOS]:
        
        response = self.client.table("MODELOS").select("*").order("modelo").limit(50).execute()

        print(response.data)
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
    