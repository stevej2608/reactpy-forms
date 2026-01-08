
from examples.form_login import LoginForm
from tests.tooling.page_containers import IContainer
from tests.tooling.playwright_helpers import page_element, input_field

# hatch test tests/test_login_form.py

async def test_form(container: IContainer):

    await container.show(LoginForm)
    await container.page_stable()

    get_error = page_element(container.page, '#email-error')

    get_email, set_email = input_field(container.page, '#email')
    get_password, _set_password = input_field(container.page, '#password')

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
