from framework.pages.page import Page
from framework.menu.menu import Menu
from .submenu.delete_worksapce import DeleteWorkspaceMenu

class WorkspaceGeneralMenu(Menu):
    def delete(self):
        page = Page()
        delete_btn = page.find_element('css selector', '[aria-describedby="delete-workspace-info"]')
        delete_menu = DeleteWorkspaceMenu(delete_btn)
        delete_menu.delete()



