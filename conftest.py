import pytest
from selenium import webdriver


def choose_browsers(browser):
    if browser == "IE":
        wd = webdriver.Ie()
    elif browser == "Chrome":
        wd = webdriver.Chrome()#desired_capabilities={"chromeOptions":{"args":["--start-fullscreen"]}})
    elif browser == "Firefox":
        wd = webdriver.Firefox()
    return wd


@pytest.fixture(scope="session") #["IE", "Chrome", "Firefox"])
def driver(request):
    fixture = choose_browsers(browser="Chrome")
    fixture.implicitly_wait(2)
    request.addfinalizer(fixture.quit)
    return fixture

