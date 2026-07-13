from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()
    # 2. Найдите и нажмите на кнопку "Start"
    button_start = driver.find_element(By.CSS_SELECTOR, "#start button")
    button_start.click()

    # 3. Дождитесь появления текста "Hello World!"
    hello = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshot/fuul_screen.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello.text == "Hello World!", "Текст не найден"

    driver.quit()
