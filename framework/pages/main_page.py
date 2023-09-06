from .page import Page
from framework.menu import MainPageMenu

class MainPage(Page):
    def __init__(self):
        super().__init__('https://todoist.com/')

    def open_menu(self) -> MainPageMenu:
        settings_btn = self.find_element_by_css_selector('[aria-label="Settings"]')
        menu = MainPageMenu(button=settings_btn)
        return menu


