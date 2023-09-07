from selenium.webdriver.remote.webelement import WebElement
from .menu import Menu
from .settings import SettingsMenu
from framework.logging import logger
from framework.pages.page import Page


class AddWorkspaceMenu(Menu):
    def __init__(self, button: WebElement):
        super().__init__(button=button, autoopen=True, openwith='button')
        page = Page()
        self.name_field = page.find_element_by_css_selector('[placeholder="The name of your team or company"]')
        self.submit_btn = page.find_element_by_css_selector('[data-gtm-id="workspace_add"]')

    def enter_workspace_name(self, workspace_name: str) -> None:
        self.name_field.send_keys(workspace_name)
        logger.info(f'entered workspace name "{workspace_name}"')

    def add(self):
        self.submit_btn.click()
        logger.info(f'added new workspace')