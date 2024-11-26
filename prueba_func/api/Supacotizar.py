import os
import dotenv
from supabase import create_client, Client

dotenv.load_dotenv()

class BaseAPI:
    def __init__(self):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")

        if not self.supabase_url or not self.supabase_key:
            raise ValueError("Faltan las credenciales de Supabase")

        self.client: Client = create_client(self.supabase_url, self.supabase_key)


    def execute_query(self, query: str):
        """Ejecuta una consulta SQL en Supabase."""
        try:
            response = self.client.rpc("execute_query", {"sql": query})
            return response.data
        except Exception as e:
            print(f"Error ejecutando consulta: {e}")
            return []