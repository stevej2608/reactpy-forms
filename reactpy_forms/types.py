from typing import Callable, Dict, Any, Union, Protocol
from reactpy.types import ComponentType, VdomDict

from reactpy_forms.field_model import FieldModel
from reactpy_forms.form_model import TFormModel

EventArgs = Dict[str, Any]

Props = Dict[str, Any]

# TODO: Tie this down

class FormFunc(Protocol):
    def __call__(self, *argv:Any, **kwarg: Dict[str, Any]) -> VdomDict: ...

#

_PropsFunc = Callable[[Props], Props]
_CompnentFunc = Callable[[_PropsFunc, FieldModel], Union[VdomDict, ComponentType]]

class FieldFunc(Protocol):
    def __call__(self, name:str, fn:_CompnentFunc) -> ComponentType: ...

#

SetModelFunc = Callable[[Union[TFormModel, Callable[[TFormModel],TFormModel]]],None]
