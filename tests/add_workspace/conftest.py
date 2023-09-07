from pytest import fixture
from framework.util.useractions import delete_workspace


@fixture()
def workspace_name():
    return 'test workspace'


@fixture(scope='function', autouse=True)
def teardown(workspace_name):
    yield
    delete_workspace(workspace_name)