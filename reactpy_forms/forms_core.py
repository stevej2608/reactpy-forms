import logging
from typing import Any, Callable, Dict, Tuple, Union, cast, overload, List

from pydantic import ValidationError
from pydantic_core import ErrorDetails

from reactpy import event, html, use_state
from reactpy.core.component import Component
from reactpy.core.hooks import current_hook
from reactpy.core.types import State, VdomDict

from reactpy_forms.field_model import FieldValidationError
from reactpy_forms.form_model import FormModel

from .types import FieldFunc, FormFunc, SetModelFunc, TFormModel, EventArgs, Props


log = logging.getLogger(__name__)

# pylint: disable=protected-access
# pyright: reportPrivateUsage=false

@overload
def use_form_state(initial_value: Callable[[], TFormModel]) -> State[TFormModel]:
    ...

@overload
def use_form_state(initial_value: TFormModel) -> State[TFormModel]:
    ...

def use_form_state(initial_value: TFormModel | Callable[[], TFormModel]) -> State[TFormModel]:
    """Create a form state model. Used in the same way
    as the reactpy hooks.use_state

    Parameters:
        initial_value:
            Defines the initial value of the state. A callable (accepting no arguments)
            can be used as a constructor function to avoid re-creating the initial value
            on each render.

    Returns:
        A tuple containing the current state and a function to update it.
    """

    model, dispatch = use_state(cast(TFormModel,initial_value))

    # TODO - change LifeCycleHook to make ._rendered_atleast_once accessible

    if not current_hook()._rendered_atleast_once: #noqa
        model.init_field_model()

    return State(model, dispatch)


def get_error(e: ValidationError) -> str:
    """Extract the user supplied error message from the Pydantic forest"""
    new_errors: List[ErrorDetails] = e.errors()
    for error in new_errors:
        msg = error['ctx']['error'].message # type:ignore
        return msg
    return 'unknown Error'


def create_form(model: TFormModel, set_model: SetModelFunc[TFormModel]) -> Tuple[FormFunc, FieldFunc]:
    """Accept the model and setter created by use_form_state() and return
    the Form & Field HOC's that will be used to wrap the form elements

    Args:
        model (FormModel): Form model created by use_form_state()
        set_model (Callable): Model setter created by use_form_state()

    Returns:
        Tuple[Form, Field]: Form & Field HOC's that will be used to wrap the form elements


    Usage:
    ```
        from pydantic import BaseModel

        class LoginFormData(BaseModel):
            email: str = None
            password: str = None


        model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))

        Form, Field = createForm(model, set_model)
        return Form(
            Field('email', lambda  props, field: html.input(props({'type':'email'}))),
            Field('password', lambda  props, field: html.input(props({'type': 'password'})))
            )

    ```
    """

    def _field(name:str, fn:Callable[[Any, Any], Any]) -> Component:

        if not model.has_field(name):
            raise FieldValidationError(f'Field "{name}" is not defined in the form model')

        # TODO: extract common code from event handlers

        @event(prevent_default=True)
        def on_change(event: EventArgs):

            field_model = model.get_field(name)

            field_model.value = event['target']['value']
            field_model.error = ''

            # log.info('on_change [%s]', field_model)

            try:

                # Update the model (this may fail validation)

                new_model = FormModel.update_model(model, update=field_model)

                # Inputs must be valid, update the external model

                set_model(new_model)


            except ValidationError as ex:

                # log.info('validation error [%s]', field_model)

                # Return the model to its previous state and set the error

                new_model = FormModel.update_model(model)

                # Update the field model with the value and the validation error.

                field_model.error = get_error(ex)
                new_model.set_field(field_model)

                # Update the external state

                set_model(new_model)

        @event(prevent_default=True)
        def on_click(event: EventArgs):
            field_model = model.get_field(name)
            # log.info('get_field_state [%s]', field_model)

            if isinstance(field_model.value, bool):
                field_model.value = not field_model.value
            elif isinstance(field_model.value, int):
                field_model.value = int(event['target']['value'])
            elif isinstance(field_model.value, str):
                field_model.value = event['target']['value']
            else:
                raise FieldValidationError(f'Field "{name}" is invalid type, expected [bool|int|str]')

            try:

                # Update the model (this may fail validation)

                new_model = FormModel.update_model(model, update=field_model)

                # Inputs must be valid, update the external model

                set_model(new_model)

            except ValidationError:
                log.info('validation error [%s]', field_model)


        field_state = model.get_field(name)

        def _props(props: Union[Props, None]=None):

            if props is None:
                props = {}

            props['name'] = name

            if 'type' in props and props['type'] in ['button', 'checkbox','radio','reset','submit']:
                props['on_click'] = on_click

                if props['type'] in ['checkbox'] and field_state.value:
                    props['checked'] = True

                if props['type'] in ['radio']:
                    if 'type' in props and str(field_state.value) == props['value']:
                        props['checked'] = True

            else:
                props['on_change'] = on_change
                if field_state.value is not None:
                    props['value'] = field_state.value

            return props

        form_input = fn(_props, field_state)
        return form_input

    def _form(*argv:Any, **kwarg: Dict[str, Any]) -> VdomDict:
        return html.form(*argv, **kwarg)

    # return [_form, _field]
    return (_form, _field)
