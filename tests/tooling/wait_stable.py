import asyncio
import os

from playwright.async_api._generated import Page

GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS", "").lower() == "true"
CLICK_DELAY = 250 if GITHUB_ACTIONS else 25  # Delay in milliseconds.


async def page_stable(page: Page) -> None:
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")
    await asyncio.sleep(CLICK_DELAY / 1000)
