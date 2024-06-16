import pytest
from playwright.async_api import Page

from examples.form_login import LoginForm
from tests.page_containers import PicoContainer
from tests.tooling.helpers import page_element, input_field


# pytest -o log_cli=1 --headed tests/test_login_form.py

@pytest.mark.anyio
async def test_form(pico_container: PicoContainer, page: Page):

    await pico_container.show(LoginForm)

    get_error = page_element(page, '#email-error')

    get_email, set_email = input_field(page, '#email')
    get_password, _set_password = input_field(page, '#password')

    # Test initial condition

    assert (await get_email()) == 'joe@gmail.com'
    assert (await get_password()) == '1234'
    assert (await get_error()) == ''

    # Add valid email

    await set_email('bigjoe@gmail.com')
    assert (await  get_email()) == 'bigjoe@gmail.com'
    assert (await get_error()) == ''

    # Add invalid email - test for error message

    await set_email('xxx')
    assert (await  get_email()) == 'xxx'

    err = await get_error()
    assert err == 'xxx is an invalid email!'

    # Add valid email

    await set_email('bigjoe@gmail.com')
    assert (await  get_email()) == 'bigjoe@gmail.com'
    assert (await get_error()) == ''
