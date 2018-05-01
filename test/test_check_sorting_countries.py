
def test_sorting_countries(driver):
    i = 0
    a = []
    driver.find_element_by_link_text("Countries").click()
    raws = driver.find_elements_by_xpath("//tbody/tr")
    while i < len(raws):
        i += 1
        link = driver.find_element_by_xpath("//tbody/tr[" + str(i) + "]/td[5]/a")
        a.append(link.text)
        if driver.find_element_by_xpath("//tbody/tr[" + str(i) + "]/td [@class='text-center']").text != str(0):
            link.click()
            o = 0
            b = []
            while o < len(driver.find_elements_by_xpath("//tbody//tr//td[3]/input")):
                o+=1
                b.append(driver.find_element_by_xpath("//tbody//tr[" + str(o) + "]//td[3]/input").get_attribute("value"))
            assert b == sorted(b)
            driver.find_element_by_link_text("Countries").click()
    assert a == sorted(a)