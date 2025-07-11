from selene import browser
import pytest

@pytest.fixture(scope='session', autouse=True)
def option_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def opening_browser():
    browser.open('https://ya.ru/')
    yield
    browser.quit()