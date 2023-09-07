from selenium.webdriver.remote.webelement import WebElement
from framework.menu.menu import Menu
from framework.pages.page import Page
from .submenu import *


class SettingsMenu(Menu):
    def __init__(self, button: WebElement = None, url: str = None):
        if button:
            openwith = 'button'
        elif url:
            openwith='url'
        super().__init__(button=button, url=url, autoopen=True, openwith=openwith)
        submenu_names = [
            'account', 'general', 'advanced', 'subscription',
            'theme', 'sidebar', 'quick-customization', 'productivity',
            'reminders', 'notifications', 'backups', 'installed'
        ]
        page = Page(None)
        buttons = list(map(
            lambda menu_name: page.find_element_by_css_selector(f'[href="/app/settings/{menu_name}"]'),
            submenu_names))
        self.submenu_buttons = dict(zip(submenu_names, buttons))
        workspace_divs = page.find_elements_by_xpath("//div[a[contains(@href, '/app/settings/workspaces')]]")
        for div in workspace_divs:
            general, memebers, billing = div.find_elements('tag name', 'a')
            workspace_name = div.find_element('tag name', 'div').text
            self.submenu_buttons[f'workspace_general {workspace_name}'] = general
            self.submenu_buttons[f'workspace_memebers {workspace_name}'] = memebers
            self.submenu_buttons[f'workspace_billing {workspace_name}'] = billing

    def open_general_submenu(self) -> GeneralMenu:
        return GeneralMenu(button=self.submenu_buttons['general'], autoopen=True, openwith='button')

    def open_account_submenu(self) -> AccountMenu:
        return AccountMenu(button=self.submenu_buttons['account'], autoopen=True, openwith='button')

    def open_workspace_general_submenu(self, workspace_name) -> WorkspaceGeneralMenu:
        return WorkspaceGeneralMenu(button=self.submenu_buttons[f'workspace_general {workspace_name}'],
                                    autoopen=True, openwith='button')




