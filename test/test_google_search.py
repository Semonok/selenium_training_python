from selenium.webdriver.common.keys import Keys

def test_google_search(driver):
    driver.get("https://www.google.ru/")
    driver.find_element_by_name("q").click()
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys("Найди что-нибудь",Keys.ENTER)