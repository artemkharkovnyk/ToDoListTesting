from framework.pages import LoginPage


def login(email: str, password: str) -> bool:
    login_page = LoginPage()
    login_page.open_with_url()
    login_page.login(email, password)
    return login_page.login_check()
