
def test_store(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_css_selector("input[type='text']").send_keys("admin")
    driver.find_element_by_css_selector("input[type='password']").send_keys("admin")
    driver.find_element_by_css_selector("button.btn.btn-default").click()
    driver.find_element_by_css_selector("i.fa.fa-chevron-circle-left").click()
    driver.find_element_by_css_selector("aside#sidebar a[href='http://localhost/litecart/en/rubber-ducks-c-1/']").click()
    ducks = driver.find_elements_by_css_selector("div.product.column.hover-light")
    for duck in ducks:
        assert len(duck.find_elements_by_css_selector("div.sticker.sale")
                   or duck.find_elements_by_css_selector("div.sticker.new")) == 1
        print("Уточка проверена")
