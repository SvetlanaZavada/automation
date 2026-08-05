from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
# Авторизуйтесь как пользователь standard_user
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button")
    login.click()
# Добавьте в корзину товары:
    sauce_labs_backpack = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack")
    sauce_labs_backpack.click()
    sauce_labs_bolt_t_shirt = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    sauce_labs_bolt_t_shirt.click()
    sauce_labs_onesie = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie")
    sauce_labs_onesie.click()
# Перейдите в корзину.
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
# Нажмите Checkout.
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()
# Заполните форму своими данными:
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Svetlana")
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Zavada")
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("610021")
# Нажмите кнопку Continue.
    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()
# Прочитайте со страницы итоговую стоимость (
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    # Проверьте, что итоговая сумма равна $58.29
    assert total == "Total: $58.29"
    driver.quit()
