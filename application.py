from selenium import webdriver

class Application:

    def login(self, driver):
        driver.find_element_by_css_selector("input[type='text']").send_keys("admin")
        driver.find_element_by_css_selector("input[type='password']").send_keys("admin")
        driver.find_element_by_css_selector("button.btn.btn-default").click()