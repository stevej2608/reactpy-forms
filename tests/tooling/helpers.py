
from playwright.async_api import Page
from .wait_page import wait_page

def page_element(page: Page, name: str):

    @wait_page(page)
    async def get_text():
        element = await page.query_selector(name)
        if element:
            value = await element.text_content()
            return value
        else:
            return None
    return get_text

def input_field(page: Page, name: str):

    @wait_page(page)
    async def get_input():
        element = await page.query_selector(name)
        if element:
            value = await element.input_value()
            return value
        return None

    @wait_page(page)
    async def set_input(value:str):
        element = await page.query_selector(name)
        if element:
            await element.fill(value)

    return [get_input, set_input]


def select_element(page: Page, name: str):
    """Returns methods to allow control of html select element

    Args:
        page (Page): The page that contains the select element
        name (str): The html selector name

    Returns:
        callables: get_selection, select_option
    """

    # https://playwright.dev/python/docs/api/class-locator#locator-select-option

    @wait_page(page)
    async def get_selection():
        element = await page.query_selector(name)
        if element:
            value = await element.get_property('value')
            return str(value)
        else:
            return None

    @wait_page(page)
    async def select_option(value:str):
        element = await page.query_selector(name)
        if element:
            await element.select_option(value)

    return get_selection, select_option


def checkbox_element(page: Page, name: str):

    @wait_page(page)
    async def get_checked():
        element = await page.query_selector(name)
        if element:
            value = await element.get_property('checked')
            # value = await element.get_property('value')
            return str(value) == 'true'
        else:
            return None

    @wait_page(page)
    async def set_checkbox(value:bool):
        element = await page.query_selector(name)
        if element:

            # https://playwright.dev/python/docs/api/class-locator#locator-set-checked
            # https://playwright.dev/python/docs/api/class-locator#locator-click

            try:
                await element.click()
            except Exception:
                pass

    return get_checked, set_checkbox


def radio_btn_element(page: Page, selector: str):

    @wait_page(page)
    async def get_radio_btn():
        element = await page.query_selector(selector)
        if element:
            value = await element.get_property('checked')
            # value = await element.get_property('value')
            return str(value) == 'true'
        else:
            return None

    @wait_page(page)
    async def set_radio_btn(value:str):
        element = await page.query_selector(f"css={selector}")
        if element:

            # https://playwright.dev/python/docs/api/class-locator#locator-set-checked
            # https://playwright.dev/python/docs/api/class-locator#locator-click

            try:
                await element.click()
            except Exception:
                pass

    return get_radio_btn, set_radio_btn
