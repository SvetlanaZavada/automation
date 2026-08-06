from selenium.webdriver.common.by import By


class Cart:
    CHECKOUT = By.ID, "checkout"
    FIRST_NAME = By.ID, "first-name"
    LAST_NAME = By.ID, "last-name"
    POSTAL_CODE = By.ID, "postal-code"
    BUTTON_CONTINUE = By.ID, "continue"
    TOTAL = By.CLASS_NAME, "summary_total_label"

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        checkout = self.driver.find_element(*self.CHECKOUT)
        checkout.click()

    def form(self):
        first_name = self.driver.find_element(*self.FIRST_NAME)
        first_name.send_keys("Svetlana")
        last_name = self.driver.find_element(*self.LAST_NAME)
        last_name.send_keys("Zavada")
        postal_code = self.driver.find_element(*self.POSTAL_CODE)
        postal_code.send_keys("610021")
        button_continue = self.driver.find_element(*self.BUTTON_CONTINUE)
        button_continue.click()

    def total(self):
        total = self.driver.find_element(*self.TOTAL).text.strip()
        return total
