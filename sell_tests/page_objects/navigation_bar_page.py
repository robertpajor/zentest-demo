from sell_tests.helpers.web_elements.web_element import ElementById, ElementByXpath
from sell_tests.page_objects.abstract_page import AbstractPage


class NavigationBarPage(AbstractPage):

    def __init__(self):
        super(NavigationBarPage, self).__init__()
        self.leads = ElementById("nav-item-leads")
        self.add_menu = ElementById("global-add")
        self.lead_in_add_menu = ElementByXpath("//*[@data-role='menu-item' and contains(. , 'Lead')]")

    def click_leads_button(self):
        self.leads.click()

    def open_add_menu(self):
        self.add_menu.click()

    def click_lead_in_add_menu(self):
        self.open_add_menu()
        self.lead_in_add_menu.click()
