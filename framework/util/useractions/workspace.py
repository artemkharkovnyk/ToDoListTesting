from framework.pages import MainPage


def delete_workspace(workspace_name: str) -> None:
    main_page = MainPage()
    main_page.open_with_url(expected_url='https://todoist.com/app/today')
    main_page_menu = main_page.open_menu()
    settings_menu = main_page_menu.open_settings_menu()
    workspace_general_menu = settings_menu.open_workspace_general_submenu(workspace_name)
    workspace_general_menu.delete()
