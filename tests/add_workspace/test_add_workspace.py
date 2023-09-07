from framework.util.useractions import add_workspace, get_workspaces


def test_add_workspace(workspace_name):
    add_workspace(workspace_name)
    assert workspace_name in get_workspaces()
