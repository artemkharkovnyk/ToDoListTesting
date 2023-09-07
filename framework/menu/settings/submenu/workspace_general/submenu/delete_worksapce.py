from framework.menu.menu import Menu
from framework.pages.page import Page

class DeleteWorkspaceMenu(Menu):
    def __init__(self, button):
        super().__init__(button=button, autoopen=True, openwith='button')
    def delete(self):
        page = Page()
        sure_checkbox = page.find_element_by_css_selector('[type="checkbox"][aria-checked="false"][value="0"]')
        sure_checkbox.click()
        delete_btn = page.find_element_by_xpath('//*[@id=":ro:"]/div/form/div/div/div/div[3]/button')
        delete_btn.click()
