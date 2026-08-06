from selenium.webdriver.common.by import By


class AuthorizationShop:

    USER_NAME = By.ID, "user-name"
    PASSWORD = By.ID, "password"
    LOGIN = By.ID, "login-button"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def authorization(self):
        username = self.driver.find_element(*self.USER_NAME)
        username.send_keys("standard_user")
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("secret_sauce")
        login = self.driver.find_element(*self.LOGIN)
        login.click()
