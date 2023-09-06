from selenium.webdriver.remote.webelement import WebElement
from .menu import Menu
from framework.logging import logger
from framework.pages.page import Page


class MainPageMenu(Menu):
    def __init__(self, button: WebElement):
        super().__init__(button=button, autoopen=True, openwith='button')
        menu = Page().find_element_by_css_selector('[role="menu"]')
        menu_elements = menu.find_elements('css selector', '[role="menuitem"]')
        self.settings_btn = menu_elements[0]
        self.add_team_workspace_btn = menu_elements[1]
        self.theme_btn = menu_elements[2]
        self.activity_log_btn = menu_elements[3]
        self.print_btn = menu_elements[4]
        self.integrations_btn = menu_elements[5]
        self.upgrade_to_pro = menu_elements[6]
        self.download_apps_btn = menu_elements[7]
        self.logout_btn = menu_elements[8]
        self.version_btn = menu_elements[9]
        self.what_is_new_btn = menu_elements[10]

    def logout(self) -> bool:
        self.logout_btn.click()
        page = Page()
        for attempt in range(1, 6):
            if page.get_current_url() == 'https://todoist.com/':
                logger.info('User was logged out')
                return True
        logger.error('Fail to logout user')




