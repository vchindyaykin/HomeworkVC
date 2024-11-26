from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from GostTeam.other.constants import VISIBILITY_ELEMENT_TIMEOUT_10_SEC
from GostTeam.elements.main_page_elements import MainPageElements

class GostTeamPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://gost.team/'
        self.orders_url = 'https://gost.team/orders'
        self.__driver = driver
        self.__elements = MainPageElements(driver=self.__driver)

    @property
    def elems(self):
        return self.__elements

    def _wait_to_load(self, element):
        WebDriverWait(driver=self.__driver, timeout=VISIBILITY_ELEMENT_TIMEOUT_10_SEC).until(
            EC.visibility_of_element_located(
                (By.XPATH, element),
            )
        )

    def open_orders(self):
        self.__driver.get(url=self.orders_url)
        self._wait_to_load(
            element='//*[@id="input_1496238230199"]'
        )