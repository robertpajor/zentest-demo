from behave.fixture import fixture_call_params, fixture

from sell_tests.configurations.account_configuration import EMAIL, PASSWORD
from sell_tests.helpers.web_elements.wait import wait_until
from sell_tests.page_objects.dashboard_page import DashboardPage
from sell_tests.page_objects.login_page import LoginPage


@fixture
def login(context):
    login_page = LoginPage()
    login_page.open()
    login_page.set_email(EMAIL)
    login_page.set_password(PASSWORD)
    login_page.click_sign_in_button()
    __wait_until_dashboard_is_loaded()


def __wait_until_dashboard_is_loaded():
    dashboard_page = DashboardPage()
    wait_until(dashboard_page.is_dashboard_title_displayed)


FIXTURES = {
    "fixture.login": fixture_call_params(login)
}
