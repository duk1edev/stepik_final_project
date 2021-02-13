import pytest
import time
from pages.product_page import ProductPage  # delete . for runtest in WINDOWS
from pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = 'Balabol123OLOLOSHENbKA'
        page.go_to_register_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        assert page.get_success_product_name() == page.get_product_name(), "Не тот товар был добавлен в корзину"
        time.sleep(10)


# ============================================================================================
# ЧЕРНОВИКИ и ПРИМЕРЫ  ДЛЯ ТЕСТОВ
# ============================================================================================
# def test_guest_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket()
#     page.should_be_empty_basket()


# class TestUserAddToBasketFromProductPage():
#     def test_guest_cant_see_success_message(browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#         page = ProductPage(browser, link)  # инициализируем Page Object
#         page.open()
#         page.should_not_be_success_message()


# def test_guest_can_add_product_to_basket(browser):
#   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#   page = ProductPage(browser, link)  # инициализируем Page Object
#   page.open()
#   page.add_to_basket()
#   assert page.get_success_product_name() == page.get_product_name(), "Товар не совпадает"


# def test_guest_cant_see_success(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)  # инициализируем Page Object
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)  # инициализируем Page Object
#     page.open()
#     page.add_to_basket()
#     page.should_disappeared_success_message()
#
# @pytest.mark.login
# class TestLoginFromProductPage():
#     @pytest.fixture(scope='function', autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title= 'Best book created by robot')
#         self.link  = self.product.link
#
#         yield
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
# дальше обычная реализация теста
#
# def test_guest_should_see_login_link(self, browser):
#     page = ProductPage(browser, self.link)
#     дальше обычная реализация теста


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer9", marks=pytest.mark.xfail)])
