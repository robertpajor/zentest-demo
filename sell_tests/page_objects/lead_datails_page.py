from sell_tests.helpers.web_elements.web_element import ElementByClassName
from sell_tests.page_objects.abstract_page import AbstractPage


class LeadDetailsPage(AbstractPage):

    def __init__(self):
        super(LeadDetailsPage, self).__init__()
        self.current_status = ElementByClassName("lead-status")

    def get_current_status(self) -> str:
        return self.current_status.get_value()
