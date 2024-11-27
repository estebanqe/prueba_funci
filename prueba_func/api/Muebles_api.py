from prueba_func.api.Supacotizar import BaseAPI
from prueba_func.model.MUEBLES import MUEBLES

class MueblesAPI(BaseAPI):
    def Muebles(self) -> list[MUEBLES]:
        
        response = self.client.table("MUEBLES").select("*").order("mueble").limit(50).execute()

        mueble_data = []
        
        if len(response.data) > 0:
            for mueble_item in response.data:
                mueble_data.append(
                    MUEBLES(
                        id=mueble_item["id"],
                        mueble=mueble_item["mueble"],
                        descripcion=mueble_item["descripcion"],
                        url_image=mueble_item["url_image"]
                    )
                )

        return mueble_data
     