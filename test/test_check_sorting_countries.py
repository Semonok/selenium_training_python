

def test_sorting_countries(driver):
    i = 0
    a=[]
    driver.find_element_by_link_text("Countries").click()
    raws = driver.find_elements_by_xpath("//tbody/tr/td[5]/a")
    while i < len(raws):
        i += 1
        a.append(driver.find_element_by_xpath("//tbody/tr[" + str(i) + "]/td[5]/a").text)
    assert a == sorted(a)