import pytest
from os import path
from appium import webdriver

from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'


@pytest.fixture
def driver():
    caps = {
        'platformName': 'iOS',
        'platformVersion': '13.6',
        'deviceName': 'iPhone 11',
        'automationName': 'XCUITest',
        'app': APP,
    }

    driver = webdriver.Remote(APPIUM, caps)
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView(driver)
