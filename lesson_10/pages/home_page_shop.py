import allure
from selenium.webdriver.common.by import By


class HomeShop:
    """
        Класс, представляющий главную страницу интернет-магазина.
        Содержит методы для добавления товаров в корзину и перехода в корзину.
        """

    # Локаторы элементов страницы
    SAUSE_LABS_BACKPACK = By.ID, "add-to-cart-sauce-labs-backpack"
    SAUSE_LABS_BOLT_T_SHIRT = By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    SAUSE_LABS_ONESIE = By.ID, "add-to-cart-sauce-labs-onesie"
    CART = By.CLASS_NAME, "shopping_cart_link"

    def __init__(self, driver):
        """
                Инициализация объекта HomeShop.

                :param driver: WebDriver - экземпляр веб-драйвера Selenium
                """
        self.driver = driver

    @allure.step("Добавление товаров в корзину")
    def adding_to_cart(self) -> None:
        """
                Добавляет три выбранных товара в корзину:
                - Sauce Labs Backpack
                - Sauce Labs Bolt T-Shirt
                - Sauce Labs Onesie

                :return: None
                """
        # Добавление рюкзака Sauce Labs
        sauce_labs_backpack = self.driver.find_element(
            *self.SAUSE_LABS_BACKPACK)
        sauce_labs_backpack.click()
        # Добавление футболки Sauce Labs Bolt T-Shirt
        sauce_labs_bolt_t_shirt = self.driver.find_element(
            *self.SAUSE_LABS_BOLT_T_SHIRT)
        sauce_labs_bolt_t_shirt.click()
        # Добавление комбинезона Sauce Labs Onesie
        sauce_labs_onesie = self.driver.find_element(
            *self.SAUSE_LABS_ONESIE)
        sauce_labs_onesie.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
                Выполняет переход на страницу корзины
                путём клика по иконке корзины.

                :return: None
                """
        cart = self.driver.find_element(*self.CART)
        cart.click()
