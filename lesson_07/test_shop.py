from selenium import webdriver
from pages.page_avtorization_shop import AuthorizationShop
from pages.home_page_shop import HomeShop
from pages.page_cart import Cart


def test_shop():
    driver = webdriver.Firefox()
    authorization = AuthorizationShop(driver)
    home = HomeShop(driver)
    cart = Cart(driver)
    authorization.open_page()
    authorization.authorization()
    home.adding_to_cart()
    home.go_to_cart()
    cart.checkout()
    cart.form()
    cart.total()

    assert cart.total() == "Total: $58.29"
    driver.quit()
