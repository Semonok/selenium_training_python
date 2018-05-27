from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StoreMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    @property
    def open_ducks_list(self):
        return self.driver.find_element_by_css_selector("ul.nav.nav-stacked.nav-pills a")

    @property
    def duck_list(self):
        return self.driver.find_elements_by_css_selector("a.link[data-toggle='lightbox']")

    @property
    def open_duck_item(self):
        return self.driver.find_element_by_css_selector("div#view-full-page a")

    def select_size(self, size):
        Select(self.driver.find_element_by_css_selector("select.form-control")).select_by_value("%s" % size)

    @property
    def add_duck_in_shopping_cart(self):
        return self.driver.find_element_by_css_selector("button.btn.btn-success")

    def wait_add_item_in_cart(self, amount=0):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(int("%i" % amount) + 1)))

    @property
    def quantity_item_in_cart(self):
        return int(self.driver.find_element_by_css_selector("span.quantity").text)
