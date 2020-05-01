from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from sell_tests.driver_setup.driver_creator import DriverCreator


class ElementFinder:
    """Class using various expectation to find web element"""

    def __init__(self, condition):
        self.driver = DriverCreator.get_driver()
        self.timeout = 15
        self.web_driver_wait = WebDriverWait(self.driver, self.timeout)
        self.condition = condition

    def create(self) -> WebElement or List[WebElement]:
        """
        Method to create web element using proper condition
        :return: Web Element or List[WebElement]
        """
        return self.web_driver_wait.until(self.condition)


class PresentElement(ElementFinder):
    """
    Class using expectation for checking that an element is present on the DOM
    of a page. This does not necessarily mean that the element is visible.
    """

    def __init__(self, locator, locator_type):
        """
        :param locator: Locator value
        :param locator_type: locator type method to search
        """
        super(PresentElement, self).__init__(ec.presence_of_element_located((locator_type, locator)))


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
