from typing import Type, Any, cast, TypeVar
from reactpy.types import ComponentType as ReactPyComponentType

NONE = cast(Any, None)

# Note: This ComponentClass implementation may need updates for ReactPy v2
# Consider using the standard @component decorator instead
class ComponentClass(ReactPyComponentType):  # type: ignore

    def __init__(self):
        # This initialization may not work correctly with ReactPy v2
        super().__init__(NONE, NONE, NONE, NONE, NONE)  # type: ignore

ComponentType = TypeVar('ComponentType', bound=ComponentClass)

def class_component(comp: Type[ComponentType]):
    """ReactPy ComponentClass decorator

    Args:
        comp (ComponentClass): Class to be wrapped

    Usage:
    ```
        from reactpy import html, run
        from utils.component_class import class_component, ComponentClass

        @class_component
        class HelloWorld(ComponentClass):

            def render(self):
                return html.h2('Hello World!')

        run(HelloWorld)
    ```
    """

    def create_component(*argv: Any, **kwargs: Any) -> ComponentType:
        return comp(*argv, **kwargs)

    return create_component
