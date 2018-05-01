
def test_sorting_geo_zones(driver):
    z = 0
    r = 0
    raw = []
    driver.find_element_by_link_text("Geo Zones").click()
    zones = driver.find_elements_by_xpath("//tbody/tr/td[3]/a")
    while z < len(zones):
        z += 1
        driver.find_element_by_xpath("//tbody//tr[" + str(z) + "]//td[3]/a").click()
        raws = driver.find_elements_by_xpath("//tbody//tr//td[3]/a")
        while r < len(raws):
            r += 1
            raw.append(driver.find_element_by_xpath("//tbody//tr[" + str(r) + "]//td[3]/a").text)
        assert raw == sorted(raw)
        driver.find_element_by_link_text("Geo Zones").click()
