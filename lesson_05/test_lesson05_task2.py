from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.find_element(By.NAME, "custname").send_keys("Svetlana")
    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()
    print("URL:", driver.current_url)
    assert driver.current_url == "https://httpbin.org"

    driver.quit()
