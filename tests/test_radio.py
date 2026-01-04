from playwright.async_api import Page

from tests.page_containers import PicoContainer
from tests.tooling.playwright_helpers import page_element, radio_btn_element

from examples.form_radio_btn import TestForm

# pytest -o log_cli=1 --headed tests/test_radio.py

async def test_select(pico_container: PicoContainer):
    """Confirm support for html radio buttons field"""

    # Render the test component

    await pico_container.show(TestForm)

    # setup helpers

    selected = page_element(pico_container.page, '#radio_example')
    get_radio_btn_checked, set_radio_btn = radio_btn_element(pico_container.page, "english")

    # Confirm initial condition

    assert (await selected()) == "Selected:language='english'"

    # Select and confirm 'French'

    get_radio_btn_checked, set_radio_btn = radio_btn_element(pico_container.page, "french")

    await set_radio_btn('french')
    assert (await  get_radio_btn_checked()) is True

    # Confirm model has been updated

    assert (await selected()) == "Selected:language='french'"

    # Select and confirm 'Thai'

    get_radio_btn_checked, set_radio_btn = radio_btn_element(pico_container.page, "thai")

    await set_radio_btn('thai')
    assert (await  get_radio_btn_checked()) is True

    # Confirm model has been updated

    assert (await selected()) == "Selected:language='thai'"

    assert True
