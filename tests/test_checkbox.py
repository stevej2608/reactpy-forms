import pytest
from playwright.async_api import Page

from tests.page_containers import PicoContainer
from tests.tooling.helpers import page_element, checkbox_element

from examples.form_checkbox import TestForm

# pytest -o log_cli=1 --headed tests/test_checkbox.py

@pytest.mark.anyio
async def test_checkbox(pico_container: PicoContainer, page: Page):
    """Confirm support for html checkbox field"""

    # Render the test component

    await pico_container.show(TestForm)

    # setup helpers

    checked = page_element(page, '#checkbox_example')

    # Confirm initial condiion

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=False thai=False'

    # Select and confirm 'Manderin'

    get_checked, set_checked = checkbox_element(page, '#mandarin')

    await set_checked(True)
    assert (await  get_checked()) is True

    # Confirm model has been updated

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=True thai=False'

    # Select and confirm 'Dothraki'

    get_checked, set_checked = checkbox_element(page, '#dothraki')

    # await check_dothraki(True)
    assert (await  get_checked()) is False

    # Confirm model has been updated

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=True thai=False'
