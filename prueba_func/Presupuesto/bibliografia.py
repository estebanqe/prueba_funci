import asyncio
from supabase import create_client, Client

# Configura tu cliente Supabase
SUPABASE_URL = "https://tu-supabase-url"
SUPABASE_KEY = "tu-supabase-key"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def obtener_urls_imagenes():
    try:
        # Consulta asincrónica en Supabase para obtener la columna 'image_url'
        response = await supabase.table("tabla_de_imagenes").select("image_url").execute()
        
        # Extrae solo las URLs de imagen
        urls_imagenes = [registro["image_url"] for registro in response.data]
        return urls_imagenes
    except Exception as e:
        print(f"Error obteniendo URLs de imágenes: {e}")
        return []





from reflex import State

class PageState(State):
    urls_imagenes: list[str] = []



import reflex as rx

def galeria_imagenes() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            PageState.urls_imagenes,
            lambda url:
                rx.image(
                    src=url,
                    width="100px",
                    height="auto",
                    border_radius="15px 50px",
                    border="5px solid #555",
                    alt="Imagen desde Supabase"
                )
        ),
        spacing="20px",
        align_items="center"
    )






https://moure.dev/preview.jpg