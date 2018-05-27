import random

def test_check_links(driver):
    driver.find_element_by_link_text("Countries").click()
    i = random.choice(driver.find_elements_by_xpath("//tbody/tr"))
    country_name = i.find_element_by_xpath("//td[5]").text
    i.find_element_by_xpath("//td[7]/a").click()
    assert country_name == driver.find_element_by_name("name").get_attribute("value")
    for link in driver.find_elements_by_css_selector("form[name=country_form] a[target=_blank]"):
        main_page = driver.current_window_handle
        link.click()
        driver.switch_to_window(driver.window_handles[1])
        status = driver.execute_script("return document.readyState")
        driver.wait.until(lambda s: status == "complete")
        link_page = driver.current_window_handle
        assert main_page != link_page
        driver.close()
        driver.switch_to_window(driver.window_handles[0])