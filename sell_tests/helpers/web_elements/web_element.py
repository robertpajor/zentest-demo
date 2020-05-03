from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from sell_tests.configurations.driver_creator import DriverManager
from sell_tests.helpers.web_elements.element_finder import PresentElements, VisibilityElement


class AbstractElement:

    def __init__(self, locator: str, locator_type: By):
        """
        :param locator: locator used to for find the element, eg. id, name, xpath
        :param locator_type: method which is used to find element using 'By' class
        """
        self.locator = locator
        self.locator_type = locator_type
        self.driver = DriverManager.get_driver()

    def get(self) -> WebElement:
        """ Method to get web element """
        return VisibilityElement(self.locator, self.locator_type).create()

    def get_list(self) -> [WebElement]:
        """ Method to get list of web elements """
        return PresentElements(self.locator, self.locator_type).create()

    def click(self):
        """ Method to click in web element """
        self.get().click()

    def set_value(self, value: str):
        """
        Method to set value in field. First it clean field and then set new value
        :param value: New value
        """
        web_element = self.get()
        web_element.clear()
        web_element.send_keys(value)

    def get_value(self) -> str:
        """
        Method to get text from value of element
        :return: Text from element
        """
        return self.get().text

    def is_displayed(self) -> bool:
        """
        Method to check if element is displayed
        :return: True or False
        """
        try:
            return self.get().is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False


class ElementById(AbstractElement):
    """ Class for searching element using id """

    def __init__(self, element_id: str):
        """
        :param element_id: string locator used to for find the element
        """
        super(ElementById, self).__init__(element_id, By.ID)


class ElementByXpath(AbstractElement):
    """ Class for searching element using xpath """

    def __init__(self, xpath: str):
        """
        :param xpath: string locator used to for find the element
        """
        super(ElementByXpath, self).__init__(xpath, By.XPATH)


class ElementByName(AbstractElement):
    """ Class for searching element using name """

    def __init__(self, name: str):
        """
        :param name: string locator used to for find the element
        """
        super(ElementByName, self).__init__(name, By.NAME)


class ElementByClassName(AbstractElement):
    """ Class for searching element using name """

    def __init__(self, name: str):
        """
        :param name: string locator used to for find the element
        """
        super(ElementByClassName, self).__init__(name, By.CLASS_NAME)


class ElementByTagName(AbstractElement):
    """ Class for searching element using name """

    def __init__(self, name: str):
        """
        :param name: string locator used to for find the element
        """
        super(ElementByTagName, self).__init__(name, By.TAG_NAME)
