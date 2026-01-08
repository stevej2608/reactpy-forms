from tests.tooling.page_containers import IContainer
from tests.tooling.playwright_helpers import page_element, checkbox_element

from examples.form_checkbox import TestForm

# pytest -o log_cli=1 --headed tests/test_checkbox.py


async def test_checkbox(container: IContainer):
    """Confirm support for html checkbox field"""

    # Render the test component

    await container.show(TestForm)

    # setup helpers

    checked = page_element(container.page, '#checkbox_example')

    # Confirm initial condition

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=False thai=False'

    # Select and confirm 'Mandarin'

    get_checked, set_checked = checkbox_element(container.page, 'mandarin')

    await set_checked(True)
    assert (await  get_checked()) is True

    # Confirm model has been updated

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=True thai=False'

    # Select and confirm 'Dothraki'

    get_checked, set_checked = checkbox_element(container.page, 'dothraki')

    # await check_dothraki(True)
    assert (await  get_checked()) is False

    # Confirm model has been updated

    assert (await checked()) == 'Selected:dothraki=False english=True french=True mandarin=True thai=False'
