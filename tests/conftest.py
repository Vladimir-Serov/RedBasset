import pytest
from selene import browser
from pages.authentication_page import AuthPage
from pages.main_site_page import MainPage
from selenium import webdriver

main_page = MainPage()
auth_page = AuthPage()


@pytest.fixture(scope='function', autouse=True)
def remote_browser():
    capabilities = {
        "browserName": 'chrome',
        "browserVersion": '114.0',
        'enableVNC': True,
        'enableVideo': False,
        'screenResolution': '1920x1080x24',
        'sessionTimeout': '8m'
    }
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://selenoid.mish.design:4444/wd/hub', options=options)

    browser.config.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()
