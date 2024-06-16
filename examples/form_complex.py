from typing import Union
from reactpy import component, event, html
from reactpy_forms import create_form, FormModel, use_form_state

from utils.logger import log, logging
from utils.pico_run import pico_run
from utils.types import EventArgs

from .components.input import FieldSet, Input, RangeSlider, Select, TextInput

class ComplexFormData(FormModel):
    search: Union[str, None] = None
    text: Union[str, None] = None
    select: Union[str, None] = None


@component
def ComplexForm():

    model, set_model = use_form_state(ComplexFormData())

    Form, Field = create_form(model, set_model)

    @event(prevent_default=True)
    def handle_submit(e: EventArgs):
        log.info('handle_submit %s', e)


    return Form(
        html.h2("Form elements"),

        # Search

        Field('search', lambda field, props : TextInput(
            props({'type': 'search', 'name': 'search', 'placeholder':'Search', 'label': 'Search', 'value':''})
            )
        ),


        # Text

        Field('text', lambda field, props : TextInput(
            props({'type': 'search', 'name': 'text', 'placeholder':'Text', 'label': 'Text', 'value':''})
            )
        ),

        html.small("Curabitur consequat lacus at lacus porta finibus."),

        # Select

        Field('select', lambda field, props : Select(
            props({'label': 'Select'}),
            html._(
                html.option({'value': '', 'selected': ''}, "Select…"),
                html.option("…")
            ))
        ),

        # File browser

        Input(type='file', id='file', name='file',label='File browser', value=''),

        # Range slider control

        RangeSlider(min=0, max=100, value=50, id='range', name='range', label='Range Slider'),

        # States

        html.div({'class_name': 'grid'},
            Input(type='text', id='valid', name='valid', placeholder='valid', label='Valid', invalid=False),
            Input(type='text', id='invalid', name='invalid', placeholder='invalid', label='Invalid', invalid=True),
            Input(type='text', id='disabled', name='disabled',placeholder='disabled' ,label='Disabled', disabled=True),

        ),

        html.div({'class_name': 'grid'},
            # Date
            Input(type='date', id='date', name='date', label='Date'),
            # Time
            Input(type='time', id='time', name='time', label='Time'),
            # Color
            Input(type='color', id='color', name='color', label='Color')

        ),
        html.div({'class_name': 'grid'},

            # Checkboxes,

            FieldSet(legend='Checkboxes',
                children=html._(
                    Input(type='checkbox', id='checkbox-1', name='checkbox-1', label='Checkbox'),
                    Input(type='checkbox', id='checkbox-2', name='checkbox-2', label='Checkbox')
                )
            ),

            # Radio buttons,

            FieldSet(legend='Radio buttons',
                children=html._(
                    Input(type='radio', id='radio-1', name='radio-1', label='Radio'),
                    Input(type='radio', id='radio-2', name='radio-2', label='Radio')
                )
            ),

            # Switch,

            FieldSet(legend='Switches',
                children=html._(
                    Input(type='checkbox', id='switch-1', name='switch-1', role='switch', label='Switch'),
                    Input(type='checkbox', id='switch-2', name='switch-2', role='switch', label='Switch')
                )
            ),

        ),
        # Buttons,
        Input(type='reset', value='Reset'),
        Input(type='submit', value='Submit')
    )

# python -m examples.form_complex

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(ComplexForm)
