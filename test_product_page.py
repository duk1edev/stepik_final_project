from pages.product_page import ProductPage  # delete . for runtest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object
    page.open()
    page.add_to_basket()


def test_product_name_success(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.get_success_product_price() == page.get_product_name(), "Товар не совпадает"
