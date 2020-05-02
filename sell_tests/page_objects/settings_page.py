from sell_tests.helpers.web_elements.web_element import ElementByClassName
from sell_tests.page_objects.abstract_page import AbstractPage


class SettingsPage(AbstractPage):

    def __init__(self):
        super(SettingsPage, self).__init__()
        self.leads = ElementByClassName("leads")

    def click_leads(self):
        self.leads.click()
