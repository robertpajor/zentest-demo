from sell_tests.helpers.web_elements.web_element import ElementByXpath
from sell_tests.page_objects.abstract_page import AbstractPage


class DashboardPage(AbstractPage):

    def __init__(self):
        super(DashboardPage, self).__init__()
        self.dashboard_title = ElementByXpath("//*[contains(@class, '_1bR--DashboardPage--dashboardTitle')]")

    def is_dashboard_title_displayed(self):
        return self.dashboard_title.is_displayed()
