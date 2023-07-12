import pytest
from selene import browser
import os

FILE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources'))


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1440
    browser.config.window_height = 776

    yield
    browser.quit()
