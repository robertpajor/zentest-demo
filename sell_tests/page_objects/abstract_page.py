from sell_tests.driver_setup.driver_creator import DriverManager
from sell_tests.helpers.web_elements.web_element import ElementByTagName


class AbstractPage:
    driver = None

    def __init__(self):
        self.driver = DriverManager.get_driver()
        self.iframe = ElementByTagName("iframe")

    def go_to(self, url: str):
        """ Loads a web page in the current browser session. """
        self.driver.get(url)

    def go_back(self):
        """ Goes one step backward in the browser history. """
        self.driver.back()

    def go_forward(self):
        """ Goes one step forward in the browser history. """
        self.driver.forward()

    def get_title(self) -> str:
        """
        Returns the title of the current page.
        :return: Page title
        """
        return self.driver.title

    def switch_to_iframe(self):
        """ Switches focus to the specified frame. """
        self.driver.switch_to.frame(self.iframe.get())

    def switch_to_default_content(self):
        """ Switch focus to the default frame. """
        self.driver.switch_to.default_content()
