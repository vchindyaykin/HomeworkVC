from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPageElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def header(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='',
        )

    @property
    def email_input(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="input_1496238230199"]'
        )