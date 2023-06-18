import os
import pytest
from dotenv import load_dotenv
from utils.helper import BaseSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from selene import browser

from utils import attach_ui

load_dotenv()

BOOKER_URL = os.getenv('booker_base_url')


@pytest.fixture(scope="session")
def booker(allure_attachments_flag=1):
    with BaseSession(base_url=BOOKER_URL) as session:
        yield session


DEFAULT_BROWSER_VERSION = "100.0"


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.hold_browser_open = True
    browser.config.window_width = '1024'
    browser.config.window_height = '768'
    browser.config.timeout = 3.0
    browser.config.base_url = "https://automationintesting.online"

    yield browser

    attach_ui.add_html(browser)
    attach_ui.add_screenshot(browser)
    attach_ui.add_logs(browser)
    attach_ui.add_video(browser)
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # browser = Browser(Config(driver))
    browser.config.driver = driver
    ui_base_url = os.getenv('UI_BASE_URL')
    browser.config.base_url = (ui_base_url)

    yield browser

    attach_ui.add_html(browser)
    attach_ui.add_screenshot(browser)
    attach_ui.add_logs(browser)
    attach_ui.add_video(browser)
    browser.quit()
