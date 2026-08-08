from selenium import webdriver
from pages.profile_page_calc import ProfilePageCalc


def test_calculator():
    driver = webdriver.Chrome()
    calculator = ProfilePageCalc(driver)
    calculator.open_calc()
    calculator.set_delay("45")
    calculator.clic_number(7)
    calculator.clic_operator("+")
    calculator.clic_number(8)
    calculator.clic_operator("=")
    calculator.wait_for_result("15")

    result = calculator.result()
    assert result == "15", f"Ожидалось 15, получено {result}"

    driver.quit()
