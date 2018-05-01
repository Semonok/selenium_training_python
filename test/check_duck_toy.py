def property(massive, value):
    massive.append(value.text)
    massive.append(value.value_of_css_property("color"))


def test_duck_toy(driver):
    properties_out = []
    properties_in = []
    driver.find_element_by_css_selector("i.fa.fa-chevron-circle-left").click()
    a = driver.find_element_by_css_selector("a.link")
    value_out_1 = a.find_element_by_css_selector("s.regular-price")
    value_out_2 = a.find_element_by_css_selector("strong.campaign-price")
    properties_out.append(a.find_element_by_css_selector("div.name").text)
    property(properties_out, value_out_1)
    property(properties_out, value_out_2)
    a.click()
    value_in_1 = driver.find_element_by_css_selector("del.regular-price")
    value_in_2 = driver.find_element_by_xpath("//del[@class='regular-price']/../strong[@class='campaign-price']")
    properties_in.append(driver.find_element_by_css_selector("h1.title").text)
    property(properties_in, value_in_1)
    property(properties_in, value_in_2)
    assert properties_out == properties_in
    print(properties_in,"\n", properties_out)