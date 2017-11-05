def test_basic(driver):
    WAIT_SEC = 20
    driver.implicitly_wait(WAIT_SEC)

    elem = driver.find_element_by_accessibility_id('testview')
    not_there = driver.find_element_by_accessibility_id('notthere')

    assert elem is not None
    assert not_there is None
