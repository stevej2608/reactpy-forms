from typing import Callable, Dict, Any, Union, Protocol
from reactpy.types import Component, VdomDict

from reactpy_forms.field_model import FieldModel
from reactpy_forms.form_model import TFormModel

EventArgs = Dict[str, Any]

Props = Dict[str, Any]

# TODO: Tie this down

class FormFunc(Protocol):
    def __call__(self, *argv:Any, **kwarg: Dict[str, Any]) -> VdomDict: ...

#

_PropsFunc = Callable[[Props], Props]
_CompnentFunc = Callable[[_PropsFunc, FieldModel], Union[VdomDict, Component]]

class FieldFunc(Protocol):
    def __call__(self, name:str, fn:_CompnentFunc) -> Component: ...

#

SetModelFunc = Callable[[Union[TFormModel, Callable[[TFormModel],TFormModel]]],None]
