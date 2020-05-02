from sell_tests.helpers.web_elements.web_element import ElementById, ElementByName
from sell_tests.page_objects.abstract_page import AbstractPage


class LoginPage(AbstractPage):

    def __init__(self):
        super(LoginPage, self).__init__()
        self.url = "https://zentest-demo.zendesk.com"
        self.email_field = ElementById("user_email")
        self.password_field = ElementById("user_password")
        self.sign_in_button = ElementByName("commit")

    def open(self):
        self.go_to(self.url)
        self.switch_to_iframe()

    def set_email(self, email: str):
        self.email_field.set_value(email)

    def set_password(self, password: str):
        self.password_field.set_value(password)

    def click_sign_in_button(self):
        self.sign_in_button.click()
        self.switch_to_default_content()
