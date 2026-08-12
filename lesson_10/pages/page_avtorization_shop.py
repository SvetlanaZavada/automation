import allure
from selenium.webdriver.common.by import By


class AuthorizationShop:
    """
        Класс, представляющий страницу авторизации интернет-магазина.
        Содержит методы для открытия страницы и выполнения авторизации.
        """

    # Локаторы элементов страницы авторизации
    USER_NAME = By.ID, "user-name"
    PASSWORD = By.ID, "password"
    LOGIN = By.ID, "login-button"

    def __init__(self, driver):
        """
               Инициализация объекта AuthorizationShop.

               :param driver: WebDriver - экземпляр веб-драйвера Selenium
               """
        self.driver = driver

    @allure.step("Открытие страницы авторизации")
    def open_page(self) -> None:
        """
                Открывает страницу авторизации интернет-магазина
                и разворачивает окно браузера на весь экран.

                :return: None
                """
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    @allure.step("Выполнение авторизации с стандартными учетными данными")
    def authorization(self) -> None:
        """
                Выполняет авторизацию на сайте с использованием
                стандартных учетных данных:
                - Логин: standard_user
                - Пароль: secret_sauce

                :return: None
                """
        # Ввод имени пользователя
        username = self.driver.find_element(*self.USER_NAME)
        username.send_keys("standard_user")
        # Ввод пароля
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("secret_sauce")
        # Нажатие кнопки входа
        login = self.driver.find_element(*self.LOGIN)
        login.click()
