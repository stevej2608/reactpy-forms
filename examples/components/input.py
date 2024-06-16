from typing import Literal, Union
from reactpy import component, html
from reactpy.core.types import VdomChildren
from utils.props import props
from utils.types import Props

from .utils import ID

InputTypes = Literal[
    'button'
    'checkbox',
    'date',
    'datetime-local',
    'email',
    'file',
    'image',
    'month',
    'number',
    'password',
    'radio',
    'reset',
    'search',
    'submit',
    'tel',
    'text', 
    'time',
    'url',
    'week', 
]

def add_id(props: Props):
    if not 'id' in props:
        id = ID.inc()
        props['id'] = id
    return props['id']


@component
def TextInput(props: Props):
    id = add_id(props)
    return html.div(
        html.label({'html_for': id},  props['label']),
        html.input(props)
    )


@component
def Input(label:Union[str,None]='', id:Union[str,None]=None, type:InputTypes='text',
          name:Union[str,None]=None, placeholder:Union[str,None]=None, value:Union[str,None]=None, role:Union[str,None]=None,
          invalid:Union[bool,None]=None, disabled:Union[bool,None]=None):

    input_props = props(include='id, type, name, placeholder, role, value, disabled')

    if invalid is not None:
        input_props['aria-invalid'] = invalid

    if type in ['checkbox', 'radio']:
        return html.div(
            html.input(input_props),
            html.label({'html_for': id}, label or '')
        )

    return html.div(
        html.label({'html_for': id}, label or '' ),
        html.input(input_props)
    )

@component
def RangeSlider(min:int=0, max:int=100, value:int=0, id:Union[str,None]=None, name:Union[str,None]=None, label:Union[str,None]=None):
    input_props = {'type': 'range', **props(include="min, max, value, id, name")}
    return html.div(
        html.label({'html_for': id}, label or '' ),
        html.input(input_props)
    )

@component
def Select(props: Props, options: VdomChildren):
    id = add_id(props)
    return html.div(
        html.label({'html_for': id}, props['label']),
        html.select(props, options)
    )

@component
def FieldSet(legend:Union[str,None]=None, children: Union[VdomChildren,None] = None):
    return html.fieldset(
        html.legend(html.strong(legend or '')),
        children if children else []
    )
