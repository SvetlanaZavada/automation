from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    elements = driver.find_elements(By.TAG_NAME, "a")
    links = len(elements)
    print(links)
    assert links == 9
    for link, elements in enumerate(elements, 1):
        print(f"ссылка {link} отображается на странице: "
              f"{elements.is_displayed()}")
    elements = driver.find_elements(By.TAG_NAME, "a")
    first_link = elements[0]
    link_text = first_link.text
    assert "1" in link_text

    driver.quit()
