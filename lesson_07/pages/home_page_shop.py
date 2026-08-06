from selenium.webdriver.common.by import By


class HomeShop:

    SAUSE_LABS_BACKPACK = By.ID, "add-to-cart-sauce-labs-backpack"
    SAUSE_LABS_BOLT_T_SHIRT = By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    SAUSE_LABS_ONESIE = By.ID, "add-to-cart-sauce-labs-onesie"
    CART = By.CLASS_NAME, "shopping_cart_link"

    def __init__(self, driver):
        self.driver = driver

    def adding_to_cart(self):
        sauce_labs_backpack = self.driver.find_element(
            *self.SAUSE_LABS_BACKPACK)
        sauce_labs_backpack.click()
        sauce_labs_bolt_t_shirt = self.driver.find_element(
            *self.SAUSE_LABS_BOLT_T_SHIRT)
        sauce_labs_bolt_t_shirt.click()
        sauce_labs_onesie = self.driver.find_element(
            *self.SAUSE_LABS_ONESIE)
        sauce_labs_onesie.click()

    def go_to_cart(self):
        cart = self.driver.find_element(*self.CART)
        cart.click()
