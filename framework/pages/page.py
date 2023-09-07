from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from typing import Optional, List
from framework.driver import Driver
from framework.logging import logger


class Page:
    def __init__(self, url=None):
        self.driver: WebDriver = Driver()
        self.url = url

    def get_current_url(self) -> str:
        return self.driver.current_url

    def open_with_url(self, attempts=3, timeout=3, expected_url=None) -> None:
        if self.url is None:
            raise Exception('Page url was not set.')
        if expected_url is None:
            expected_url = self.url
        wait = WebDriverWait(self.driver, timeout=5)
        wait.until(expected_conditions.presence_of_element_located(('tag name', 'body')))
        self.driver.get(self.url)
        logger.info(f'driver opening url "{self.url}"')
        for attempt in range(1, attempts + 1):
            current_url = self.get_current_url()
            logger.info(f'Current url is {current_url} expects {expected_url}. Attempt {attempt}')
            if current_url == expected_url:
                return
            sleep(timeout)
        raise Exception(f'Could not open {self.url}')

    def find_element(self, by_selector, identifier, attempts=3, timeout=2) -> Optional[WebElement]:
        for attempts in range(1, attempts + 1):
            try:
                logger.info(f"Trying to find element with {by_selector} '{identifier}'. Attempt: {attempts}")
                element = self.driver.find_element(by_selector, identifier)
                logger.info(f"element with {by_selector} '{identifier}' was found")
                return element
            except Exception as e:
                logger.info(f"Failed to found element with {by_selector} '{identifier}'. {e}")
            sleep(timeout)
        return None

    def find_elements(self, by_selector, identifier, attempts=3, timeout=2) -> List[WebElement]:
        for attempts in range(1, attempts + 1):
            try:
                logger.info(f"Trying to find elements with {by_selector} '{identifier}'. Attempt: {attempts}")
                elements = self.driver.find_elements(by_selector, identifier)
                logger.info(f"elements with {by_selector} '{identifier}' was found")
                if len(elements) != 0:
                    return elements
                raise Exception('')
            except Exception as e:
                logger.info(f"Failed to found elements with {by_selector} '{identifier}'. {e}")
            sleep(timeout)
        return []

    def find_element_by_css_selector(self, selector:str) -> Optional[WebElement]:
        return self.find_element(By.CSS_SELECTOR, selector)

    def find_elements_by_xpath(self, path: str) -> List[WebElement]:
        return self.find_elements(By.XPATH, path)

    def find_element_by_id(self, id_: str) -> Optional[WebElement]:
        return self.find_element(By.ID, id_)

    def find_element_by_xpath(self, xpath: str) -> Optional[WebElement]:
        return self.find_element(By.XPATH, xpath)





