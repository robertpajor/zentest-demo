import os
from selenium import webdriver


class DriverCreator:
    relative_driver_path = "./chrome_driver/chromedriver"
    driver = None

    @staticmethod
    def create():
        DriverCreator.driver = webdriver.Chrome(DriverCreator.__get_driver_path())

    @staticmethod
    def quit():
        DriverCreator.driver.quit()

    @staticmethod
    def get_driver():
        return DriverCreator.driver

    @staticmethod
    def __get_driver_path():
        current_file_dir = os.path.dirname(__file__)
        driver_path = os.path.join(current_file_dir, DriverCreator.relative_driver_path)
        return driver_path
