## reactpy-forms

![](./docs/img/reactpy-forms.jpg)

Headless forms for ReactPy

### Features

- [X] Headless, CSS agnostic
- [X] Field validation 
- [X] 100% fully typed python


## Usage

	pip install reactpy-forms

[form_login.py](./examples/form_login.py)
```python

class LoginFormData(FormModel):
    email: Union[str, None] = None
    password: Union[str, None] = None


@component
def LoginForm():

    model, set_model = use_form_state(LoginFormData(email="joe@gmail.com", password="1234"))

    Form, Field = create_form(model, set_model)

    @event(prevent_default=True)
    def onclick(event: EventArgs):
        log.info('SUBMIT [%s]', model)

    return Form(
        html.h2("Login"),
        Field('email', lambda field, props: TextInput('Email', field, props({'id': 'email', 'type':'email'}))),
        Field('password', lambda field, props: TextInput('Password', field, props({'id': 'password'}))),
        SubmitButton('Login', model, onclick=onclick)
    )

```


[modularforms]: https://modularforms.dev/solid/guides/introduction

