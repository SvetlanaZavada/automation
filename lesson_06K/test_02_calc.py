from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")
    seven = driver.find_element(By.XPATH, "//span[text()='7']")
    seven.click()
    plus = driver.find_element(By.XPATH, "//span[text()='+']")
    plus.click()
    eight = driver.find_element(By.XPATH, "//span[text()='8']")
    eight.click()
    equals = driver.find_element(By.XPATH, "//span[text()='=']")
    equals.click()
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15", f"Ожидалось 15, получено {result}"

    driver.quit()
