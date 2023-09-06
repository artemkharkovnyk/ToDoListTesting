from framework.driver import Driver


def driver_setup() -> None:
    Driver('chrome', '/usr/bin/chromedriver')
