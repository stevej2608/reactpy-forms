
from reactpy import component, html
from reactpy_forms import FormModel, create_form, use_form_state
from utils.logger import log, logging
from utils.pico_run import pico_run


class FormData(FormModel):
    dothraki: bool = False
    english: bool = True
    french: bool = True
    mandarin: bool = False
    thai: bool = False

@component
def TestForm():

    model, set_model = use_form_state(FormData)
    Form, Field = create_form(model, set_model)

    # https://picocss.com/docs/forms/checkboxes

    form = Form(
        html.fieldset(
            html.legend("Language preferences:"),
            Field('english', lambda field, props : html.label(
                html.input(props({'type': 'checkbox', 'name': 'english'})),
                "English"
            )),
            Field('french', lambda field, props : html.label(
                html.input(props({'type': 'checkbox', 'name': 'french'})),
                "French"
            )),
            Field('mandarin', lambda field, props : html.label(
                html.input(props({'type': 'checkbox', 'name': 'mandarin', 'id': 'mandarin'})),
                "Mandarin"
            )),
            Field('thai', lambda field, props : html.label(
                html.input(props({'type': 'checkbox', 'name': 'thai'})),
                "Thai"
            )),
            Field('dothraki', lambda field, props : html.label(
                html.input(props({'type': 'checkbox', 'name': 'dothraki', 'id': 'dothraki', 'disabled': True})),
                "Dothraki"
            ))
        )

    )

    return html.div(
        html.h2({'id': 'checkbox_example'}, f"Selected:{model}"),
        form
    )

# python -m examples.form_checkbox

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(TestForm)
