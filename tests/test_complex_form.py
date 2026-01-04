from examples.form_complex import ComplexForm
from tests.tooling.page_containers import IContainer

# pytest -o log_cli=1 --headed tests/test_complex_form.py


async def test_form(container: IContainer):
    await container.show(ComplexForm)
    assert True
