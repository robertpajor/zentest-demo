from sell_tests.helpers.web_elements.web_element import ElementByXpath, ElementById, ElementByClassName
from sell_tests.page_objects.abstract_page import AbstractPage


class LeadsSettingsPage(AbstractPage):

    def __init__(self):
        super(LeadsSettingsPage, self).__init__()
        self.lead_statuses = ElementByXpath("//*[@data-toggle='lead-status']")
        self.edit_status_button_xpath = "//*[text()='{}']/../..//button[text()='Edit']"
        self.status_name_field_path = "//input[@value='{}']"
        self.save_status_button = ElementByXpath("//*[text()='Edit Lead Status']/../../.."
                                                 "//button[contains(@class, 'save')]")

    def click_lead_statuses(self):
        self.lead_statuses.click()

    def click_edit_lead_status(self, status_name: str):
        edit_lead_status_button = ElementByXpath(self.edit_status_button_xpath.format(status_name))
        edit_lead_status_button.click()

    def change_status_name(self, old_name: str, new_name: str):
        status_name_field = ElementByXpath(self.status_name_field_path.format(old_name))
        status_name_field.set_value(new_name)

    def click_save_status_button(self):
        self.save_status_button.click()
