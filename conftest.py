import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store', default=None,
    )

@pytest.fixture()
def browser(request):
    language = request.config.getoption('language')
    language = None
    if language == 'en-gb':
        browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...'
    )
    browser.quit()
