from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_delete_test_product(driver):
    driver.find_element_by_xpath("//li[2]/a").click()
    old_products = []
    new_products = []
    i = 0
    while i < len(driver.find_elements_by_xpath("//tr[@class]/td[3]/a")):
        i += 1
        test = driver.find_element_by_xpath("//tr[@class][" + str(i) + "]/td[3]/a")
        old_products.append(test.text)
        if test.text == "Test":
            driver.find_element_by_xpath(
                "//tr[@class][" + str(i) + "]/td[3]/a/../../td/input[@type='checkbox']").click()
            driver.find_element_by_name("delete").click()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to_alert().accept()
    o = 0
    while o < len(driver.find_elements_by_xpath("//tr[@class]/td[3]/a")):
        o += 1
        test = driver.find_element_by_xpath("//tr[@class][" + str(o) + "]/td[3]/a")
        new_products.append(test.text)
    assert old_products != new_products