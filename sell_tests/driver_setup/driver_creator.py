import os
from selenium import webdriver


class DriverManager:
    relative_driver_path = "./chrome_driver/chromedriver"
    driver = None

    @staticmethod
    def create():
        DriverManager.driver = webdriver.Chrome(DriverManager.__get_driver_path())

    @staticmethod
    def quit():
        DriverManager.driver.quit()

    @staticmethod
    def get_driver():
        return DriverManager.driver

    @staticmethod
    def __get_driver_path():
        current_file_dir = os.path.dirname(__file__)
        driver_path = os.path.join(current_file_dir, DriverManager.relative_driver_path)
        return driver_path
