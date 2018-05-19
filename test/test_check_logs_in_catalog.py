import os

def test_check_logs(driver):
    driver.find_element_by_link_text("Catalog").click()
    driver.find_element_by_link_text("Rubber Ducks").click()
    i = 2
    while i <= len(driver.find_elements_by_xpath("//tr[@class]/td[3]/a")):
        i += 1
        driver.find_element_by_xpath("//tr[@class][" + str(i) + "]/td[3]/a").click()
        assert not driver.get_log('browser')
        driver.back()
    driver.save_screenshot('C:\\autotests\\'+ os.path.basename(__file__)+".png")