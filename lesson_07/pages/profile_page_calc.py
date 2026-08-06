from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePageCalc:

    DELAY = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver

    def open_calc(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, second):
        delay = self.driver.find_element(*self.DELAY)
        delay.clear()
        delay.send_keys(second)

    def clic_number(self, number):
        number = self.driver.find_element(
            By.XPATH, f"//span[text()='{number}']")
        number.click()

    def clic_operator(self, operator):
        operator = self.driver.find_element(
            By.XPATH, f"//span[text()='{operator}']")
        operator.click()

    def result(self):
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected_result, timeout=46):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result))
