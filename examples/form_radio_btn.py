
from reactpy import component, html
from reactpy_forms import FormModel, create_form, use_form_state
from utils.logger import log, logging
from utils.pico_run import pico_run


class FormData(FormModel):
    language: str = "english"


@component
def TestForm():

    model, set_model = use_form_state(FormData)
    Form, Field = create_form(model, set_model)

    # https://picocss.com/docs/forms/radios


    form = Form(
        html.fieldset(
            html.legend("Language preference:"),
            Field('language', lambda props, _ : html.label(
                html.input(props({'type': 'radio', 'value': 'english'})),
                "English"
            )),
            Field('language', lambda props, _ : html.label(
                html.input(props({'type': 'radio', 'value': 'french'})),
                "French"
            )),
            Field('language', lambda props, _ : html.label(
                html.input(props({'type': 'radio', 'value': 'manderin'})),
                "Mandarin"
            )),
            Field('language', lambda props, _ : html.label(
                html.input(props({'type': 'radio', 'value': 'thai'})),
                "Thai"
            )),
            Field('language', lambda props, _ : html.label(
                html.input(props({'type': 'radio', 'value': 'dothraki', 'disabled': ''})),
                "Dothraki"
            ))
        )

    )

    return html.div(
        html.h2({'id': 'radio_example'}, f"Selected:{model}"),
        form
    )

# python -m examples.form_radio_btn

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(TestForm)
