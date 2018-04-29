from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_local_admin(driver):
    o=1
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_css_selector("input[type='text']").send_keys("admin")
    driver.find_element_by_css_selector("input[type='password']").send_keys("admin")
    driver.find_element_by_css_selector("button.btn.btn-default").click()
    out_elements = len(driver.find_elements_by_css_selector("span.name"))
    while o <= out_elements:
        driver.find_element_by_xpath("(//span[@class='name'])[" + str(o) + "]").click()
        o += 1
        i = 1
        while i <= len(driver.find_elements_by_css_selector("ul.docs span.name")):
            element = driver.find_element_by_xpath("(//ul[@class='docs']//span[@class='name'])[" + str(i) + "]")
            #link = element.text
            element.click()
            #assert WebDriverWait(driver, 5).until(EC.title_contains(link))
            i += 1
        driver.find_element_by_css_selector("img[alt='My Store']").click()
