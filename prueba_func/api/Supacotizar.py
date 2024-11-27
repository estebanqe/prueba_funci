import os
import dotenv
from supabase import create_client, Client



class BaseAPI:
    

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.client: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )