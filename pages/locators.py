from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE = (By.CLASS_NAME, "price_color")
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
