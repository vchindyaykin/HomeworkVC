import pytest
from selenium import webdriver

from GostTeam.page.gostteam_page import GostTeamPage

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def gost_team_page(browser: webdriver) -> GostTeamPage:
    return GostTeamPage(driver=browser)