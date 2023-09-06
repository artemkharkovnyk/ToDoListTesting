from pytest import fixture
from framework.util.setup import driver_setup
from framework.util.useractions import login, logout
from framework.logging import logger

from secrets import PASSWORD, EMAIL


@fixture(scope='session', autouse=True)
def setup():
    logger.info('Suite setup was started')
    driver_setup()
    assert login(EMAIL, PASSWORD)
    logger.info('Suite setup was ended')


@fixture(scope='session', autouse=True)
def teardown():
    logger.info('Suite teardown was started')
    assert logout()
    logger.info('Suite teardown was ended')
