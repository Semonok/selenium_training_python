from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test.test_shopping_cart import r_d

class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")

    @property
    def remove_item(self):
        return self.driver.find_element_by_css_selector("button.btn.btn-danger")

    @property
    def item_list(self):
        return self.driver.find_elements_by_css_selector("tr.item")

    @property
    def item_price(self):
        return self.driver.find_element_by_xpath("//tr[@class='item']/td[5]")

    @property
    def subtotal_price_of_all_items(self):
        return self.driver.find_element_by_xpath("//table[@class='table table-striped table-bordered data-table']/tbody/tr[1]/td[2]")

    @property
    def text_when_list_is_empty(self):
        return self.driver.find_element_by_css_selector("div.cart.wrapper em").text

    def change_subtotal_price(self, subtotal_price, price):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//table[@class='table table-striped table-bordered data-table']/tbody/tr[1]/td[2]"),"$" + str(r_d(subtotal_price) - r_d(price)) ))