from selenium import webdriver
from pages.page_avtorization_shop import AuthorizationShop
from pages.home_page_shop import HomeShop
from pages.page_cart import Cart
import allure


@allure.epic("Интернет-магазин Sauce Demo")
@allure.feature("Полный цикл покупки")
@allure.story("Оформление заказа")
@allure.description("""
            Тест проверяет полный цикл оформления заказа:
            1. Авторизация на сайте
            2. Добавление трёх товаров в корзину
            3. Переход в корзину
            4. Оформление заказа
            5. Заполнение формы
            6. Проверка итоговой стоимости
            Ожидаемый результат: Итоговая сумма должна быть $58.29
        """)
@allure.title("Проверка полного цикла покупки трёх товаров")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop():
    # Инициализация веб-драйвера
    with allure.step("Настройка веб-драйвера Firefox"):
        #  options = Options()
        #  options.add_argument("--headless")  # Для headless режима
        driver = webdriver.Firefox()
    # Создание объектов страниц
    with allure.step("Инициализация страниц"):
        authorization = AuthorizationShop(driver)
        home = HomeShop(driver)
        cart = Cart(driver)
    # 1. Авторизация
    with allure.step("Открытие страницы авторизации"):
        authorization.open_page()
    with allure.step("Выполнение авторизации с учетными данными"
                     " standard_user/secret_sauce"):
        authorization.authorization()
    # 2. Добавление товаров в корзину
    with allure.step("Добавление трёх товаров в корзину"):
        home.adding_to_cart()
    # 3. Переход в корзину
    with allure.step("Переход в корзину"):
        home.go_to_cart()
    # 4. Оформление заказа
    with allure.step("Нажатие кнопки 'Checkout' для оформления заказа"):
        cart.checkout()
    # 5. Заполнение формы
    with allure.step("Заполнение формы с личными данными"):
        cart.form()
    # 6. Получение итоговой суммы
    with allure.step("Получение итоговой стоимости заказа"):
        cart.total()
    # 7. Проверка итоговой суммы
    with allure.step("Проверка итоговой стоимости заказа"):
        assert cart.total() == "Total: $58.29"
    driver.quit()
