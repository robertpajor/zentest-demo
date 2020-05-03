from behave.fixture import fixture_call_params, fixture

from sell_tests.configurations.configuration import EMAIL, PASSWORD
from sell_tests.page_objects.login_page import LoginPage


@fixture
def login(context):
    login_page = LoginPage()
    login_page.open()
    login_page.set_email(EMAIL)
    login_page.set_password(PASSWORD)
    login_page.click_sign_in_button()


FIXTURES = {
    "fixture.login": fixture_call_params(login)
}
