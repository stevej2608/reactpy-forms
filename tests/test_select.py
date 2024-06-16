
import pytest
from playwright.async_api import Page

from tests.page_containers import PicoContainer
from tests.tooling.helpers import page_element, select_element

from examples.form_select import TestForm

# pytest -o log_cli=1 --headed tests/test_select.py

@pytest.mark.anyio
async def test_select(pico_container: PicoContainer, page: Page):
    """Confirm support for html select field"""

    # Render the test component

    await pico_container.show(TestForm)

    # setup helpers

    selected = page_element(page, '#selected_example')
    select, select_option = select_element(page, '#select_example')

    # Confirm initial condiion

    assert (await selected()) == 'Selected:None'

    # Select and confirm 'Japanese'

    await select_option('Japanese')
    assert (await  select()) == 'Japanese'

    # Confirm model has been updated

    assert (await selected()) == 'Selected:Japanese'

    # Select and confirm 'Italian'

    await select_option('Italian')
    assert (await  select()) == 'Italian'

    # Confirm model has been updated

    assert (await selected()) == 'Selected:Italian'

    assert True
