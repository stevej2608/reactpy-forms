from playwright.async_api import Page

from tests.page_containers import PicoContainer
from tests.tooling.playwright_helpers import page_element, select_element

from examples.form_select import TestForm

# pytest -o log_cli=1 --headed tests/test_select.py

async def test_select(pico_container: PicoContainer):
    """Confirm support for html select field"""

    # Render the test component

    await pico_container.show(TestForm)
    await pico_container.page_stable()
    
    # setup helpers

    selected = page_element(pico_container.page, '#selected_example')
    get_select_option, set_select_option = select_element(pico_container.page, '#select_example')

    # Confirm initial condiion

    assert (await selected()) == 'Selected:None'

    # Select and confirm 'Japanese'

    await set_select_option('Japanese')
    assert (await  get_select_option()) == 'Japanese'

    # Confirm model has been updated

    assert (await selected()) == 'Selected:Japanese'

    # Select and confirm 'Italian'

    await set_select_option('Italian')
    assert (await  get_select_option()) == 'Italian'

    # Confirm model has been updated

    assert (await selected()) == 'Selected:Italian'

    assert True
