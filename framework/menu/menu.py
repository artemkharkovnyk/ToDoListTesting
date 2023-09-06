from selenium.webdriver.remote.webelement import WebElement
from framework.logging import logger
from framework.pages.page import Page


class Menu:
    def __init__(self,
                 button: WebElement = None,
                 url: str = None,
                 name: str = None,
                 autoopen: bool = False,
                 openwith: str = 'button'):
        self.button = button
        self.url = url
        self.name = name
        if autoopen:
            {'button': self.open_with_button, 'url': self.open_with_url}.get(openwith)()

    def open_with_button(self):
        self.button.click()
        logger.info(f'Menu "{self.name}" was opened with using button')

    def open_with_url(self):
        Page(url=self.url).open_with_url()
        logger.info(f'Menu "{self.name}" was opened with using url {self.url}')
