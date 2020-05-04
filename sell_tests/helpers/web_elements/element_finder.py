from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from sell_tests.configurations.driver_manager import DriverManager


class ElementFinder:
    """ The base class for finding web elements """

    def __init__(self, condition):
        self.driver = DriverManager.get_driver()
        self.timeout = 15
        self.web_driver_wait = WebDriverWait(self.driver, self.timeout)
        self.condition = condition

    def create(self) -> WebElement or List[WebElement]:
        """
        Method creates web element using proper condition
        :return: Web Element or List[WebElement]
        """
        return self.web_driver_wait.until(self.condition)


class VisibilityElement(ElementFinder):
    """
    Class using expectation for checking that an element is present on the DOM of a page and visible.
    Visibility means that the element is not only displayed but also has a height and width that is greater than 0.
    """

    def __init__(self, locator, locator_type):
        """
        :param locator: locator id
        :param locator_type: locator type method to search
        """
        super(VisibilityElement, self).__init__(ec.visibility_of_element_located((locator_type, locator)))


class PresentElements(ElementFinder):
    """
    Class using expectation for checking that there is at least one element present on a web page.
    """

    def __init__(self, locator, locator_type):
        """
        :param locator: Locator value
        :param locator_type: locator type method to search
        """
        super(PresentElements, self).__init__(ec.presence_of_all_elements_located((locator_type, locator)))
