from time import sleep
from .page import Page
from framework.logging import logger


class LoginPage(Page):
    def __init__(self):
        super().__init__('https://todoist.com/auth/login')

    def login(self, email: str, password: str) -> None:
        email_field = self.find_element_by_css_selector('[placeholder = "Enter your email..."]')
        password_field = self.find_element_by_css_selector('[placeholder="Enter your password..."]')
        submit_btn = self.find_element_by_css_selector('[data-gtm-id="start-email-login"]')
        logger.info('Attempt to login')
        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_btn.click()

    def login_check(self, attempts=3, timeout=2) -> bool:
        for attempt in range(1, attempts + 1):
            if self.get_current_url() == 'https://todoist.com/app/today':
                logger.info('User was logged in')
                return True
            sleep(timeout)
        logger.info('User was not logged in')
        return False
