from sell_tests.helpers.web_elements.web_element import ElementByXpath
from sell_tests.page_objects.abstract_page import AbstractPage


class LeadsPage(AbstractPage):

    def __init__(self):
        super(LeadsPage, self).__init__()
        self.lead_xpath = "//*[@class='NUZ--IndexItemRow--IndexItemRow' and contains(.,'{}')]"
        self.filters_button = ElementByXpath("//button[contains(.,'Filters')]")
        self.clear_all_filters_button = ElementByXpath("//button[contains(@class,'FiltersLayoutHeader--clearButton')]")

    def select_lead_by_name(self, lead_name: str):
        ElementByXpath(self.lead_xpath.format(lead_name)).click()

    def click_clear_all_filters_button(self):
        self.clear_all_filters_button.click()

    def click_filters_button(self):
        self.filters_button.click()

    def is_clear_all_filters_button_displayed(self) -> bool:
        return self.clear_all_filters_button.is_displayed()

    def is_lead_on_list(self, lead_name: str):
        lead = ElementByXpath(self.lead_xpath.format(lead_name))
        return lead.is_displayed()
