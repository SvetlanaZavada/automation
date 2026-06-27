from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")
    driver.find_element(By.CSS_SELECTOR, "[href='/forms/post']").click()
    print("URL:", driver.current_url)
    assert driver.current_url.endswith("/forms/post")
    driver.back()
    print("URL:", driver.current_url)
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
