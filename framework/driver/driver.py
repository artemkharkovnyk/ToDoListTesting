from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome
from framework.logging import logger


class Driver(WebDriver):
    __driver = None

    def __new__(cls, driver, *args, **kwargs):
        cls.__driver = {
            'chrome': Chrome
        }.get(driver)(*args, **kwargs)
        def new(cls):
            return cls.__driver
        cls.__new__ = new
        logger.info('Driver class stored selenium driver object')
