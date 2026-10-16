import pytest
from selenium import webdriver
@pytest.fixture
def navegador():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()