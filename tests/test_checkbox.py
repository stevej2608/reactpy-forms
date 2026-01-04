from playwright.async_api import Page

from tests.page_containers import PicoContainer
from tests.tooling.playwright_helpers import page_element, checkbox_element

from examples.form_checkbox import TestForm

# pytest -o log_cli=1 --headed tests/test_checkbox.py


async def test_checkbox(pico_container: PicoContainer):
    """Confirm support for html checkbox field"""

    # Render the test component

    await pico_container.show(TestForm)

    # setup helpers

    checked = page_element(pico_container.page, '#checkbox_example')

    # Confirm initial condition

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=False thai=False'

    # Select and confirm 'Mandarin'

    get_checked, set_checked = checkbox_element(pico_container.page, 'mandarin')

    await set_checked(True)
    assert (await  get_checked()) is True

    # Confirm model has been updated

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=True thai=False'

    # Select and confirm 'Dothraki'

    get_checked, set_checked = checkbox_element(pico_container.page, 'dothraki')

    # await check_dothraki(True)
    assert (await  get_checked()) is False

    # Confirm model has been updated

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=True thai=False'
