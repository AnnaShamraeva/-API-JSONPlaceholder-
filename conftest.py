import pytest
from selenium import webdriver

from url import UrlAndEndpoint


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Google()
    driver.get(UrlAndEndpoint.BASE_URL)
    yield driver
    driver.quit()





    


