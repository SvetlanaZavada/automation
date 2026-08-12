import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Cart:
    """
        Класс, представляющий страницу корзины
        и оформления заказа.
        Содержит методы для перехода к оформлению,
        заполнения формы и получения итоговой суммы.
        """
    # Локаторы элементов страницы
    CHECKOUT = By.ID, "checkout"
    FIRST_NAME = By.ID, "first-name"
    LAST_NAME = By.ID, "last-name"
    POSTAL_CODE = By.ID, "postal-code"
    BUTTON_CONTINUE = By.ID, "continue"
    TOTAL = By.CLASS_NAME, "summary_total_label"

    def __init__(self, driver):
        """
                Инициализация объекта CartPage.

                :param driver: WebDriver - экземпляр веб-драйвера Selenium
                """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажатие кнопки 'Checkout' для перехода к оформлению заказа")
    def checkout(self) -> None:
        """
                Выполняет переход на страницу оформления заказа
                путём клика по кнопке 'Checkout'.

                :return: None
                """
        checkout = self.driver.find_element(*self.CHECKOUT)
        checkout.click()

    @allure.step("Заполнение формы оформления заказа")
    def form(self) -> None:
        """
                Заполняет форму оформления заказа тестовыми данными:
                - Имя: Svetlana
                - Фамилия: Zavada
                - Почтовый индекс: 610021

                После заполнения формы нажимает кнопку 'Continue'.

                :return: None
                """
        # Заполнение поля "Имя"
        first_name = self.driver.find_element(*self.FIRST_NAME)
        first_name.send_keys("Svetlana")
        # Заполнение поля "Фамилия"
        last_name = self.driver.find_element(*self.LAST_NAME)
        last_name.send_keys("Zavada")
        # Заполнение поля "Почтовый индекс"
        postal_code = self.driver.find_element(*self.POSTAL_CODE)
        postal_code.send_keys("610021")
        # Нажатие кнопки "Continue"
        button_continue = self.driver.find_element(*self.BUTTON_CONTINUE)
        button_continue.click()

    @allure.step("Получение итоговой стоимости заказа")
    def total(self) -> str:
        """
                Извлекает и возвращает итоговую
                стоимость заказа
                с страницы подтверждения.

                :return: str - строка с общей стоимостью
                (например, "Total: $29.99")
                """
        total = self.driver.find_element(*self.TOTAL).text.strip()
        return total
