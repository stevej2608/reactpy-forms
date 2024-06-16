from typing import Union
from reactpy import component, html
from reactpy_forms import FormModel, create_form, use_form_state
from utils.logger import log, logging
from utils.pico_run import pico_run

class FormData(FormModel):
    favorite_food: Union[str, None] = None

@component
def TestForm():

    model, set_model = use_form_state(FormData)

    Form, Field = create_form(model, set_model)

    # https://picocss.com/docs/forms/select

    form = Form(
        Field('favorite_food', lambda field, props : html.select(
            props({'id': 'select_example'}),
            html._(
                html.option("Select your favorite cuisine.."),
                html.option("Italian"),
                html.option("Japanese"),
                html.option("Thai"),
                html.option("French")
            ))
        ),
    )

    return html.div(
        html.h2({'id': 'selected_example'}, f"Selected:{model.favorite_food}"),
        form
    )

# python -m examples.form_select

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(TestForm)

