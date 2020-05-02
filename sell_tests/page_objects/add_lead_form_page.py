from sell_tests.helpers.web_elements.web_element import ElementByXpath, ElementByClassName
from sell_tests.page_objects.abstract_page import AbstractPage


class AddLeadFormPage(AbstractPage):

    def __init__(self):
        super(AddLeadFormPage, self).__init__()
        self.first_name = ElementByXpath("//*[@data-action='lead-first-name-input']//input")
        self.last_name = ElementByXpath("//*[@data-action='lead-last-name-input']//input")
        self.company_name = ElementByXpath("//*[@data-action='lead-company-name-dropdown']//input")
        self.save_and_visit_button = ElementByXpath("//button[@data-action='save-and-visit']")

    def set_first_name(self, first_name: str):
        self.first_name.set_value(first_name)

    def set_last_name(self, last_name: str):
        self.last_name.set_value(last_name)

    def set_company_name(self, company_name: str):
        self.company_name.set_value(company_name)

    def click_save_and_visit_button(self):
        self.save_and_visit_button.click()
