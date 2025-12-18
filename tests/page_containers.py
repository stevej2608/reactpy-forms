from reactpy import component, html
from reactpy.types import ComponentType
from reactpy.testing import DisplayFixture


from utils.server_options.pico_options import PICO_CSS
from .tooling import page_stable

class PicoContainer:
    """Simple wrapper for the reactpy component being tested"""

    def __init__(self, display:DisplayFixture):
        self.display = display

    async def show(self, app: ComponentType) -> None:
        """Show a ReactPy component in a Pico CSS styled container.

        Args:
            app: A component function (not called - pass the function itself)
        """

        @component
        def AppContainer():
            return html._(
                html.head(
                    html.link(PICO_CSS)
                ),
                app()  # Call the component here inside AppContainer
            )

        await self.display.show(AppContainer)


    async def page_stable(self):
        await page_stable(self.display.page)
