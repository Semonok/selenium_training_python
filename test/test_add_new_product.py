from selenium.webdriver.support.ui import Select

def test_add_new_product(driver):
    driver.find_element_by_xpath("//li[2]/a").click()
    driver.find_element_by_xpath("//li[3]/a[@class='btn btn-default']").click()
    driver.find_element_by_css_selector("label.btn.btn-default").click()
    driver.find_element_by_name("name[en]").send_keys("Test")
    driver.find_element_by_name("code").send_keys("1")
    Select(driver.find_element_by_name("manufacturer_id")).select_by_value("1")
    driver.find_element_by_name("product_groups[]")
    driver.find_element_by_name("date_valid_from").send_keys(10122010)
    driver.find_element_by_name("date_valid_to").send_keys(10122010)
    driver.find_element_by_link_text("Information").click()
    driver.find_element_by_name("short_description[en]").send_keys("Test item")
    driver.find_element_by_link_text("Prices").click()
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_value("EUR")
    driver.find_element_by_name("purchase_price").send_keys("10")
    driver.find_element_by_name("save").click()
    i=0
    test_products = 0
    while i < len(driver.find_elements_by_xpath("//tr[@class]/td[3]/a")):
        i+=1
        if driver.find_element_by_xpath("//tr[@class][" + str(i) + "]/td[3]/a").text == "Test":
            test_products +=1
    assert test_products == 1
