from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "NjY1ZDIxYTUtY2NhMS00NDAwLWIzOTYtYmE4NjRkZGM0NWQz",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/test98463")
    url_1 = driver.current_url
    print(f"Первый адрес {url_1}")
    driver.delete_all_cookies()
    driver.add_cookie({
        "name": "SESSION",
        "value": "MTM0Y2Y1ZjMtNmUxNy00YjYzLWE0NDktNTE3MzQyOWE2NTZh",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/test3754")
    url_2 = driver.current_url
    print(f"Второй адрес {url_2}")

    assert url_1 != url_2, "ошибка"
    driver.quit()
