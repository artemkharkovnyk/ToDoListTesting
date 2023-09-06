from framework.pages import LoginPage, MainPage


def login(email: str, password: str) -> bool:
    login_page = LoginPage()
    login_page.open_with_url()
    login_page.login(email, password)
    return login_page.login_check()


def logout() -> bool:
    main_page = MainPage()
    main_page.open_with_url(expected_url='https://todoist.com/app/today')
    menu_page_menu = main_page.open_menu()
    return menu_page_menu.logout()

