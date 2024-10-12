import reflex as rx
import prueba_func.utils as utils
from prueba_func.api.api import live, featured, schedule
from prueba_func.model.Featured import Featured
from prueba_func.model.Live import Live

USER = "mouredev"


class PageState(rx.State):

    timezone = ""
    live_status = Live(live=False, title="")
    next_live = ""
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = await live(USER)

    async def check_schedule(self):
        if self.timezone == "":
            return rx.call_script(
                utils.LOCAL_TIMEZONE_SCRIPT,
                PageState.update_timezone
            )
        else:
            await self.update_timezone(self.timezone)

    async def update_timezone(self, timezone: str):
        self.timezone = timezone
        self.next_live = utils.next_date(await schedule(), self.timezone)

    async def featured_links(self):
        self.featured_info = await featured()