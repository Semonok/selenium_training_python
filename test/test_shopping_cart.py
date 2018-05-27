from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.by import By

def r_d(cash):
    return float(cash[1:])

def test_shopping_cart(driver):
    driver.find_element_by_css_selector("i.fa.fa-chevron-circle-left").click()
    driver.find_element_by_css_selector("ul.nav.nav-stacked.nav-pills a").click()
    for i in range(5):
        duck = random.choice(driver.find_elements_by_css_selector("a.link[data-toggle='lightbox']"))
        duck.click()
        driver.find_element_by_css_selector("div#view-full-page a").click()
        duck_size = driver.find_elements_by_css_selector("select.form-control")
        if len(duck_size) > 0:
            Select(duck_size[0]).select_by_value("Medium")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        assert driver.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i+1)))
    driver.find_element_by_css_selector("div#cart a").click()
    items = driver.find_elements_by_css_selector("button.btn.btn-danger")
    for i in range(len(items)):
        price = driver.find_element_by_xpath("//tr[@class='item']/td[5]").text
        subtotal_price_path = "//table[@class='table table-striped table-bordered data-table']/tbody/tr[1]/td[2]"
        subtotal_price = driver.find_element_by_xpath(subtotal_price_path).text
        driver.find_element_by_css_selector("button.btn.btn-danger").click()
        if i == len(items)-1:
            assert driver.find_element_by_css_selector("div.cart.wrapper em").text == "There are no items in your cart."
        else:
            assert driver.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, subtotal_price_path),"$" + str(r_d(subtotal_price) - r_d(price)) ))
