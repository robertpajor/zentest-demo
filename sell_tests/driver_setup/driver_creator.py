import os
from selenium import webdriver


class DriverCreator:
    relative_driver_path = "./chrome_driver/chromedriver"
    driver = None

    def __init__(self):
        print("webdriver init")
        self.create()

    def create(self):
        self.driver = webdriver.Chrome(self.__get_driver_path())

    def quit(self):
        self.driver.quit()

    def __get_driver_path(self):
        current_file_dir = os.path.dirname(__file__)
        driver_path = os.path.join(current_file_dir, self.relative_driver_path)
        return driver_path
