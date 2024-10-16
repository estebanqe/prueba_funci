import reflex as rx
from prueba_func.api.api import live, featured
from prueba_func.model.Featured import Featured

USER = "esteban"

class PageState(rx.State):
    
    is_live: bool
    featured_info: list[Featured]

    
    async def check_live(self):
        self.is_live = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()