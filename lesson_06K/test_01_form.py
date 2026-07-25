from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_validation():
    driver = webdriver.ChromiumEdge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")
    phone_number = driver.find_element(By.NAME, "phone")
    phone_number.send_keys("+7985899998787")
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")
    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")
    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")
    submit_button = driver.find_element(
        By.XPATH, "//button[@type='submit' and text()='Submit']")
    submit_button.click()

    zip_code = driver.find_element(By.ID, "zip-code")
    zip_code_color = zip_code.value_of_css_property("background-color")
    expected_colors = "#f8d7da"
    assert zip_code_color == expected_colors or "rgba(248, 215, 218, 1)", \
        f"Zip code должен быть красным, а сейчас {zip_code_color}"
    green_fields = ["first-name", "last-name", "address", "e-mail",
                    "phone", "city", "country", "job-position", "company"]
    expected_green = "#d1e7dd"

    for field_id in green_fields:
        element = driver.find_element(By.ID, field_id)
        actual_color = element.value_of_css_property("background-color")
        assert actual_color == expected_green or "rgba(209, 231, 221, 1)"\
            f"Поле {field_id} должно быть зеленым, а сейчас {actual_color}"

    driver.quit()
