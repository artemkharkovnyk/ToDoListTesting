from typing import List
from .page import Page
from framework.menu import MainPageMenu, AddWorkspaceMenu


class MainPage(Page):
    def __init__(self):
        super().__init__('https://todoist.com/')

    def open_menu(self) -> MainPageMenu:
        settings_btn = self.find_element_by_css_selector('[aria-label="Settings"]')
        menu = MainPageMenu(button=settings_btn)
        return menu

    def open_add_workspace_menu(self):
        buttons = self.find_elements_by_tag('button')
        open_menu_button = None
        for btn in buttons:
            if btn.text == 'Add team workspace':
                open_menu_button = btn
                break
        if open_menu_button is None:
            raise Exception('Could not find "Add team workspace" button')
        return AddWorkspaceMenu(open_menu_button)

    def get_workspaces(self) -> List[str]:
        workspace_names = []
        workspaces_container = self.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div")
        for workspace_container in workspaces_container.find_elements('xpath', '*'):
            workspace_name = workspace_container.find_element('tag name', 'a').text
            workspace_names.append(workspace_name)
        return workspace_names
