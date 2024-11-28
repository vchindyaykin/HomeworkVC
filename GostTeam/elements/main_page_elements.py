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
    @property
    def name_input(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="input_1496238250184"]'
        )
    @property
    def telegram_input(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="input_1688999403010"]'
        )
    @property
    def comment_input(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="input_1496238259342"]'
        )
    @property
    def sent_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="form710819711"]/div[2]/div[7]/button'
        )