import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

fixture = None

@pytest.fixture(scope="session") #["IE", "Chrome", "Firefox"])
def driver(request):
    global fixture
    fixture = choose_browsers(browser="Chrome")
    #fixture = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8080"}})
    fixture.wait = WebDriverWait(fixture, 5)
    login_admin(fixture)
    fixture.implicitly_wait(2)
    request.addfinalizer(fixture.quit)
    return fixture


def choose_browsers(browser):
    global wd
    if browser == "IE":
        wd = webdriver.Ie()
    elif browser == "Chrome":
        wd = webdriver.Chrome()#desired_capabilities={"chromeOptions":{"args":["--start-fullscreen"]}})
    elif browser == "Firefox":
        wd = webdriver.Firefox()
    return wd


def login_admin(self):
    self.get("http://localhost/litecart/admin")
    self.find_element_by_css_selector("input[type='text']").send_keys("admin")
    self.find_element_by_css_selector("input[type='password']").send_keys("admin")
    self.find_element_by_css_selector("button.btn.btn-default").click()


def logout(self):
    self.find_element_by_css_selector("i.fa.fa-sign-out.fa-lg").click()

